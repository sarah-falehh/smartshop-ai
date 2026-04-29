"""
sentiment/routes.py
====================
Flask blueprint for Objective 2 — Sentiment Analysis.

Endpoints:
  POST /api/sentiment/<id> → analyze reviews of a product + persist result
"""

from flask import Blueprint, request, jsonify
from database import get_product, update_product

bp = Blueprint("sentiment", __name__)

@bp.route("/sentiment/product_id/", methods=["POST"])
def sentiment(product_id):
    """
    Analyze the reviews of a product from the catalogue,
    then persist the sentiment score back into products.json.

    Response:
    {
      "product_id": "prod_001",
      "score": 0.88,
      "label": "positive",
    }
    """
    product = get_product(product_id)
    
    # TODO: Get the result from the product reviews
    score = 0.55
    label = "neutral"

    # Persist into the shared catalogue
    update_product(product_id, {
        "sentiment_score": score,
        "sentiment_label": label,
    })

    return jsonify({
        "product_id": product_id,
        "sentiment_score": score,
        "sentiment_label": label,
    })
