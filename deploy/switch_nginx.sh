#!/bin/bash
set -e

COLOR=$1   # blue or green

if [[ "$COLOR" == "blue" ]]; then
    cp nginx.blue.conf nginx.conf
elif [[ "$COLOR" == "green" ]]; then
    cp nginx.green.conf nginx.conf
else
    echo "Usage: ./switch_nginx.sh [blue|green]"
    exit 1
fi

# Reload Nginx
docker exec urlqr-nginx nginx -s reload || docker restart urlqr-nginx


