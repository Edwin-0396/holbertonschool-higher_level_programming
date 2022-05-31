#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = list(text)
    for curr in range(len(text)):
        if text[curr] in ".?:" and text[curr + 1] == ' ':
            text[curr + 1] = "\n\n"
        print(text[curr], end="")
