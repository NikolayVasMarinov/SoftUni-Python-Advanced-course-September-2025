def sorting_cheeses(**cheeses_dict) -> str:
    cheeses_dict = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for (cheese, quantities) in cheeses_dict:
        result.append(cheese)
        quantities = sorted(quantities, reverse=True)
        result += quantities
    return "\n".join(str(x) for x in result)