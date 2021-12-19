import pronotepy
from client import DiscordTemplate, client
import time

periods = client.periods

number_notes = 0
temp_note = 0
initialise = True
while True:
    print(time.strftime("%H:%M:%S"))
    for period in periods:
        if initialise:
            for note in period.grades:
                number_notes += 1
            print(f"initialisation effectuée avec {number_notes} notes enregistrées")
            initialise = False
        else : 
            for note in period.grades:
                temp_note += 1 

                if temp_note > number_notes:
                    print("***** Nouvelle Note *****\n")
                    print(f"Note: {note.grade}/{note.out_of} En {note.subject.name} Date: {note.date}\n")
                    print("***********************\n")
                    message = DiscordTemplate()
                    message.send(note,client.parametres_utilisateur['donneesSec']['donnees']['ressource']["L"].split()[-1])

            if temp_note == number_notes:
                print("Pas de nouvelle note")

            number_notes = temp_note
            temp_note = 0
        break
    
    time.sleep(300) # time to sleep before checking again