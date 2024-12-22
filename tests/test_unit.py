import pytest
from app.extQuestions import getQuestions, getAsk

@pytest.mark.parametrize("text", [
    'On weekends, people often spend their time in different ways. What do you usually do on weekends? Yesterday, the weather was so beautiful that I decided to take a walk in the park. While walking, I thought about a book our friend recently recommended. Have you read it yet? Spending time outdoors or with friends always seems to improve my mood. Speaking of new experiences, do you think it’s worth trying the new restaurant everyone is talking about? After a lot of hesitation, I finally signed up for the gym. Why is it that some people find it so easy to stay motivated when starting something new? Later this evening, my family and I are planning to watch a movie together. I wonder if the weather tomorrow will be good enough for a picnic—it would be such a nice way to relax. If not, I might stay home and try cooking a new dish I’ve been curious about. Weekends are always a great chance to recharge and try something different!'
])
def test_question_finder(text):
    response = getQuestions(text)
    assert len(response) >= 4


@pytest.mark.parametrize("text, question, search_words", [
    ('Potatoes are delicious.', 'Are potatoes tasty?', ['are', 'potatoes', 'tasty', 'yes'])
])
def test_ai_response(text, question, search_words):
    response = getAsk(text, question)
    found_words = [word for word in search_words if word.lower() in response.lower()]
    assert len(found_words) >= len(search_words) / 1.5
