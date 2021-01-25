import requests
import argparse


def get_respo(user):
    url = 'https://api.github.com/users/{}/repos'.format(user)
    f = requests.get(url)
    data_get = f.json()
    result = [respo_info.get('html_url') for respo_info in data_get]
    return result


def main():
    parser = argparse.ArgumentParser(
        description='to list all respo from github of a user',
    )

    parser.add_argument('user', type=str)
    user = parser.parse_args().user
    print(get_respo(user))


if __name__ == "__main__":
    main()
