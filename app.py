from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index.html', message = 'Hello Flask!', contacts = ['c1', 'c2', 'c3']);
    return render_template('index.html')
@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/draw/<int:num>')
def drawx(num):
    pyramid = ""
    for i in range(1, num + 1):
        pyramid += "x" * i + "\n"
    return f'''
        <head><title>DrawXPyramid</title></head>
        <pre>{pyramid}</pre>
        <h2>  เปลี่ยนจำนวนได้ </h2>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/tech">Tech</a></li>
            <li><a href="/myid">MyID</a></li>
            <li><a href="/draw/3">Draw</a></li>
        </ul>'''

@app.route('/myid')
def id():
    return '''
        <head><title>MyID</title></head>
        <h1> 68130022 </h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/tech">Tech</a></li>
            <li><a href="/myid">MyID</a></li>
            <li><a href="/draw/3">Draw</a></li>
        </ul>'''


@app.route('/sum/<x>/<y>')
def sm(x,y):
    try:
        z = int(x) + int(y)
        return  f"The result of sum between {x} and {y} is {z}"
    except:
        return "You are using miss data type for operation"
    
@app.route('/concat/<x>/<y>')
def ct(x,y):
    z = x + y
    return  f"The result of concatenate between {x} and {y} is {z}"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80, debug=True)