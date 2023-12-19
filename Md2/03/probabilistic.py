import numpy as np

I, J, K, M, = 2, 0, 0, 8
# I, J, K, M, = 2, 0, 3, 3

STATES = ["s_0", "s_1"]
INPUT_ALPHABET = ["a", "b"]
START_STATE = "s_" + str(J % 2)
ACCEPTING_STATES = ["s_" + str(K % 2)]
LAMBDA = 0.5
TRANSITION_MATRIX = {
    "a": np.array([
        [0, 1],
        [1, 0]
    ]),
    "b": np.array([
        [1/(M + 3), (M+2)/(M+3)],
        [1/(M + 3), (M+2)/(M+3)]
    ])
}
MAX_LENGTH = 4

def probabilistic_automaton(str: str) -> bool:
    state_probabilities = np.zeros(len(STATES))
    state_probabilities[STATES.index(START_STATE)] = 1

    for i in range(len(str)):
        state_probabilities = np.dot(
            state_probabilities, TRANSITION_MATRIX[str[i]])

    # print(f"Word: {str}")
    # for j in range(len(state_probabilities)):
    #     print(f"{state_probabilities[j]:.4f}", end=" ")
    # print()

    return state_probabilities[STATES.index(ACCEPTING_STATES[0])] >= LAMBDA


if __name__ == "__main__":
    words = []

    for i in range(MAX_LENGTH + 1):
        for j in range(2**i, 2**(i+1)):
            word = bin(j)[3:].replace("0", "a").replace("1", "b")
            if probabilistic_automaton(word):
                words.append(word)

    print(f"Words accepted by the probabilistic automaton ({len(words)}): ")
    for word in words:
        print(f"{word if word != "" else "ε"}, ", end="")
