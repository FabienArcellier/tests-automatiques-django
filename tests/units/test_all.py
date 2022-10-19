from unittest import TestCase

from polls.votes import count_votes


class VotesTests(TestCase):

    def test_count_votes_should_add_all_the_votes_together(self):
        votes = [0, 5, 12, 0, 12]
        self.assertEqual(count_votes(votes), 29)
