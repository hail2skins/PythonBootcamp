# Import question class from question_model
from question_model import Question

# Import question_data from data.py and create a list of Question objects from the data.
from data import question_data

# Create a list of question objects from the data.
question_bank = [] # empty list to store question objects
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
print(question_bank[0].text)