import os
import shutil
from _datetime import datetime
from PIL import Image

class ImageOrganizer:

    def folder_path_from_photo_date(self, file):
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def photo_shooting_date(self, file):
        photo = Image.open(file)
        info = photo._getexif()
        try:
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
            else:
                date = datetime.fromtimestamp(os.path.getmtime(file))
        except:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def move_photo(self, file):
        new_folder = self.folder_path_from_photo_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def relocate_photo(self):

        num = 0
        img = ('jpg', 'jpeg', 'png')

        for files in  os.listdir('.'):

            if any(files.lower().endswith(img) for i in img):
                self.move_photo(files)




org = ImageOrganizer()
org.relocate_photo()




