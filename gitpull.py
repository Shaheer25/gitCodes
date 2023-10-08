from github import Github
import os

# GitHub username or organization name
username = "Shaheer25"
# GitHub personal access token (create one in your GitHub account settings)
access_token = "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"
# Local directory where repositories will be cloned
local_directory = "C:\\Users\\Shaheer\\Desktop\\Shaheer"

# Create a GitHub instance using your personal access token
github = Github(access_token)

# Get the user or organization
user_or_org = github.get_user()  # For a user
# user_or_org = github.get_organization("your_organization")  # For an organization

# Iterate through all repositories of the user or organization
for repo in user_or_org.get_repos():
    # Clone the repository to the local directory
    repo_url = repo.clone_url
    repo_name = repo.name
    repo_path = os.path.join(local_directory, repo_name)
    
    # Check if the repository already exists locally
    if os.path.exists(repo_path):
        print(f"Repository {repo_name} already exists. Skipping.")
    else:
        print(f"Cloning repository: {repo_name}")
        os.system(f"git clone {repo_url} {repo_path}")

print("All repositories cloned.")
