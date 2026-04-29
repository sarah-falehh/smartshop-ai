"""
Objectif 4 — Automatic product categorization  [STUB]
=======================================================
Replace stub with CLIP zero-shot classification.
Endpoint contract: POST /api/categorize
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("categorization", __name__)

CATEGORIES = ["electronics", "furniture", "clothing", "food", "sports", "books", "toys", "beauty"]


@bp.route("/categorize", methods=["POST"])
def categorize():
    """
    Expected body: { "image_path": "static/images/prod_001.jpg" }
    Expected response: { "category": "electronics", "confidence": 0.94 }
    """
    data = request.get_json()
    image_path = data.get("image_path")

    if not image_path:
        return jsonify({"error": "image_path is required"}), 400

    # ── TODO: load CLIP, encode image + category labels, return argmax ──────
    # import clip, torch
    # model, preprocess = clip.load("ViT-B/32")
    # ...
    category   = "electronics"   # stub
    confidence = 0.94            # stub
    # ────────────────────────────────────────────────────────────────────────

    return jsonify({"category": category, "confidence": confidence})
