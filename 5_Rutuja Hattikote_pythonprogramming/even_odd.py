input_tuple = tuple(map(int, input("Enter a tuple of numbers separated by spaces: ").split()))
odd_numbers = []
even_numbers = []
for number in input_tuple:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
if odd_numbers:
            print("Odd numbers:", odd_numbers)
else:
            print("No odd numbers found in the tuple.")
        
if even_numbers:
            print("Even numbers:", even_numbers)
else:
            print("No even numbers found in the tuple.")