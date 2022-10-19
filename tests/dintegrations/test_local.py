import os
from unittest import TestCase

from fixtup import fixtup

from polls.local import load_polls, serialize_polls


class LocalTest(TestCase):

    def test_load_polls_should_load_questions_from_csv_file(self):
        with fixtup.up('polls'):
            polls = load_polls(os.getcwd())
            assert len(polls) == 2

    def test_load_polls_should_load_choices_in_questions_from_csv_file(self):
        with fixtup.up('polls'):
            polls = load_polls(os.getcwd())
            assert len(polls[0].local_choices) == 3

    def test_serialize_polls_should_write_polls_as_json(self):
        with fixtup.up('polls'):
            polls = load_polls(os.getcwd())
            json_dump_path = os.path.join(os.getcwd(), 'file.json')
            polls = serialize_polls(json_dump_path, polls)
            assert os.path.isfile(json_dump_path), f"{json_dump_path} is missing"
