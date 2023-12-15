#!/bin/bash

while getopts "gb" flag
do
    case "${flag}" in
        g) cp GitC/GitC/git.py bin/git.py;;
        b) cp bin/git.py GitC/GitC/git.py;;
    esac
done
