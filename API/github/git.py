import requests

def get_repositories(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization":f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        repo_names = [repo['name'] for repo in data]
        return repo_names
    else:
        print(f"Error: {response.status_code}")

def delete_repository(username, token, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {
            'Authorization': f'token {token}',
            'X-GitHub-Api-Version': '2022-11-28'
            }
    response = requests.delete(url, headers=headers)
    try:
        if response.status_code == 204:
            print("repo sucessfully deleted")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except:
        print("ERROR WITH RETURNED JSON")


    # url = f"https://api.github.com/repos/{username}/{repo_name}"
    # headers = {"Authorization": f"token {token}"}
    # response = requests.delete(url, headers=headers)
    # if response.status_code == 200:
    #     print(f"Successfully deleted {repo_name}")
    # else:
    #     print(f"Error: {response.status_code} - {response.json().get('message')}")

if __name__ == "__main__":
    import os
    with open(os.path.expanduser("~/Code/cod/keys/github")) as f:
        key = f.read().strip().split("\n")[0].split(" | ")[0]
        print(key)
    # --- Fix the deleting portion of the code ___ 12/12/23
    repos = get_repositories("Codog808", key)
    print(repos)
    while True:
        name = input("Give me Repo Name: ")
        delete_repository("Codog808", key, name) 

