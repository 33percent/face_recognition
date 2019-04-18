import face_recognition
from PIL import Image, ImageDraw

image_of_bill = face_recognition.load_image('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]


image_of_steve = face_recognition.load_image('./img/unknown/Steve Jobs.jpg')
steve_image_encoding = face_recognition.face_encodings(image_of_steve)[0]

# create an array of encodings and names

known_face_encodings = [
     bill_face_encoding,
     steve_image_encoding
]

known_face_name = [
    'Bill gates',
    'Steve Jobs'
]

# load a test image to find faces

test_image = face_recognition.load_image_file('./img/groups/bill-steve.jpg')

# find faces in test image

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# convert to PIL format
pil_image = Image.fromarray(test_image)

# create a imagedraw instance
draw = ImageDraw.Draw(pil_image)

# loop through faces in test image

for (top, right, bottom, left), face_encoding in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding )
    name = 'Unknown Person '

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_name[first_match_index]

# draw box
draw.rectangle(((left,top),(right, bottom)),outline=(0,0,0))

# draw a label
text_width, text_height = draw.textsize(name)
draw.rectangle(((left, bottom - text_height - 10 ), (right, bottom)), fill=(0,0,0,), outline=(0,0,0))
draw.text((left+6, bottom - text_height - 10), name, fill=(255,255,255,255))

del draw

pil_image.show()


pil_image.save('identify.jpg')