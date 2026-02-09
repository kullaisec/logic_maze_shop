from db.store import get_user, bind_device

def login(user_id, device_id):
    user = get_user(user_id)

    if not user:
        return "Invalid user", 401

    if not user.get("device_id"):
        bind_device(user_id, device_id)
        return "Logged in (new device)"

    if user["device_id"] == device_id:
        return "Logged in"

    return "New device detected", 403
