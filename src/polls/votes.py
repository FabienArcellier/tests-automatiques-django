import typing
from typing import List

if typing.TYPE_CHECKING:
    from polls.models import Choice


def count_votes(votes: List[int]) -> int:
    return sum(votes)


def count_votes_from_choices(choices: List['Choice']):
    votes = []
    for choice in choices:
        votes.append(choice.votes)

    return count_votes(votes)
