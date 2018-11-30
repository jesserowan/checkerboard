from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display():
    return render_template('index.html')

@app.route('/<x>/<y>')
def display_x_y(x, y):
    return render_template('index.html', columns = int(int(x)/2), rows = int(int(y)/2))

if __name__ == '__main__':
    app.run(debug=True)