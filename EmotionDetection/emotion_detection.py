import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detect service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Parsing the JSON response from the API

    formatted_response = json.loads(response.text)
    # Getting the emotions from the dictionary
    # If the response status code is 200, extract the emotions from the response
    if response.status_code == 200:
    # Extracting the emotion scores
        emotions1 = formatted_response['emotionPredictions']
        emotions2 = emotions1[0]
        emotions3 = emotions2['emotion']
    

        anger_score = emotions3['anger']
        disgust_score = emotions3['disgust']
        fear_score = emotions3['fear']
        joy_score = emotions3['joy']
        sadness_score = emotions3['sadness']
    # Finding the dominant emotion

        dominant_emotion = max(emotions3, key = emotions3.get)
    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None


    # Returning a dictionary containing sentiment analysis results
    return{'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
