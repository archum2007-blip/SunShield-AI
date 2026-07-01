from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    skin_type = request.form["skin_type"]
    city = request.form["city"]
    water_intake = request.form["water_intake"]
    sunscreen_usage = request.form["sunscreen_usage"]
    outdoor_hours = int(request.form["outdoor_hours"])

    recommendation = []
    risk = "Low"

    if outdoor_hours >= 8:
        risk = "High"
        recommendation.append("Avoid prolonged sun exposure.")
        recommendation.append("Apply sunscreen every 2-3 hours.")

    elif outdoor_hours >= 4:
        risk = "Medium"
        recommendation.append("Use sunscreen before going outdoors.")

    else:
        recommendation.append("Maintain your current skincare routine.")

    if water_intake == "Less than 2 Litres":
        recommendation.append("Increase your daily water intake.")

    if sunscreen_usage == "Never":
        recommendation.append("Start using sunscreen daily.")

    if skin_type == "Dry":
        recommendation.append("Use a moisturizer regularly.")
    elif skin_type == "Oily":
        recommendation.append("Use an oil-free face wash.")
    elif skin_type == "Combination":
        recommendation.append("Use products suitable for combination skin.")
    elif skin_type == "Sensitive":
        recommendation.append("Choose fragrance-free skincare products.")

    return render_template(
        "result.html",
        name=name,
        age=age,
        gender=gender,
        skin_type=skin_type,
        city=city,
        risk=risk,
        recommendations=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)