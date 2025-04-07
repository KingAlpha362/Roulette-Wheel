num = int(input("Enter a number from (0-36):\n"))

if num == 0:
    color = "Green"
elif 1 <= num <= 10:
    color = "Red" if num % 2 == 0 else "Black"
elif 11 <= num <= 18:
    color = "Black" if num % 2 == 0 else "Red"
elif 19 <= num <= 28:
    color = "Red" if num % 2 == 0 else "Black"
elif 29 <= num <= 36:
    color = "Black" if num % 2 == 0 else "Red"
else:
    print("Error, try again.")

print(f"The pocket is {num} and the color is {color}.")
