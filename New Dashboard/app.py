from flask import Flask, render_template

finance_app = Flask(__name__)

@finance_app.route('/')
def dashboard():
    
    return render_template(
        'dashboard.html',
        title="Financial Dashboard",
        name="Financial Dashboard")

if __name__ == "__main__":
    finance_app.run(host='0.0.0.0', port=8080, debug=True)
