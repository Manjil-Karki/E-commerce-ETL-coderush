import pandas as pd
import re
import json


def clean_names(title):
    pattern = re.compile(r'^[a-zA-Z0-9 ]+')
    match = re.search(pattern, title)
    if match:
        return match.group()
    else:
        return title
    
def clean_price(price):
    price = price.replace('\'', '"')
    price = json.loads(price)
    if 'discount' in price.keys():
        on_sale = True
        discount = price['discount']
        original_price = price['originalPrice']['value']
        sale_price = price['salePrice']['value']
    else:
        on_sale = False
        discount = None
        original_price = price['salePrice']['value']
        sale_price = price['salePrice']['value']
    
    return on_sale, discount, original_price, sale_price


def clean_ratings(rating):
    try:
        pattern = r'(?<=[a-zA-Z])\'(?=[a-zA-Z])'
        rating = re.sub(pattern, '', rating)
        rating = rating.replace("'", '"')
        rating = rating.replace('True', 'true')
        rating = rating.replace('False', 'false')
        rating = json.loads(rating)
        average = rating['ratings']['average']
        scores = rating['ratings']['scores']
        reviews = rating['reviews']
        review_text = ""
        for review in reviews:
            review_text += review['reviewContent']
        return average, scores, review_text
    except Exception as e:
        return None, None, None


def clean_specifications(specs):
    spec_str = specs.replace("\\xa0", '')
    spec_str = spec_str.replace('"', '')
    spec_str = spec_str.replace("'", '"')
    spec = json.loads(spec_str)
    spec = spec[list(spec.keys())[0]]
    return spec['features']


if __name__ == "__main__":
    new_df = pd.DataFrame()
    df = pd.read_csv("darazphones/data/phonesCrawler.csv")
    new_df['name'] = df['title'].apply(clean_names)
    new_df['scraped_time'] = df['time']
    cleaned_prices = df['price'].apply(clean_price)
    new_df['on_sale'], new_df['discount'], new_df['original_price'], new_df['sale_price'] = zip(*cleaned_prices)
    cleaned_reviews = df['review'].apply(clean_ratings)
    new_df['average_rating'], new_df['scores'], new_df['review_texts'] = zip(*cleaned_reviews)
    spec = df['specifications'].apply(clean_specifications)
    temp_df = pd.DataFrame(list(spec))
    new_df = pd.concat([new_df, temp_df], axis = 1)
    new_df.to_csv("./transformed.csv", index=False)