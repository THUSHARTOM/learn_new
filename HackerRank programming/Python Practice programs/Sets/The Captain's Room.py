if __name__ == '__main__':
    k = int(input())
    s = input()
    numbers = [int(i) for i in s.split()]
    set_a = set(numbers)
    sum_a = sum(set_a)
    set_sum = sum_a * k
    total_sum = sum(numbers)
    print((set_sum - total_sum)//(k-1))