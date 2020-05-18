import os
import sqlite3

base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = base_dir.replace("db_conf", "alegrosz")
path = os.path.join(base_dir, 'db', 'alegrosz.db')

# TODO find in os how to travers file's structure
conn = sqlite3.connect(path)
c = conn.cursor()

def show_results(data):
    if data == "items":
        return show_items()


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

# TODO jak odpale show_tables jako script w termnalu to ma mnie zapytać którą tabelę chce zobaczyć a następnie wyślwieltlić tylko ta jedną


def show_categories():
    categories = c.execute("""SELECT
        c.name, c.id
        FROM
        categories AS c
    """)

    print("CATEGORY")
    print(f"{'#' * 40}")
    for row in categories:
        print(f"category_name: {row[0]} ({row[1]})")
        print(f"{'#' * 40}")


def show_subcategories():
    subcategories = c.execute("""SELECT
        s.name, s.id, c.name, c.id
        FROM
        subcategories AS s
        INNER JOIN categories AS c ON s.category_id = c.id
    """)

    print("SUBCATEGORY")
    print(f"{'#' * 40}")
    for row in subcategories:
        print(f"subcategory name: {row[0]} ({row[1]})")
        print(f"category name: {row[2]} ({row[3]})")


def show_comments():
    comments = c.execute("""SELECT
        cm.id, cm.content, i.id, i.title
        FROM
        comments AS cm
        INNER JOIN items AS i ON cm.item_id = i.id
    """)

    print("COMMENTS")
    print(f"{'#' * 40}")
    for row in comments:
        print(f"comment_id: {row[0]}")
        print(f"content: {row[1]}")
        print(f"item_id: {row[2]}")
        print(f"item_title: {row[3]}")
        print(f"{'#' * 40}")
