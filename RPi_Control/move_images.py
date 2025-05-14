import os

# img_dir = "AnnotatedImages_Fernando_2/OriginalImages"
# mask_dir = "AnnotatedImages_Fernando_2/AnnotatedImages"

img_dir = "image_dataset_1/original/"
mask_dir = "image_dataset_1/mask/"

names = [n.split(".")[0] for n in os.listdir(img_dir)]

print(len(names))

    
    