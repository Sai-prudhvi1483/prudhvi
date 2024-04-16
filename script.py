from github import Github

# Your GitHub personal access token
GITHUB_TOKEN = "your_github_token"

# Repository details
REPO_OWNER = "your_github_username"
REPO_NAME = "your_repo_name"

# Environment variable to update
ENV_VAR_NAME = "VERSION"
NEW_VALUE = "1.0.1"  # New version number

def update_env_var():
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

        # Get the environment named 'production'
        env = repo.get_environment("production")

        # Delete the old environment variable
        env.remove_secret(ENV_VAR_NAME)

        # Create a new environment variable with the updated value
        env.add_secret(ENV_VAR_NAME, NEW_VALUE)

        print(f"Environment variable {ENV_VAR_NAME} updated successfully!")
    except Exception as e:
        print(f"Error updating environment variable: {str(e)}")

if __name__ == "__main__":
    update_env_var()
