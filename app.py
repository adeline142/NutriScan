import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- Your Original Logic (Corrected) ---
class Meal:
    def __init__(self, description):
        self.description = description
        self.sugar = 0
        self.sodium = 0
        self.calories = 0
        self.protein = 0

    def analyze(self):
        healthy = random.random() > 0.4
        self.sugar = 8 if healthy else 35
        self.sodium = 500 if healthy else 1000
        self.calories = 400 + random.randint(0, 200)
        self.protein = 25 + random.randint(0, 20)
        return healthy

# --- HTML Template (The UI) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NutriScan Flask</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #f4f7f6; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        input { padding: 10px; width: 250px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .result { margin-top: 20px; text-align: left; border-top: 1px solid #eee; padding-top: 20px; }
        .healthy { color: green; } .unhealthy { color: red; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🥗 NutriScan App</h1>
        <form method="POST">
            <input type="text" name="meal" placeholder="What did you eat?" required>
            <button type="submit">Analyze</button>
        </form>

        {% if meal %}
        <div class="result">
            <h3>Results for: {{ meal.description }}</h3>
            <p>🔥 <b>Calories:</b> {{ meal.calories }}</p>
            <p>💪 <b>Protein:</b> {{ meal.protein }}g</p>
            <p>🍬 <b>Sugar:</b> {{ meal.sugar }}g</p>
            <p>🧂 <b>Sodium:</b> {{ meal.sodium }}mg</p>
            
            {% if is_healthy %}
                <h4 class="healthy">✅ Healthy meal choice!</h4>
            {% else %}
                <h4 class="unhealthy">⚠️ This meal is not healthy.</h4>
            {% endif %}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    meal = None
    is_healthy = None
    if request.method == "POST":
        meal_input = request.form.get("meal")
        meal = Meal(meal_input)
        is_healthy = meal.analyze()
    return render_template_string(HTML_TEMPLATE, meal=meal, is_healthy=is_healthy)

if __name__ == "__main__":
    app.run(debug=True)