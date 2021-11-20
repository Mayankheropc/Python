# First, def a function, start_process, that takes one argument p. Then, if the start_process function receives an 
# p equal to "Yes", it should return "Start Process" Alternatively, elif p is equal to "No", then the function 
# should return "Start Process Aborted". Finally, if start_process gets anything other than those inputs, the 
# function should return "Sorry for the input".

# By - Mayank Singh
# Date of Creation - 03-11-2021
# Last Modified - 05-11-2021

def start_process(x):
    ch = x.upper()
    value = ""
    if ch == "YES" or ch == "Y":
        value += "Process Started"
        return value
    elif ch == "NO" or ch == "N":
        value += "Start Process Aborted"
        return value
    else:
        value = "Sorry for the input"
        return value

p = input("Do you want to start the process? (Yes or No): ")

print(start_process(p))


# Output

# Do you want to start the process? (Yes or No): Y
# Process Started

# Do you want to start the process? (Yes or No): yes
# Process Started

# Do you want to start the process? (Yes or No): no
# Start Process Aborted

# Do you want to start the process? (Yes or No): asa
# Sorry for the input