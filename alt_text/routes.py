"""
Objectif 1 — Alt-text generator  [STUB]
========================================
Replace the stub response with your ResNet-50 + Transformer model.
Endpoint contract: POST /api/alt-text
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("alt_text", __name__)


@bp.route("/alt-text", methods=["POST"])
def generate_alt_text():
    """
    Expected body: { "image_path": "static/images/prod_001.jpg" }
    Expected response: { "alt_text": "A pair of wireless headphones in black" }
    """
    data = request.get_json()
    image_path = data.get("image_path")

    if not image_path:
        return jsonify({"error": "image_path is required"}), 400

    # ── TODO: replace stub with your ResNet-50 + Transformer model ──────────
    alt_text = f"[STUB] Descriptive alt text for image: {image_path}"
    # ────────────────────────────────────────────────────────────────────────

    return jsonify({"alt_text": alt_text})
