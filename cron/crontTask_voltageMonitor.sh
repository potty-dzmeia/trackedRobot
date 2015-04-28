#!/bin/bash

#voltage=$(./measureVoltage.py >&1)               
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
#echo "$DIR"
$DIR/speakVoltage.sh `$DIR/measureVoltage.py`
