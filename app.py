"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template
from flask_restful import Api, Resource

# API用Router
from api.router import router


# pylint: disable=C0103
def create_app():
    # Flask Appインスタンス生成
    app = Flask(__name__, template_folder='templates/liff-test/dist', static_folder='templates/liff-test/dist', static_url_path='')

    # DB設定
    # app.config.from_object(config.Config)
    # db.init_db(app)
    # db.init_ma(app)

    # APIのRouter設定
    app.register_blueprint(router)
    return app


# アプリ生成
app = create_app()
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')


@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def main(path):
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template("index.html",
        message=message,
        Service=service,
        Revision=revision)
