#!/bin/bash
SCREEN=3
Xvfb :1 -nolisten tcp -screen :1 1280x800x24 &
xvfb="$!"
echo $!
DISPLAY=:1 arduino "$@"
echo $@
kill -9 $xvfb
