from flask import Blueprint, render_template, request, session
import markdown
import os

from app.extSubtitles import download_video, extract_subtitles
from app.extQuestions import getQuestions, getAsk

bp = Blueprint('main', __name__, url_prefix='/')


@bp.get('/')
def index():
    return render_template('index.html')


@bp.get('/faq')
def faq():
    return render_template('faq.html')


@bp.get('/aboutus')
def aboutus():
    return render_template('about.html')


@bp.post('/')
def results():
    video_url = request.form['videoUrl']

    video_path = download_video(video_url)
    subtitles = extract_subtitles(video_path)
    os.remove(video_path)

    session['subtitles'] = subtitles
    return render_template('results.html', subtitles=subtitles)


@bp.post('/writequestions')
def writequestions():
    questions = getQuestions(session.get('subtitles'))

    return render_template('questions.html', questions=questions)


@bp.get('/changebutton')
def changebutton():
    return render_template('button.html')


@bp.post('/ask')
def ask():
    question = request.form['question']
    answer = getAsk(session.get('subtitles'), question)
    final_answer = markdown.markdown(answer)

    return render_template('response.html', final_answer=final_answer, question=question)