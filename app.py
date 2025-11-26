import flask as f

app = f.Flask(__name__)

@app.route('/')
def index():
    return f.render_template('index.html')

app.run(debug=True)