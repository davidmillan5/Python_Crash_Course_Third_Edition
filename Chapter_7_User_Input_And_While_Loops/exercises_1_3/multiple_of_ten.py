multiple_of_ten = int(input("Enter a number, and I'll tell you if it's multiple of ten or not: "))
if multiple_of_ten % 10 == 0:
    print(f"\nThe number {multiple_of_ten} is multiple of ten.")
else:
    print(f"\nThe number {multiple_of_ten} is not a multiple of ten.")