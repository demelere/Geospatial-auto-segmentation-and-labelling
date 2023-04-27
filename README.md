### Intro
This is a pipeline that uses Python and the Segment Anything (SAM) and Grounding DINO models to automatically segment and label satellite image data from Umbra's synthetic aperture radar (SAR) open dataset

### Running the project
* Run `docker build -t auto-segment-label-satellite-images .` to build the Docker image
* Run the Docker container with `docker run -p 4000:80 auto-segment-label-satellite-images`