from github import Github

# Your GitHub personal access token
GITHUB_TOKEN = "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"

# Repository details
REPO_OWNER = "Sai-prudhvi1483"
REPO_NAME = "prudhvi"

# Environment variable to update
ENV_VAR_NAME = "VERSION"
NEW_VALUE = "1.0.5"  # New version number

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
