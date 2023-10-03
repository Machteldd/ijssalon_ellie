def presenteer (dictionary, totaal):
    for key in dictionary:
        print (f"{key} : {dictionary[key]} euro")
    print ("================")
    print (f"totaal : {totaal} euro")
print (presenteer ({'vis': 10, 'vlees' : 25, 'overig' : 15}, totaal = 50))