'''Implementation of counting sort'''
def countingsort(unsorted_numbers, max):
    numbers_to_count = [0]*(max+1)
    for number in unsorted_numbers:
        numbers_to_count[number] += 1
    sorted_numbers = []
    for number, count in enumerate(numbers_to_count):
        for number_of_times in range(count):
            sorted_numbers.append(number)
    return sorted_numbers
print(countingsort([4,6,2,2,7,3,8,9],9))
print(countingsort([4,6,2,7,3,8,9],9))
