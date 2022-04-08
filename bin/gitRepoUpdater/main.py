import argparse
import sys
from collections import namedtuple
from datetime import datetime

from functions.functions import *

CommandLineArguments = namedtuple("CommandLineArguments", "repo_file_path base_dir verbose")


def init_logger(verbose: bool):
    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(datetime.today().strftime('%Y_%m_%d_%H-%M-%S') + ".log")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    if verbose:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)


def init_argparse():
    parser = argparse.ArgumentParser(prog='gitRepoUpdater',
                                     description='automatically clones or updates git repositories')
    parser.add_argument('--repos',
                        help='Absolute or relative path to the txt file containing the repo list',
                        type=str,
                        required=True)
    parser.add_argument('--base',
                        help='Absolute or relative path to the base directory containing all the repos',
                        type=str,
                        required=True)
    parser.add_argument('--v',
                        help='Verbose, if set all the logfile output will also be present in console',
                        action='store_true',
                        required=False)
    return parser


def main():
    arg_parser = init_argparse()
    args = arg_parser.parse_args()
    repo_file_path = args.repos
    base_dir = args.base
    verbose = args.v

    init_logger(verbose)

    if not repo_file_is_valid(repo_file_path):
        logger.error("repo file: {0} is invalid".format(repo_file_path))
        sys.exit()

    if not os.path.isdir(base_dir):
        os.mkdir(base_dir)

    run(repo_file_path, base_dir)


if __name__ == "__main__":
    main()
