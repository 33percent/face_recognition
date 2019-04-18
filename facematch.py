import face_recognition


image_of_bill = face_recognition.load_image('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image('./img/unknown/bill-gates-4.jpg')
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]


# comparing two images

results = face_recognition.compare([bill_face_encoding], unknown_image_encoding)

if results[0]:
    print('this is bill bro')
else:
    print('this ain"t bill bro')