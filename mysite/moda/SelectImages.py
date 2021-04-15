import pandas as pd
import os

from .QuadTree import *
from mysite.settings import BASE_DIR


class SelectImages:
    def __init__(self):
        self.sample = 12
        self.df_quadtree = pd.read_csv(os.path.join(BASE_DIR, 'moda/static/anno/points.txt'))

    def select_images_distance(self):
        qt = QuadTree()
        return qt.select_img_quadtree(self.df_quadtree, self.sample)

    def select_images_svm(self):
        return []
