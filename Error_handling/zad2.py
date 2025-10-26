text = input()
try:
    times_repeated = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text * times_repeated)