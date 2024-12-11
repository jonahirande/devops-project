from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of fitness advice
fitness_tips = [
    "Drink plenty of water throughout the day.",
    "Make sure to warm up before you start your workout.",
    "Include both cardio and strength training in your fitness routine.",
    "Rest and recovery are just as important as exercise.",
    "Focus on form over speed to avoid injury.",
	"Do workouts you enjoy",
    "Cut your coffee calories",
    "Keep a fitness journal",
    "Pay attention to your thoughts",
    "Eat the rainbow",
    "Avoid processed food",
    "Make sure you drink water",
    "Increase your protein",
    "Eat a balanced diet with plenty of protein and vegetables.",
    "Get at least 7-8 hours of sleep each night for optimal recovery.",
    "Take breaks and stretch during long hours of sitting.",
    "Set achievable fitness goals to stay motivated.",
    "Try new exercises to keep your routine interesting and challenging.",
	
]

# Endpoint to fetch random fitness advice
@app.route('/fitness-advice', methods=['GET'])
def get_fitness_advice():
    try:
        # Return a random fitness tip
        tip = random.choice(fitness_tips)
        return jsonify({"fitness_tip": tip}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
