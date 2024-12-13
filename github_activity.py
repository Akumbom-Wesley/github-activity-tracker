import sys
import json
import http.client
import os
import time

CACHE_FILE = "activity_cache.json"
CACHE_EXPIRY = 300  # 5 minutes


def fetch_with_cache(username):
    # Check if the cache exists and is fresh
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as file:
            cache = json.load(file)
            if cache["username"] == username and time.time() - cache["timestamp"] < CACHE_EXPIRY:
                print("Using cached data...")
                return cache["events"]

    # Fetch data from API
    events = fetch_github_activity(username)

    # Cache the data
    if events:
        with open(CACHE_FILE, 'w') as file:
            json.dump({"username": username, "timestamp": time.time(), "events": events}, file)

    return events


def fetch_github_activity(username):
    """
    Fetch the recent GitHub activity of a user using the GitHub API.

    Args:
        username (str): The GitHub username

    Returns:
        list: A list of recent events if successful, otherwise None.
    """
    # Define API endpoint
    url = f"/users/{username}/events"

    # Create a connection to the GitHub API
    connection = http.client.HTTPSConnection("api.github.com")

    try:
        # Send a GET request to the API
        headers = {"User-Agent": "Python GitHub Activity Fetcher"}
        connection.request("GET", url, headers=headers)

        # Get the response
        response = connection.getresponse()

        # If the response status is not 200, handle the error
        if response.status != 200:
            print(f"Error: Unable to fetch activity for user {username}. HTTP Status Code: {response.status}")
            return None

        # Parse the response
        data = response.read()
        events = json.loads(data)

        # Return the list of events
        return events

    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return None

    finally:
        # Close the connection
        connection.close()


def main():
    # Get username and optional filter type
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username> [--type <event_type>]")
        return

    username = sys.argv[1]
    event_type = None
    if len(sys.argv) > 3 and sys.argv[2] == "--type":
        event_type = sys.argv[3]

    events = fetch_with_cache(username)

    if events:
        if event_type:
            events = [event for event in events if event["type"] == event_type]

        print("Recent Activity:")
        for event in events[:10]:
            if event["type"] == "PushEvent":
                print(f"- Pushed {len(event['payload']['commits'])} commits to {event['repo']['name']}")
                for commit in event["payload"]["commits"]:
                    print(f"  Commit: {commit['message']}")
            elif event["type"] == "IssuesEvent":
                print(f"- {event['payload']['action'].capitalize()} an issue in {event['repo']['name']}: {event['payload']['issue']['title']}")
            else:
                print(f"- {event['type']} on {event['repo']['name']}")

    else:
        print("No activity found or an error occurred.")


if __name__ == "__main__":
    main()
