# Python
import spacy
import json
import nltk
import requests

# Load spacy language model
nlp = spacy.load("en-core-web-sm-mirror")

# Retrieve a list of all chatbot answers
chatbot_responses = json.load(open("chatbot_responses.json"))

# Define a function to retrieve relevant answers to a query
def get_response(query):
    # Use the spaCy library to determine the intent of the query
    doc = nlp(query)
    intent = ""
    # Loop through all of the entities in the query and determine intent
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            intent = "greeting"
        elif entity.label_ == "QUESTION":
            intent = "question"
        elif entity.label_ == "INFORMATION":
            intent = "information"
        elif entity.label_ == "COMMAND":
            intent = "command"
    # Match the query with the appropriate response from the chatbot_responses data
    response_list = chatbot_responses[intent]
    response = response_list[nltk.FreqDist(response_list).max()]
    # Return the response
    return response
