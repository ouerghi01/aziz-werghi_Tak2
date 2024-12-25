import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

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
    model = SentenceTransformer("all-MiniLM-L6-v2")
    corpus = data["Question"].to_list()
    matrix = model.encode(corpus + [question])
    most_similar_index = np.argmax(
        model.similarity(matrix[:-1], matrix[-1].reshape(1, -1)).flatten()
    ).item()
    
    return data["Answer"][most_similar_index]
