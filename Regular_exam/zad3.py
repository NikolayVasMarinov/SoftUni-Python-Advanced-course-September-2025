def classify_books(*args, **kwargs) -> str:
    fiction_books = []
    nonfiction_books = []

    for is_fiction, book in args:
        if is_fiction == "fiction":
            fiction_books.append(book)
        else:
            nonfiction_books.append(book)

    kwargs = {value: key for key, value in kwargs.items()}

    fiction_books = sorted(fiction_books, key= lambda x: kwargs[x])

    nonfiction_books = sorted(nonfiction_books, key= lambda x: kwargs[x], reverse= True)

    result: list[str] = []

    if fiction_books:
        result.append("Fiction Books:")
        result.extend(f"~~~{kwargs[book]}#{book}" for book in fiction_books)

    if nonfiction_books:
        result.append("Non-Fiction Books:")
        result.extend(f"***{kwargs[book]}#{book}" for book in nonfiction_books)

    return "\n".join(result)