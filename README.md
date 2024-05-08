# Программа для создания карточек товаров из БД Postgresql

Создание карточек товаров с использованием данных из базы Postgresql - это процесс, который позволяет представить информацию о каждом продукте в удобном и структурированном виде. Эта программа помогает автоматизировать работу по созданию карточек, что значительно экономит время и повышает эффективность работы.

## Используемые технологии

Программа разработана с использованием следующих технологий:

- Postgresql 16
- Ubuntu Server
- PyCharm

## Инструкция по установке и настройке

### 1. Установите Postgresql на Ubuntu и разрешите подключения к базе данных, отредактировав конфигурационный файл.
`sudo apt-get update`<br/>
`sudo apt-get install postgresql-std-16`<br/>
`sudo nano /var/lib/pgpro/std-16/data/postgresql.conf`<br/>

Меняем эту строчку:
`listen_addresses = '*'`<br/>

### 2. Создайте базу данных с таблицами.<br/>
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
 
`CREATE TABLE categories (
 category_id SERIAL PRIMARY KEY,
 name VARCHAR(255) NOT NULL
 );`<br/>
 
### 3. В файле "test.py" поменяйте сетевые настройки сервера базы данных.<br/>

`conn = psycopg2.connect(dbname="name_db", host='ip_address', user='admin', password='admin', port=5432)`

### 4. Указать количество и каким товарам создаем карточки.
   
 Указываем количество товара.

`for j in range(10):`<br/>

 В `category_id` указываем порядковый номер категории.<br/>
 
`cursor.execute(f"SELECT  *  FROM products WHERE product_id = {j} AND category_id = 2")`<br/>

### 5. В файле "index.html" отредактируйте ссылки в разделе контактов.<br/>
`<div class="phone">Phone: +79999999999</div>`<br/>
`<div class="email">Email: info@example.com</div>`<br/>
`<a href="https://t.me/"><img src="telega.png" alt="Telegram"></a>`<br/>
`<a href="https://wa.me/"><img src="wha.png" alt="WhatsApp"></a>`<br/>

## Поддержка и контакты

Если у вас возникли вопросы или проблемы с использованием программы, пожалуйста, свяжитесь со мной:

- Email: vladimir.bystrov20180@yadnex.ru
- Telegram: https://t.me/vbystrov1
