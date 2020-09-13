import textract
import re
import uuid
import subprocess
import os
import re
from pathlib import Path
import chardet

class FileExtract:
    def extract_text_docs(self, file):
        text = textract.process(file)
        text = text.decode('utf-8')
    # Decodes text
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    # Removes \n \r \t
        text = re.sub(' +', ' ', text)
    # Removes extra white spaces
        return text


    def extract_images_docs(self, file):
        pass


    def extract_images_epub(self, file):
        pass

    def extract_images_odt(self, file):
        pass


    def extract_text_pdf(self, file):
        text_file = "Services/text_files/" + str(uuid.uuid4()) + ".txt"
        """Extract text"""
        subprocess.call(["./Services/pdftotext", file, text_file])

        """TODO: check if the txt contains any unknown character and remove it"""
        with open(text_file, 'rb') as raw:
            raw_text = raw.read()
        encoding_dict = chardet.detect(raw_text)
        text = raw_text.decode(encoding_dict["encoding"])
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text)
        text = re.sub(' +', ' ', text)
        """Remove txt files"""
        os.remove(text_file)
        return text


    def extract_images_pdf(self, file):
        image_folder = "Services/images/" + str(uuid.uuid4()) + "/"
        os.mkdir(image_folder)
        images = []
        """Extract images"""
        subprocess.call(["./Services/pdfimages", "-j", file, image_folder])
        for path in Path(image_folder).rglob('*.jpg'):
            images.append(path.name)
        """TODO: remove rest files"""
        images_list = []
        for image in images:
            images_list.append(image_folder+str(image))
        final_response = {
            "images": images_list,
            "images_folder": image_folder
        }
        return final_response


