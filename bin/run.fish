#!/usr/bin/env fish
# Runs the ttc module.

cd (status dirname)/..
set -x PYTHONPATH '.'
python3 -m ttc
