from typing import Any, Iterable, Iterator, Sequence, Tuple

from numpy.typing import NDArray

def _kasai(s: NDArray[Any], sa: NDArray[Any]) -> NDArray[Any]: ...
def _kasai_bytes(s: bytes, sa: NDArray[Any]) -> NDArray[Any]:
    """
    Same as _kasai but with a const first argument.

    TODO: Cython does not support const fused types arguments YET
    but it will be fixed in the 0.30 release
    <https://github.com/pandas-dev/pandas/issues/31710>
    """
    ...

def kasai(
    s: str | bytes | NDArray[Any], sa: NDArray[Any] | None = None
) -> NDArray[Any]: ...
def _lcp_segtree(
    s: NDArray[Any],
    sa: NDArray[Any],
    lcp: NDArray[Any],
) -> tuple[NDArray[Any], NDArray[Any]]: ...
def lcp_segtree(
    s: str | bytes | NDArray[Any],
    sa: NDArray[Any] | None = None,
    lcp: NDArray[Any] | None = None,
) -> tuple[NDArray[Any], NDArray[Any]]: ...
def _lcp_query(
    rank: NDArray[Any],
    segtree: NDArray[Any],
    queries: Sequence[Tuple[int, int]],
) -> NDArray[Any]: ...
def lcp_query(
    segtree: tuple[NDArray[Any], NDArray[Any]],
    queries: Sequence[Tuple[int, int]],
) -> NDArray[Any]: ...
def _levenshtein(a: NDArray[Any], b: NDArray[Any]) -> int: ...
def levenshtein(
    a: str | bytes | NDArray[Any], b: str | bytes | NDArray[Any]
) -> int: ...
def most_frequent_substrings(
    lcp: NDArray[Any],
    length: int,
    limit: int = 0,
    minimum_count: int = 1,
) -> tuple[NDArray[Any], NDArray[Any]]:
    """
    Find the most frequent substrings of a given length in a string.
    If `limit` is not 0, only the `limit` most frequent substrings are returned.
    If `minimum_count` is not 1, only the substrings that occur at least `minimum_count` times are returned.

    Parameters
    ----------

    lcp : np.ndarray
        lcp array
    length : int
        length of the substrings to compare
    limit : int (default 0)
        number of substrings to extract, 0 for all of them
    minimum_count : int (default 1)
        ignore the substrings that occur less than `minimum_count` times


    Returns
    -------
    positions : np.ndarray
        position in the suffix array
    counts : np.ndarray
        number of occurrences, decreasing
    """
    ...

def repeated_substrings(
    suffix_array: NDArray[Any],
    lcp: NDArray[Any],
) -> list[tuple[int, int, int]]:
    """
    See https://github.com/louisabraham/pydivsufsort/issues/42 for more details

    Parameters
    ----------
    suffix_array : np.ndarray
        suffix array
    lcp : np.ndarray
        lcp array

    Returns
    -------
    ranges : list
        list of (start, end, length) tuples
        All positions in suffix_array[start:end] correspond to
        the same repeated substring with that length.
    """
    ...

def _common_substrings(
    suffix_array: NDArray[Any],
    lcp: NDArray[Any],
    len1: int,
    limit: int,
) -> list[tuple[int, int, int]]: ...
def _min_rotation(s: bytes | NDArray[Any]) -> int: ...
def _min_rotation_bytes(s: bytes | NDArray[Any]) -> int: ...
def min_rotation(s: str | bytes | NDArray[Any]) -> int: ...
def _longest_previous_factor(
    s: str | bytes | NDArray[Any],
    sa: NDArray[Any],
    lcp: NDArray[Any],
) -> NDArray[Any]:
    """
    Crochemore, Maxime, Lucian Ilie, and William F. Smyth.
    "A simple algorithm for computing the Lempel Ziv factorization."
    Data Compression Conference (DCC 2008). IEEE, 2008.
    """
    ...

def longest_previous_factor(
    s: str | bytes | NDArray[Any],
    sa: NDArray[Any] | None = None,
    lcp: NDArray[Any] | None = None,
) -> NDArray[Any]: ...
def lempel_ziv_factorization(
    lpf: NDArray[Any], complexity: bool = False
) -> list[int]: ...
def _lempel_ziv_complexity(
    s: NDArray[Any], sa: NDArray[Any], lcp: NDArray[Any]
) -> int: ...
def lempel_ziv_complexity(
    s: str | bytes | NDArray[Any],
    sa: NDArray[Any] | None = ...,
    lcp: NDArray[Any] | None = ...,
) -> int: ...
def kmp_censor_stream(censor: str, stream: Iterable[str]) -> Iterator[str]:
    """
    Uses KMP algorithm to censor text from a stream of str.
    """
    ...
