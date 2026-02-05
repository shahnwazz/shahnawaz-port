from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    try:
        data = request.get_json(force=True)
        message = data.get("message")

        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(message.strip() + "\n---\n")

        return jsonify({
            "status": "success",
            "message": "✅ Message sent anonymously!"
        }), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "status": "error",
            "message": "Server error"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    try:
        data = request.get_json(force=True)
        message = data.get("message")

        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(message.strip() + "\n---\n")

        return jsonify({
            "status": "success",
            "message": "✅ Message sent anonymously!"
        }), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "status": "error",
            "message": "Server error"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    try:
        data = request.get_json(force=True)
        message = data.get("message")

        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(message.strip() + "\n---\n")

        return jsonify({
            "status": "success",
            "message": "✅ Message sent anonymously!"
        }), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "status": "error",
            "message": "Server error"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
