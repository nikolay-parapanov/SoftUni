def find_positive_and_negative_sums(*args):
    positive_sum = 0
    negative_sum = 0

    for el in args:
        if int(el) >= 0:
            positive_sum += int(el)
        else:
            negative_sum += int(el)

    return negative_sum, positive_sum


nums = [int(x) for x in input().split()]

negative_sum, positive_sum = find_positive_and_negative_sums(*nums)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
