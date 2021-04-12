start = int(input("Start number: "))
end = int(input("Finish number: "))

def sum_nat(start, end):
    if start == end:
        return 1
    else:
        return end + sum_nat(start, end - 1)


print(sum_nat(start, end))