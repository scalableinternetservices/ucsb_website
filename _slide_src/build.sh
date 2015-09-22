#!/bin/sh

DESTINATION="../slides/"

function process_file {
    # Process only files with .md extension
    if [[ ${1: -3} != ".md" ]]; then
        echo "Ignoring $1 (does not have .md extension)"
        return
    fi

    # Create the config.cfg file
    sed "s/<SOURCE>/$1/" CONFIG_TEMPLATE.CFG > config.cfg

    # Run landslide
    landslide config.cfg > /dev/null
    if [ $? -eq 0 ]; then
        echo "Built $1"
    else
        echo "Failed to build $1. Aborting!"
        rm -f config.cfg presentation.html
        exit 3
    fi

    # Move the file to the appropriate locaation
    base=${1::${#1}-3}
    mv presentation.html "$DESTINATION/$base.html"
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
rm config.cfg

exit 0;
