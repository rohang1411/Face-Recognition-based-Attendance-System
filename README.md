# Face-Recognition-based-Attendance-System

Developed a face recognition-based attendance system using OpenCV, face-recognition, ZMQ protocol and SMTP libraries.
Implemented on a raspberry pi for portability and IoT compatibility. Frames captured by the raspberry pi are transferred to the server using ZMQ protocol for processing and face recognition.
Automatic export of attendance reports in Excel format and e-mail reports generation from the captured data using openpyxl library

## LIBRARIES REQUIRED

### CLIENT
1. opencv
2. imagezmq
3. argparse
4. imutils
5. socket
6. time

## SERVER
1. dlib
2. opencv
3. face_recognition
4. pickle
5. smtp
6. time
7. os
8. argparse
9. openpyxl
10. socket


## STEPS TO RUN

1. First store the images of the studentsm these will be used to generate face data.
2. Then run the following commands to generate face encodings and save the to the pickle file. Add the following lines in the server.py file below line 29. Also change the paths and file names accordingly.
```python

 person1_face = face_recognition.load_image_file("/Users/yathartharora/Downloads/yatharth.jpg")
 person1_face_encoding = face_recognition.face_encodings(person1_face)[0];

 person2_face  = face_recognition.load_image_file("/Users/yathartharora/Downloads/rohan.jpg")
 person2_face_encoding = face_recognition.face_encodings(person2_face)[0];

 person3_face  = face_recognition.load_image_file("/Users/yathartharora/Downloads/milind.jpg")
 person3_face_encoding = face_recognition.face_encodings(person3_face)[0];


 known_face_encodings = [person1_face_encoding,person2_face_encoding,person3_face_encoding]

 known_name_face = ["person1","person2","person3"]
 
```

3. First run the server.py file on the server
4. Then run the clientside.py on the client pc(here Raspberry Pi). Also provide the IPv4 address of the server with -s argument
5. That's it, you now have your own face recognition attendence system running. 
