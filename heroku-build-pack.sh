#!/bin/sh

# this pack is valid for apps with a hello.txt in the root
heroku run flask db upgrade -a rbl-backend
