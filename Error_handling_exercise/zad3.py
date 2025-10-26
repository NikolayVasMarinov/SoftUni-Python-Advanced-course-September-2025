class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

SPECIAL_CHARACTERS = {"@", "*", "&", "%"}
while (password := input()) != "Done":
    special_character_present: bool = False

    if len(password) < 8:
        raise PasswordTooCommonError("Password must contain at least 8 characters")

    if password.isnumeric() or password.isalpha() or {password}.issubset(SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    for character in SPECIAL_CHARACTERS:
        if character in password:
            special_character_present = True

    if not special_character_present:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
