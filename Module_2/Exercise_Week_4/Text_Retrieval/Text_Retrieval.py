import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vi_data_df = pd.read_csv(
    'Module_2/Exercise_Week_4/Text_Retrieval/vi_text_retrieval.csv')
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

# Question 10
print(context_embedded.toarray()[7][0])
print()


def cosine_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(
        context_embedded, query_embedded).reshape((-1,))

    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        print("Score:", cosine_scores[idx])
        print(vi_data_df.iloc[idx, 2])
        print("===========")


question = vi_data_df.iloc[0]['question']

# Question 11
print(cosine_search(question, tfidf_vectorizer, top_d=5))
print("##########")


def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_score = np.corrcoef(
        query_embedded.toarray(),
        context_embedded.toarray()
    )
    corr_scores = corr_score[0][1:]

    for idx in corr_scores.argsort()[-top_d:][::-1]:
        print("Score:", corr_scores[idx])
        print(vi_data_df.iloc[idx, 2])
        print("===========")


# Question 12
print(corr_search(question, tfidf_vectorizer, top_d=5))
