# Training Notes for Synopsis ML Model

Plan is:

1. ✓ Create an image data set download script with our labels and search 
2. ✓ Download images from google via `synopsis_categories_and_concepts_image_downloader.py` 
3. ✓ Attempt to train without manually pruning the data (by manually finessing the google search terms)
4. Manually prune some of the poorer quality categories and measure the accuracy recall gains (this is mostly for curiosity and quantitative data for a blog / medium post to be honest)
5. Build sperate classifiers (non multi categorymulti label / attribute) models for each disctinct groupings of concept 
6. Run inference on our entire data setto get a fully labelled multi category data set boostrapped
7. Train a final model on our entire data set.


## Current Issues:

* AutoML's labels have a set length, and our 'knowledge graph' reverse DNS label naming scheme is too long, and clips our labels so they occasionally resolve to the same entry for multiple concepts. This is bad. We should re-think this for AutoML
* * temporary solution - remove the synopsis.image dns prefix for labels (since its implied at this stage and prepend that using CoreML Tools on our resultant models and labels? 

* Some of our categories return the same image for different concepts, requiring us to either set up a multi label classifier or manually prune for duplicates.

## Training Results:

[See our google sheet for ongoing training results](https://docs.google.com/spreadsheets/d/1OMRt1g6umE6Ipn6KPlmKh5k0RDUNPma5ESEK1bJGGzQ/edit#gid=0)
