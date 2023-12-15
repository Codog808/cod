#!/usr/bin/env python3
import requests
import json
import subprocess as sp
import os
import signal
import sys

def read_my_data():
    import pkg_resources
    json_path = pkg_resources.resource_filename('GitC', 'git_commands.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def local_or_global_for_git_commands():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        changes_file_path = os.path.join(script_dir, "data/git_commands.json")
        with open(changes_file_path) as f:
            return json.load(f)
    except:
        return read_my_data()

def check_if_file_exists(filename):
    ignore = ['__pycache__/', 'venv/', '.git_config.json']
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            gitignore = "\n".join(ignore)
            f.write(gitignore)
        return 1
    else:
        return 0

class Git:
    """Object to ease the use of git"""
    def __init__(self, repository_name, username, access_token, branch):
        self.access_token = access_token.strip()
        self.repository_name = repository_name.strip()
        self.username = username.strip()
        self.branch = branch.strip()
        check_if_file_exists(".gitignore")
    class Repository:
        """Tools which create or checks repositories of a certain user"""
        def __init__(self, parent):
            self.parent = parent
        def create(self):
            """Creates a repository using the GitHub API"""
            url = "https://api.github.com/user/repos"
            headers = {
                "Authorization": f"token {self.parent.access_token}",
                "Accept": "application/vnd.github.v3+json"
            }
            data = {
                "name": self.parent.repository_name
            }
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code == 201:
                print(f"{self.parent.repository_name} has been created successfully")
                return True
            else:
                print(response.text)
                return False
        def check(self, save=False):
            url = f"https://api.github.com/users/{self.parent.username}/repos"
            headers = {
                "Authorization": f"token {self.parent.access_token}",
                "Accept": "application/vnd.github.v3+json"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                repositories = response.json()
                if save:
                    filename = f"repository_{self.username}"
                    with open(filename, 'w') as f:
                        f.write(str(repositories))
                        f.close()
                for repository in repositories:
                    if repository['name'] == self.parent.repository_name:
                        print(f"Repository '{repository['name']}' Does Exist...")
                        return True
                print(self.parent.repository_name, "Does NOT Exist...")
                return False
    class Synch:
        """To push, merge, or work in a different branch in Git"""
        def __init__(self, parent):
            self.parent = parent
            self.commands = {
              "add": "git add .",
              "commit": "git commit -m 'gfs'",
              "push": "git push -u origin",
              "pull": "git pull origin",
              "branch": "git branch",
              "checkout": "git checkout", 
              "remote": "git remote add origin"
            }
            self.origin = f"https://{self.parent.access_token}@github.com/{self.parent.username}/{self.parent.repository_name}.git"
        def remote(self):
            """Set Remote Origin"""
            command = self.commands["remote"].split(" ") + [self.origin]
            sp.run(command)
            # print(command)
            return True
        def activate(self):
            """Push all files in a directory to specified branch"""
            order = ['add', 'commit', 'branch', 'checkout', 'push']
            for command_index, i in enumerate(order):
                print("Runnning Step...", command_index + 1)
                if (command_index < 2):
                    command = self.commands[i].split(" ")
                    # print(command)
                    sp.run(command)
                else:
                    # print(self.branch)
                    command = self.commands[i].split(" ") + [self.parent.branch]
                    sp.run(command)
                print()
            return True
        def merge(self):
            pass

def main():

    git_token_path = os.path.expanduser("~/Projects/keys/github")
    with open(git_token_path) as f:
        token = f.read().strip()

    try:
        with open(".git_config.json", 'r') as file:
            changes = json.load(file)
    except FileNotFoundError:
        print("\n\n### No configurations were found; create one using 'set' ###\n\n")
        os.kill(os.getpid(), signal.SIGTERM)

    # Get the values from the changes, or set defaults if no changes were made
    branch = changes.get('branch', 'main')
    repository = changes.get('repository', '')
    username = changes.get('username', '')
    other_token = changes.get('token', '')
    if len(other_token) >= len(token):
        token = other_token

    init = Git(repository, username, token, branch)
    # if init == False:
    #    print(".git_config.json is not created. Create one using the 'set.py' file; 'set.py -h' to see usage.")
    #    return ValueError
    return init

if __name__ == "__main__":
    initalize = main()
    # initalize = Git("test", "Codog808", token)
    sync = initalize.Synch(initalize)
    # sync.activate()
    print("Testing Synch")
    sync.remote()
    repo = initalize.Repository(initalize)
    print("Testing Repository")
    repo.check()

