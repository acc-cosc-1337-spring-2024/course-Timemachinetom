import decisions

options = input("Enter options")
options = float(options) # Converts options to number

total = input ("Enter total")
total= float(total) #Converts total to number

ratio = decisions.get_options_ratio(options, total) #Saves the output of get_options_ratio to ratio

result = decisions.get_faculty_rating(ratio)
print(result)