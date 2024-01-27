import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Valid subreddit, print titles of the first 10 hot posts
        posts = response.json().get('data', {}).get('children', [])

        if not posts:
            print("No posts found in the subreddit.")
        else:
            for i, post in enumerate(posts[:10], start=1):
                print(f"{i}. {post['data']['title']}")
    else:
        # Invalid subreddit, print None
        print(None)

if __name__ == "__main__":
    # Example usage
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name
