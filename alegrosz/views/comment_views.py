from flask import Blueprint, render_template, url_for
from werkzeug.utils import escape, redirect

from alegrosz.db.db import get_db
from alegrosz.forms.comments_form import NewCommentForm

comment_bp = Blueprint("comment", __name__, url_prefix="/comments")

@comment_bp.route('/add', methods=['POST'])
def add_comment():
    conn = get_db()
    c = conn.cursor()
    form = NewCommentForm()

    if form.validate_on_submit():
        c.execute("""INSERT INTO comments (content, item_id) VALUES (?, ?)""",
                  (
                      escape(form.content.data),
                      form.item_id.data
                  )
                  )
        conn.commit()

       # return render_template("/_comment.html", content=form.content.data)
    return redirect(url_for("items.get_item", item_id=form.item_id.data))