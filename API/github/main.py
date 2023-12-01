from git import delete_repositories, get_repositories
# Python cannot recognize /
import os
# print(os.listdir("~/"))
with open(os.path.expanduser("~/Keys/github")) as f:
    key = f.read().strip()

for _ in range(10000):
    print("The Killing of Repositories")
    repos = get_repositories(username="Codog808", token=key)
    print(repos)
    repo = input("\nType the name of the Repo you wish to Delete: ")
    delete_repositories(token=key, username="Codog808", repo_name=repo)
