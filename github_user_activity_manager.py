from cache import get_data_from_cache, store_data_into_cache
from github_service import get_activity_data

# Displays data retrieved from either the GitHub API or the cache
# Also performs filtering by event type when needed
def display_data(username, event_type=None):
    user_activity = get_data_from_cache(username)
    if not user_activity:
        # To check if caching works
        #print("Cache miss")
        user_activity = get_activity_data(username)
        
        if user_activity.get("error"):
            print("Error: ", user_activity["error"])
            return
        
        user_activity = user_activity["data"]
        store_data_into_cache(username, user_activity)
    else:
        user_activity = user_activity["data"]    
    if not event_type:
        print(user_activity)
        return
    # filtered_data = []
    # for activity in user_activity:
    #     if activity["type"] == event_type:
    #         filtered_data.append(activity)
    filtered_data = [activity for activity in user_activity if activity["type"] == event_type]
    print(filtered_data)
    return
    