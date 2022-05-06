from datetime import *
from git import *
from optparse import OptionParser
from collections import namedtuple

import csv
import os
import sys
import logging
import argparse

current_working_path = os.getcwd()

logger = logging.getLogger(__name__)

parser = OptionParser()


def init_argparse():
    parser = argparse.ArgumentParser(prog='gitExtractCommits',
                                     description='Generates a CSV File of all commits from git Repos contained in a target dir')
    parser.add_argument("-t", "--Targetdir",
                        action="store",
                        help="Absulute Path from home directory to the target directory",
                        type=str,
                        required=True)
    parser.add_argument("-v", "--Verbose",
                        dest="verbose",
                        default=False,
                        help="Verbose, if set all the logfile output will also be present in console",
                        required=False)
    parser.add_argument("-n", "--Name",
                        action="store",
                        type=str,
                        default="Default_Commit_Log",
                        help="Name for the output file",
                        required=False)
    parser.add_argument("-l", "--Logs",
                        action="store",
                        type=str,
                        help="Absolute Path for the location where the log should be saved ",
                        required=False)

    return parser


def init_logger(verbose: bool, logs_location_path):
    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    log_location = check_logs_location(logs_location_path)
    file_handler = logging.FileHandler(log_location + "/" + datetime.today().strftime("%Y%m%d%H-%M-%S") + "_gitCommitExtract.log")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    if verbose:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)


def main():
    arg_parser = init_argparse()
    args = arg_parser.parse_args()
    targetdir_path = args.Targetdir
    output_filename = args.Name
    verbose = args.verbose
    logs_location_path = args.Logs

    init_logger(verbose, logs_location_path)

    get_target_dir(targetdir_path)
    get_subdirs(targetdir_path, output_filename)


def check_logs_location(logs_location_path):
    if logs_location_path is not None:
        log_location = logs_location_path
    else:
        log_location = "./log/"

    if not os.path.isdir(log_location):
        os.mkdir(log_location)

    return log_location


def get_target_dir(target_path):
    try:
        os.chdir(target_path)
        print("Current working directory: {0}".format(os.chdir(target_path)))
        logger.info("Changed to target dir {0}".format(os.chdir(target_path)))
        return target_path
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(target_path))
        logger.error("Directory: {0} does not exist".format(target_path))
        quit()
    except NotADirectoryError:
        print("{0} is not a directory".format(target_path))
        logger.error("{0} is not a directory".format(target_path))
        quit()
    except PermissionError:
        print("You do not have permissions to change to {0}".format(target_path))
        logger.error("You do not have permissions to change to {0}".format(target_path))
        quit()


def get_subdirs(targetdir_path, output_filename):
    current_dir = os.getcwd()
    subfolders = [f.path for f in os.scandir(current_dir) if f.is_dir()]
    number_subdirs = len(subfolders)
    if subfolders:
        print("The target dir contains {0} folders.\nPaths: {1}".format(number_subdirs, subfolders))
        logger.info("Number of Subdirs {0}, Subdir Paths".format(number_subdirs, subfolders))
        enter_subdir(subfolders, targetdir_path, output_filename)
        return subfolders
    else:
        print("The target dir is empty")
        logger.error("The target dir is empty, nothing found in {0}".format(os.getcwd()))
        return 0


def enter_subdir(subfolders, targetdir_path, output_filename):
    os.chdir(current_working_path)
    with open(output_filename, "w") as f:
        header = ['Targetdir', 'Date', 'Commit-Hash', 'Author']
        print("This works")
        writer = csv.writer(f)
        writer.writerow(header)
        for subfolder in subfolders:
            os.chdir(subfolder)
            print("Entering subfolder: {0}".format(subfolder))
            logger.info("Entered subfolder: {0}".format(subfolder))
            get_commit_logs(subfolder, writer)
            os.chdir(targetdir_path)


def get_commit_logs(subfolder, writer):
    global repo_name
    try:
        repo = Repo(subfolder)
        repo_name = repo.working_tree_dir.split("/")[-1]
        for commit in repo.iter_commits():
            commit_data = [repo_name, commit.committed_datetime.strftime("%Y%m%d"), commit.hexsha, commit.author]
            writer.writerow(commit_data)
            print("Added new entry: Targetdir: {0}, Date: {1}, Commit Hash: {2}, Author: {3}".format(repo_name,
                                                                                                     commit.committed_datetime.strftime(
                                                                                                         "%Y%m%d"),
                                                                                                     commit.hexsha,
                                                                                                     commit.author))
            logger.info("Added new entry: Targetdir: {0}, Date: {1}, Commit Hash: {2}, Author: {3}".format(repo_name,
                                                                                                           commit.committed_datetime.strftime(
                                                                                                               "%Y%m%d"),
                                                                                                           commit.hexsha,
                                                                                                           commit.author))

    except InvalidGitRepositoryError:
        print("This directory does not contain git")
        logger.info("Folder does not contain git: {0}".format(subfolder))


if __name__ == "__main__":
    main()
