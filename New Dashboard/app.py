from flask import Flask, render_template

dashboard_app = Flask(__name__)


@dashboard_app.route('/')
def dashboard():

    return render_template(
        'dashboard.html',
        title="<name> Dashboard",
        name="<name> Dashboard")


if __name__ == "__main__":
    dashboard_app.run(host='0.0.0.0', port=8080, debug=True)
