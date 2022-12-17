#!/bin/bash

# Set the repository path
REPO_PATH="/path/to/repository"

# Change to the repository directory
cd "$REPO_PATH"

# Get a list of all branches in the repository
branches=$(git branch -a)

# Split the list of branches into an array
IFS=$'\n' read -rd '' -a branch_array <<< "$branches"

# Get the number of branches
num_branches=${#branch_array[@]}

# Generate a random number between 0 and the number of branches - 1
random_index=$((RANDOM % num_branches))

# Check out the branch at the random index
git checkout "${branch_array[$random_index]}"
