import logging
from collections import namedtuple
from datetime import datetime

from functions.functions import *

CommandLineArguments = namedtuple("CommandLineArguments", "repo_file_path base_dir verbose")


def init_logger(verbose: bool):
    log_formatter = logging.Formatter("%(asctime)s - %(levelname): %(message)s")
    root_logger = logging.getLogger()

    file_handler = logging.FileHandler(datetime.today().strftime('%Y_%m_%d_%H:%M:%S') + ".log")
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)


def main():
    command_line_arguments = get_valid_input_arguments()
    repo_file_path = command_line_arguments.repo_file_path
    base_dir = command_line_arguments.base_dir
    verbose = command_line_arguments.verbose

    init_logger(verbose)
    run(repo_file_path, base_dir)


if __name__ == "__main__":
    main()
