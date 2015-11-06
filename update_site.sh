#!/bin/sh

# Ensuring running from the script directory
if [[ $(dirname $0) != "." ]]; then
    echo "Must run $(basename $0) from its directory."
    exit 1
fi

# Check arguments
if [ $# -lt 1 ]; then
    echo "Usage: $0 COMMIT_MESSAGE"
    exit 1
fi


# Test for landslide
command -v ghp-import > /dev/null
if [ $? -ne 0 ]; then
    echo "The python package ghp-import is not installed."
    echo "Try: pip install ghp-import"
    exit 2
fi

# Rebuild _site
jekyll build

# Push
ghp-import _site/ -pm "$*"


exit 0;
