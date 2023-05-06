from ImageToVideo import ImageToVideo
import os, os.path


def main():
    towerImage = os.path.abspath("../images/tower.png")
    horseImage = os.path.abspath("../images/horse.png")
    images = [towerImage, horseImage]
    with ImageToVideo() as leiapixBot:
        leiapixBot.convertImage(images)

if __name__ == "__main__":
    main()

