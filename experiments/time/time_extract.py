# This program will extract time-related information from user reviews for items

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import pandas as pd
import gzip
import json

from tqdm import tqdm
from datetime import datetime


# Set seq data path and item category
data_path = r'DATA_PATH'
item_type = 'Office_Products'
seq_path = data_path + r'\\'+item_type+'.json.gz'


# keywords to check in review text
keyword_map = {
    "season": ["winter", "summer", "autumn", "spring"],
    "festival": ["easter", "good friday", "valentine", "april fool", "christmas", "xmas", "new year", "birthday", "halloween", ],
}

# function to read json file


def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield json.loads(l)


def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

# Check time-related keywords in review text and add to result map if it presents


def extract_keyword_type(review):

    review = nltk.word_tokenize(review)
    review = " ".join(review)
    review_map = {}
    for ktype in keyword_map:
        intercept = []
        for w in keyword_map[ktype]:
            if w in review:
                intercept.append(w)

        if len(intercept) > 0:
            review_map[ktype] = intercept
    return review_map


# init the monthly sales count to zero
def init_item():
    prop_map = {}
    prop_map["month"] = {}
    prop_map["month"]["January"] = 0
    prop_map["month"]["February"] = 0
    prop_map["month"]["March"] = 0
    prop_map["month"]["April"] = 0
    prop_map["month"]["May"] = 0
    prop_map["month"]["June"] = 0
    prop_map["month"]["July"] = 0
    prop_map["month"]["August"] = 0
    prop_map["month"]["September"] = 0
    prop_map["month"]["October"] = 0
    prop_map["month"]["November"] = 0
    prop_map["month"]["December"] = 0
    prop_map["season"] = []
    prop_map["festival"] = []
    return prop_map


# read seq data
df = getDF(seq_path)
maxid = df.shape[0]

item_map = {}
for i in tqdm(range(0, maxid), ncols=100):
    try:
        review = df["reviewText"].values[i]
        if not isinstance(review, str):
            review = ""
        asin = df["asin"].values[i]
        summary = df["summary"].values[i]
        style = df["style"].values[i]
        overall = df["overall"].values[i]
        unixReviewTime = df["unixReviewTime"].values[i]

        # Get month from review timesamp
        month = datetime.utcfromtimestamp(unixReviewTime).strftime('%B')

        # Get keywords from review text
        keywords_list = extract_keyword_type(review.lower())

        # Init and add sales count
        if asin not in item_map:
            item_map[asin] = init_item()
        item_map[asin]["month"][month] += 1

        # append keywords from review text to item
        for ktype in keywords_list:
            for keyword in keywords_list[ktype]:
                if keyword not in item_map[asin][ktype]:
                    item_map[asin][ktype].append(keyword)
        # Debug use
        # print(df["reviewText"].values[i])
        # print(str(i)+"......")
        # print("\n+review " + review)
        # print("\n+summary " + summary)
        # print("\n+overall " + str(overall))
        # print("\n+unixReviewTime " + str(unixReviewTime))
        # print("\n+unixReviewTime " + month)
        # print(style)
    except Exception as e:
        print(e)

# Save result to json file
json_object = json.dumps(item_map, indent=2)
file = open('./time/'+item_type+'2.json', 'w')
file.write(json_object)
file.close()
summary_list = {}
