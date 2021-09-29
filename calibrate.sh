#!/bin/bash
if ["$1" -eq ""]
then
  echo Calling DP-4 as standard...
else
  echo Calling with parameter $1...
fi

python3 /home/paul/scripts/map_input_huion.py $1
