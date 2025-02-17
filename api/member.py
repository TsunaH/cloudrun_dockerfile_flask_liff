from flask import jsonify

import logging
import google.cloud.logging

# Logger設定
logging.basicConfig(
        format="[%(asctime)s][%(levelname)s] %(message)s",
        level=logging.DEBUG
    )
logger = logging.getLogger()

# Cloud Logging ハンドラを logger に接続
logging_client = google.cloud.logging.Client()
logging_client.setup_logging()


def getMemberInfo():
    logger.info("getMemberInfo")
    data = {
      'name': 'apiName',
      'email': 'apiMail',
      'points': 23232,
      'note': 'apiNote',
    }
    logger.info(f"{data}")
    return jsonify(data), 200
