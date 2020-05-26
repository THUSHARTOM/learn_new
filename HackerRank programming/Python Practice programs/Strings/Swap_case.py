def swap_case(s):
    w =[]
    for i in range(len(s)):
        if s[i].islower():
            w.append(s[i].upper())
        else:
            w.append(s[i].lower())
    w = "".join(w)
    return w

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)