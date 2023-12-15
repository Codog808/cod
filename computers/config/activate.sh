#!/bin/bash

# Output from your python script
output=$(python directories.py)
echo $output

# Save old IFS and set new one to space
OIFS=$IFS
IFS=$'\n'
count=1

# Read each directory and add it to the PATH
for dir in $output; do
        dir_clean=$(echo $dir | tr -d '\n' | tr -d '\r')
        
        # Check if export line is already in .bashrc
        if ! grep -q "export PATH=.*$dir_clean" ~/.bashrc; then
            # Export for the current session
            export PATH=$PATH:$dir_clean
            # Append the export to .bashrc for future sessions
            echo "export PATH=\$PATH:$dir_clean" >> ~/.bashrc
	    echo "added to bashrc"
	else
	    echo "already in bashrc"
        fi
done

# Restore IFS
IFS=$OIFS

echo $PATH

