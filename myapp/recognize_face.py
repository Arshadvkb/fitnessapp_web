# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import psycopg2
from psycopg2.extras import RealDictCursor


def iud(qry,val):
    con=psycopg2.connect(host='localhost',port=5432,user='postgres',password='kickboxer',database='fitness_app')
    cmd=con.cursor()
    cmd.execute(qry,val)
    con.commit()
    con.close()

def selectone(qry,val):
    con=psycopg2.connect(host='localhost',port=5432,user='postgres',password='kickboxer',database='fitness_app')
    cmd=con.cursor(cursor_factory=RealDictCursor)
    cmd.execute(qry,val)
    res=cmd.fetchone()
    con.close()
    return res

def selectall(qry):
    con=psycopg2.connect(host='localhost',port=5432,user='postgres',password='kickboxer',database='fitness_app')
    cmd=con.cursor(cursor_factory=RealDictCursor)
    cmd.execute(qry)
    res=cmd.fetchall()
    con.close()
    return res
def selectall2(qry,val):
    con=psycopg2.connect(host='localhost',port=5432,user='postgres',password='kickboxer',database='fitness_app')
    cmd=con.cursor(cursor_factory=RealDictCursor)
    cmd.execute(qry,val)
    res=cmd.fetchall()
    con.close()
    return res

def rec_face_image(imagepath):
	print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")


	detected_name=[]
	idddss=imagepath.split('/')


	ap = argparse.ArgumentParser()

	data = pickle.loads(open(r'C:\Users\cas\Desktop\fitnessapp_web\fitnessaapp\faces.pickles', "rb").read())

	# load the input image and convert it from BGR to RGB
	image = cv2.imread(imagepath)
	#print(image)
	h,w,ch=image.shape

	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# detect the (x, y)-coordinates of the bounding boxes corresponding
	# to each face in the input image, then compute the facial embeddings
	# for each face

	boxes = face_recognition.face_locations(rgb,
		model='hog',)
	encodings = face_recognition.face_encodings(rgb, boxes)

	# initialize the list of names for each face detected
	names = []

	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known
		# encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding,tolerance=0.45)
		name = "Unknown"
		print (matches)

		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:

				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
				print(name,"================")
				if name not in detected_name:
					detected_name.append(name)
			print(counts, " rount ")
			# determine the recognized face with the largest number of
			# votes (note: in the event of an unlikely tie Python will
			# select first entry in the dictionary)

			name = max(counts, key=counts.get)
			print("result1111111", name)
	return detected_name


def camera():

	# import the opencv library
	import cv2

	# define a video capture object
	vid = cv2.VideoCapture(0)

	while (True):

		# Capture the video frame
		# by frame
		ret, frame = vid.read()
		cv2.imwrite("sample.png",frame)
		res=rec_face_image("sample.png")

		for i in res:
			q="SELECT * FROM myapp_attendance WHERE USER_id=%s AND date=CURRENT_DATE"

			res=selectall2(q,(i,))
			if len(res)>0:
				pass
			else:
				iud("INSERT INTO myapp_attendance (date, status, USER_id) VALUES(CURRENT_DATE,'P',%s)",(i,))
				# iud("INSERT INTO `smart_att_depression` VALUES(NULL,CURDATE(),%s,%s,%s)", (hr, emo, sid))
			print(i,"=====================2")

		# Display the resulting frame
		cv2.imshow('frame', frame)

		# the 'q' button is set as the
		# quitting button you may use any
		# desired button of your choice
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# After the loop release the cap object
	vid.release()
	# Destroy all the windows
	cv2.destroyAllWindows()
camera()
