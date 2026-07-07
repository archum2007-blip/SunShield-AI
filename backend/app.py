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

    # UV Risk Prediction
    if outdoor_hours >= 8:
        risk = "High"
        recommendation.append("Avoid prolonged sun exposure.")
        recommendation.append("Apply sunscreen every 2-3 hours.")

    elif outdoor_hours >= 4:
        risk = "Medium"
        recommendation.append("Use sunscreen before going outdoors.")

    else:
        recommendation.append("Maintain your current skincare routine.")

    # Water Intake
    if water_intake == "Less than 2 Litres":
        recommendation.append("Increase your daily water intake.")

    # Sunscreen Usage
    if sunscreen_usage == "Never":
        recommendation.append("Start using sunscreen daily.")

    # Skin Type Recommendation
    if skin_type == "Dry":
        recommendation.append("Use a moisturizer regularly.")
    elif skin_type == "Oily":
        recommendation.append("Use an oil-free face wash.")
    elif skin_type == "Combination":
        recommendation.append("Use products suitable for combination skin.")
    elif skin_type == "Sensitive":
        recommendation.append("Choose fragrance-free skincare products.")

    # Prediction Confidence
    if risk == "High":
        confidence = "95%"
    elif risk == "Medium":
        confidence = "85%"
    else:
        confidence = "90%"

    return render_template(
        "result.html",
        name=name,
        age=age,
        gender=gender,
        skin_type=skin_type,
        city=city,
        water_intake=water_intake,
        sunscreen_usage=sunscreen_usage,
        outdoor_hours=outdoor_hours,
        risk=risk,
        confidence=confidence,
        recommendations=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)