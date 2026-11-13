from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Attendance Tracker"


@app.route("/api/employees")
def employees():
    return {"employees": ["Alice", "Bob", "Charlie"]}


if __name__ == "__main__":
    app.run(debug=True)
