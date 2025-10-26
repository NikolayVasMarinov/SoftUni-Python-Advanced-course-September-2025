from collections import deque
from typing import Deque

strengths: list[int] = [int(x) for x in input().split()]
accuracies: Deque[int] = deque(int(x) for x in input().split())
scored_goals: int = 0

while strengths and accuracies:
    strength: int = strengths[-1]
    accuracy: int = accuracies[0]

    if strength + accuracy == 100:
        scored_goals += 1
        strengths.pop()
        accuracies.popleft()

    elif strength + accuracy < 100:
        if strength < accuracy:
            strengths.pop()

        elif strength > accuracy:
            accuracies.popleft()

        else:
            accuracies.popleft()
            strengths[-1] = strength + accuracy

    else:
        strengths[-1] = strength - 10
        accuracies.rotate(-1)

if scored_goals == 0:
    print("Paul failed to score a single goal.")

elif scored_goals < 3:
    print("Paul failed to make a hat-trick.")

elif scored_goals == 3:
    print("Paul scored a hat-trick!")

else:
    print("Paul performed remarkably well!")

if scored_goals != 0:
    print(f"Goals scored: {scored_goals}")

if strengths:
    print(f"Strength values left: ", end="")
    print(*strengths, sep=", ")

if accuracies:
    print(f"Accuracy values left: ", end="")
    print(*accuracies, sep=", ")