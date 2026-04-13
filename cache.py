import os
import json
from datetime import datetime, timedelta

# Stores data into cache, creates new file if not exists
def store_data_into_cache(username, data):
    if not os.path.exists("user_activity.json"):
        with open("user_activity.json", mode="w", encoding="utf-8") as write_file:
            user_activity = {}
            user_activity[username] = {"data": data, "cached_at": datetime.now().isoformat()} 
            json.dump(user_activity, write_file, indent=2)
            return
    with open("user_activity.json", mode="r+", encoding="utf-8") as file:
        try:
            all_activity = json.load(file)
        except json.JSONDecodeError as e:
            print("Unable to read cache", e)
            return None
        all_activity[username] = {"data": data, "cached_at": datetime.now().isoformat()}
        file.seek(0)
        file.truncate()
        json.dump(all_activity, file, indent=2)

# Gets data from cache if newer than a day else deletes that event from cache
def get_data_from_cache(username):
    if not os.path.exists("user_activity.json"):
        return None
    with open("user_activity.json", mode="r+", encoding="utf-8") as read_file:
        try:
            all_activity = json.load(read_file)
        except json.JSONDecodeError as e:
            print("Unable to read cache")
            return None
        individual_activity = all_activity.get(username)
        if not individual_activity:
            return None
        if datetime.now() - datetime.fromisoformat(individual_activity["cached_at"]) > timedelta(hours=24):
            del all_activity[username]
            read_file.seek(0)
            read_file.truncate()
            json.dump(all_activity, read_file, indent=2)
            return None
        return individual_activity
        