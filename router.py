import os

from flask import Blueprint
from flask import Flask, render_template, request

# 顧客情報用の処理
from api import member

router = Blueprint('router', __name__)

collection = None

@router.route('/', defaults={'path': ''})
@router.route('/<path>')
def main(path):
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    # コレクション取得
    global collection
    collection = request.args.get("cd")

    return render_template("index.html",
        message=message,
        Service=service,
        Revision=revision)


@router.route('/api/apitest', methods=['POST'])
def apitest():
    # global collection
    result = member.getMemberInfo(collection)
    return result
