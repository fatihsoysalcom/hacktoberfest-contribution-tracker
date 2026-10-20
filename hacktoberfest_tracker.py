import requests
import os

# This script simulates checking for Hacktoberfest contributions.
# In a real-world scenario, you'd use the GitHub API.
# For this example, we'll mock a simple check.

def get_github_contributions(username):
    """
    Simulates fetching contribution data for a GitHub user.
    In a real application, this would involve GitHub API calls.
    """
    print(f"Simulating fetching contributions for {username}...")
    # Mock data representing contributions (e.g., number of PRs merged)
    # This is a placeholder for actual API interaction.
    mock_contributions = {
        "octocat": 5,  # Example: User 'octocat' has 5 contributions
        "user_with_no_contributions": 0
    }
    return mock_contributions.get(username, 0) # Default to 0 if user not in mock data

def check_hacktoberfest_eligibility(username, required_contributions=4):
    """
    Checks if a user is eligible for Hacktoberfest based on their contributions.
    """
    contributions = get_github_contributions(username)
    print(f"User '{username}' has {contributions} contributions.")

    if contributions >= required_contributions:
        print(f"Congratulations! '{username}' is eligible for Hacktoberfest!")
        return True
    else:
        print(f"'{username}' needs {required_contributions - contributions} more contributions to be eligible for Hacktoberfest.")
        return False

if __name__ == "__main__":
    # This is where you'd typically get the username, perhaps from command line arguments or environment variables.
    # For this example, we'll hardcode a few.
    print("--- Hacktoberfest Contribution Checker ---")

    # Example 1: A user who is eligible
    check_hacktoberfest_eligibility("octocat")
    print("\n") # Add a newline for better readability

    # Example 2: A user who is not eligible
    check_hacktoberfest_eligibility("user_with_no_contributions")
    print("\n")

    # Example 3: A user not in our mock data
    check_hacktoberfest_eligibility("another_user")

    print("\n--- Simulation Complete ---")
