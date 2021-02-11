from imutils.video import VideoStream 
import imagezmq 
import argparse 
import socket 
import time 
import RPi.GPIO as GPIO

#  TCP_IP = '192.168.1.15'
TCP_PORT = 5999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen()
print("DONE.....")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(27, GPIO.HIGH)

ap = argparse.ArgumentParser()
ap.add_argument("-s","--server-ip",required=True,help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(args["server_ip"]))
print(sender)
print("Connected")

rpiName = socket.gethostname()
vs = VideoStream(src=0, resolution=(640,480), framerate=24).start()
time.sleep(2.0)
count=0

while True:
    frame = vs.read()
    count+=1
    print(count)
    if count % 10 == 0:
    	sender.send_image(rpiName,frame)
    	s.listen()
    	conn, addr = s.accept()
    	data = conn.recv(20).decode("utf-8")
    	print(data)
    	conn.send(data.encode())
    	if data == "DETECTED":
            GPIO.output(27,GPIO.LOW)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.HIGH)
conn.close()
