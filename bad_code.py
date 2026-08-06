# Bad Python Code to test ReviewSentinel

import os
import pickle

def unsafe_function(user_input):
    # Security vulnerability: shell injection / unsafe eval
    eval(user_input)

def load_data(filename):
    # Security vulnerability: unsafe pickle deserialization
    with open(filename, 'rb') as f:
        return pickle.load(f)

def logic_bug(items):
    # Logic bug: index out of bounds or division by zero potential
    for i in range(len(items) + 1):
        item = items[i]
        print(item)

def maintainability_issue():
    # Code smell: unused variable and bad naming
    X = 10
    y = 20
    return y
