#Using clean_product_dataset_00_2000.csv

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer #Import TfIdfVectorizer from scikit-learn

import re


prod_data = pd.read_csv('clean_product_dataset_00_2000.csv', low_memory=False)


def _removeNonAscii(s):
    return "".join(i for i in s if  ord(i)<128)

def make_lower_case(text):
    return text.lower()



def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

#Converting text descriptions into vectors using TF-IDF using Bigram or Trigram
tf = TfidfVectorizer(ngram_range=(2, 2), stop_words='english', lowercase = False)

tfidf_matrix = tf.fit_transform(prod_data['Description'].values.astype('U'))
total_words = tfidf_matrix.sum(axis=0)

#Finding the word frequency
freq = [(word, total_words[0, idx]) for word, idx in tf.vocabulary_.items()]
freq =sorted(freq, key = lambda x: x[1], reverse=True)

#converting into dataframe
bigram = pd.DataFrame(freq)

#trigram = pd.DataFrame(freq)
bigram.rename(columns = {0:'bigram', 1: 'count'}, inplace = True)

#trigram.rename(columns = {0:'trigram', 1: 'count'}, inplace = True)
#Taking first 10 records
bigram = bigram.head(10)
prod_data['item_name'] = prod_data['Product Name']
prod_data['item_name'] = prod_data['item_name'].apply(_removeNonAscii)
prod_data['item_name'] = prod_data['item_name'].apply(func=make_lower_case)
#prod_data['item_name'] = prod_data['item_name'].apply(func=remove_punctuation)
prod_data['item_name'] = prod_data['item_name'].apply(func=remove_html)
prod_data["text"] =  prod_data['Description'] + ' '+ prod_data['item_name'] + ' ' + prod_data['Category'] + ' ' + prod_data['Tags']+ ' ' + prod_data['slug']
df_shop = prod_data[['Id','Product Name','text','Image','slug']]

tf = TfidfVectorizer(ngram_range=(2, 2), stop_words='english', lowercase = False)
tfidf_matrix = tf.fit_transform(df_shop['text'].values.astype('U'))
total_words = tfidf_matrix.sum(axis=0)
total_words

#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df_shop['text'].values.astype('U'))

from sklearn.metrics.pairwise import linear_kernel
#Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim[1]
tfidf.vocabulary_

indices = pd.Series(prod_data.index, index=df_shop['slug']).drop_duplicates()

def get_recommendations(slug, cosine_sim=cosine_sim):
    # Get the index of the items that matches the title
    idx = indices[slug]

    # Get the pairwsie similarity scores of all items
    sim_scores = list(enumerate(cosine_sim[idx])) # Sort the items
    #Sort the products based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar items
    sim_scores = sim_scores[1:5]# Item indicies, Get the items indices
    shop_indices = [i[0] for i in sim_scores]


    # It reads the top 5 recommended Items titles and print the images
    return (df_shop['slug'].iloc[shop_indices])
    



#get_recommendations('guillow-airplane-design')