import os

from flask import Blueprint

router = Blueprint('router', __name__)


@router.route('/', defaults={'path': ''})
@router.route('/<path>')
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


@router.route('/api/apitest', methods=['GET'])
def apitest():
    text = "apiからの返却値"
    return text
