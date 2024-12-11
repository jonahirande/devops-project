from flask import Flask, jsonify
import random

app = Flask(__name__)

# A collection of dad jokes
DAD_JOKES = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "What do you call fake spaghetti? An impasta!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Two fish are in a tank. One turns to the other and says, “Any idea how to drive this thing?”",
    "Why does a chicken coop only have two doors? Because if it had four it would be a sedan",
    "What did the pirate say on his birthday? “Aye, matey!”",
    "I was going to tell a sodium joke, then I thought, “Na.”",
    "What's a witch's favorite subject in school? Spelling.",
    "Why are frogs good at baseball? They know how to catch fly balls.",
    "What's the easiest building to lift? A lighthouse."
]

@app.route('/joke', methods=['GET'])
def get_joke():
    joke = random.choice(DAD_JOKES)
    return jsonify({"joke": joke})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

