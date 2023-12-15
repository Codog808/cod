#!/usr/bin/env python3

from git import main as initialize

def main():
    init = initialize()
    sync = init.Synch(init)
    sync.to_main()

if __name__ == '__main__':
    main()
