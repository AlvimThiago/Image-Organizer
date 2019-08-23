import os
import shutil

f = "ImageOrganizer.exe"
sourceTeste = ('C:\\Users\\alvim\OneDrive\\Desktop\\New folder\\dist')
source = ('.\\dist')
destination = ('C:\\Program Files\\ImageOrganizer')
if not os.path.exists(destination):
    shutil.copytree(source, destination)
else:
    shutil.rmtree(destination)
    shutil.copytree(source, destination)

# os.system(r"C:\Users\alvim\PycharmProjects\ImageOrganizer\imgorg.reg")
os.system(r'C:\"Program Files"\ImageOrganizer\ImageOrganizer_ContextMenu.reg')