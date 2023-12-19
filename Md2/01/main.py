I, J, K, M, = 2, 0, 0, 8
# I, J, K, M, = 2, 0, 3, 3

STATES = ["s_0", "s_1", "s_2"]
INPUT_ALPHABET = ["0", "1"]
STACK_ALPHABET = ["z", "$"]
START_STATE = "s_0"
START_STACK_SYMBOL = "$"
ACCEPTING_STATES = ["s_0"]
TRANSITION_FUNCTION = {
    ("s_0", "", "$"): ("s_1", "z$"),
    ("s_1", "0", "z"): ("s_1", "zzz"),
    ("s_1", "", "z"): ("s_2", ""),
    ("s_2", "1", "z"): ("s_2", ""),
    ("s_2", "0", "z"): ("s_0", ""),
    ("s_" + str(K % 3), "1", "z"): ("s_" + str(M % 3), "zz"),
}
MAX_LENGTH = 4


def pushdown_automaton(str: str, curr_state: str, stack: str) -> bool:

    def accept(str: str, state: str, stack: str, symbol: str) -> bool:
        for i in range(1, len(stack) + 1):
            key = (state, symbol, stack[:i])
            if key in TRANSITION_FUNCTION:
                new_state, new_stack_insert = TRANSITION_FUNCTION[key]
                new_stack = new_stack_insert + stack[i:]
                if pushdown_automaton(str, new_state, new_stack):
                    return True
        return False

    if accept(str, curr_state, stack, ""):  # epsilon transition
        return True

    if str == "":  # end of input
        return curr_state in ACCEPTING_STATES

    return accept(str[1:], curr_state, stack, str[0])  # normal transition


if __name__ == "__main__":
    words = []
    for i in range(MAX_LENGTH + 1):
        for j in range(2**i, 2**(i+1)):
            word = bin(j)[3:]
            if pushdown_automaton(word, START_STATE, START_STACK_SYMBOL):
                words.append(word)

    print(f"Words accepted by the PDA ({len(words)}): ")
    for word in words:
        print(f"{word if word != "" else "ε"}, ", end="")
