"""
Objectif 3 — Visual product recommendations  [STUB]
=====================================================
Replace stub with ResNet-50 embedding extraction + cosine similarity.
Endpoint contract: GET /api/similar/<product_id>
"""

from flask import Blueprint, jsonify

bp = Blueprint("recommendations", __name__)


@bp.route("/similar/<product_id>", methods=["GET"])
def get_similar(product_id: str):
    """
    Expected response:
    {
      "product_id": "prod_001",
      "similar": [
        { "id": "prod_002", "name": "...", "score": 0.91 },
        ...
      ]
    }
    """
    # ── TODO: extract embedding for product_id, compute cosine similarity ──
    stub_similar = [
        {"id": "prod_002", "name": "Ergonomic Office Chair", "score": 0.87},
        {"id": "prod_003", "name": "Slim Fit Denim Jacket",  "score": 0.74},
    ]
    # ───────────────────────────────────────────────────────────────────────

    return jsonify({"product_id": product_id, "similar": stub_similar})
