import numpy as np

STATES = ["s_0", "s_1", "s_2", "s_3", "s_4", "s_5"]
INPUT_ALPHABET = ["a", "b"]
START_STATE = "s_0"
ACCEPTING_STATES = ["s_2", "s_4"]
LAMBDA = 0.0755 + 0.2482
A_FIRST, A_SECOND = 0.9, 0.5
B_FIRST, B_SECOND = 0.91, 0.95

TRANSITION_MATRIX = {
    "a": np.array([
        [0, 0.5 * A_FIRST, 0.5 * (1 - A_FIRST), 0.5, 0, 0],
        [0, A_FIRST, 1 - A_FIRST, 0, 0, 0],
        [0, 0, A_SECOND, 0, 0, 1 - A_SECOND],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1]
    ]),
    "b": np.array([
        [0, 0.5, 0, 0.5 * B_FIRST, 0.5 * (1 - B_FIRST), 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, B_FIRST, 1 - B_FIRST, 0],
        [0, 0, 0, 0, B_SECOND, 1 - B_SECOND],
        [0, 0, 0, 0, 0, 1]
    ])
}


def probabilistic_automaton(str: str) -> bool:
    """
    Accepts only string that contains 3 a's and 14 b's.

    Args:
        str (str): The input string to be checked.

    Returns:
        bool: True if the string is accepted, False otherwise.
    """
    state_probabilities = np.zeros(len(STATES))
    state_probabilities[STATES.index(START_STATE)] = 1

    for i in range(len(str)):
        state_probabilities = np.dot(
            state_probabilities, TRANSITION_MATRIX[str[i]])
        # for j in range(len(state_probabilities)):
        #     print(f"{state_probabilities[j]:.4f}", end=" ")
        # print()

    for j in range(len(state_probabilities)):
        print(f"{state_probabilities[j]:.4f}", end=" ")
    print()

    # return if sum of accepting states is greater than lambda

    return sum(state_probabilities[STATES.index(state)] for state in ACCEPTING_STATES) >= LAMBDA


if __name__ == "__main__":

    words = [
        ("b" * 14) + ("a" * 3),
        ("b" * 14) + ("a" * 4),
        ("b" * 15) + ("a" * 3),
        ("b" * 13) + ("a" * 3),
        ("a" * 3) + ("b" * 14),
        ("b" * 7) + ("a" * 2) + ("b" * 7),
        ("b" * 7) + ("a" * 3) + ("b" * 7)
    ]

    tests = {
        ("b" * 14) + ("a" * 3): True,
        ("b" * 14) + ("a" * 4): False,
        ("b" * 15) + ("a" * 3): False,
        ("b" * 13) + ("a" * 3): False,
        ("a" * 3) + ("b" * 14): True,
        ("b" * 7) + ("a" * 2) + ("b" * 7): False,
        ("b" * 7) + ("a" * 3) + ("b" * 7): True
    }

    for word in words:
        print(f"Word {word}: {probabilistic_automaton(word)}")

    for word, result in tests.items():
        assert probabilistic_automaton(word) == result

    print("All tests passed!")
