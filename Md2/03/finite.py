I, J, K, M, = 2, 0, 0, 8

STATES = ["s_0", "s_1"]
INPUT_ALPHABET = ["a", "b"]
START_STATE = "s_" + str(J % 2)
ACCEPTING_STATES = ["s_" + str(K % 2)]
TRANSITION_FUNCTION = {
    ("s_0", "a"): ("s_1"),
    ("s_0", "b"): ("s_1"),
    ("s_1", "a"): ("s_0"),
    ("s_1", "b"): ("s_1")
}
MAX_LENGTH = 4


def finite_state_machine(str: str) -> bool:
    current_state = START_STATE

    for i in range(len(str)):
        current_state = TRANSITION_FUNCTION[(current_state, str[i])]

    return current_state in ACCEPTING_STATES


if __name__ == "__main__":
    words = []

    for i in range(MAX_LENGTH + 1):
        for j in range(2**i, 2**(i+1)):
            word = bin(j)[3:].replace("0", "a").replace("1", "b")
            if finite_state_machine(word):
                words.append(word)

    print(f"Words accepted by the FSM ({len(words)}): ", words)
