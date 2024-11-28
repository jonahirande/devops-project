from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# In-memory store for the secret number and guesses count
secret_number = None
guess_count = 0

# Initialize the game
@app.route('/start', methods=['GET'])
def start_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0
    return jsonify({"message": "Game started! Guess a number between 1 and 100."}), 200

# Guess a number
@app.route('/guess', methods=['POST'])
def guess_number():
    global guess_count, secret_number

    if secret_number is None:
        return jsonify({"error": "Game not started yet. Use /start to begin."}), 400

    data = request.get_json()
    guess = data.get('guess')

    if guess is None:
        return jsonify({"error": "No guess provided"}), 400

    guess_count += 1

    if guess < secret_number:
        return jsonify({"message": "Too low! Try again.", "attempts": guess_count}), 200
    elif guess > secret_number:
        return jsonify({"message": "Too high! Try again.", "attempts": guess_count}), 200
    else:
        return jsonify({"message": f"Correct! The secret number was {secret_number}. It took you {guess_count} attempts.", "attempts": guess_count}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)  # Port changed to 5004

