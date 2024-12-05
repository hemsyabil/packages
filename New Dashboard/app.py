from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template(
        'dashboard.html',
        title="TCM Dashboard",
        name="TCM Dashboard")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
