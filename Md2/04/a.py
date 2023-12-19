import numpy as np

state_probabilities = np.array([0.5, 0, 0])
state_transition_matrix_a = np.array([[0.9, 0.1, 0], [0, 0.5, 0.5], [0, 0, 1]])
state_transition_matrix_b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

str = "aaaa"

for i in range(len(str)):
    if str[i] == "a":
        state_probabilities = np.dot(state_probabilities, state_transition_matrix_a)
    elif str[i] == "b":
        state_probabilities = np.dot(state_probabilities, state_transition_matrix_b)
    print(i + 1, str[i], state_probabilities)




