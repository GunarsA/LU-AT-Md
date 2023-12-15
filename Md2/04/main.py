import numpy as np

STATES = ["s_0", "s_1", "s_2", "s_3", "s_4", "s_5", "s_6", "s_7", "s_8",]
INPUT_ALPHABET = ["a", "b"]
START_STATE = "s_0"
ACCEPTING_STATES = ["s_7"]

LAMBDA, FIRST, SECOND = 0.496, 0.91, 0.95
TRANSITION_MATRIX = {
    "a": np.array([
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]),
    "b": np.array([
        [FIRST, 1 - FIRST, 0, 0, 0, 0, 0, 0, 0],
        [0, SECOND, 0, 0, 0, 0, 0, 0, 1 - SECOND],
        [0, 0, FIRST, 1 - FIRST, 0, 0, 0, 0, 0],
        [0, 0, 0, SECOND, 0, 0, 0, 0, 1 - SECOND],
        [0, 0, 0, 0, FIRST, 1 - FIRST, 0, 0, 0],
        [0, 0, 0, 0, 0, SECOND, 0, 0, 1 - SECOND],
        [0, 0, 0, 0, 0, 0, FIRST, 1 - FIRST, 0],
        [0, 0, 0, 0, 0, 0, 0, SECOND, 1 - SECOND],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ])
}


def probabilistic_automaton(str: str) -> bool:
    state_probabilities = np.zeros(len(STATES))
    state_probabilities[STATES.index(START_STATE)] = 1

    for i in range(len(str)):
        state_probabilities = np.dot(
            state_probabilities, TRANSITION_MATRIX[str[i]])

    for j in range(len(state_probabilities)):
        print(f"{state_probabilities[j]:.4f}", end=" ")
    print()

    return state_probabilities[STATES.index(ACCEPTING_STATES[0])] >= LAMBDA


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

    for word in words:
        print(f"Word {word}: {probabilistic_automaton(word)}")
