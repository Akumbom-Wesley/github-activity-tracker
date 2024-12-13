import sys

def main():
    # Check if a username is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Error: Please provide a github username.")
        print("Usage:  github_activity.py <username>")
        sys.exit(1)

    # Get the github username from the command-line arguments
    username = sys.argv[1]
    print(f"Fetching activity for GitHub user: {username}")

if __name__ == "__main__":
    main()