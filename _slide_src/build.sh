#!/bin/sh

DESTINATION="../slides/"

function process_file {
    if [[ ${1: -3} != ".md" ]]; then
        echo "Ignoring $1 (does not have .md extension)"
        return
    fi
    base=${1::${#1}-3}
    landslide $1 -cro > "$DESTINATION/$base.html"
    if [ $? -eq 0 ]; then
        echo "Built $1"
    else
        echo "Failed to build $1. Aborting!"
        rm -rf theme/
        exit 3
    fi
}


# Ensuring running from the script directory
if [[ $(dirname $0) != "." ]]; then
    echo "Must run $(basename $0) from its directory."
    exit 1
fi

# Check arguments
if [ $# -lt 1 ]; then
    echo "Usage: $0 [MARKDOWN_INPUT...]"
    exit 1
fi

# Test for landslide
command -v landslide > /dev/null
if [ $? -ne 0 ]; then
    echo "The python package landslide is not installed."
    echo "Try: pip install landslide"
    exit 2
fi

# Process each file
for arg in "$@"; do
    process_file "$arg"
done
rm -rf theme/

exit 0;
