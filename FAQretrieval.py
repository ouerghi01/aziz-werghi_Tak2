import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize
stop_words  = set(stopwords.words('english'))
def read_data(path):
    """
    Reads a CSV file from the specified path.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.

    Exceptions:
        ValueError: If the file format is incorrect.
        TypeError: If the path is invalid or incompatible.
    """
    try:
        return pd.read_csv(path)
    except (ValueError, TypeError):
        print("Caught a ValueError or TypeError!")
        return

def find_best_response(question):
    """
    Finds the best response for a given question from a pre-defined dataset.

    This function uses a pre-trained SentenceTransformer model to encode the
    questions and compare their similarity with the user-provided question.
    The most similar question's answer is returned.

    Args:
        question (str): The input question to be answered.

    Returns:
        str: The most relevant answer from the dataset.

    Workflow:
        1. Load the dataset from "Data/questions_and_answers.csv".
        2. Encode all questions in the dataset along with the input question.
        3. Compute similarity between the input and dataset questions.
        4. Return the answer corresponding to the most similar question.

    Exceptions:
        Exception: Handles and reports unexpected errors.
    """

    data = read_data("Data/questions_and_answers.csv")
    # Normalize and remove stopwords from the corpus and the question
    question, corpus = preprocess_question_and_corpus(question, data)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    matrix = model.encode(corpus + [question])
    most_similar_index = np.argmax(
        model.similarity(matrix[:-1], matrix[-1].reshape(1, -1)).flatten()
    ).item()
    
    return data["Answer"][most_similar_index]

def preprocess_question_and_corpus(question, data):
    """
    Preprocesses a given question and a corpus of questions by tokenizing,
    converting to lowercase, removing stop words, and applying stemming.

    Args:
        question (str): The question to preprocess.
        data (pandas.DataFrame): A DataFrame containing a column "Question"
        with the corpus of questions to preprocess.

    Returns:
        tuple: A tuple containing the preprocessed question (str) and the 
        preprocessed corpus (list of str).
    """
    ps = PorterStemmer()
    corpus = [" ".join([ ps.stem( w.lower()) for w in word_tokenize(p) if w.lower() not in stop_words]) for p in data["Question"].to_list()]
    question = " ".join([ps.stem(w.lower()) for w in word_tokenize(question) if w.lower() not in stop_words])
    return question,corpus
