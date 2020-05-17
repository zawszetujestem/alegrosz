import os
import sqlite3

base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = base_dir.replace("db_conf", "alegrosz")
path = os.path.join(base_dir, 'db', 'alegrosz.db')

# TODO find in os how to travers file's structure
conn = sqlite3.connect(path)
c = conn.cursor()

def show_items():
    items = c.execute("""SELECT
        i.id, i.title, i.description, i.prize, i.image, c.name, c.id, s.name, s.id
        FROM
        items AS i
        INNER JOIN categories AS c ON i.category_id = c.id
        INNER JOIN subcategories AS s ON i.subcategory_id = s.id
    """)

    print("ITEMS")
    print(f"{'#' * 40}")
    for row in items:
        print(f"id: {row[0]}")
        print(f"title: {row[1]}")
        print(f"description: {row[2]}")
        print(f"prize: {row[3]}")
        print(f"image: {row[4]}")
        print(f"category name: {row[5]} ({row[6]})")
        print(f"subcategory name: {row[7]} ({row[8]})")
        print(f"{'#' * 40}")

# TODO write 3 functions (show_categories, show_subcategories, show_comments)
# TODO jak odpale show_tables jako script w termnalu to ma mnie zapytać którą tabelę chce zobaczyć a następnie wyślwieltlić tylko ta jedną
