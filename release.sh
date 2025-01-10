#!/bin/bash

# Check if a version number is provided
if [ -z "$1" ]; then
    echo "Usage: ./release.sh <version>"
    echo "Example: ./release.sh 1.1.1"
    exit 1
fi

VERSION=$1

# Add all files
git add .

# Commit changes
git commit -m "Release v${VERSION}"

# Create and push tag
git tag "v${VERSION}"
git push && git push origin "v${VERSION}"

echo "Released version ${VERSION}"
echo "Check GitHub Actions for the publishing status: https://github.com/sentnl/nodepulse-python/actions" 