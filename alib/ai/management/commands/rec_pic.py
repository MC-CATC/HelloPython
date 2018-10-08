# -*- coding: utf-8 -*-
import logging

import face_recognition
from PIL import Image
from django.core.management.base import BaseCommand

from ai.face.face_util import locate_faces, mark_names
from ai.face.image_util import get_known_faces
from ai.face.path_util import image_path, output_path

log = logging.getLogger(__name__)


# https://blog.csdn.net/hongbin_xu/article/details/76284134
class Command(BaseCommand):
    help = 'face in picture'

    def handle(self, *args, **options):
        known_names, known_faces = get_known_faces()

        img = face_recognition.load_image_file(image_path('obama_and_biden.jpg'))
        face_locations, face_names = locate_faces(img, known_faces, known_names)

        img = mark_names(img, face_locations, face_names)
        img_pil = Image.fromarray(img)
        img_pil.save(output_path('recognized.jpg'))

        img_pil.show()
        return str(face_names)
