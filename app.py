import flask as f

app = f.Flask(__name__)

@app.route('/')
def index():
    title = 'Página inicial ( Huygnes )'
    return f.render_template('index.html', title=title)

@app.route('/login')
def login():
    title = 'Login'
    return f.render_template('login.html',title=title)



if __name__ == '__main__':
    app.run(debug=True) # <-- REMOVA ISSO NO PA!