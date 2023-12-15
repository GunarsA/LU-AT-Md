import numpy as np

state_probabilities = np.array([1, 0, 0])
state_transition_matrix_a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
state_transition_matrix_b = np.array([[0.9, 0.1, 0], [0, 0.96, 0.04], [0, 0, 1]])

str = "bbaabbaaaaaaabbbbaabaabbbbbb"

for i in range(len(str)):
    if str[i] == "a":
        state_probabilities = np.dot(state_probabilities, state_transition_matrix_a)
    elif str[i] == "b":
        state_probabilities = np.dot(state_probabilities, state_transition_matrix_b)
    print(i, state_probabilities)



