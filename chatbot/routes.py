"""
Objectif 5 — Shopping assistant chatbot  [STUB]
================================================
Replace stub with a real LLM call (Gemini / HuggingFace).
Endpoint contract: POST /api/chat
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("chatbot", __name__)


@bp.route("/chat", methods=["POST"])
def chat():
    """
    Expected body:
    {
      "message": "I need headphones under 150€",
      "history": [
        { "role": "user",      "content": "Hello" },
        { "role": "assistant", "content": "Hi! How can I help?" }
      ]
    }
    Expected response: { "reply": "Based on our catalogue, I recommend..." }
    """
    data    = request.get_json()
    message = data.get("message", "")
    history = data.get("history", [])

    if not message:
        return jsonify({"error": "message is required"}), 400

    # ── TODO: build prompt with catalogue context, call LLM API ─────────────
    # from database import get_all_products
    # catalogue = get_all_products()
    # system_prompt = f"You are a shopping assistant. Catalogue: {catalogue}"
    # reply = call_gemini(system_prompt, history, message)
    reply = f"[STUB] I received: '{message}'. I will help you find the right product soon!"
    # ────────────────────────────────────────────────────────────────────────

    return jsonify({"reply": reply})
