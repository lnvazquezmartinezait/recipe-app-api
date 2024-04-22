#!/bin/bash

set -e

envsubst < /etc/nginx/default.con.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'