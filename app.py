from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/compute')
def compute():
    n = request.args.get('n', default=10, type=int)

    if n > 200:
        n = 200

    x = list(range(1, n + 1))

    data = {
        "x": x,
        "O(1)": [1 for _ in x],
        "O(log n)": [round(math.log2(i), 2) for i in x],
        "O(n)": x,
        "O(n log n)": [round(i * math.log2(i), 2) for i in x],
        "O(n^2)": [i * i for i in x]
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)