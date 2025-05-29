from typing import Iterable, Iterator, Sequence, Tuple

import numpy as np

def _kasai(s: np.ndarray, sa: np.ndarray) -> np.ndarray: ...
def _kasai_bytes(s: bytes, sa: np.ndarray) -> np.ndarray:
    """
    Same as _kasai but with a const first argument.

    TODO: Cython does not support const fused types arguments YET
    but it will be fixed in the 0.30 release
    <https://github.com/pandas-dev/pandas/issues/31710>
    """
    ...

def kasai(s: str | bytes | np.ndarray, sa: object = None) -> np.ndarray: ...
def _lcp_segtree(
    s: np.ndarray,
    sa: np.ndarray,
    lcp: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]: ...
def lcp_segtree(
    s: str | bytes | np.ndarray,
    sa: object = None,
    lcp: object = None,
) -> tuple[np.ndarray, np.ndarray]: ...
def _lcp_query(
    rank: np.ndarray,
    segtree: np.ndarray,
    queries: Sequence[Tuple[int, int]],
) -> np.ndarray: ...
def lcp_query(
    segtree: tuple[np.ndarray, np.ndarray],
    queries: Sequence[Tuple[int, int]],
) -> np.ndarray: ...
def _levenshtein(a: np.ndarray, b: np.ndarray) -> int: ...
def levenshtein(a: str | bytes | np.ndarray, b: str | bytes | np.ndarray) -> int: ...
def most_frequent_substrings(
    lcp: np.ndarray,
    length: int,
    limit: int = 0,
    minimum_count: int = 1,
) -> tuple[np.ndarray, np.ndarray]: ...
def repeated_substrings(
    suffix_array: np.ndarray,
    lcp: np.ndarray,
) -> list[tuple[int, int, int]]: ...
def _common_substrings(
    suffix_array: np.ndarray,
    lcp: np.ndarray,
    len1: int,
    limit: int,
) -> list[tuple[int, int, int]]: ...
def _min_rotation(s: bytes | np.ndarray) -> int: ...
def _min_rotation_bytes(s: bytes | np.ndarray) -> int: ...
def min_rotation(s: str | bytes | np.ndarray) -> int: ...
def _longest_previous_factor(
    s: str | bytes | np.ndarray,
    sa: np.ndarray,
    lcp: np.ndarray,
) -> np.ndarray: ...
def longest_previous_factor(
    s: str | bytes | np.ndarray,
    sa: np.ndarray | None = None,
    lcp: np.ndarray | None = None,
) -> np.ndarray: ...
def lempel_ziv_factorization(
    lpf: np.ndarray, complexity: bool = False
) -> list[int]: ...
def _lempel_ziv_complexity(s: np.ndarray, sa: np.ndarray, lcp: np.ndarray) -> int: ...
def lempel_ziv_complexity(
    s: str | bytes | np.ndarray,
    sa: np.ndarray | None = ...,
    lcp: np.ndarray | None = ...,
) -> int: ...
def kmp_censor_stream(censor: str, stream: Iterable[str]) -> Iterator[str]: ...
