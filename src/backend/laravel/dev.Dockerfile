FROM php:8.3-fpm

WORKDIR /app

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

RUN apt-get update 

RUN apt-get install npm -y --fix-missing

RUN apt-get install -y \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl \
    libzip-dev
    
RUN docker-php-ext-install mysqli pdo pdo_mysql

COPY package.json package-lock.json composer.json composer.lock ./docker-entrypoint.sh /app/

RUN composer update --no-autoloader --no-scripts

RUN composer install --no-autoloader --no-scripts

RUN npm install

# Hotfix for Sanctum Work with MongoDB
#RUN sed 's/Illuminate\\Database/MongoDB\\Laravel\\/' vendor/laravel/sanctum/src/PersonalAccessToken.php

ENTRYPOINT [ "./docker-entrypoint.sh"]