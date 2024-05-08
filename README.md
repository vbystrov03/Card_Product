# Программа для создания карточек продуктов из БД Postgresql

Эта программа предназначена для работы с базой данных Postgresql и создания карточек продуктов.

## Используемые технологии

Программа разработана с использованием следующих технологий:

- Postgresql 16
- Ubuntu Server
- PyCharm

## Инструкция по установке и настройке

1. Установите Postgresql на Ubuntu и разрешите подключения к базе данных, отредактировав конфигурационный файл.
`sudo apt-get update`<br/>
`sudo apt-get install postgresql-std-16`<br/>
`sudo nano /var/lib/pgpro/std-16/data/postgresql.conf`<br/>

Меняем эту строчку:
`listen_addresses = '*'`<br/>

2. Создайте базу данных с таблицами.<br/>
`CREATE DATABASE test;
 CREATE TABLE products (
 product_id SERIAL PRIMARY KEY,
 name VARCHAR(255) NOT NULL,
 description TEXT,
 price NUMERIC(10, 2) NOT NULL,
 quantity INTEGER NOT NULL CHECK (quantity > 0),
 image_url VARCHAR(255),
 category_id INTEGER REFERENCES categories(category_id)
 );`<br/>
 
3. В файле "test.py" поменяйте сетевые настройки сервера базы данных.<br/>
`conn = psycopg2.connect(dbname="name_db", host='ip_address', user='admin', password='admin', port=5432)`

5. В файле "index.html" отредактируйте ссылки в разделе контактов.<br/>
`<div class="phone">Phone: +79999999999</div>`<br/>
`<div class="email">Email: info@example.com</div>`<br/>
`<a href="https://t.me/"><img src="telega.png" alt="Telegram"></a>`<br/>
`<a href="https://wa.me/"><img src="wha.png" alt="WhatsApp"></a>`<br/>

## Поддержка и контакты

Если у вас возникли вопросы или проблемы с использованием программы, пожалуйста, свяжитесь со мной:

- Email: vladimir.bystrov20180@yadnex.ru
- Telegram: https://t.me/vbystrov1
