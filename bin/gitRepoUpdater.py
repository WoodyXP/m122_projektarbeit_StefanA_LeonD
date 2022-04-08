import sys

from gitRepoUpdaterFunctions import *

print(sys.argv)

base_dir = sys.argv[2]

with open(sys.argv[1]) as f:
    repos = f.readlines()


for repo in repos:
    print("repo entry: " + repo)
    remote_url = repo.split(" ")[0]
    target_dir = repo.split(" ")[1].rstrip()
    repo_dir = os.path.join(base_dir, target_dir)
    if dir_is_repo(repo_dir):
        repo = git.Repo(repo_dir)

        if repo_matches_remote(repo, remote_url):
            print("pulling repo")
            repo.remotes.origin.pull()
            repo.close()
        else:
            delete_repo(repo_dir)
            clone_repo(repo_dir, remote_url)
    else:
        if os.path.exists(repo_dir) and os.path.isdir(repo_dir):
            shutil.rmtree(repo_dir)

        clone_repo(repo_dir, remote_url)
