from flask import Flask, request,render_template, redirect, url_for, flash
import requests
from resources.item import blp as ItemBluePrint
from resources.user import blp as UserBluePrint
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST

app = Flask(__name__)
#configuration 
app.config["PROGATE_EXCEPRIONS"]=True
app.config["API_TITLE"]="Items Rest API"
app.config["API_VERSION"]="v1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPENAPI_URL_PREFIX"]="/"
app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui" #url jaha per humjaake dcumentation show honge
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  #i get proper ui... jo uska code hai vo is url pe likha hai

app.config["JWT_SECRET_KEY"]="1328588524410703591907289438365903699"

api = Api(app)
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_blocklist_in_loader(jwt_header, jwt_playload):
    return jwt_playload['jti'] in BLOCKLIST

@jwt.revoked_token_loader
def revoke_token_callback(jwt_header, jwt_playload):
    return (
        {
            "description":"User has been logged out",
            "error":"token_revoked"
        },
        401
    )


api.register_blueprint(ItemBluePrint) #to register the bluePrint
api.register_blueprint(UserBluePrint)


# ---------------- FRONTEND ROUTES ----------------
API_BASE = "http://localhost:5000"  # Change if deployed

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/items")
def items_page():
    try:
        res = requests.get(f"{API_BASE}/item")  # Calling your REST API
        items = res.json()
    except Exception:
        items = []
    return render_template("items.html", items=items)

@app.route("/add-item", methods=["GET", "POST"])
def add_item_page():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        payload = {"name": name, "price": float(price)}
        res = requests.post(f"{API_BASE}/item", json=payload)
        if res.status_code == 201:
            flash("Item added successfully!", "success")
            return redirect(url_for("items_page"))
        else:
            flash("Failed to add item", "danger")
    return render_template("add_item.html")
