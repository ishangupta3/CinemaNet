# CinemaNet

CinemaNet is a set of data and trained models to help run inference to classify images / frames of a video with an eye for photographic, cinemgraphic, composition and color labelling.

CinemaNet aims to give out of the box useful classification of images / frames of video to cinematographers, editors, archivists, and anyone interested in extracting classification in a cinema / video context.

## Getting the Data Set

Install the dependencies for our data set download script:

Install [Google Image Downloader](https://github.com/hardikvasa/google-images-download) and install [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) with a matching version to your currently installed Google Chrome browser (for me, it was 74.x). Google Chrome Driver is required to download more than 100 images per google image query.

You can then run `python synopsis_categories_and_concepts_image_downloader.py` to get the **unfiltered** raw data set - which will contain some bad images in the training set.

The data set we are working with has images pruned from the above download results. Once we finish we will provide zip files for easier download.

You can follow along with the [Running Training Notes](https://github.com/Synopsis/CinemaNet/blob/master/Running%20Training%20Notes.md) to see the steps we are taking if you want to train yourself. 

Sign up for Googles AutoML Vision cloud service if you want to train your own model. At the time of this writing you will get approximately $300 in free credits.

See [Running Training Notes](https://github.com/Synopsis/CinemaNet/blob/master/Running%20Training%20Notes.md) for more info on training a model.
