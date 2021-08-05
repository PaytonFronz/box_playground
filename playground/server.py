from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "this is the playground assignment!"

@app.route('/play')
def boxes():
   return render_template("playground.html", x = int(3))

@app.route('/play/<int:x>')
def add_boxes(x):
    return render_template("playground.html", x = int(x))

@app.route('/play/<int:x>/<box_color>')
def color_the_boxes(x, box_color):
    return render_template("playground.html", x = int(x), BoxColor = box_color)

if __name__=="__main__":   
    app.run(debug=True)  