"""
This script fetches the latest events for a given GitHub username and prints them and also generates a username.txt .

How to use:
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 github_user_activity.py <username>
"""
import sys
import requests

def format_event(event):
    if event['type'] == 'IssueCommentEvent':
        return f"- commented on issue #{event['payload']['issue']['number']}"
    elif event['type'] == 'PushEvent':
        return f"- pushed to {event['repo']['name']}"
    elif event['type'] == 'IssuesEvent':
        return f"- created issue #{event['payload']['issue']['number']}"
    elif event['type'] == 'WatchEvent':
        return f"- starred {event['repo']['name']}"
    elif event['type'] == 'PullRequestEvent':
        return f"- created pull request #{event['payload']['pull_request']['number']}"
    elif event['type'] == 'PullRequestReviewEvent':
        return f"- reviewed pull request #{event['payload']['pull_request']['number']}"
    elif event['type'] == 'PullRequestReviewCommentEvent':
        return f"- commented on pull request #{event['payload']['pull_request']['number']}"
    elif event['type'] == 'CreateEvent':
        return f"- created {event['payload']['ref_type']} {event['payload']['ref']}"
    else:
        return f"- {event['type']}"

def get_latest_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Error fetching events: {response.status_code}")
        return

    events = response.json()
    filename = f"{username}.txt"

    with open(filename, "w") as f:
        header = f"Latest events for {username}:\n"
        print(header.strip())
        f.write(header)

        for event in events:
            message = format_event(event)
            print(message)
            f.write(message + "\n")

    print(f"\nSaved output to {filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_events(sys.argv[1])
    else:
        print("Please provide a GitHub username")