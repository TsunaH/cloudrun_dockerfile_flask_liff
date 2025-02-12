"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__, template_folder='templates/liff-test/dist', static_folder='templates/liff-test/dist', static_url_path='')


@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def hello(path):
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template("index.html",
        message=message,
        Service=service,
        Revision=revision)


@app.route('/vue')
def vue():
    return render_template('liff-test/test.html')


@app.route("/liff-test/<path>")
def path(path):
    return render_template(f"liff-test/{path}")


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
