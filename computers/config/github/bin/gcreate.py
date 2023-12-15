#!/usr/bin/env python3
# from GitC.git import Git
# import GitC.git as git
import json
import time
from git import main as initialize

def main():
    init = initialize()
    repo = init.Repository(init)
    check = repo.create()
    if check:
        print("Success")
    else:
        print("Failure, repository is already made; otherwise, check json output")
    return True

if __name__ == '__main__':
    main()

