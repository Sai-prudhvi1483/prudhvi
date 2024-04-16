import os
import requests
import json
from base64 import b64encode


GITHUB_TOKEN = "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"
REPO_OWNER = "Sai-prudhvi1483"
REPO_NAME = "prudhvi"
VARIABLES = {
    "VERSION": os.getenv('VERSION', '1.0.0'),  # Default to '1.0.0' if VERSION is not set
    # Add more variables as needed
}
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def increment_version(version):
    # Split the version into major, minor, and patch numbers
    major, minor, patch = map(int, version.split('.'))

    # Increment the patch number
    patch += 15

    # Join the numbers back into a version string
    new_version = f"{major}.{minor}.{patch}"

    return new_version

def update_variables():
    for key, value in VARIABLES.items():
        # Increment the version if the key is 'VERSION'
        if key == 'VERSION':
            value = increment_version(value)

        # Secrets must be Base64 encoded
        encoded_value = b64encode(value.encode()).decode()

        data = {
            "encrypted_value": encoded_value,
            "key_id": "key_id"
        }
        response = requests.put(f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/secrets/{key}", headers=HEADERS, json=data)
        if response.status_code == 204:
            print(f"Variable {key} updated successfully!")
        else:
            print(f"Failed to update variable {key}. Status code: {response.status_code}")

if __name__ == "__main__":
    update_variables()
