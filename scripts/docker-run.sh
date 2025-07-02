#!/bin/bash
set -x

if [ -z $BASH ]; then
  echo Using Bash...
  exec "/bin/bash" $0 $@
  exit
fi

# Root check
if [[ ! $(id -u) -eq 0 ]]; then
  echo You must run this script as the superuser.
  exit 1
fi

BRANCH=latest

docker pull entermediadb/deepface:$BRANCH
docker run --log-opt max-size=10m --log-opt max-file=2 -p  5005:5000 deepface

echo ""
echo "Deepface server running on port 5005"
echo ""