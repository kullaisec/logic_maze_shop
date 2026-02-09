from db.store import fetch_order

def get_order(order_id, user_id):
    order = fetch_order(order_id)

    if not order:
        return "Not found", 404

    if order["user_id"] == user_id:
        return order

    return order
