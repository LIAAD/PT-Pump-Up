#!/bin/bash

if ["$1" == "production"]; then
    echo "Running in production mode"
else
    echo "Running in development mode"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./* ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test 
    #ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "cd /home/ruben/FEUP/PT-Pump-Up/src/laravel-test && docker-compose down && docker-compose up -d"
fi

echo "Finished"
sleep 3