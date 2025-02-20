import os

from urllib.parse import urlparse, parse_qs

from flask import Blueprint
from flask import Flask, render_template, request

# 顧客情報用の処理
from api import member

import logging
import google.cloud.logging
from google.cloud import firestore

# Logger設定
logging.basicConfig(
        format="[%(asctime)s][%(levelname)s] %(message)s",
        level=logging.DEBUG
    )
logger = logging.getLogger()

# Cloud Logging ハンドラを logger に接続
logging_client = google.cloud.logging.Client()
logging_client.setup_logging()


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
    query_param = parse_qs(urlparse(request.url).query)
    collection = query_param.get("cd")[0]
    logger.info("/_/_/_/_/ main() /_/_/_/_")
    logger.info(f"collection:{collection}")

    return render_template("index.html",
        message=message,
        Service=service,
        Revision=revision)


@router.route('/api/apitest', methods=['POST'])
def apitest():
    # global collection
    result = member.getMemberInfo(collection)
    return result
