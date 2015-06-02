#!/bin/bash

#echo "Number of params is $#"

if [ "$#" -lt 1 -o "$#" -gt 1 ] ;
then
  echo "Script expects one parameter"
  exit 1
fi


echo "Current voltage is $1 volts!" | festival --tts 