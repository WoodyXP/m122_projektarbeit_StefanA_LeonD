import logging
import validators
import git
import os
import re

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
    if not os.path.exists(path):
        logger.info("creating path: {0} for repo: {1}".format(path, remote_url))
        os.mkdir(path)
    try:
        git.Repo.clone_from(remote_url, path)
        logger.info("cloning repo: {0} to path: {1}".format(remote_url, path))
    except git.exc.GitError:
        logger.error("error while cloning repo: {0} to path {1}".format(remote_url, path))
        return


def repo_file_is_valid(path):
    with open(path) as f:
        for line in f:
            if not validators.url(line.split()[0]):
                logger.error("repo url: {0} is invalid".format(line.split()[0]))
                return False
            if not re.match("^[A-Za-z0-9-]*$", line.split()[1]):
                logger.error(
                    "target directory: {0} is invalid, should only contain numbers and letters".format(line.split()[1]))
                return False
    f.close()
    return True


def clean_up_repo_dir(repo_dir_names, base_dir):
    all_repos = []
    for sub_dir in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, sub_dir)) and dir_is_repo(os.path.join(base_dir, sub_dir)):
            all_repos.append(sub_dir)

    non_matches = list(set(all_repos).difference(repo_dir_names))

    logger.info("repositories that are no longer in the repo text file and will be deleted: {0}".format(" ".join(non_matches)))

    for non_match in non_matches:
        delete_repo(os.path.join(base_dir, non_match))


def run(repo_file_path, base_dir):
    repo_dir_names = []
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
        repo_dir_names.append(target_dir)

    clean_up_repo_dir(repo_dir_names, base_dir)
