from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
from filepath import *
import logging

# make for fonts, also seprate for psd files
# make one for pesu phy chem etc, del folder based on name

#from "filepath" file all local file paths are imported here
source_dir = downloads
dest_dir_video = vid
dest_dir_image = img
dest_dir_documents = doc
dest_dir_psd = psd
dest_dir_pesu = pesu

#Misc files
photoshop_extensions = [".psd"]
illustrator_extensions =[".ai"]
font_extensions = [".ttf",".otc",".otf",".ttc"]
trash_name = ["trash","later","bin"]
pesu_name = ["u1","u2","u3""u4","pesu","chem","phy","chemistry","epd","electronics","physics",
             "mech","mechanical","mech","mechanics","maths","math","unit","notes"]




# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

# supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"): # checks if file with same name already exists
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# here entries is an iterator obj (scandir scans the directory & gets an iterator of os.DirEntry obj)
def on_cleaner():
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            check_video_files(entry, name)
            check_image_files(entry, name)
            check_document_files(entry, name)


def check_video_files(entry, name):  # Checks all Video Files
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")

def check_image_files(entry, name):  # * Checks all Image Files
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

def check_document_files(entry, name):  # * Checks all Document Files
    for documents_extension in document_extensions:
        if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
            move_file(dest_dir_documents, entry, name)
            logging.info(f"Moved document file: {name}")
            

on_cleaner()