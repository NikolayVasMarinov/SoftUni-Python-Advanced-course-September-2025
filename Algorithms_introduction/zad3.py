def draw_figure(n) -> None:
    if n == 0: return

    print(n * "*")
    draw_figure(n - 1)
    print(n * "#")

num: int = int(input())
draw_figure(num)