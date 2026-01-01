# GitHub User Activity CLI

A simple Python CLI tool that fetches and displays recent GitHub activity for a given user using the GitHub Events API.

## Features
- Fetches recent public GitHub events
- Supports common event types (Push, PR, Issues, Stars, etc.)
- Prints output to console
- Saves output to `<username>.txt`

## Tech Stack
- Python
- Requests
- GitHub REST API

## Setup

```bash
git clone https://github.com/puwenesveran/github-user-activity.git
cd github-user-activity
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
