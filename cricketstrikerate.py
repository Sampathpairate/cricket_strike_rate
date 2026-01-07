runs = int(input("Enter runs scored: "))
balls = int(input("Enter balls faced: "))

if balls == 0:
    print("Balls faced cannot be zero. Strike rate cannot be calculated.")
else:
    strike_rate = (runs / balls) * 100
    print(f"Strike Rate: {strike_rate:.2f}")