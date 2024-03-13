#!/bin/bash

if ["$1" == "production"]; then
    echo "Running in production mode"
else
    echo "Running in development mode"

    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r /home/ruben/FEUP/PT-Pump-Up/src/laravel-test/app/"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./app ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    
    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r /home/ruben/FEUP/PT-Pump-Up/src/laravel-test/bootstrap/"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./bootstrap ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    
    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r /home/ruben/FEUP/PT-Pump-Up/src/laravel-test/config/"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./config ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    
    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r /home/ruben/FEUP/PT-Pump-Up/src/laravel-test/database/"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./database ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    
    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r /home/ruben/FEUP/PT-Pump-Up/src/laravel-test/resources/"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./resources ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    
    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r /home/ruben/FEUP/PT-Pump-Up/src/laravel-test/routes/"
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./routes ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./storage/app/public/* ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/storage/app/public
    
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./composer.json ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./composer.lock ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./package.json ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./package-lock.json ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/
    scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./vite.config.js ruben@10.61.13.5:/home/ruben/FEUP/PT-Pump-Up/src/laravel-test/

    ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "cd /home/ruben/FEUP/PT-Pump-Up/src/laravel-test && docker compose down && docker compose up -d"
fi

echo "Finished"
sleep 3