import textwrap

def wrap(string, max_width):
    wraped = textwrap.TextWrapper(width=max_width)
    output = wraped.wrap(text=string)
    final = ""
    for i in output:
        final = str(final) + str(i) + "\n"
    return final

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)