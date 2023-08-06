input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
unique_numbers=[]
for number in input_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
print("List of unique numbers:", unique_numbers)            