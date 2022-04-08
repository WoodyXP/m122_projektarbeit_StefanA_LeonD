import shutil
import validators
import git
import os


def dir_is_repo(path):
    print("Check if path is repo: " + path)
    try:
        _ = git.Repo(path).git_dir
        return True
    except (git.exc.InvalidGitRepositoryError, git.exc.NoSuchPathError):
        return False


def repo_matches_remote(repo, remote_url):
    return repo.remotes.origin.url == remote_url


def delete_repo(path):
    git.rmtree(path)


def clone_repo(path, remote_url):
    print("cloning repo: " + remote_url + "to path: " + path)
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        git.Repo.clone_from(remote_url, path)
    except git.exc.GitError:
        # TODO logging
        print("error while cloning")
        return


def repo_file_is_valid(path):
    with open(path) as inputfile:
        giturl_list = [line.split(None, 1)[0] for line in inputfile]
        for giturl in giturl_list:
            validated_entry = validators.url(giturl)
            if validated_entry != True:
               print("This URL: " + giturl + " is invalid")
               ## TODO: Logging
    inputfile.close()
