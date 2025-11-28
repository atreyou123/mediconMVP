from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from triage.classifier import TriageClassifier
from guidance.guidance import GuidanceModule
from booking.booking import BookingModule
from database.database import DatabaseModule

app = Flask(__name__)
CORS(app)

# Path to FRONT-END folder OUTSIDE backend
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend"))

triage = TriageClassifier()
guidance = GuidanceModule()
booking = BookingModule()
db = DatabaseModule()


# -------------------------------
# TRIAGE API
# -------------------------------
@app.route("/api/triage", methods=["POST"])
def triage_route():
    data = request.json
    symptom = data.get("symptom", "")
    level = triage.classify(symptom)
    recommendation = guidance.get_recommendation(level)
    db.save({"symptom": symptom, "level": level})
    return jsonify({"level": level, "recommendation": recommendation})


# -------------------------------
# BOOKING API
# -------------------------------
@app.route("/api/book", methods=["POST"])
def book_route():
    data = request.json
    name = data.get("name")
    symptom = data.get("symptom")
    result = booking.book(name, symptom)
    return jsonify({"message": result})


# -----------------------------------
# SERVE FRONTEND (index.html + assets)
# -----------------------------------
@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, "index.html")

@app.route("/<path:filename>")
def serve_static_files(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)


