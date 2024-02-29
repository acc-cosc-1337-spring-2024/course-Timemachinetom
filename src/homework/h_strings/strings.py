# Strings Homework
# Hamming Distance - Return the Hamming distance between two strings

def get_hamming_distance (dna1, dna2): #dna1 and dna2 should be the same length
    distance = 0 #create variable for distance and start at 0
    L = len (dna1) #Use L as the range for the Loop below
    for i in range (L): #Loop through both strings to compare the symbols in each
        if dna1[i] != dna2[i]: #Add 1 to distance if the symbols do not match
            distance += 1
    return distance #Returns the final value for distance

def get_dna_complement (dna):
    Complement = 0 #Use Complement as a variable to return the reversed Complement
    for i in reversed(dna): #loop through the string in reverse
        if i == "A":
            if isinstance (Complement, str) == True: #check if complement is a string, it should be after the first loop
                Complement = Complement + "T" #if complement is already a string, concatenate the strings
            else: # on the first loop, Complement wil not be a string
                Complement = "T" #makes Complement into a string and begins the reversed complement string
        if i == "T":
            if isinstance (Complement, str) == True: 
                Complement = Complement + "A"
            else:
                Complement = "A"
        if i == "G":
            if isinstance (Complement, str) == True: 
                Complement = Complement + "C"
            else:
                Complement = "C"
        if i == "C":
            if isinstance (Complement, str) == True: 
                Complement = Complement + "G"
            else:
                Complement = "G"
    return Complement #Returns the final string for the reversed Complement