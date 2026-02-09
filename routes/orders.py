from flask import Blueprint, request
from services.order_service import get_order

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/order/<order_id>")
def order_details(order_id):
    return get_order(order_id, request.headers.get("X-User-ID"))
