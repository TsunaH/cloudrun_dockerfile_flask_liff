"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template
from flask_restful import Api, Resource

# API用Router
from router import router


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
