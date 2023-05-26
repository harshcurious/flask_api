from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {"user_id": user_id, "name": "John Doe",
                 "email": "john.doe@gmail.com"}
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201


# Curl format:
# curl -X POST -H "Content-Type: application/json" -d '{"name": "linuxize", "email": "linuxize@example.com"}' http://127.0.0.1:5000/create-user

if __name__ == "__main__":
    app.run(debug=True)
