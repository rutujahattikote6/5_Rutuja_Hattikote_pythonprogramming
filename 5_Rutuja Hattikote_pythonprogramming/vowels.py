String=input("Enter a string:")
vowels ="aeiouAEIOU"
vowel_count=0
   
for char in String:
        if char in vowels:
            vowel_count += 1
    


print(f"Number of vowels in the string: ", vowel_count)
