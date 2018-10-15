# -*- coding: utf-8 -*-
import logging

import cv2
from django.core.management.base import BaseCommand

from ai.util.path_util import image_path, output_path
from face.face.face_change import ChangeFace
from face.face.image_util import read_image

log = logging.getLogger(__name__)


# https://blog.csdn.net/hongbin_xu/article/details/79179194
class Command(BaseCommand):
    help = 'change face in picture'

    def handle(self, *args, **options):
        changer = ChangeFace()

        src_img_file = image_path('obama_and_biden.jpg')
        dst_img_file = image_path('kit_with_rose.jpg')

        dst_img = read_image(dst_img_file)
        src_img = read_image(src_img_file)

        cv2.imshow('Pic Dst', dst_img)
        cv2.imshow('Pic Src', src_img)

        changer.load_images(dst_img_file, src_img_file)
        img_changed = changer.run(False, False)

        file_save = output_path('changed.jpg')
        cv2.imwrite(file_save, img_changed)
        cv2.imshow('Changed Pic', read_image(file_save))

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return file_save