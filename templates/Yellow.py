from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def yellow():
    return render_template('Yellow.html')

if __name__ == '__main__':
    app.run(debug=True)

