#Integrate HTML with flask
#This is also called jinja 2 techniques
#HTTP verb GET POST

from flask import Flask,redirect,url_for,render_template,request


# Building url dynamically 
#Variable rules for url building 

# WSGI Application
app=Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+str(score)
@app.route('/fail/<int:score>')
def failed(score):
    return "The person has failed and the marks is "+str(score)

@app.route('/result/<int:marks>')
def results(marks):
    r=""
    if marks<30:
        r='failed'
    else:
        r='success'
    return redirect(url_for(r,score=marks)) #here r has function name 

@app.route('/submit',methods=['POST','GET'])
def submittttt():
    if request.method=='POST':
        name=(request.form['name'])
        email=(request.form['email'])
        message=(request.form['message'])
    return render_template('submit.html',name=name,email=email,message=message)



if __name__=='__main__':
    app.run(debug=True)

#in return we can also pass html code