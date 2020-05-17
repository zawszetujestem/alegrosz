import os
import sqlite3

base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = base_dir.replace("db_conf", "alegrosz")
path = os.path.join(base_dir, 'db', 'alegrosz.db')

# TODO find in os how to travers file's structure
print(path)
conn = sqlite3.connect(path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS items")
c.execute("DROP TABLE IF EXISTS categories")
c.execute("DROP TABLE IF EXISTS subcategories")
c.execute("DROP TABLE IF EXISTS comments")

c.execute("""CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)""")

c.execute("""CREATE TABLE subcategories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category_id INTIGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)""")

c.execute("""CREATE TABLE items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    prize REAL,
    image TEXT,
    category_id INTEGER,
    subcategory_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
    FOREIGN KEY(subcategory_id) REFERENCES subcategories(id)
)""")

c.execute("""CREATE TABLE comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    item_id INTEGER,
    FOREIGN KEY(item_id) REFERENCES items(id)
)""")

categories = [("books",), ("movies",), ("music",)]

c.executemany("INSERT INTO categories (name) VALUES (?)", categories)

subcategories = [("action", 1),
                 ("war", 1),
                 ("comedy", 2),
                 ("animation", 2),
                 ("pop", 3),
                 ("rock", 3),
                 ("electro", 3),
                 ("disco", 3)]

c.executemany("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", subcategories)

items = [
    ("action_book_1", "best action book", 35.04, "", 1, 1),
    ("war_book_1", "best war book", 33.36, "", 1, 2),
    ("comedy_movie_1", "best comedy movie", 45.54, "", 2, 1),
    ("animation_movie_1", "best animation movie", 57.90, "", 2, 2),
    ("pop_music_1", "best pop song", 11.76, "", 3, 1),
    ("rock_music_1", "best rock song", 10.99, "", 3, 2),
    ("electro_music_1", "best electro song", 20.56, "", 3, 3),
    ("disco_music_1", "best disco song", 27.99, "", 3, 4)
]

c.executemany("INSERT INTO items (title, description, prize, image, category_id, subcategory_id) VALUES (?, ?, ?, ?, ?, ?)", items)


comments = [
    ("Best book", 1),
    ("Best movie", 4),
    ("Best music", 6)
]


c.executemany("INSERT INTO comments (content, item_id) VALUES (?, ?)", comments)


conn.commit()
conn.close()

print('Database is created and initialize')
