# import data from data.py
from data import question_data

# Question model class for quiz game. Should have two attributes: text and answer.
class Question():
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
