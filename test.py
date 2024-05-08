from jinja2 import Template
import psycopg2


"""print('Напишите адрес сервера и порт. (через пробел)')
ip_add = input().split()
print('Напишите имя пользователя и пароль для подключения к БД. (через пробел)')
name = input().split()"""

def click_btn():
    print('123')

try:
    # Подключение к базе данных
    conn = psycopg2.connect(dbname="my_ecommerce_db", host='192.168.120.143', user='admin', password='admin', port=5432)
    cursor = conn.cursor()

    for j in range(10):
        # Получение информации о товаре из базы данных
        cursor.execute(f"SELECT  *  FROM products WHERE product_id = {j} AND category_id = 2")
        result = cursor.fetchone()
        if result:
            product = dict(zip([i[0] for i in cursor.description], result))
        else:
            continue

        # Загрузка HTML шаблона
        with open('index.html') as file:
            template = Template(file.read())

        # Заполнение шаблона информацией о товаре
        output = template.render(product=product)

        # Создание HTML файла
        with open(f'{result[1]}.html', 'w') as file:
            file.write(output)

    print('Карточки товаров созданы.')

except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
