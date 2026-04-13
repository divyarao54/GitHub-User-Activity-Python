import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Fetches user activity from the GitHub API
def get_activity_data(username):
    API_KEY = os.getenv("GITHUB_ACCESS_TOKEN")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        data = requests.get(url=f"https://api.github.com/users/{username}/events/public", headers=headers)
        data.raise_for_status()
        return {"data": data.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}