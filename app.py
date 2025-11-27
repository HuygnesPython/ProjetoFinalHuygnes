import flask as f

app = f.Flask(__name__)

@app.route('/')
def index():
    return f.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # <-- REMOVA ISSO no PA!