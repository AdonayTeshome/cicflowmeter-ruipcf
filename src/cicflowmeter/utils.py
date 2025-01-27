import uuid
import numpy
from itertools import islice, zip_longest
from typing import Any, Dict, Iterable, List, Tuple, Union


def grouper(iterable: Iterable, n: int, max_groups: int = 0, fillvalue: Any = None) -> Iterable[Tuple[Any, ...]]:
    """Collect data into fixed-length chunks or blocks"""

    if max_groups > 0:
        iterable = islice(iterable, max_groups * n)

    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def random_string() -> str:
    return uuid.uuid4().hex[:6].upper().replace("0", "X").replace("O", "Y")


def get_statistics(alist: List[Union[int, float]]) -> Dict[str, Union[int, float]]:
    """Get summary statistics of a list"""
    iat = dict()

    if len(alist) > 1:
        iat["total"] = sum(alist)
        iat["max"] = max(alist)
        iat["min"] = min(alist)
        iat["mean"] = numpy.mean(alist)
        iat["std"] = numpy.sqrt(numpy.var(alist))
    else:
        iat["total"] = 0
        iat["max"] = 0
        iat["min"] = 0
        iat["mean"] = 0
        iat["std"] = 0

    return iat
