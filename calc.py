def calculate():
    modifier = 0
    baseline = 350

    n = int(input("How many side projects? "))

    for project in range(n):
        projectSuccess = 0
        for skill in range(3): # Each project has 3 ability checks
            roll = int(input(f"ability score {project + 1}.{skill + 1}? ")) # Appends the project and skill check for each iteration
            projectSuccess += roll
        projectAvg = projectSuccess / 3
        modifier += projectAvg

    d100 = int(input("d100 roll? "))

    baseline_input = input("baseline? (default 350) ") 
    if baseline_input: # Only overwrites the value if a number is entered, skips if you just hit enter
        baseline = int(baseline_input)

    multiplier = (d100 + modifier - 50) / 33 

    result = baseline * multiplier
    result = round(result /25) * 25 # Round to the nearest 25

    if result >= 0:
        print(f"Your monthly profits are {result} gold")
    else:
        print(f"Your monthly expenses are (-{abs(result)}) gold")


if __name__ == "__main__":
    calculate()