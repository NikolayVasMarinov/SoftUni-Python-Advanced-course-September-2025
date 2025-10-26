number_of_chemical_compounds: int = int(input())

unique_chemical_elements: set[str] = set(element
                                         for _ in range(number_of_chemical_compounds)
                                         for element in input().split())

print(*unique_chemical_elements, sep= "\n")