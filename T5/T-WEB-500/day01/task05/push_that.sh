#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Error: No commit message."
    exit 1
fi

git add .

git commit -m "$1"

git push origin main

if [ $? -eq 0 ]; then
    echo "Push successful."
else
    echo "Error: Push failed."
    exit 1
fi

exit 0
