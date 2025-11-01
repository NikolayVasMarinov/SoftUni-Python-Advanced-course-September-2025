def find_smallest_subset(universe: set[int], sets: list[set[int]]) -> list[set[int]]:
    chosen_sets: list[set[int]] = []

    while sets:
        best_set = max(sets, key=lambda x: len(universe.intersection(x)))
        if not universe:
            break

        universe.difference_update(best_set)
        chosen_sets.append(best_set)
        sets.remove(best_set)

    return chosen_sets

universe: set[int] = set(map(int, input().split(", ")))
sets_count: int = int(input())

sets: list[set[int]] = [set(map(int, input().split(", "))) for _ in range(sets_count)]

result = find_smallest_subset(universe, sets)

if result:
    print(f"Sets to take ({len(result)}):")
    for s in result:
        s = map(str, sorted(s))
        print("{", ", ".join(s), "}")
else:
    print("No solution exists")