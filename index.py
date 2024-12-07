from flask import Flask, render_template, session, request
import sys
import os
import io
import markdown

from extSubtitles import download_video, extract_subtitles
from extQuestions import getQuestions, getAsk

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

app.secret_key = '123456'

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/faq')
def faq():
    return render_template ('faq.html')

@app.get('/aboutus')
def aboutus():
    return render_template ('about.html')

@app.post('/')
def results():
    video_url = request.form['videoUrl']
    
    video_path = download_video(video_url)
    subtitles = extract_subtitles(video_path)
    os.remove(video_path)

    session['subtitles'] = subtitles
    return render_template('results.html', subtitles=subtitles)

@app.post('/writequestions')
def writequestions():
    questions = getQuestions(session.get('subtitles'))

    return render_template('questions.html', questions=questions)

@app.get('/changebutton')
def changebutton():
    return render_template('button.html')

@app.post('/ask')
def ask():
    question = request.form['question']
    answer = getAsk(session.get('subtitles'), question)
    final_answer = markdown.markdown(answer)

    return render_template ('response.html', final_answer=final_answer, question=question)

if __name__ == '__main__':
    app.run(debug=True)
