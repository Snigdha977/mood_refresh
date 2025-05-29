from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    mood = None
    videos = []
    if request.method == 'POST':
        user_input = request.form.get('mood')
        mood = detect_mood(user_input)
        # For demo, mock video URLs based on mood
        videos = get_videos_for_mood(mood)
    return render_template('index.html', mood=mood, videos=videos)

def detect_mood(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return "happy"
    elif analysis.sentiment.polarity < -0.1:
        return "sad"
    else:
        return "neutral"

def get_videos_for_mood(mood):
    if mood == "happy":
        return ["https://www.youtube.com/embed/d-diB65scQU", "https://www.youtube.com/embed/2Vv-BfVoq4g"]
    elif mood == "sad":
        return ["https://www.youtube.com/embed/hLQl3WQQoQ0", "https://www.youtube.com/embed/4N3N1MlvVc4"]
    else:
        return ["https://www.youtube.com/embed/l482T0yNkeo"]

if __name__ == '__main__':
    app.run(debug=True)
