#!/bin/bash

echo "Sleeping for 1 second to wait for Docker Volumes to mount"

sleep 1

npm run dev &

php artisan inertia:start-ssr &

php artisan serve --host=0.0.0.0 --port=8000