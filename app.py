from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html', active_page='inicio')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html', active_page='inicio')

@app.route('/comite')
def comite():
    return render_template('comite.html', active_page='comite')

@app.route('/conferencistas')
def conferencistas():
    return render_template('conferencistas.html', active_page='conferencistas')

@app.route('/convocatorias')
def convocatorias():
    return render_template('convocatorias.html', active_page='convocatorias')

@app.route('/programa')
def programa():
    return render_template('programa.html', active_page='programa')

@app.route('/guias')
def guias():
    return render_template('guias.html', active_page='guias')

@app.route('/registro')
def registro():
    return render_template('registro.html', active_page='registro')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)