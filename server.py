"""
This server interface is web application deployment for
emotion detection application
Calls emotion detection analyser function
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function gets an input from a text box 
    calls an emotion detector function to find the emotion scores
    of the text and finds the dominant emotion. In case of invalid input
    it displays an error
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant = response['dominant_emotion']
    if dominant is None:
        return "Invalid text! Please try again!."
    # Return a formatted string with the emotion label and score
    message = f"For the given statement, the system response is 'anger': {anger_score}, \
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. \
    The dominant emotion is {dominant}."
    return message
@app.route("/")
def render_index_page():
    """
    This is a rendering function for the emotion detection web application
    """
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
