def main():
    # Ask how many students are in the class
    student_count = int(input("How many students to enter? "))

    # Lists to store data
    names = []
    scores = []

    # Loop to get student details
    for i in range(student_count):
        print(f"Student {+ i + 1}")
        
        # Clean up the name input
        name_input = str(input("Name: ").strip().title())
        names.append(name_input)

        # Keep asking for score until valid (0-100)
        while True:
            score_input = int(input("Score: "))
            
            # Check for valid range
            if score_input < 0 or score_input > 100:
                print("Invalid score. Must be 0-100.")
                continue
            else:
                break
        
        scores.append(score_input)

    # Print results
    print("--- Class Summary ---")
    
    # Loop through the lists and print pass/fail
    # Pass mark is 40
    for i in range(len(names)):
        if scores[i] < 40:
            result = "Fail"
        else:
            result = "Pass"
        
        print(f"{i + 1}: {names[i]} - {scores[i]} ({result})")

# Call the main function
main()
