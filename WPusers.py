import requests
import sys
import random
import time
from urllib.parse import urljoin

# Define multiple user-agent strings to rotate through
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
]

def fetch_usernames(url, proxies=None):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    # Define the endpoints to check
    rest_api_endpoint = urljoin(url, '/wp-json/wp/v2/users')
    usernames = []

    def get_usernames_from_api(api_url):
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(api_url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                username = user.get('slug')
                if username and username not in usernames:
                    usernames.append(username)
                    print(f'User found: {username}')
        else:
            print(f"Received status code {response.status_code} for {api_url}")
        return usernames

    def get_username_from_author(endpoint, user_id):
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(f"{endpoint}{user_id}", headers=headers, proxies=proxies, allow_redirects=True)
        if response.status_code == 200:
            username = response.url.rstrip('/').split('/')[-1]
            if username and username not in usernames:
                usernames.append(username)
                print(f'User {user_id} found: {username}')
        return usernames

    print(f"Checking REST API endpoint: {rest_api_endpoint}")
    get_usernames_from_api(rest_api_endpoint)
    if not usernames:
        print("No usernames found with REST API. Checking author endpoints...")
        author_endpoint = url.rstrip('/') + '/?author='
        for user_id in range(1, 20):  # Adjust the range as needed
            get_username_from_author(author_endpoint, user_id)
            time.sleep(random.uniform(1, 3))  # Random delay to avoid detection

    return usernames

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python WPusers.py <url> [<proxy>]")
        sys.exit(1)

    url = sys.argv[1]
    proxies = {
        'http': sys.argv[2],
        'https': sys.argv[2]
    } if len(sys.argv) == 3 else None

    usernames = fetch_usernames(url, proxies)
    if usernames:
        print(f"Usernames found: {', '.join(usernames)}")
    else:
        print("No usernames found or the endpoints are not accessible.")
