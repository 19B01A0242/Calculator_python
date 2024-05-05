# main.py
from mean_var_std import calculate

# Test the function
input_list = list(map(int,input().split()))
result = calculate(input_list)
print(result)
