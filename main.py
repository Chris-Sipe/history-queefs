from ImageToVideo.ImageToVideo import ImageToVideo

def main():
    # get images from text descriptions via midJourney

    # get animated images from images via leiapix
    imageToVideo = ImageToVideo()
    imageToVideo.convert()

    # stitch together animates images into video via premiere

if __name__ == "__main__":
    main()

