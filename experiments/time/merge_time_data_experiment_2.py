

# Import JSON module
import json
import numpy as np
from tqdm import tqdm


# Config for finetune data
time_folder_path = r'.\time_pretrain\\'
meta_json_path = r'.\meta_data.json'
item_categories = ['Musical_Instruments']
item_categories = ['Automotive', 'Cell_Phones_and_Accessories', \
              'Clothing_Shoes_and_Jewelry', 'Electronics', 'Grocery_and_Gourmet_Food', 'Home_and_Kitchen', \
              'Movies_and_TV', 'CDs_and_Vinyl']

# Config for pretrain data
# train_json_path = r'.\pretrain_data\meta_data.json'
# pretrain_categories = ['Automotive', 'Cell_Phones_and_Accessories', \
#               'Clothing_Shoes_and_Jewelry', 'Electronics', 'Grocery_and_Gourmet_Food', 'Home_and_Kitchen', \
#               'Movies_and_TV', 'CDs_and_Vinyl']

# use shortform for shorter token
month_keys = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# Only add month with sales count >= 75th percentile and is non-zero to the sentence
def get_month_count_sentence(item_prop):
    count_list = []

    for m in item_prop['month']:
        count_list.append(item_prop['month'][m])

    high_count = np.percentile(count_list, 75)

    temp_list = []

    # Get max count
    max_count = 0
    for m in item_prop['month']:
        count = item_prop['month'][m]
        if count > max_count:
            max_count = count

    # Normalize count range to 0-1
    if max_count > 0:
        for m in item_prop['month']:
            item_prop['month'][m] /= max_count

    for m in month_keys:
        if m in item_prop['month'].keys():
            temp_list.append(item_prop['month'][m])
        else:
            temp_list.append(0)



    return temp_list


# Main
f = open(meta_json_path)
train_data = json.load(f)

# Add time attributes to meta file
for cat in item_categories:
    print("pretrain_categories" + cat)
    time_json_path = time_folder_path+cat+'.json'
    f = open(time_json_path)
    time_data = json.load(f)

    for id in tqdm(time_data, ncols=100):
        if id in train_data:
            item_prop_time = time_data[id]
            item_prop_train = train_data[id]

            item_prop_train["month"] = get_month_count_sentence(item_prop_time)
            item_prop_train["season"] = " ".join(item_prop_time["season"]) if len(
                item_prop_time["season"]) > 0 else "all"
            item_prop_train["festival"] = " ".join(item_prop_time["festival"]) if len(
                item_prop_time["festival"]) > 0 else "all"


# add default values if there is no user review for the item
for id in tqdm(train_data, ncols=100):
    item_prop_train = train_data[id]

    if not "month" in item_prop_train:
        item_prop_train["month"] = [1.0] * 12
    if not "season" in item_prop_train:
        item_prop_train["season"] = "all"
    if not "festival" in item_prop_train:
        item_prop_train["festival"] = "all"

# Save
with open('meta_data_with_time_all.json', 'w', encoding='utf8') as f:
    json.dump(train_data, f)
