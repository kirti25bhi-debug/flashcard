import random

def flashcard_program():
    
    flashcards = {}

    print("--- Welcome to the Python Flashcard App ---")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new flashcard")
        print("2. Take the quiz")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

       
        if choice == '1':
            question = input("\nEnter the Question: ")
            answer = input("Enter the Answer: ")
            
            
            flashcards[question] = answer 
            print("Flashcard added successfully!")

       
        elif choice == '2':
            if not flashcards:
                print("\nYou have no flashcards yet! Add some first.")
            else:
                print("\n-QUIZ STARTED-")
                
                questions = list(flashcards.keys())
                random.shuffle(questions)

                for q in questions:
                    print(f"\nQuestion: {q}")
                    input("Press Enter to see the answer....")
                    print(f"Answer: {flashcards[q]}")
                
                print("\n-End of Quiz-")

        
        elif choice == '3':
            print("Goodbye!")
            break
            
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


flashcard_program()
