import re


def increment_string(strng):
    pos = re.search(r"\d+$", strng)

    if pos is None:
        return strng + "1"

    else:
        result = strng[pos.span()[0] :]
        new_strng = strng[: pos.span()[0]]

        print(f"{new_strng}{str(int(result) + 1).zfill(len(result))}")

        return f"{new_strng}{str(int(result) + 1).zfill(len(result))}"
