def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\nYour Notes:")
            print(file.read())
    except FileNotFoundError:
        print("No notes yet.")

while True:
    print("\n--- Notes App ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")