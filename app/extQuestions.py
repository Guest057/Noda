import ollama
import re

def getQuestions (cont):
    response = ''

    stream = ollama.chat(
        model='llama3',
        messages=[{
            'role': 'user',
            'content': 'Extract all questions from this text: ' + cont + '// Use format [number].[question] //Dont write extra text at the start just questions'
            }],
        stream=True,
    )

    for chunk in stream:
        response += chunk['message']['content']
    
    questions = re.findall(r'[^\n.!?]*\?', response)
    return [q.strip() for q in questions]

def getAsk(cont, ques):
    response = ''

    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 
                'content': 'Read this text: ' + cont + '. I have a question(s): ' + ques
                }],
        stream=True,
    )

    for chunk in stream:
        response += chunk['message']['content']

    return response