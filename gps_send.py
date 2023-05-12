import pyrebase
import serial
import pynmea2

const firebaseConfig = {
    "apiKey": "AIzaSyB_gqA4MjApx3_R1mcBMloL4bukSB_mz1M",
    "authDomain": "seekerpro-59d1f.firebaseapp.com",
    "databaseURL": "https://seekerpro-59d1f-default-rtdb.firebaseio.com",
    "projectId": "seekerpro-59d1f",
    "storageBucket": "seekerpro-59d1f.appspot.com",
    "messagingSenderId": "275606278896",
    "appId": "1:275606278896:web:48ec4c9c3c1391f96de835",
    "measurementId": "G-Y80MXFQSDV"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

while True:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data[0:6] == '$GPRMC':
                newmsg=pynmea2.parse(n_data)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                print(gps)
                data = {"LAT": lat, "LNG": lng}
                db.update(data)
                print("Data sent")