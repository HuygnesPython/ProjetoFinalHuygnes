import flask as f
# import mysql.connector as my
nome1 = ''
app = f.Flask(__name__)

@app.route('/')
def index():
    title = 'Página inicial'
    return f.render_template('index.html', title=title)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    title = 'Cadastro'
    if f.request.method == 'GET':
        return f.render_template('cadastro.html',title=title)
    
    if f.request.method == 'POST':
        nome1 = f.request.form.get('nome')
        carro = f.request.form.get('carro')

        if carro != 'Não' or carro != 'Sim':
            return f.redirect(f.url_for('cadastro'))

        if carro == 'Não':
            return f.render_template('sem_carro.html')
        
        if carro == 'Sim':
            return f.redirect(f.url_for('cadastro_carro'))

@app.route('/cadastro_carro', methods=['GET', 'POST'])
def cadastro_carro():
    if f.request.method == 'GET':
        return f.render_template('cadastro_carro.html')
    if f.request.method == 'POST':
        nome2 = f.request.form.get('nome2')
        return f.render_template('cadastro_carro.html')






if __name__ == '__main__':
    app.run(debug=True) # <-- REMOVA ISSO NO PA!