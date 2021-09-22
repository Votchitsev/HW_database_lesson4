import sqlalchemy
print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql://votchitsev:55555@localhost:5432/Music_Platform')
connection = engine.connect()


select_1 = connection.execute("SELECT album_title, release_year FROM album WHERE release_year = 2018;").fetchall()
print('Запрос 1 - ', select_1)

select_2 = connection.execute("SELECT track_title, len FROM track ORDER BY len DESC;").fetchone()
print('Запрос 2 - ', select_2)

select_3 = connection.execute("SELECT track_title FROM track WHERE len >= 150;").fetchall()
print('Запрос 3 - ', select_3)

select_4 = connection.execute("SELECT name FROM collection WHERE release_year >= 2018 and release_year <= 2020;").\
    fetchall()
print('Запрос 4 - ', select_4)

select_5 = connection.execute("SELECT name FROM artist WHERE (LENGTH(name) - LENGTH(replace(name, '_', ''))) = 0").\
    fetchall()
print('Запрос 5 - ', select_5)

select_6 = connection.execute("SELECT track_title FROM track WHERE track_title LIKE '%%Love%%'").fetchall()
print('Запрос 6 - ', select_6)
