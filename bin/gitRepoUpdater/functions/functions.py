import logging
import sys
import validators
import git
import os
from ..main import CommandLineArguments

logger = logging.getLogger(__name__)


def dir_is_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except (git.exc.InvalidGitRepositoryError, git.exc.NoSuchPathError):
        return False


def repo_matches_remote(repo, remote_url):
    return repo.remotes.origin.url == remote_url


def delete_repo(path):
    logger.info("removing repository: {0}".format(path))
    git.rmtree(path)


def clone_repo(path, remote_url):
    logger.info("cloning repo: {0} to path: {1}".format(remote_url, path))
    if not os.path.exists(path):
        logger.info("creating path: {0} for repo: {1}".format(path, remote_url))
        os.mkdir(path)
    try:
        git.Repo.clone_from(remote_url, path)
    except git.exc.GitError:
        # TODO logging
        logger.error("error while cloning repo: {0} to path {1}".format(remote_url, path))
        return


def repo_file_is_valid(path):
    with open(path) as inputfile:
        giturl_list = [line.split(None, 1)[0] for line in inputfile]
        for giturl in giturl_list:
            validated_entry = validators.url(giturl)
            if not validated_entry:
                print("This URL: " + giturl + " is invalid")
                ## TODO: Logging
    inputfile.close()


def get_valid_input_arguments():
    if not len(sys.argv) < 2:
        repo_file_path = sys.argv[1]
        base_dir = sys.argv[2]

        if repo_file_is_valid(repo_file_path) and os.path.isdir(base_dir):
            if len(sys.argv) == 3:
                verbose = sys.argv[3]
                if verbose == '-v':
                    return CommandLineArguments(repo_file_path, base_dir, True)
                else:
                    logger.error("argument {0} doesn't match expected -v".format(verbose))
            else:
                return CommandLineArguments(repo_file_path, base_dir, False)
        else:
            logger.error("repo file path: {0} or base path: {1} is invalid".format(repo_file_path, base_dir))

    logger.error("invalid arguments")
    sys.exit()


def run(repo_file_path, base_dir):
    with open(repo_file_path) as f:
        repos = f.readlines()

    for repo in repos:
        remote_url = repo.split(" ")[0]
        target_dir = repo.split(" ")[1].rstrip()
        repo_dir = os.path.join(base_dir, target_dir)
        if dir_is_repo(repo_dir):
            repo = git.Repo(repo_dir)

            if repo_matches_remote(repo, remote_url):
                logger.info("pulling updates for repo: {0}".format(repo_dir))
                repo.remotes.origin.pull()
                repo.close()
            else:
                logger.info("repo url: {0} doesnt match origin url of repo: {1}".format(remote_url, repo_dir))
                delete_repo(repo_dir)
                clone_repo(repo_dir, remote_url)
        else:
            clone_repo(repo_dir, remote_url)
