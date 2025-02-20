from flask import jsonify, request

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


def getMemberInfo(collection):
    logger.info(f"getMemberInfo url:{request.url}, params:{request.get_json()}")
    request_json = request.get_json()
    lineId = request_json.get('lineId')

    db = firestore.Client()
    data = db.collection(collection).document(lineId).get().to_dict()
    logger.info(f"firestore:{data}")
    return jsonify(data), 200
