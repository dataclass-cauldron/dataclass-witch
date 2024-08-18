from typing import Literal, ClassVar, Generic, Union, List, Tuple, Dict, Callable

import pytest

from dataclass_witch.type_def import T
from dataclass_witch.utils.typing_compat import get_origin, get_args


@pytest.mark.parametrize(
    "tp,expected",
    [
        (Literal[42], Literal),
        (int, int),
        (ClassVar[int], ClassVar),
        (Generic, Generic),
        (Generic[T], Generic),
        (Union[T, int], Union),
        (List[Tuple[T, T]][int], list),
    ],
)
def test_get_origin(tp, expected):
    actual = get_origin(tp)
    assert actual is expected


@pytest.mark.parametrize(
    "tp,expected",
    [
        (Dict[str, int], (str, int)),
        (int, ()),
        (Callable[[], T][int], ([], int)),
        pytest.param(
            Union[int, Union[T, int], str][int],
            (int, str),
        ),
        pytest.param(
            Union[int, Tuple[T, int]][str],
            (int, Tuple[str, int]),
        ),
    ],
)
def test_get_args(tp, expected):
    actual = get_args(tp)
    assert actual == expected
