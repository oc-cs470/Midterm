from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/site01')
def site01():
    return render_template('site01.html')

@app.route('/site02')
def site02():
    return render_template('site02.html')

@app.route('/site03')
def site03():
    return render_template('site03.html')

if __name__ == '__main__':
    app.run(debug=True)

