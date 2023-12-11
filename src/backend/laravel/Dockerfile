FROM php:8.3-fpm-alpine

WORKDIR /app

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

RUN apk add npm

COPY composer.json .
COPY composer.lock .
COPY artisan .

COPY package.json .

RUN composer install --no-scripts --no-autoloader --no-interaction --prefer-dist

RUN npm install

ENTRYPOINT [ "php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]