from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']

    heart = int(request.form['heart'])
    temp = float(request.form['temp'])
    oxygen = int(request.form['oxygen'])
    bp = int(request.form['bp'])

    weight = float(request.form['weight'])
    height = float(request.form['height'])
    sleep = int(request.form['sleep'])
    water = int(request.form['water'])
    exercise = request.form['exercise']

    bmi = weight / (height * height)

    report = []
    suggestions = []

    # Suggestions
    if bmi > 25:
        suggestions.append("👉 Reduce weight and do exercise")
    if bmi < 18.5:
        suggestions.append("👉 Increase healthy food intake")
    if sleep < 7:
        suggestions.append("👉 Sleep at least 7 hours")
    if water < 6:
        suggestions.append("👉 Drink more water")
    if exercise.lower() == "no":
        suggestions.append("👉 Start regular exercise")

    # Heart
    if heart < 60:
        report.append("⚠️ Low Heart Rate")
    elif heart > 120:
        report.append("🚨 High Heart Rate")
    else:
        report.append("✅ Heart Rate Normal")

    # Temp
    if temp < 35:
        report.append("⚠️ Low Temperature")
    elif temp > 38:
        report.append("⚠️ High Temperature")
    else:
        report.append("✅ Temperature Normal")

    # Oxygen
    if oxygen < 95:
        report.append("⚠️ Low Oxygen")
    else:
        report.append("✅ Oxygen Normal")

    # BP
    if bp > 140:
        report.append("⚠️ High BP")
    elif bp < 90:
        report.append("⚠️ Low BP")
    else:
        report.append("✅ BP Normal")

    # BMI status
    if bmi < 18.5:
        report.append("⚠️ Underweight")
    elif bmi > 30:
        report.append("🚨 Obesity")
    elif bmi > 25:
        report.append("⚠️ Overweight")
    else:
        report.append("✅ Normal BMI")

    # Final decision
    if heart > 120 or temp > 40 or oxygen < 85 or bp > 160:
        final = "🚨 EMERGENCY - Go to Doctor Immediately"
        color = "red"
    else:
        final = "✅ Patient Stable"
        color = "green"

    return render_template(
        'result.html',
        name=name,
        report=report,
        bmi=round(bmi, 2),
        final=final,
        suggestions=suggestions,
        color=color
    )

if __name__ == '__main__':
    app.run(debug=True)