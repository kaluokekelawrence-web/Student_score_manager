from detail_input_system import collect_class_records
import grading_system as gs

student_records, pass_mark = collect_class_records()
while True:
    print("\n1--Highest score")
    print("\n2--Lowest score")
    print("\n3--Class average")
    print("\n4--Summary")
    print("\n5--Ranking (from first to last)")
    print("\n6--Leave")
    try:
        choice = int(input("Select an option (1-6): "))
    except ValueError:
        print("Invalid input. Enter a number between 1 and 6.")
        continue
    if choice == 1:
        gs.highest_score_record(student_records)
    elif choice == 2:
        gs.lowest_score_record(student_records)
    elif choice == 3:
        gs.class_average(student_records)
    elif choice == 4:
        print("\n--- Summary ---")
        gs.print_all_records(student_records)
        gs.print_pass_fail(student_records, pass_mark)
    elif choice == 5:
        gs.ranking_system(student_records, pass_mark)
    elif choice == 6:
        print("See you soon")
        break
    else:
        print("Invalid choice. Please select 1-6.")