import psycopg2

username = 'postgres'
password = 'andron112233andy'
database = 'lab_2_database'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT artist_name, COUNT(painting_name) FROM the_most_famous_painting LEFT JOIN  artist ON the_most_famous_painting.painting_id =  artist.artist_id GROUP BY artist_name
'''

query_2 = '''
SELECT genre, COUNT(genre_id) FROM genre INNER JOIN bio USING(genre_id) GROUP BY genre
'''
query_3 = '''
SELECT genre_name, COUNT(about_bio) FROM bio LEFT JOIN genre ON bio.genre_id = genre.genre_id GROUP BY genre_name
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    print('\nquery 1:')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\nquery 2:')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\nquery 3:')
    cur.execute(query_3)
    for row in cur:
        print(row)
