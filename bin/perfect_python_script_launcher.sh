#!/bin/bash

. ~/venv/perfectpythonscript/bin/activate
export PYTHONPATH=$PYTHONPATH:$(dirname $(dirname $0))
echo $PYTHONPATH
python -m pps.perfectpythonscript $@

