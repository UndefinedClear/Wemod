from flask import Flask, render_template, request, jsonify
import random

port = 5556
app = Flask(__name__)

# Global game state
players = ["Alice", "Bob", "Charlie", "Dave"]
common_word = "apple"
unique_word_player = random.choice(players)
round_count = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_game", methods=["POST"])
def start_game():
    global round_count
    round_count = 1
    unique_word_player = random.choice(players)
    return jsonify({"message": f"The game has started! {unique_word_player} has the unique word.", "round": round_count})

@app.route("/ask_question", methods=["POST"])
def ask_question():
    question = request.json.get('question')
    # Here, you'd normally handle yes/no questions, but for simplicity:
    return jsonify({"message": f"Question asked: {question}"})

@app.route("/guess", methods=["POST"])
def guess():
    guess = request.json.get('guess')
    global round_count
    if guess == unique_word_player:
        return jsonify({"message": "Congratulations! You guessed the correct person!"})
    else:
        round_count += 1
        return jsonify({"message": "Wrong guess. Keep trying!", "round": round_count})

if __name__ == "__main__":
    app.run(port=port, debug=True)
