from ImageToVideo.ImageToVideo import ImageToVideo
from PremiereScript.RunPremiere import RunPremiere

def main():
    # get images from text descriptions via midJourney

    # get animated images from images via leiapix
    imageToVideo = ImageToVideo()
    imageToVideo.convert()

    # stitch together animates images into video via premiere
    runPremiere = RunPremiere()
    runPremiere.run()

if __name__ == "__main__":
    main()

