from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return '<h1>Welcome!</h1>'
@app.route('/form')
def hello1():
    return render_template('login.html')
@app.route('/mylogin')
def hello2():
    return render_template('myinfo.html')
if __name__=='__main__':
    app.run(debug=True)