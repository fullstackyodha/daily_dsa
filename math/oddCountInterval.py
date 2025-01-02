def countOdds(low: int, high: int):
    length = high - low + 1
    count = length // 2  # number of odd numbers in even length range

    # length is odd and left number is odd
    if length % 2 and low % 2:
        count += 1

    # length is even
    return count


print(countOdds(3, 7))
