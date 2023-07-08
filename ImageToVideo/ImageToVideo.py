import os, os.path
import shutil
from operator import itemgetter
from ImageToVideo.LeiapixBot import LeiapixBot

class ImageToVideo: 
    def Convert():
        # go to leiapix site and convert images to animations
        towerImage = os.path.abspath("ImageToVideo/images/tower.png")
        horseImage = os.path.abspath("ImageToVideo/images/horse.png")
        images = [towerImage, horseImage]
        with LeiapixBot() as leiapixBot:
            leiapixBot.convertImage(images)

        # move animations from downloads to input vids folder
        downloads_dir = "C:\\Users\\YourUsername\\Downloads"
        destination_dir = "C:\\Users\\chris\\OneDrive\\Documents\\history-queefs\\history-queefs\\premiere-script\\input-vids"

        # check if the destination directory exists
        if not os.path.isdir(destination_dir):
            os.mkdir(destination_dir)

        # get all files' paths and their last modification time in the downloads directory
        files = [(f, os.path.getmtime(os.path.join(downloads_dir, f))) for f in os.listdir(downloads_dir) if os.path.isfile(os.path.join(downloads_dir, f))]

        # sort the files by the modification time in descending order
        files.sort(key=itemgetter(1), reverse=True)

        # move the most 3 recent files to the destination directory
        for f, _ in files[:3]:
            shutil.move(os.path.join(downloads_dir, f), os.path.join(destination_dir, f))
