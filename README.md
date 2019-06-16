# CinemaNet

CinemaNet is a set of data and trained models to help run inference to classify images / frames of a video with an eye for photographic, cinemgraphic, composition and color labelling.

CinemaNet aims to give out of the box useful classification of images / frames of video to cinematographers, editors, archivists, and anyone interested in extracting classification in a cinema / video context.

## Getting the Data Set

Note, the raw data set is only useful if you plan on training your own models or are interested in helping optimize, classify and iterate on the quality of the models. Generally speaking its probably not useful!

### 1 - Check out the repository

Ensure that you have git checked out this repository or have done a download of this repository via the green `clone or download` button on the project page.

### 2 Install the dependencies for our data set download script:

Ensure you have PIP installed. Install [Google Image Downloader](https://github.com/hardikvasa/google-images-download) and install [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) with a matching version to your currently installed Google Chrome browser (for me, it was 74.x). Google Chrome Driver is required to download more than 100 images per google image query.

### 2.1 Install PIP if necessary.

`sudo easy_install pip` in your Terminal.app command line. 

### 2.2 Install Google Image Downloader via:

`pip install google_images_download` in your terminal.app

### 2.3 Install Chrome Driver

Check that you have a version of Google Chrome installed in the defaul `/Applications/Google Chrome.app` location.
Launch Chrome and check the version number by going to 'About Chrome' in the `Chrome` Menu.

Download a matching version of `Google Chrome Driver` and place it into the same directory as these scripts. 

### Getting the Data Set

You can then run `python synopsis_categories_and_concepts_image_downloader.py` to get the **unfiltered** raw data set - which will contain some noisy / misclassified images in the training set due to how Google Images returns results.

This download should be roughly 7.5 GB and contain roughly 63 thousand images.

The data set we are working with has images manually pruned from the above download results. 

You can follow along with the [Running Training Notes](https://github.com/Synopsis/CinemaNet/blob/master/Running%20Training%20Notes.md) to see the steps we are taking if you want to train yourself. 

Sign up for Googles AutoML Vision cloud service if you want to train your own model. At the time of this writing you will get approximately $300 in free credits.

See [Running Training Notes](https://github.com/Synopsis/CinemaNet/blob/master/Running%20Training%20Notes.md) for more info on training a model.
