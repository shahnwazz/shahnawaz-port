from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

# 📧 LOCAL EMAIL CONFIG
EMAIL_USER = "shahnwazmohmmad@gmail.com"
EMAIL_PASS = "pbmhhhlggtlmcddm"
EMAIL_TO   = "shahnwazmohmmad@gmail.com"

def send_email_alert(message):
    try:
        msg = EmailMessage()
        msg["Subject"] = "📩 New Anonymous Message (Local)"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO
        msg.set_content(
            f"You received a new anonymous message:\n\n{message}"
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
    except Exception as e:
        print("Email error:", e)

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

        send_email_alert(message)

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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
