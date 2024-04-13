############################################################################
# Write your script down below.
# You script should work for the following cases:
# Case 1: Negative input
# Case 2: Input out of range
# Case 3: Repeated input
# It is required for above cases to work to get the full score.
############################################################################

num_choices = 4

choices = []

for i in range(num_choices):
  while True:
    try:
      choice = int(input(f"Enter choice {i + 1}: "))
      if 0 <= choice <= 9:
        if choice not in choices:
          choices.append(choice)
          break
        else:
          print("Please choose a different numeral at each time.")
      else:
        print("Please choose a numeral from 0 to 9.")
    except ValueError:
      print("Invalid input. Please enter an integer.")

print("Your choices are:", choices)
