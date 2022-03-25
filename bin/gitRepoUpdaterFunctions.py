import git
import os


def dir_is_repo(path):
    print("check if if path is repo: " + path)
    try:
        _ = git.Repo(path).git_dir
        return True
    except (git.exc.InvalidGitRepositoryError, git.exc.NoSuchPathError):
        return False


def repo_matches_remote(repo, remote_url):
    return repo.remotes.origin.url == remote_url


def delete_repo(path):
    os.remove(path)


def clone_repo(path, remote_url):
    print("cloning repo: " + remote_url + "to path: " + path)
    os.mkdir(path)
    git.Repo.clone_from(remote_url, path)
