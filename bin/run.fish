#!/usr/bin/env fish
# Runs the ttc module.

cd (status dirname)/..
set -x PYTHONPATH '.'
set -x PYGAME_HIDE_SUPPORT_PROMPT '1'
python3 -m ttc
