import requests
import json
import subprocess as sp
import os
import pkg_resources

def read_my_data():
    json_path = pkg_resources.resource_filename('GitC', 'git_commands.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

git_token_path = os.path.expanduser("~/Projects/keys/github")
with open(git_token_path) as f:
    token = f.read().strip()

https = "https://"
github= "@github.com/"
e = ".git"

ignore = ['__pycache__/', 'venv/']
def check_if_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            gitignore = "\n".join(ignore)
            f.write(gitignore)
        return 1
    else:
        return 0

class Git:
    """Object to ease the use of git"""
    def __init__(self, repository_name, username, access_token):
        self.access_token = access_token.strip()
        self.repository_name = repository_name.strip()
        self.username = username.strip()
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
        def __init__(self, parent, branch="main"):
            self.parent = parent
            self.branch = branch
            # with open("git_commands.json") as f:
            #    self.commands= json.load(f)
            self.commands = read_my_data()
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
                print(command_index)
                if (command_index < 2):
                    command = self.commands[i].split(" ")
                    # print(command)
                    sp.run(command)
                else:
                    # print(self.branch)
                    command = self.commands[i].split(" ") + [self.branch]
                    sp.run(command)
            return True
        def merge(self):
            pass

if __name__ == "__main__":
    initalize = Git("test", "Codog808", token)
    sync = initalize.Synch(initalize, "test")
    # sync.activate()
    # sync.remote()
    repo = initalize.Repository(initalize)
    repo.check()

