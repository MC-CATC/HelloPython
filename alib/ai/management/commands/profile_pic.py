import json
import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face import FaceEncoder
from ai.face.face_util import get_faces
from ai.face.path_util import image_path, face_path
from ai.util.file_util import save, get_dir

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'profile face in pic'

    def handle(self, *args, **options):
        # image
        frame = cv2.imread(image_path('obama_and_biden.jpg'))
        cv2.imshow('Pic', frame)

        # detect
        faces = get_faces(frame)
        log.info('faces: %d', len(faces))

        for i, face in enumerate(faces):
            cv2.imshow('Face', face.image)

            # 存在本地
            face.index = i
            face.image_file = '0_%d.jpg' % face.index
            file_save = face_path(face.image_file)
            log.info('Face: %s', file_save)
            cv2.imwrite(file_save, face.image)

        cv2.destroyAllWindows()

        if len(faces) <= 0:
            return 'No faces'

        profile = json.dumps(faces, cls=FaceEncoder)
        return save(get_dir(face_path(faces[0].image_file)), 'profiled_pic.json', profile.encode('utf-8'))
