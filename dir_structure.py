from random import random
import os
from glob import glob
import json
# Path to your images
image_paths = glob("trainingset/*")
#Path to your annotations from VIA tool
annotation_file = 'kylo_luke.json'
#clean up the annotations a little
annotations = json.load(open(annotation_file))
cleaned_annotations = {}
for k,v in annotations['_via_img_metadata'].items():
    cleaned_annotations[v['filename']] = v
# create train and validation directories
train_annotations = {}
valid_annotations = {}
# 20% of images in validation folder
for img in image_paths:
    # Image goes to Validation folder
    if random()<0.2:
        os.system("cp "+ img + " procdata/val/")
        img = img.split("/")[-1]
        valid_annotations[img] = cleaned_annotations[img]
    else:
        os.system("cp "+ img + " procdata/train/")
        img = img.split("/")[-1]
        train_annotations[img] = cleaned_annotations[img]
# put different annotations in different folders
with open('procdata/val/via_region_data.json', 'w') as fp:
    json.dump(valid_annotations, fp)
with open('procdata/train/via_region_data.json', 'w') as fp:
    json.dump(train_annotations, fp)
