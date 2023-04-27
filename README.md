### Intro
This is a pipeline that uses Python and the Segment Anything (SAM) and Grounding DINO models to automatically segment and label satellite image data from Umbra's synthetic aperture radar (SAR) open dataset.  It is a multi-modal application of multiple SOTA transformer models (Segment Anything for segmentation, Grounding DINO for bounding box and label generation) to SAR satellite imagery.  

### Code outline
This repository contains: 
* A proof of concept notebook for demonstrating how to use SAM and Grounding DINO together to segment and label satellite images
* A draft of a pipeline to automate loading and processing images from datasets and model them

### Running the pipeline
* Run `docker build -t auto-segment-label-satellite-images .` to build the Docker image
* Run the Docker container with `docker run -p 4000:80 auto-segment-label-satellite-images`