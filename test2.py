def add_explanation(line):
    return line + '!'


update_line = add_explanation

print(update_line("Hi baby"))


def beautify(text):
    return text + '!!!'

def make_line(func, words):
    return "hello " + func(words)

print(make_line(beautify, "world"))
