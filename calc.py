import random

def calculate():
    modifier = 0
    baseline = 350

    n = int(input("How many side projects? "))

    for project in range(n):
        projectSuccess = 0
        for skill in range(3): # Each project has 3 ability checks
            roll_input = ""
            contest = random.randint(1, 10) + random.randint(1, 10) + 4
            roll_input = input(f"ability check {project + 1}.{skill + 1}? | contest = {contest} (Y/n) ") # Appends the project and skill check for each iteration
            
            #successed are discretionary by the DM
            if roll_input == "n" or roll_input == "N":
                projectSuccess = projectSuccess
            else:
                projectSuccess += 1
        
        modifier_input = 0
        
        #dice roll is determined by number of successes
        if projectSuccess == 1:
            modifier_input = int(input(f"d8 roll for Project {project + 1}? "))
        elif projectSuccess == 2:
            modifier_input = int(input(f"d10 roll for Project {project + 1}? "))
        elif projectSuccess == 3:
            modifier_input = int(input(f"d12 roll for Project {project + 1}? "))
        else:
            print(f"Project Success = {projectSuccess}")

            
        modifier += modifier_input

    print(f"modifier = {modifier}")

    d100 = int(input("d100 roll? "))

    baseline_input = input("baseline? (default 350) ") 
    if baseline_input: # Only overwrites the value if a number is entered, skips if you just hit enter
        baseline = int(baseline_input)

    multiplier = (d100 + modifier - 50) / 33 
    print(f"multiplier = {multiplier:.2f}")

    result = baseline * multiplier
    print(f"result = {baseline} * {multiplier:.2f}")
    result = round(result /25) * 25 # Round to the nearest 25

    if result >= 0:
        print(f"Your monthly profits are {result} gold")
    else:
        print(f"Your monthly expenses are ({result}) gold")


if __name__ == "__main__":
    calculate()