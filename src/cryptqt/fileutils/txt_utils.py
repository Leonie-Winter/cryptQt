def makefile(text: str, filename: str) -> None:
    """
    test_function does blah blah blah.

    :param p1: describe about parameter p1
    :param p2: describe about parameter p2
    :return: None, output is written to a file
    """   
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


# turn txt into string 
def fileToString(filename: str) -> str:
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
        return content
