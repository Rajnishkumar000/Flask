from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
        #read camera frames
        success,frame=camera.read() 

        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('videoStreamingUsingWebcam\Haarcascades\haarcascade_frontalface_default.xml')
            # eye_cascade=cv2.CascadeClassifier('videoStreamingUsingWebcam\Haarcascades\haarcascade_eye.xml')

            faces=detector.detectMultiScale(frame,1.1,7)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,255),1)

                # roi_gray=gray[y:y+h,x:x+w] #face
                # roi_color=frame[y:y+h,x:x+w]

                # eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
                # for(ex,ey,ew,eh) in eyes:
                #     cv2.rectangle(roi_color,(ex,ey),(ex+w,ey+h),(0,255,0),2)



 

            ret,buffer=cv2.imencode('.jpg',frame) 
            frame=buffer.tobytes()

            yield(b'--frame\r\n' b'Content-Type:image/jpeg\r\n\r\n'+frame+b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def videoss():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=='__main__':
    app.run(debug=True)
