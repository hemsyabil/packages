from flask import Flask, render_template
import plotly.graph_objs as go
import plotly  # Add this import
import json

app = Flask(__name__)


@app.route('/')
def dashboard():
    graphs = []
    for i in range(4):
        fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 1, 2])])
        graphs.append(json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))
    
    return render_template('dashboard.html', 
                           title="Dashboard",
                            name="Dashboard",
                           graphs=graphs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
