#!/usr/bin/env bash

echo "Running script with parameters: [$1] [$2]"
echo "MYENV = [$MYENV]"

sleep 2s

>&2 echo "Ups! This is error"

echo "Data processed"

exit 33