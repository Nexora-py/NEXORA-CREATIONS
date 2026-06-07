from flask import Flask, render_template, request, jsonify
import io
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data.get("code", "")

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code, {})
        output = sys.stdout.getvalue()

        if not output:
            output = "Code executed successfully (no output)"

        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"output": str(e)})

    finally:
        sys.stdout = old_stdout


if __name__ == "__main__":
    app.run(debug=True)