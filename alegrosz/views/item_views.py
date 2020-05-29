from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect, unescape

from alegrosz.db.db import get_db
from alegrosz.forms.category_form import CategoryForm
from alegrosz.forms.comments_form import NewCommentForm
from alegrosz.forms.item_form import NewItemForm, EditItemForm, RemoveItemForm
from alegrosz.helpers.images import save_image_upload

items_bp = Blueprint("items", __name__, url_prefix="/items")


@items_bp.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    removeItemForm = RemoveItemForm()
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

    try:
        item = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "price": row[3],
            'image': row[4],
            "category": row[5],
            "subcategory": row[6]
        }

    except TypeError:
        item = {}

    comments = []

    if item:
        comments_from_db = c.execute("""SELECT content FROM comments
        WHERE item_id = ? 
        ORDER BY id DESC
        """, (item_id,))
        comments = [{"content": row[0]} for row in comments_from_db]

    commentForm = NewCommentForm()
    commentForm.item_id.data = item_id
    return render_template('/item.html', item=item, removeItemForm=removeItemForm, commentForm=commentForm,
                           comments=comments)


@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    form = CategoryForm()
    conn = get_db()
    c = conn.cursor()

    c.execute("""SELECT id, name FROM categories""")
    categories = c.fetchall()
    form.category.choices = categories

    c.execute("""SELECT id, name FROM subcategories WHERE category_id = ?""", (1,))
    subcategories = c.fetchall()
    form.subcategory.choices = subcategories

    if request.method == 'POST':
        filename = ""
        if form.image.data:
            filename = save_image_upload(form.image.data)
        c.execute("""INSERT INTO items(title, description, price, image, category_id, subcategory_id) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            form.title.data,
            form.description.data,
            float(form.price.data),
            filename,
            form.category.data,
            form.subcategory.data
        ))

        conn.commit()
        flash(f"Item {form.title.data} has been successfully added.", "success")
        return redirect(url_for('main.index'))

    return render_template('add.html', form=form)


@items_bp.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    conn = get_db()
    c = conn.cursor()
    item_from_db = c.execute("""SELECT * FROM items WHERE id = ?""", (item_id,))
    row =c.fetchone()

    try:
        item = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "price": row[3],
            'image': row[4]
        }
    except TypeError:
        item = {}



    if item:
        form = EditItemForm()
        if form.validate_on_submit():
            filename = item['image']

            if form.image.data:
                filename = save_image_upload(form.image.data)

            c.execute("""UPDATE items SET
            title = ?,
            description = ?,
            price = ?,
            image = ? WHERE id = ?
            """, (
                form.title.data,
                form.description.data,
                float(form.price.data),
                filename,
                item_id
            ))
            conn.commit()

            flash(f"Item {form.title.data} has been successfully edited.", "success")
            return redirect(url_for('items.get_item', item_id=item_id))

        form.title.data = item["title"]
        form.description.data = unescape(item["description"])
        form.price.data = item["price"]

        if form.errors:
            flash("{form.error}", "danger")

        return render_template('edit.html', form=form, item=item)

    return redirect(url_for("main.index"))


@items_bp.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    conn = get_db()
    c = conn.cursor()
    item_from_db = c.execute("""SELECT * FROM items WHERE id = ?""", (item_id,))
    row =c.fetchone()


    try:
        item = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "price": row[3],
            'image': row[4]
        }
    except TypeError:
        item = {}

    if item:
        c.execute("""DELETE FROM items WHERE id = ?""", (item_id,))
        conn.commit()

        flash(f"Item {item['title']} has been successfully removed.", "success")
    else:
        flash(f"This item does not exist", "danger")
    return redirect(url_for('main.index'))
