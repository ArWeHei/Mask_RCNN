from random import random
import os
from glob import glob
import json
# Path to your images
image_paths = glob("witcher/*/annotated/*.jpg")
#Path to your annotations from VIA tool
annotation_files = glob("witcher/*/annotated/annotations.json")
#clean up the annotations a little
cleaned_annotations = {}
train_annotations = {}
valid_annotations = {}

os.system("mkdir "+"procdata")
os.system("mkdir "+"procdata/train/")
os.system("mkdir "+"procdata/val/")

for annotation_file in annotation_files:
    annotations = json.load(open(annotation_file))
    for k,v in annotations['_via_img_metadata'].items():
            cleaned_annotations[v['filename']] = v
    # create train and validation directories
    # 20% of images in validation folder
for img in image_paths:
    #breakpoint()
    # Image goes to Validation folder
    img_name = img.split("/")[-1]
    if random()<0.1:
        os.system("cp "+ img + " procdata/val/")
        valid_annotations[img_name] = cleaned_annotations[img_name]
    
    os.system("cp "+ img + " procdata/train/")
    train_annotations[img_name] = cleaned_annotations[img_name]
# put different annotations in different folders
with open('procdata/val/via_region_data.json', 'w') as fp:
    json.dump(valid_annotations, fp)
with open('procdata/train/via_region_data.json', 'w') as fp:
    json.dump(train_annotations, fp)
