#!/bin/bash

echo "Sleeping for 1 second to wait for Docker Volumes to mount"

sleep 1

npm run dev &

composer dump-autoload 

php artisan key:generate

php artisan migrate

php artisan db:seed

php artisan serve --host=0.0.0.0 --port=8000