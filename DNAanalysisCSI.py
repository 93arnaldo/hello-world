#This iis the Program to find the suspect of eating the IceCream

Suspect_DNA = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"


print 'The DNA of the suspect is: \n' + Suspect_DNA

#We create now the different characteristics using dictionaries

Hair_colour = {
"Black" : "CCAGCAATCGC",
"Brown" : "GCCAGTGCCG",
"Blonde" : "TTAGCTATCGC"
}

Facial_Shape = {
'Square' : 'GCCACGG',
'Round' : 'ACCACAA',
'Oval' : 'AGGCCTCA'
}

Eye_colour = {
'Blue' : 'TTGTGGTGGC',
'Green' : 'GGGAGGTGGC',
'Brown' : 'AAGTAGTGAC'
}

Gender = {
'Female' : 'TGAAGGACCTTC',
'Male' : 'TGCAGGAACTTC'
}

Race = {
'White' : 'AAAACCTCA',
'Black' : 'CGACTACAG',
'Asian' : 'CGCGGGCCG'
}

#Now, we create each of the suspects that we will later compare, at the end the program will figure out which is the bad guy by comparing lists of the two dictionaries

Eva = {
 'Gender' : 'Female',
'Race' : 'White',
'Hair color' : 'Blonde',
'Eye color' : 'Blue',
'Face shape' : 'Oval'
}

Larisa = {
'Gender' : 'Female',
'Race' : 'White',
'Hair color' : 'Brown',
'Eye color' : 'Brown',
'Face shape' : 'Oval'
}

Matej = {
'Gender' : 'Male',
'Race' : 'White',
'Hair color' : 'Black',
'Eye color' : 'Blue',
'Face shape' : 'Oval'
}

Miha = {
'Gender' : 'Male',
'Race' : 'White',
'Hair color' : 'Brown',
'Eye color' : 'Green',
'Face shape' : 'Square'
}

#Now, we write down the variables we want to figure out of the suspect
#Be careful not to define them with the same name s as the dictionaries

Hair = "unknown yet"
Facial = "unknown yet"
Eyes = "unknown yet"
MALEorFEMALE = "unknown yet"
WHITEorBLACKorASIAN = "unknon yet"

Criminal_characteristics_list = []

for gender in Gender:
    if Suspect_DNA.find(Gender[gender]) > 0:
        print "The criminal is " + gender + "!"
        MALEorFEMALE = gender
        Criminal_characteristics_list.append(MALEorFEMALE)

for race in Race:
    if Suspect_DNA.find(Race[race]) > 0:
        print "The criminal is " + race + "!"
        WHITEorBLACKorASIAN = race
        Criminal_characteristics_list.append(WHITEorBLACKorASIAN)

for hair in Hair_colour: #We start a for loop for the dictionaries of caracteristics and DNA letters
    if Suspect_DNA.find(Hair_colour[hair]) > 0: #The function find(), gives as an output a number which is the location of the item you are looking for in the string that you aply the funciton find(). But, if there is no value, then python returns a -1. this means that we can assume that if python gives us a value higher than 0, then means that pythin has found it and the key is stored as "hair" in this case
        print "The hair colour of the criminal is " + hair + "!"
        Hair = hair
        Criminal_characteristics_list.append(Hair)
        
for eyes in Eye_colour:
    if Suspect_DNA.find(Eye_colour[eyes]) > 0:
        print "The colour of the eyes of the criminal is " + eyes + "!"
        Eyes = eyes
        Criminal_characteristics_list.append(Eyes)

for facial in Facial_Shape:
    if Suspect_DNA.find(Facial_Shape[facial]) > 0:
        print "The facial shape of the criminal looks like a " + facial + "!"
        Facial = facial
        Criminal_characteristics_list.append(Facial)
        
print Criminal_characteristics_list
        
if Eva.values() == Criminal_characteristics_list:
    print "The Crimila is Eva"
    
if Larisa.values() == Criminal_characteristics_list:
    print "The Crimila is Larisa"
    
if Matej.values() == Criminal_characteristics_list:
    print "The Crimila is Matej"
    
if Miha.values() == Criminal_characteristics_list:
    print "The Crimila is Miha"
    
