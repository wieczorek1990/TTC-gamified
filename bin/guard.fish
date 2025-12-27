#!/usr/bin/env fish
# Runs checks.

cd (status dirname)/..
echo 'Guard!' &&
 black ttc/
