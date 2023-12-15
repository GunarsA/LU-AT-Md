I, J, K, M, = 2, 0, 0, 3

import numpy as np

state_probabilities = np.array([1, 0])
state_transition_matrix_a = np.array([[0, 1], [1, 0]])
state_transition_matrix_b = np.array([[1/(M + 3), (M+2)/(M+3)], [1/(M + 3), (M+2)/(M+3)]])

str = "aabbaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

for i in range(len(str)):
    if str[i] == "a":
        state_probabilities = np.dot(state_probabilities, state_transition_matrix_a)
    elif str[i] == "b":
        state_probabilities = np.dot(state_probabilities, state_transition_matrix_b)
    print(i + 1, str[i], state_probabilities)
