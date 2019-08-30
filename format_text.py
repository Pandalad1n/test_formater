#! /usr/bin/python3

MAX_LINE_LEN = 80


def wrap(lines):
    for line in lines:
        line_len = 0
        begin = 0
        words = line.replace("\n", "").split(" ")
        for i, word in enumerate(words):
            line_len += len(word) + (1 if i != len(words) - 1 else 0)
            if line_len >= MAX_LINE_LEN:
                yield join_padded(words[begin:i]) + "\n"
                begin = i
                line_len = len(word)

        if line_len:
            yield " ".join(words[begin:]) + "\n\n"


def join_padded(words):
    line_len = 0
    for word in words:
        line_len += len(word)
    line_len += len(words) - 1
    gap = MAX_LINE_LEN - line_len
    i = 0
    while gap > 0:
        if i >= len(words) - 1:
            i = 0
        else:
            words[i] += " "
            i += 1
            gap -= 1

    return " ".join(words)


def format_file():
    with open('input.txt', 'r') as s_in, open('output.txt', 'w') as s_out:
        for i in wrap(s_in):
            s_out.write(i)


if __name__ == '__main__':
    format_file()
