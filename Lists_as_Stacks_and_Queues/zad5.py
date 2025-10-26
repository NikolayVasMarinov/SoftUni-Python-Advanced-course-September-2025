from collections import deque

kids_playing_hot_potato: deque[str] = deque(input().split(" "))
elimination_toss: int = int(input())
current_toss: int = 0


while len(kids_playing_hot_potato) > 1:
    current_toss += 1

    if current_toss % elimination_toss == 0:
        eliminated_kid: str = kids_playing_hot_potato.popleft()

        print(f"Removed {eliminated_kid}")
        continue

    kids_playing_hot_potato.append(kids_playing_hot_potato.popleft())


print(f"Last is {kids_playing_hot_potato[0]}")