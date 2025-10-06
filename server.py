from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
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
    else:
    # Return a formatted string with the emotion label and score
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant)
@app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)