from flask import Blueprint, render_template

from alegrosz.db.db import get_db

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/")
def index():
    conn = get_db()
    c = conn.cursor()

    items_form_db = c.execute("""SELECT
        i.id, i.title, i.description, i.price, i.image, c.name, s.name
        FROM
        items AS i
        INNER JOIN categories AS c ON i.category_id = c.id
        INNER JOIN subcategories AS s ON i.subcategory_id = s.id
        ORDER BY i.id DESC
    """)

    items = []
    for row in items_form_db:
        item = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "price": row[3],
            'image': row[4],
            "category": row[5],
            "subcategory": row[6]
        }
        items.append(item)

    return render_template("index.html", items=items)


@main_bp.errorhandler(404)
def not_found(exception):
    return "Page not found"


@main_bp.errorhandler(500)
def server_not_found(exception):
    return "Internal server error"
