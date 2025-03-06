from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world1():
    return render_template('index1.html')

@app.route('/1')
def hello_world2():
    return render_template('index2.html')

@app.route('/2')
def hello_world3():
    return render_template('index3.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080) 

