from PIL import Image
from IPython.display import display
import random
import json
import os
import datetime

# setting
now_date = datetime.datetime.now().strftime('%y%m%d_%H%M%S')


# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["001", "002", "003"]
background_weights = [33, 33, 34]

bg_effect = ["001", "002", "003"]
bg_effect_weights = [33, 33, 34]

body = ["001", "002", "003"]
body_weights = [33, 33, 34]

glasses = ["001", "002", "003"]
glasses_weights = [33, 33, 34]

hat = ["001", "002", "003"]
hat_weights = [33, 33, 34]

totem = ["001", "002", "003"]
totem_weights = [33, 33, 34]

wing = ["001", "002", "003"]
wing_weights = [33, 33, 34]



#Classify traits (네이밍은 나중에 다시...)

background_files = {
    "001": "background_001",
    "002": "background_002",
    "003": "background_003",
}

bg_effect_files = {
    "001": "bg_effect_001",
    "002": "bg_effect_002",
    "003": "bg_effect_003",
}

body_files = {
    "001": "body_001",
    "002": "body_002",
    "003": "body_003",
}

glasses_files = {
    "001": "glasses_001",
    "002": "glasses_002",
    "003": "glasses_003",
}

hat_files = {
    "001": "hat_001",
    "002": "hat_002",
    "003": "hat_003",
}

totem_files = {
    "001": "totem_001",
    "002": "totem_002",
    "003": "totem_003",
}

wing_files = {
    "001": "wing_001",
    "002": "wing_002",
    "003": "wing_003",
}

## Generate Traits

# TOTAL_IMAGES = 2178  # 생성하려는 임의의 고유 이미지 수
TOTAL_IMAGES = 10  # 생성하려는 임의의 고유 이미지 수

all_images = []


# A recursive function to generate unique image combinations
def create_new_image():
    new_image = {}  #

    # For each trait category, select a random trait based on the weightings
    new_image["Background"] = random.choices(background, background_weights)[0]
    new_image["Bg_effect"] = random.choices(bg_effect, bg_effect_weights)[0]
    new_image["Body"] = random.choices(body, body_weights)[0]
    new_image["Glasses"] = random.choices(glasses, glasses_weights)[0]
    new_image["Hat"] = random.choices(hat, hat_weights)[0]
    new_image["Totem"] = random.choices(totem, totem_weights)[0]
    new_image["Wing"] = random.choices(wing, wing_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

# Get Trait Counts

background_count = {}
for item in background:
    background_count[item] = 0

bg_effect_count = {}
for item in bg_effect:
    bg_effect_count[item] = 0

body_count = {}
for item in body:
    body_count[item] = 0

glasses_count = {}
for item in glasses:
    glasses_count[item] = 0

hat_count = {}
for item in hat:
    hat_count[item] = 0

totem_count = {}
for item in totem:
    totem_count[item] = 0

wing_count = {}
for item in wing:
    wing_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    bg_effect_count[image["Bg_effect"]] += 1
    body_count[image["Body"]] += 1
    glasses_count[image["Glasses"]] += 1
    hat_count[image["Hat"]] += 1
    totem_count[image["Totem"]] += 1
    wing_count[image["Wing"]] += 1

print(background_count)
print(bg_effect_count)
print(body_count)
print(glasses_count)
print(hat_count)
print(totem_count)
print(wing_count)

#### Generate Images

os.mkdir(f'./export/{now_date}')

for item in all_images:
    im1 = Image.open(f'./resource/mandoo/background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./resource/mandoo/bg_effect/{bg_effect_files[item["Bg_effect"]]}.png').convert('RGBA')
    im3 = Image.open(f'./resource/mandoo/wing/{wing_files[item["Wing"]]}.png').convert('RGBA')
    im4 = Image.open(f'./resource/mandoo/body/{body_files[item["Body"]]}.png').convert('RGBA')
    im5 = Image.open(f'./resource/mandoo/glasses/{glasses_files[item["Glasses"]]}.png').convert('RGBA')
    im6 = Image.open(f'./resource/mandoo/hat/{hat_files[item["Hat"]]}.png').convert('RGBA')
    im7 = Image.open(f'./resource/mandoo/totem/{totem_files[item["Totem"]]}.png').convert('RGBA')

    # Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)

    # Convert to RGB
    rgb_im = com6.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save(f"./export/{now_date}/" + file_name)