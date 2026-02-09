def is_admin(user):
    return "admin" in user.get("role", "")
