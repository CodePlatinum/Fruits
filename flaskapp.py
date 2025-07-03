from flask import Flask, render_template, request

app = Flask(__name__)

fruits = [
    {"name": "Яблуко", "color": "#e74c3c", "description": "Смачне червоне яблуко."},
    {"name": "Банан", "color": "#f1c40f", "description": "Солодкий жовтий банан."},
    {"name": "Ківі", "color": "#27ae60", "description": "Соковитий зелений ківі."},
]

@app.route("/", methods=["GET", "POST"])
def index():
    fruit = None
    if request.method == "POST":
        selected_name = request.form.get("fruit_name")
        fruit = next((f for f in fruits if f["name"] == selected_name), None)
    return render_template("indexik.html", fruits=fruits, fruit=fruit)

if __name__ == "__main__":
    app.run(debug=True)
