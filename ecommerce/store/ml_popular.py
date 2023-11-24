import numpy as np
import pandas as pd
from django.urls import reverse


def popular_products():
    paradise_ratings = pd.read_csv('behaviour_data.csv')
    paradise_ratings = paradise_ratings.dropna()

    product_data = pd.read_csv('product_data.csv')

    popular_products = pd.DataFrame(paradise_ratings.groupby('product_Id')['rating'].count())
    most_popular = popular_products.sort_values('rating', ascending=False)

    data_ratings = most_popular.sample(20)
    print(data_ratings)
    merged_dataset = pd.merge(data_ratings, product_data, on='product_Id', how='left')
    final_data = merged_dataset[['title', 'brand', 'price', 'description', 'slug', 'image', 'category_id']]
    final_data['category_id'] = final_data['category_id'].astype(int)
    

    return final_data.sample(8)

def get_absolute_url(self):
        return reverse("product-info", args=[self.slug])