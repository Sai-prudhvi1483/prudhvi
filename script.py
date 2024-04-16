import os
from github import Github

# Your GitHub personal access token
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Repository details
REPO_OWNER = "Sai-prudhvi1483"
REPO_NAME = "prudhvi"


# Secret to update
SECRET_NAME = "VERSION"
NEW_VALUE = "1.0.9"  # New version number

def update_secret():
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

        # Update the secret
        g.get_user().get_repo(REPO_NAME).create_secret(SECRET_NAME, NEW_VALUE)

        print(f"Secret {SECRET_NAME} updated successfully!")
    except Exception as e:
        print(f"Error updating secret: {str(e)}")

if __name__ == "__main__":
    update_secret()
