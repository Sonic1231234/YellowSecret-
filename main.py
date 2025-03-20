from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/itex/')
def itex():
    return render_template('itex.html')

@app.route('/dota/')
def dota():
    return render_template('Dota.html')

@app.route('/blur/')
def blur():
    return render_template('Blur.html')

if __name__ == '__main__':
    app.run(debug=True)