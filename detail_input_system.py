def collect_class_records():
    student_records = {}
    while True:
        try:
            student_names = input("Name (or done): ").lower().strip()
            if not student_names:
                print("Name cannot be empty. Please enter a valid name.")
                continue
            if student_names == "done":
                if len(student_records) < 5:
                    print("Enter at least five students records")
                else:
                    break
                continue
            if student_names in student_records:
                print(f"{student_names} already exists. Duplicate names not allowed.")
                continue   
            max_name_length = 20
            if len(student_names) > max_name_length:
                print(f"Name is too long. Maximum {max_name_length} characters allowed.")
                continue
            if not student_names.isalpha():
                print("Name must contain only letters (A-Z, a-z). No spaces, numbers, or symbols.")
                continue
            student_score = int(input("Score: "))
            if not 0 <= student_score <= 100:
                print("Score must be between 0 and 100.")
                continue
            else:
                student_records[student_names] = student_score
        except ValueError:
            print("Invalid score. Please enter a whole number.")
    while True:
        try:
            cut_off = input(" \nCut Off:")
            if cut_off.isdigit():
                pass_mark = int(cut_off)
                if 0 <= pass_mark <= 100:
                    break
                else:
                    print("enter an integer btw 0 and 100")
            else:
                print("enter an integer btw 0 and 100")        
        except ValueError:
            print("enter a correct value")
    print("\nProceeding to menu...")
    return student_records, pass_mark