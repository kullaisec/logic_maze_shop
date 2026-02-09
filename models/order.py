def create_order(user_id, total):
    return {
        "user_id": user_id,
        "total": total,
        "status": "PENDING"
    }
