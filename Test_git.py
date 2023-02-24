import os
import git
import git_config

# Replace the URL with your own GitHub repository URL
repo_url = 'https://github.com/RobinSequeira/mottest_vehicle.git'
# Replace the path with the local path where you want to clone the repository
local_path = '/python_scripts'

# Get the GitHub credentials from environment variables
username = 'RobinSequeira'
access_token = git_config.git_access_token
# Clone the repository using the GitPython library
if username and access_token:
    git.Git().clone(repo_url, local_path, auth=(username, access_token))
else:
    print("GitHub credentials not found in environment variables.")