if __name__ =='__main__':
    a = int(input())
    roll_a =[]
    roll_b =[]
    roll_a=input().split(" ") #Take inputs with space as delimiter
    b = int(input())
    roll_b = input().split(" ")
    set_a = set(roll_a)

    set_b = set(roll_b)
    RES =set_a.symmetric_difference(set_b)

    print(len(RES))