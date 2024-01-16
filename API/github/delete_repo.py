import requests

def main(username, repo_name, token):
    # # Your GitHub username
    # username = 'your_username'

    # # The name of the repository you want to delete
    # repo_name = 'repository_to_delete'

    # # Your personal access token
    # token = 'your_github_token'

    # GitHub API URL for deleting a repository
    api_url = f'https://api.github.com/repos/{username}/{repo_name}'

    # Headers including your GitHub token for authentication
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send a DELETE request to the GitHub API
    response = requests.delete(api_url, headers=headers)

    # Check if the deletion was successful
    if response.status_code == 204:
        print("Repository deleted successfully.")
    else:
        print("Failed to delete the repository:", response.json())

