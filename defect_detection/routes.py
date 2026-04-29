"""
Objectif 6 — Defective image detection  [STUB]
================================================
Replace stub with OpenCV heuristics or a trained binary classifier.
Endpoint contract: POST /api/check-image
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("defect_detection", __name__)


@bp.route("/check-image", methods=["POST"])
def check_image():
    """
    Expected body: { "image_path": "static/images/prod_001.jpg" }
    Expected response:
    {
      "ok": true,
      "reason": null
    }
    — or —
    {
      "ok": false,
      "reason": "Image is too blurry (variance: 12.3)"
    }
    """
    data = request.get_json()
    image_path = data.get("image_path")

    if not image_path:
        return jsonify({"error": "image_path is required"}), 400

    # ── TODO: compute Laplacian variance for blur, check brightness, etc. ───
    # import cv2, numpy as np
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # blur_score = cv2.Laplacian(img, cv2.CV_64F).var()
    # if blur_score < 100: return {"ok": False, "reason": f"Too blurry ({blur_score:.1f})"}
    ok     = True   # stub
    reason = None   # stub
    # ────────────────────────────────────────────────────────────────────────

    return jsonify({"ok": ok, "reason": reason})
