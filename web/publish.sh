#!/bin/bash

if [ "$1" == "production" ]; then
    echo "Running in production mode"
    path="/home/ruben/FEUP/PT-Pump-Up/src/laravel"
else
    echo "Running in development mode"
    path="/home/ruben/FEUP/PT-Pump-Up/src/laravel-test"

fi

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r $path/app/"
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./app ruben@10.61.13.5:$path/

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r $path/bootstrap/"
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./bootstrap ruben@10.61.13.5:$path/

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r $path/config/"
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./config ruben@10.61.13.5:$path/

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r $path/database/"
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./database ruben@10.61.13.5:$path/

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r $path/resources/"
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./resources ruben@10.61.13.5:$path/

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "rm -r $path/routes/"
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up -r ./routes ruben@10.61.13.5:$path/

scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./storage/app/public/* ruben@10.61.13.5:$path/storage/app/public

scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./composer.json ruben@10.61.13.5:$path/
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./composer.lock ruben@10.61.13.5:$path/
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./package.json ruben@10.61.13.5:$path/
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./package-lock.json ruben@10.61.13.5:$path/
scp -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ./vite.config.js ruben@10.61.13.5:$path/

ssh -i ~/.ssh/INESC/pt-pump-up/pt-pump-up ruben@10.61.13.5 "cd /home/ruben/FEUP/PT-Pump-Up/src/laravel-test && docker compose down && docker compose up -d"


echo "Finished"
sleep 3