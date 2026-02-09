from flask import Flask
from routes.auth import auth_bp
from routes.orders import orders_bp
from routes.coupons import coupons_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(coupons_bp)

if __name__ == "__main__":
    app.run()
