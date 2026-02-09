from flask import Blueprint, request
from services.auth_service import login

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login_route():
    return login(
        request.json.get("user_id"),
        request.headers.get("X-Device-ID")
    )
