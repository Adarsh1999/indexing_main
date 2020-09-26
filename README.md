# indexing_main
Starts indexing files from az storage

## Installation

```
sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
```

## Container Required
docker run -d -p 80:3000 --name unoconv zrrrzzt/docker-unoconv-webservice
