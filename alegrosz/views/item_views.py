from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from alegrosz.db.db import get_db
from alegrosz.forms.item_form import NewItemForm

items_bp = Blueprint("items", __name__, url_prefix="/items")


@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    form = NewItemForm()
    conn = get_db()
    c = conn.cursor()

    if request.method == 'POST':
        c.execute("""INSERT INTO items(title, description, price, image, category_id, subcategory_id) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            form.title.data,
            form.description.data,
            float(form.price.data),
            "",
            1,
            1
        ))

        conn.commit()

        return redirect(url_for('main.index'))
    return render_template('add.html', form=form)


@items_bp.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    c = get_db().cursor()
    row = []
    item_from_db = c.execute("""SELECT
                               i.id, i.title, i.description, i.price, i.image, c.name, s.name
                               FROM
                               items AS i
                               INNER JOIN categories AS c ON i.category_id = c.id
                               INNER JOIN subcategories AS s ON i.subcategory_id = s.id
                               WHERE i.id = ?""",
                   (item_id,))

    row = c.fetchone()

    item = {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "price": row[3],
        'image': row[4],
        "category": row[5],
        "subcategory": row[6]
    }

    return render_template('/item.html', item=item)