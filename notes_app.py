# a notes app that saves data (CLI)
# started: April 8, 2026 (morning)
# finished: April 9, 2026 (morning)
import time
import os

def view_notes():
    
    # check for errors
    try:
        print("================ NOTES ================")

        # open the text file
        with open("notes.txt", "r") as notes:
            # print each note in the text file
            for note in notes:
                print(note)
        
        print("=======================================")
    
    # if the file does not exist, tell the user
    except FileNotFoundError:
        print("There are no notes to view!")
        

def add_notes():
    # ask the user what note to add
    note_to_add = input("What note would you like to add? ").strip().title()

    # ('a' appends/adds to the file, 'w' would rewrite over the entire file)
    # open the text file
    with open("notes.txt", "a") as notes:
         # add the note to the text file 
        notes.write(note_to_add)
        # add a new line for next note
        notes.write("\n")
        
        
    print("Adding note...")
    time.sleep(3)
    
    print("Note added!")
    

def delete_notes():
    # check for errors
    try:
        # view notes to show user what they can delete
        view_notes()
        
        note_to_delete = input("What note would you like to delete? ").lower().strip()
        time.sleep(3)

        # empty list for all notes except the one the user wants to remove
        new_notes = []
        # go through all notes to see if it exists
        with open("notes.txt", "r") as notes:
            for note in notes:
                # to avoid formatting errors
                note = note.lower().strip()
                
                # skip over the note the user wants to delete
                if note == note_to_delete:
                    continue
                # add all other notes to the new notes list
                else:
                    new_notes.append(note)
        
        # rewrite a new text file with new notes
        with open("notes.txt", "w") as notes:
            for note in new_notes:
                # for visual aesthetic reasons
                note = note.title()
                
                notes.write(note)
                # new line in between notes
                notes.write("\n")
        
        print("Note successfully deleted!")
                    
        
        
    
    # if the file does not exist, tell the user
    except FileNotFoundError:
        print("There are no notes to view!")
        
        
def clear_notes():
    try:
        print("Clearing all notes...")
        time.sleep(3)
        
        # delete the text file using the os module
        os.remove("notes.txt")
        
        
        print("Cleared all notes!")
        
    except FileNotFoundError:
        print("There are no notes to view!")


# main loop
while True:
    # display options
    print("================ TO DO LIST ================")
    print("1.  View notes")
    print("2.  Add notes")
    print("3.  Delete notes")
    print("4.  Clear all notes")
    print("5.  Leave")
    print("============================================")


    # prompt user what to do
    choice = input("")

    # direct user to do what they want
    if choice == "1":
        view_notes()

    elif choice == "2":
        add_notes()

    elif choice == "3":
        delete_notes()
        
    elif choice == "4":
        clear_notes()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

    time.sleep(3)
