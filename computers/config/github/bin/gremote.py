#!/usr/bin/env python3
# import GitC.git as git
import json
from git import main as initialize
def main():
    init = initialize()
    sync = init.Synch(init)
    sync.remove_remote()
    sync.remote()
    print("Sucess")
    return True
if __name__ == "__main__":
    main()



