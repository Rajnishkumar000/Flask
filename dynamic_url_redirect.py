from flask import Flask,redirect,url_for


# Building url dynamically 
#Variable rules for url building 

# WSGI Application
appMERA=Flask(__name__)

@appMERA.route('/')
def mainpage():
    return "This is mainpage"


@appMERA.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+str(score)
@appMERA.route('/fail/<int:score>')
def failed(score):
    return "The person has failed and the marks is "+str(score)

@appMERA.route('/result/<int:marks>')
def results(marks):
    r=""
    if marks<30:
        r='failed'
    else:
        r='success'
    return redirect(url_for(r,score=marks)) #here r has function name 
    


if __name__=='__main__':
    appMERA.run(debug=True)

#in return we can also pass html code