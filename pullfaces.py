from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top , right, bottom, left = face_location

    face_image = Image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    # show image
    pil_image.show()
    # saves images 
    pil_image.save(f'{top}.jpg')
