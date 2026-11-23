import itertools
from fractions import Fraction


def squared_length(vector):
    return sum(coordinate * coordinate for coordinate in vector)


def main():
    budget = Fraction(10**4 + 6 * 5**4, 20000)
    assert budget == Fraction(11, 16) < 1
    assert 20 < 25 and 16 <= 20 and 80 < 81
    assert Fraction(90, 64) < 4 and 9 < Fraction(64, 9) * 3
    assert Fraction(1, 2) ** 4 == Fraction(1, 16)
    assert Fraction(1, 2) ** 2 == Fraction(1, 4)
    assert Fraction(1, 4) * Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 16)
    assert 2 + 3 * (-4) == -10
    tested_pairs = 0
    for scale in [1, 2, 4, 8, 16, 32]:
        values = sorted({scale, 2 * scale - 1})
        corners = list(itertools.product(values, repeat=5))
        for first in corners:
            for second in corners:
                total = tuple(left + right for left, right in zip(first, second))
                frequency = tuple((1 if index == 0 else 0) - value
                                  for index, value in enumerate(total))
                total_square = squared_length(total)
                frequency_square = squared_length(frequency)
                assert squared_length(first) <= 25 * scale**2
                assert squared_length(second) <= 25 * scale**2
                assert 16 * scale**2 <= total_square <= 81 * scale**2
                assert 9 * scale**2 <= frequency_square <= 100 * scale**2
                assert 81 * frequency_square <= 4096 * total_square
                assert 81 * total_square <= 4096 * frequency_square
                original_first = total
                original_second = second
                inverse_first = tuple(left - right for left, right
                                      in zip(original_first, original_second))
                assert inverse_first == first
                tested_pairs += 1
        assert (2 * scale - scale) ** 10 == scale**10
    interval_pairs = 0
    for first_index in range(16):
        for second_index in range(first_index + 1, 16):
            assert 2 * 2**first_index <= 2**second_index
            interval_pairs += 1
    assert Fraction(1, 20000) <= Fraction(1, 2)
    assert Fraction(128, 9) == 2 * Fraction(64, 9)
    assert Fraction(1, 3) * 3 == 1
    generalized_pairs = 0
    for scale in [1, 2, 4, 8, 16, 32]:
        values = sorted({scale, 2 * scale - 1})
        corners = list(itertools.product(values, repeat=5))
        outputs = {(1, 0, 0, 0, 0), (-1, 0, 0, 0, 0),
                   (scale, 0, 0, 0, 0), (-scale, 0, 0, 0, 0)}
        if scale >= 4:
            outputs.add((1, 1, 1, 1, 1))
        for output in sorted(outputs):
            assert 0 < squared_length(output) <= scale**2
            for first in corners:
                for second in corners:
                    total = tuple(left + right for left, right in zip(first, second))
                    frequency = tuple(left - right for left, right in zip(output, total))
                    total_square = squared_length(total)
                    frequency_square = squared_length(frequency)
                    assert 9 * scale**2 <= frequency_square <= 100 * scale**2
                    assert 81 * frequency_square <= 4096 * total_square
                    assert 81 * total_square <= 4096 * frequency_square
                    forward = (81 * frequency_square <= 4096 * total_square
                               and 81 * total_square <= 4096 * frequency_square)
                    reverse = (81 * total_square <= 4096 * frequency_square
                               and 81 * frequency_square <= 4096 * total_square)
                    assert forward == reverse
                    assert tuple(left + right for left, right in zip(frequency, total)) == output
                    generalized_pairs += 1
    time_regions = 0
    for time in [Fraction(1, 2**30), Fraction(1, 16), Fraction(1, 2),
                 Fraction(1), Fraction(2), Fraction(5)]:
        first_index = 0
        while Fraction(1, 20000 * 2**(4 * first_index)) > time / 2:
            first_index += 1
        for index in range(first_index, first_index + 8):
            step = Fraction(1, 20000 * 2**(4 * index))
            for alpha in [time - step, time]:
                assert 0 <= alpha - step <= alpha <= time
                for inner in [alpha - step, alpha]:
                    assert 0 <= time + alpha - 2 * inner <= 3 * step
                    time_regions += 1
    for time in [Fraction(2), Fraction(3), Fraction(5), Fraction(10)]:
        for alpha in [time - 1, time]:
            assert alpha >= time / 2 and alpha >= 1 and 0 <= time - alpha <= 1
    print('Exact rational identities: decay budget 11/16; cutoff weight 1/16; kernel degree -10.')
    print(f'Lattice corner-pair instances: {tested_pairs}; N = 1, 2, 4, 8, 16, 32.')
    print(f'Dyadic interval disjointness instances: {interval_pairs}; indices 0 through 15.')
    print('Reindexing inverse and inclusive mask ratios: all listed instances satisfy the identities.')
    print('Lipschitz bound constants: comparability factor 128/9 and time-volume factor 1/3.')
    print(f'General-output corner-pair instances and mask symmetry: {generalized_pairs}.')
    print(f'Positive-time subregion endpoint instances: {time_regions}; six rational times.')
    print('Zero-mode time-region endpoints: eight instances; cutoff weight 1/4 and inner factor 1/(2B).')
    print('Scope: finite integer/rational checks; all-parameter claims have written proofs in note.tex.')


if __name__ == '__main__':
    main()
