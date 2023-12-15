#!/usr/bin/env python3
import argparse
import json
import os

def main():
    defaults = {
        'branch': 'main',
        'repository': '',
        'username': '',
        'token': ''
    }

    parser = argparse.ArgumentParser(description="Set The Branch, Repo, Token, and Username for git")
    parser.add_argument('-b', '--branch', type=str, default=None)
    parser.add_argument('-u', '--username', type=str, default=None)
    parser.add_argument('-r', '--repository', type=str, default=None)
    parser.add_argument('-t', '--token', type=str, default=None)

    args = parser.parse_args()
    filename = ".git_config.json"

    if os.path.exists(filename):
        # print(filename, "it exists")
        with open(filename, 'r') as file:
            config = json.load(file)
    else:
        config = defaults.copy()

    if args.branch is not None:
        config['branch'] = args.branch
    if args.repository is not None:
        config['repository'] = args.repository
    if args.username is not None:
        config['username'] = args.username
    if args.token is not None:
        config['token'] = args.token    

    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

    print("Success")
    return True

if __name__ == "__main__":
    main()

