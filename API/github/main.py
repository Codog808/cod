from git import delete_repositories, get_repositories
# Python cannot recognize /
import os
# print(os.listdir("~/"))
with open(os.path.expanduser("~/projects/Keys/github")) as f:
    key = f.read().strip().split()[0].split(" | ")[0]

repos = get_repositories(username="Codog808", token=key)
print(repos)
delete_repositories(username="Codoog808", token=key, repo_name="test")
# for _ in range(10000):
#     print("The Killing of Repositories")
#     repos = get_repositories(username="Codog808", token=key)
#     print(repos)
#     repo = input("\nType the name of the Repo you wish to Delete: ")
#     delete_repositories(token=key, username="Codog808", repo_name=repo)
