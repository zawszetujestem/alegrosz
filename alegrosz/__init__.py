from flask import Flask, g


def create_app():
    alegrosz = Flask(__name__)

    from alegrosz.views.main_views import main_bp

    alegrosz.register_blueprint(main_bp)

    return alegrosz


app = create_app()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()