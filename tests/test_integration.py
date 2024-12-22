import pytest

from app.factory import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"You need it" in response.data


def test_faq_page(client):
    response = client.get('/faq')
    assert response.status_code == 200
    assert b"FAQ" in response.data


def test_results_page(client, mocker):
    mock_download_video = mocker.patch('app.blueprints.main.download_video', return_value='test_video_path.mp4')
    mock_extract_subtitles = mocker.patch('app.blueprints.main.extract_subtitles', return_value='Mock Subtitles')

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.makedirs')
    mocker.patch('os.remove')

    response = client.post('/', data={'videoUrl': 'http://testvideo.com'})

    assert response.status_code == 200
    assert b"Mock Subtitles" in response.data
    mock_download_video.assert_called_once_with('http://testvideo.com')
    mock_extract_subtitles.assert_called_once_with('test_video_path.mp4')


def test_writequestions_page(client, mocker):
    mock_chat = mocker.patch('ollama.chat', return_value=[
        {'message': {'content': "1. What is your name?\n2. How are you?"}}
    ])

    with client.session_transaction() as sess:
        sess['subtitles'] = 'Mock Subtitles'

    response = client.post('/writequestions')

    assert response.status_code == 200
    assert b"What is your name?" in response.data
    assert b"How are you?" in response.data
    mock_chat.assert_called_once()


def test_ask_page(client, mocker):
    mock_chat = mocker.patch('ollama.chat', return_value=[
        {'message': {'content': "This is a mock answer."}}
    ])

    with client.session_transaction() as sess:
        sess['subtitles'] = 'Mock Subtitles'

    response = client.post('/ask', data={'question': 'Test Question'})

    assert response.status_code == 200
    assert b"This is a mock answer." in response.data
    assert b"Test Question" in response.data
    mock_chat.assert_called_once()
