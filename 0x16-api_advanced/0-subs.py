import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Valid subreddit, return the number of subscribers
        data = response.json().get('data')
        return data.get('subscribers', 0)
    else:
        # Invalid subreddit, return 0
        return 0

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")

