"""
[장점]
runtime 줄이기
related issues : graph, trees, search

[주의]
1. specify base case : -> infinite recursion and crash
2. update arguments : update each recursions -> 그래야 base case까지 reach할 수 있다.
"""
def downward_count(number):
    print(number)
    # base case
    if number == 0:   # A recursive call with a different argument
        return 0
    downward_count(number - 1)

#downward_count(5)

def rec_count(number):
    print(number)
    # base case
    if number == 0:  # A recursive call with a different argument
        return 0
    rec_count(number - 1)
    print(number)

rec_count(5)