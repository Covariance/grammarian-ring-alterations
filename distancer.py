from itertools import product
from typing import Callable, Iterable, List

from Levenshtein import distance as lev_dist # type: ignore
    

def find_equidistances(word: str, dist: int, words: Iterable[str], metric: Callable[[str, str], int] = lev_dist) -> List[str]:
    if dist == 0:
        return [word]
    return [other_word for other_word in words if metric(word, other_word) == dist]


def as_sum_of(number: int, count_of: int) -> List[List[int]]:
    if count_of == 1:
        return [[number]]
    
    ans: List[List[int]] = []
    for this in range(0, number + 1):
        with_this = [[this] + repr for repr in as_sum_of(number - this, count_of - 1)]
        ans += with_this
    
    return ans


def find_equidistances_sentence(sentence: str, dist: int, words: Iterable[str], metric: Callable[[str, str], int] = lev_dist) -> List[str]:
    splitted = sentence.split()
    
    distributions = as_sum_of(dist, len(splitted))
    
    result : List[str] = []
    
    for distribution in distributions:
        options : List[List[str]] = []
        for word, word_dist in zip(splitted, distribution):
            options.append(find_equidistances(word, word_dist, words, metric))
        
        result += list(map(lambda lst: ' '.join(lst), product(*options)))
    
    return result
