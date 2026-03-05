import random
import sys

verbose = "-v" in sys.argv or "--verbose" in sys.argv
help = "-h" in sys.argv or "--help" in sys.argv


def calculate():
    modifier = 0
    baseline = 350

    n = int(input("How many side projects? "))

    for project in range(n):
        projectSuccess = 0
        for skill in range(3): # Each project has 3 ability checks
            roll_input = ""
            contest = random.randint(1, 10) + random.randint(1, 10) + 4
            while True:
                roll_input = input(f"ability check {project + 1}.{skill + 1}? | contest = {contest} (Y/n) ")
                if roll_input.lower() in ("y", "n", ""): # Accepts Y, N, or enter (default Y)
                    break
                print("Please enter Y or N") # Rejects anything else

            #successes are discretionary by the DM
            if roll_input.lower() != "n":
                projectSuccess += 1
            if verbose:
                print(f"projectSuccess count = {projectSuccess}")
        
        modifier_input = 0
        
        #dice roll is determined by number of successes
        if projectSuccess >= 1:
            if verbose:
                print(f"{projectSuccess} successes = 1d{6 + (projectSuccess * 2)}")
        else:
            break

        if projectSuccess == 1:
            while True:
                modifier_input = int(input(f"d8 roll for Project {project + 1}? "))
                if 1 <= modifier_input <= 8: # Valid d8 range
                    break
                print("Roll must be between 1 and 8") # Rejects anything out of range
        elif projectSuccess == 2:
            while True:
                modifier_input = int(input(f"d10 roll for Project {project + 1}? "))
                if 1 <= modifier_input <= 10: # Valid d10 range
                    break
                print("Roll must be between 1 and 10") # Rejects anything out of range
        elif projectSuccess == 3:
            while True:
                modifier_input = int(input(f"d12 roll for Project {project + 1}? "))
                if 1 <= modifier_input <= 12: # Valid d12 range
                    break
                print("Roll must be between 1 and 12") # Rejects anything out of range
        else:
            print(f"Project Success = {projectSuccess}")

            
        modifier += modifier_input

    if verbose:
        print(f"modifier = {modifier}")

    while True:
        d100 = int(input("d100 roll? "))
        if 1 <= d100 <= 100: # Valid d100 range
            break
        print("Roll must be between 1 and 100") # Rejects anything out of range

    baseline_input = input("baseline? (default 350) ") 
    if baseline_input: # Only overwrites the value if a number is entered, skips if you just hit enter
        baseline = int(baseline_input)

    multiplier = (d100 + modifier - 50) / 33 
    if verbose:
        print(f"multiplier = ({d100} + {modifier} - 50) / 33")
    
    if verbose:
        print(f"multiplier = {multiplier:.2f}")

    result = baseline * multiplier
    
    if verbose:
        print(f"result = {baseline} * {multiplier:.2f}")
    
    result = round(result /25) * 25 # Round to the nearest 25

    if result >= 0:
        print(f"Your monthly profits are {result} gold")
    else:
        print(f"Your monthly expenses are ({result}) gold")


if __name__ == "__main__":
    if help:
        print("5e expense calculator for Acq Inc. Use --verbose or -v for debugging output.")
    else:
        calculate()