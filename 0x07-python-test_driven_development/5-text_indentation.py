#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """A function that prints a text with 2 new lines after each of these characters

    Args:
        text: the text to be formated
    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:" or text[c] == "\n":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
