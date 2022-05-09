# shellcheck disable=SC2239
#!/bin/bash

sudo apt update
sudo apt install python3
sudo apt install python3-pip
echo "y"

chmod 755 gitExtractCommits.py
chmod 755 gitRepoUpdater.py
chmod 755 gitRepoUpdaterFunctions.py

pip3 install -r requirements.txt
