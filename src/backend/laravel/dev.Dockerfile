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


RUN pecl install mongodb

RUN docker-php-ext-enable mongodb

COPY package.json package-lock.json composer.json composer.lock ./docker-entrypoint.sh /app/

RUN composer install --no-autoloader

RUN npm install

# Hotfix for Sanctum Work with MongoDB
RUN sed 's/Illuminate\\Database/MongoDB\\Laravel\\/' vendor/laravel/sanctum/src/PersonalAccessToken.php

ENTRYPOINT [ "./docker-entrypoint.sh"]