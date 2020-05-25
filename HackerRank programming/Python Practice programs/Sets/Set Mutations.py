if __name__ =='__main__':
    no_of_a = int(input())
    set_a =[]
    set_a=set(input().split(" "))
    no_of_otherSets = int(input())

    for i in range(no_of_otherSets):
        op_name, length = input().split(maxsplit=1)
        lst =[]
        if op_name == "intersection_update":
            inp = input().split(" ")
            set_b = set(inp)
            set_a.intersection_update(set_b)

        elif op_name == "update":
            inp = input().split(" ")
            set_b = set(inp)
            set_a.update(set_b)

        elif op_name == "symmetric_difference_update":
            inp = input().split(" ")
            set_b = set(inp)
            set_a.symmetric_difference_update(set_b)

        elif op_name == "difference_update":
            inp = input().split(" ")
            set_b = set(inp)
            set_a.difference_update(set_b)
    sum1 = 0

    final_list = list(set_a)
    
    for i in range(len(final_list)):
        sum1 = sum1 + int(final_list[i])
    print(sum1)