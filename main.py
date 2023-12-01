import face_recognition
import cv2


checkout_cap1=cv2.VideoCapture('Father ALWAYS say NORTHERNERS are DIFFERENT more LOYAL 🐺🐻🔥.mp4')
checkout_cap2=cv2.VideoCapture('inside_20231024132800.mp4')

checkin_cap1=cv2.VideoCapture('front_202310241328.mp4')
checkin_cap2=cv2.VideoCapture('We KNOW no KING but The KING in the NORTH whose name is STARK 🐻🔥🐺 gameofthrones got jonsnowedit.mp4')

counter=0

threshold = 0.6
ref_face_encodings=[]
ref_time=[]
def checkin(image,timein):
    ref_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ref_encoding_frame = face_recognition.face_encodings(ref_image)
    for i in ref_encoding_frame:
            ref_face_encodings.append(i)
            ref_time.append(timein)
def checkout(image,timeout):
    query_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)            
    query_face_locations = face_recognition.face_locations(query_image)
    query_face_encodings = face_recognition.face_encodings(query_image, query_face_locations)
    for (top, right, bottom, left), query_face_encoding in zip(query_face_locations, query_face_encodings):
            face_distances = face_recognition.face_distance(ref_face_encodings, query_face_encoding)
            if len(face_distances>0):
              idx = min(enumerate(face_distances), key=lambda x: x[1])[0]
              print(f"Index: {idx}, Time go out: {timeout}, Time go in: {ref_time[idx]}")
            
while True:
    ret,checkout_frame1=checkout_cap1.read()
    ret2,checkout_frame2=checkout_cap2.read()
    
    ret3,checkin_frame1=checkin_cap1.read()    
    ret4,checkin_frame2=checkin_cap2.read()
    
    if ret2 and ret and ret3 and ret4:  
      if counter%30==0:
        if counter== 108000:
            ref_face_encodings=[]
            ref_time=[]
        checkin(checkin_frame1,checkin_cap1.get(cv2.CAP_PROP_POS_MSEC))
        checkin(checkin_frame2,checkin_cap2.get(cv2.CAP_PROP_POS_MSEC))
        
        checkout(checkout_frame1,checkout_cap1.get(cv2.CAP_PROP_POS_MSEC))
        checkout(checkout_frame2,checkout_cap2.get(cv2.CAP_PROP_POS_MSEC))
        
      counter+=1
    else :
        break  