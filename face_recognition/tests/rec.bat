face_recognition --cpus 4 --show-distance true ./known_people ./unknown_pictures
face_recognition --cpus 4 --show-distance true ./known_people ./test_images

face_recognition --cpus 4 --tolerance 0.44 ./known_people ./unknown_pictures
face_recognition --cpus 4 --tolerance 0.44 ./known_people ./test_images
