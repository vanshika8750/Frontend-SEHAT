from flask import Flask,jsonify,request
from flask_cors import CORS
import random
import pyrebase
from twilio.rest import Client
app=Flask(__name__)
prev=0
CORS(app)
config={
    'apiKey': "AIzaSyDeG_7WW_fq2FtdswAQWEtQRM9CBNXiRgw",
    'authDomain': "sehat-8de79.firebaseapp.com",
    'databaseURL': "https://sehat-8de79-default-rtdb.firebaseio.com",
    'projectId': "sehat-8de79",
    'storageBucket': "sehat-8de79.appspot.com",
    'messagingSenderId': "47743319189",
    'appId': "1:47743319189:web:e701fbee1d15dd2bbdef9c",
}
firebase=pyrebase.initialize_app(config)
db = firebase.database()
storage=firebase.storage()
account_sid = "AC417ef321df1099daa1648a95da3b2a76"
auth_token = "1931e1f8c94996558df56a9c461e6030"
client = Client(account_sid, auth_token)
# Function to get data from the firebase
def getFire():
    try:
        data=db.get()
        if data.val():
            print (data.val())
        else :
            print ("Not available")
    except Exception as e:
        print ("Error",str(e))
#Function to get audio data from vite frontend
@app.route("/api/receive", methods=['POST'])
def form():
    files = request.files['audio']
    try:
        storage.child("Audio/file1.wav").put(files)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#Function to send data to the firebase
def sendFire():
    data=999999999999
    db.child("Patients").child(data).child("Name").set("Vanshika Jain")
    print("Data sent")
@app.route('/api/data',methods=['GET'])
def get_data():
    data={
        "message":"Hello this is api end point"
    }
    return jsonify(data)
@app.route('/api/getting',methods=['POST'])
def add_data():
    submit_data=request.get_json()
    print(submit_data)
    return 'Done',201
@app.route('/api/otp',methods=['POST'])
def otp_data():
    global prev
    submit_data=request.get_json()
    pov=0
    number=0
    while (pov<4):
        number=number*10 + int(submit_data[pov])
        pov=pov+1
    print(number)
    print(prev)
    if (number==prev):
        return 'Done',201
    else :
        return 'False', 500
@app.route('/api/adhar',methods=['POST'])
def adhar_data():
    global prev
    submit_data=request.get_json()
    print(submit_data)
    random_8_digit_number = random.randint(1000, 9999)
    try:
        data=db.child('Patients').child(submit_data).child('Number').get()
        prev=random_8_digit_number
        if data.val():
            phone_number="+91"+str(data.val())
            message="your OTP is "+str(random_8_digit_number)
            message=client.messages.create(
                to=phone_number,
                from_="+16787103295",
                body=message
            )  
            print("message sent")
    except Exception as e:
        print ("Error",str(e))
    return 'Done',201
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)