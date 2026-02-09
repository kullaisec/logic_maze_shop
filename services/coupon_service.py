USED_COUPONS = set()

def apply_coupon(code, total):
    if code in USED_COUPONS:
        return total

    if code.startswith("SAVE"):
        discount = int(code.replace("SAVE", ""))
        USED_COUPONS.add(code)
        return max(total - discount, 0)

    return total
