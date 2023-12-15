#!/usr/bin/env python3
# from GitC.git import Git
# import GitC.git as git
import json
import time
from git import main as initialize
from gcheck import main as check_repo_exists
def main():
    init = initialize()
    check_repo_exists()
    time.sleep(1)
    print()
    sync = init.Synch(init)
    sync.activate()

    print("Success")
    return True

if __name__ == '__main__':
    main()

