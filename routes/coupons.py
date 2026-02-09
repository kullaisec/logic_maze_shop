from flask import Blueprint, request
from services.coupon_service import apply_coupon

coupons_bp = Blueprint("coupons", __name__)

@coupons_bp.route("/apply-coupon", methods=["POST"])
def apply():
    return apply_coupon(
        request.json.get("coupon"),
        request.json.get("order_total")
    )
