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

def delete_repositories(username, token, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print(f"Successfully deleted {repo_name}")
    else:
        print(f"Error: {response.status_code} - {response.json().get('message')}")


