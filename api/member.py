from flask import jsonify


def getMemberInfo():
    data = {
      'name': 'apiName',
      'email': 'apiMail',
      'points': 23232,
      'note': 'apiNote',
    }
    return jsonify(data), 200
