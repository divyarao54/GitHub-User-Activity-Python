# GitHub User Activity

**Problem Statement URL** - [https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)

**Solution Link** - [https://roadmap.sh/projects/github-user-activity/solutions?u=690b33dfce70eef65bc6b75e](https://roadmap.sh/projects/github-user-activity/solutions?u=690b33dfce70eef65bc6b75e)

## Usage Instructions

- Clone this repository.
- Create a .env file with your GitHub Access Token as the content. It should look like this `GITHUB_ACCESS_TOKEN=<your-access-token-here>`
- To view user activity run `python github_user_activity_cli.py github-activity "<username>" "<event-type>"` where `<event-type>` is optional and can be one of [these](https://docs.github.com/en/rest/using-the-rest-api/github-event-types?apiVersion=2022-11-28)
