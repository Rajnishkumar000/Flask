from flask import Flask

# WSGI Application
appMERA=Flask(__name__)
# appTERA=Flask(__name__)

@appMERA.route('/')
def welcome():
    return 'Welcome to my webpage OK and subscribe it BYE'
@appMERA.route('/members')
def welcome2():
    return 'Memberss'
@appMERA.route('/members/kachra')
def welcome3():
    return 'kachra'

@appMERA.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+str(score)
@appMERA.route('/fail/<int:score>')
def failed(score):
    return "The person has failed and the marks is "+str(score)

@appMERA.route('/result/<int:score>')
def results(score):
    r=""
    if score<30:
       r=failed(score)
    else:
        r=success(score)
    return r
    


# @appTERA.route('/')
# def welcome3():
#     return "YE TERA APP HAI"

if __name__=='__main__':
    appMERA.run(debug=True)
    # appTERA.run(debug=True)
