import csv
import io
import json
import os.path
from datetime import datetime
from typing import List

from polls.models import Question, Choice


def load_polls(directory: str) -> List[Question]:
    """
    charge un sondage depuis plusieurs fichiers csv

    :param directory:
    :return:
    """
    polls = []
    polls_lookup = {}
    with io.open(os.path.join(directory, 'polls.csv')) as filep:
        reader = csv.reader(filep, delimiter=';')
        for row in reader:
            if len(row) != 2:
                continue

            question = Question(question_text=row[0], pub_date=datetime.fromisoformat(row[1]))
            polls.append(question)
            polls_lookup[question.question_text] = question

    with io.open(os.path.join(directory, 'choices.csv')) as filep:
        reader = csv.reader(filep, delimiter=';')
        for row in reader:
            if len(row) != 2:
                continue

            question = polls_lookup[row[0]]
            choice = Choice(question=question, choice_text=row[1])
            question.local_choices.append(choice)

    return polls


def serialize_polls(path: str, polls: List[Question]):
    """
    serialize un sondage au format json

    :param polls:
    :return:
    """
    serialized_polls = []
    for question in polls:
        serialized_question = {"question_text": question.question_text, "pub_date": question.pub_date.isoformat(), "choices": []}

        for choice in question.local_choices:
            serialized_question["choices"].append({"choice_text": choice.choice_text})

        serialized_polls.append(serialized_question)

    with io.open(path, 'w') as filep:
        json.dump(serialized_polls, filep)

