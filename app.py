from flask import request, jsonify
from config import app, db
from models import Key


@app.route("/api/keys", methods=["GET"])
def getKeys():
    keys = Key.query.all()
    json_keys = [x.to_json() for x in keys]  # list(map(lambda x: x.to_json(), keys))
    return jsonify({"keys": json_keys})


@app.route("/api/add", methods=["POST"])
def addKey():
    key = request.json.get("key")
    # account = request.json.get("account")
    if not key:
        return jsonify({"message": "Activation key must be provided"}), 400

    new_key = Key(activation_key=key)

    try:
        db.session.add(new_key)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "key successfully added"}), 201


@app.route("/api/update/<string:key>", methods=["PUT"])
def update_key(key):
    key = Key.query.filter_by(activation_key=key).first()
    if not key:
        return jsonify({"message": "invalid key"})

    data = request.json
    key.account = data.get("account", key.account)
    key.created_at = data.get("date", key.created_at)

    db.session.commit()

    return jsonify({"message": "key activated successfully!"}), 200


@app.route("/api/delete/<string:key>", methods=["DELETE"])
def deleteKey(key):
    key = Key.query.filter_by(activation_key=key).first()
    if not key:
        return jsonify({"message": "invalid key"})

    db.session.delete(key)
    db.session.commit()

    return jsonify({"message": "key deleted!"}), 200


if __name__ == "__main__":

    app.run()
