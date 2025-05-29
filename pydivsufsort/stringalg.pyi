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
) -> tuple[NDArray[Any], NDArray[Any]]: ...
def repeated_substrings(
    suffix_array: NDArray[Any],
    lcp: NDArray[Any],
) -> list[tuple[int, int, int]]: ...
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
) -> NDArray[Any]: ...
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
def kmp_censor_stream(censor: str, stream: Iterable[str]) -> Iterator[str]: ...
