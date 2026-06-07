from flask import Flask, render_template, request, jsonify
import io
import contextlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data.get("code", "")

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})

        result = output.getvalue()

        if not result:
            result = "Code executed successfully (no output)"

    except Exception as e:
        result = str(e)

    return jsonify({"output": result})

if __name__ == "__main__":
    app.run(debug=True)