implementation of python's face recognition module.

to match from folder to folder
    face_recognition source_dir destination_dir
    face_recognition ./img/known ./img/unknown

to find distance
    face_recognition --show-distance true ./img/known ./img/unknown

setting tolerance
    face_recognition --tolerance 0.50 ./img/known ./img/unknown


findfaces.py
    used to find the number of faces in an image

facematch.py
    used to compare two images and verify

pullfaces.py
    used to pull all the faces from an image and save them separately