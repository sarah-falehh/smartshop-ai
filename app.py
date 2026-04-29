"""
main.py — SmartShop AI entry point
====================================
The integration lead owns this file.
Add a new blueprint here when a module is ready.
"""

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# ── Import blueprints (swap stubs for real ones as modules are completed) ──
from alt_text.routes       import bp as alt_text_bp
from sentiment.routes      import bp as sentiment_bp
from recommendations.routes import bp as recommendations_bp
from categorization.routes  import bp as categorization_bp
from chatbot.routes         import bp as chatbot_bp
from defect_detection.routes import bp as defect_bp

app = Flask(__name__, static_folder="static")
CORS(app)  # allow the frontend to call the API

# ── Register blueprints ────────────────────────────────────────────────────
app.register_blueprint(alt_text_bp,        url_prefix="/api")
app.register_blueprint(sentiment_bp,       url_prefix="/api")
app.register_blueprint(recommendations_bp, url_prefix="/api")
app.register_blueprint(categorization_bp,  url_prefix="/api")
app.register_blueprint(chatbot_bp,         url_prefix="/api")
app.register_blueprint(defect_bp,          url_prefix="/api")

# ── Healthcheck ────────────────────────────────────────────────────────────
@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "platform": "SmartShop AI"})

# ── Serve the frontend ─────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
