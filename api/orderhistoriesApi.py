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


def getOrderhistories(collection):
    logger.info(f"getOrderhistories url:{request.url}, params:{request.get_json()}, collection:{collection}")
    request_json = request.get_json()
    lineId = request_json.get('lineId')
    logger.info(f"lineId:{lineId}")
    db = firestore.Client()
    documentId = f"orderhistories_{lineId}"
    data = db.collection(collection).document(documentId).get().to_dict()
    logger.info(f"get data:{data}")
    logger.info(f"firestore:{data}")
    return jsonify(data), 200
