import logging

import cv2
from django.core.management.base import BaseCommand

from ai.util.path_util import image_path, face_path
from face.face.face_crop import CropFace

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'crop face in pic'

    def handle(self, *args, **options):
        cropper = CropFace()

        # image
        frame = cv2.imread(image_path('obama_and_biden.jpg'))
        cv2.imshow('Pic', frame)

        # detect
        face_locations, faces = cropper.run(frame)
        log.info('faces: %d', len(faces))

        for i, face in enumerate(faces):
            cv2.imshow('Face', face)

            # 存在本地
            file_save = face_path('0_%d.jpg' % i)
            log.info('Face: %s', file_save)
            cv2.imwrite(file_save, face)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return str(len(faces))