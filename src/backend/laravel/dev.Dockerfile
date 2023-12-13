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

COPY . .

RUN composer update

RUN composer install

RUN npm install

RUN npm run build

ENTRYPOINT [ "php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]