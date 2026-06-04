from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/comite')
def comite():
    return render_template('comite.html')

@app.route('/conferencistas')
def conferencistas():
    return render_template('conferencistas.html')

@app.route('/convocatorias')
def convocatorias():
    return render_template('convocatorias.html')

@app.route('/programa')
def programa():
    return render_template('programa.html')

@app.route('/guias')
def guias():
    return render_template('guias.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)