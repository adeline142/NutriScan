// OOP CLASS: Meal
class Meal {
    constructor(description) {
        this.description = description;
        this.sugar = 0;
        this.sodium = 0;
        this.calories = 0;
        this.protein = 0;
    }

    analyze() {
        const healthy = Math.random() > 0.4;

        this.sugar = healthy ? 8 : 35;
        this.sodium = healthy ? 500 : 1000;
        this.calories = 400 + Math.floor(Math.random() * 200);
        this.protein = 25 + Math.floor(Math.random() * 20);

        return healthy;
    }
}

// OOP CLASS: App Controller
class NutriScanApp {
    constructor() {
        this.scanButton = document.getElementById("scanButton");
        this.mealInput = document.getElementById("mealInput");
        this.resultsSection = document.getElementById("resultsSection");

        this.init();
    }

    init() {
        this.scanButton.addEventListener("click", () => this.run());
    }

    run() {
        if (this.mealInput.value.trim() === "") {
            alert("Please enter a meal!");
            return;
        }

        const meal = new Meal(this.mealInput.value);
        const isHealthy = meal.analyze();

        this.displayResults(meal, isHealthy);
    }

    displayResults(meal, isHealthy) {
        document.getElementById("calResult").textContent = meal.calories;
        document.getElementById("proteinResult").textContent = meal.protein;
        document.getElementById("sugarResult").textContent = meal.sugar;
        document.getElementById("sodiumResult").textContent = meal.sodium;

        this.resultsSection.classList.remove("hidden");

        this.updateFeedback(meal, isHealthy);
    }

    updateFeedback(meal, isHealthy) {
        const summary = document.getElementById("feedbackSummary");
        const feedbackText = document.getElementById("feedbackText");
        const smartFeedback = document.getElementById("smartFeedback");

        if (isHealthy) {
            summary.textContent = "✅ Healthy meal choice!";
            summary.className = "feedback-summary bg-green-100 text-green-800";
            smartFeedback.style.borderColor = "#22c55e";
            feedbackText.textContent =
                "Good balance of nutrients. Keep choosing whole and fresh foods.";
        } else {
            summary.textContent = "⚠️ This meal is not healthy.";
            summary.className = "feedback-summary bg-red-100 text-red-800";
            smartFeedback.style.borderColor = "#ef4444";
            feedbackText.textContent =
                "High sugar or sodium detected. Consider reducing processed foods.";
        }
    }
}

// Initialize App
new NutriScanApp();
