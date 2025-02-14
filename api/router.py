from flask import Blueprint

router = Blueprint('router', __name__)


@router.route('/api/apitest', methods=['GET'])
def apitest():
    text = "apiからの返却値"
    return text
