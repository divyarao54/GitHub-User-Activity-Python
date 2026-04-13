import sys
from github_user_activity_manager import display_data

# Main function which defines the CLI for this project
def main():
    if(len(sys.argv) < 3):
        print("Usage: github_user_activity_cli github-activity <username> <event-type-optional>")
        return
    
    if(sys.argv[1] != "github-activity"):
        print("Unrecognized command. Only github-activity supported.")
        return
    
    username = sys.argv[2]
    event_type = sys.argv[3] if len(sys.argv) > 3 else None
    if event_type:
        display_data(username, event_type)
    else:
        display_data(username)
    return

if __name__ == "__main__":
    main()