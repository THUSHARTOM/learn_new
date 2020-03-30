for eachchar in 'python':
    if eachchar == 'p':
        pass  # passes the current iteration
    else:
        print("current letter = ", eachchar)

for eachval in range(2, 20, 5):  # prints and increment by 5 by deafault this is one

    if eachval > 15:
        break  # breaks the loop
    else:
        continue  # skips the current iteration
    print(eachval)

print("Loop terminaterd")
