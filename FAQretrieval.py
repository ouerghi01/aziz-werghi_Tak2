import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
def read_data (path):
    try :
        return pd.read_csv(path)
    except(ValueError, TypeError) :
        print("Caught a ValueError or TypeError!")
        return
def find_best_reponse(question):
    data= read_data("Data/questions_and_answers.csv")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    corpus = data["Question"].to_list()
    matrix=model.encode(corpus+[question])
    most_similar_index =np.argmax(model.similarity(matrix[:-1],matrix[-1].reshape(1,-1)).flatten()).item()
    return data["Answer"][most_similar_index]



