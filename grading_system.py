def highest_score_record(records):
    if not records:
        print("NO records")
        return
    highest_score = max(records.values())
    top_students = [name for name, score in records.items() if score == highest_score]
    if len(top_students) == 1:
        print(f"The best student is {top_students[0]} with a score of {highest_score}")
    else:
        print(f"The best students, all with a score of {highest_score}, are: {', '.join(top_students)}")


def lowest_score_record(records):
    if not records:
        print("NO records")
        return
    lowest_score = min(records.values())
    worst_students = [name for name, score in records.items() if score == lowest_score]
    if len(worst_students) == 1:
        print(f"The poorest grade is held by {worst_students[0]} with a score of {lowest_score}")
    else:
        print(f"The lowest score is {lowest_score} obtained by: {', '.join(worst_students)}")


def class_average(records):
    if not records:
        print("NO records")
        return
    total = sum(records.values())
    count = len(records)
    average = total / count
    print(f"The class average is {average:.2f}")	


def print_all_records(records):
    if not records:
        print("No records to display.")
        return
    for name, score in records.items():
        print(f"{name}: {score}")


def print_pass_fail(records, pass_mark):
    if not records:
        print("No records available.")
        return
    passed = []
    failed = []
    for name, score in records.items():
        if score >= pass_mark:
            passed.append(name)
        else:
            failed.append(name)
    print(f"Passed ({len(passed)} students):")
    if passed:
        print("  " + ", ".join(passed))
    else:
        print("  None")
    print(f"Failed ({len(failed)} students):")
    if failed:
        print("  " + ", ".join(failed))
    else:
        print("  None")


def ranking_system(records, pass_mark):
    sorted_students = sorted(records.items(), key=lambda x: x[1], reverse=True)
    print("\n--- Class Ranking ---")
    for rank, (name, score) in enumerate(sorted_students, start=1):
        status = "Passed" if score >= pass_mark else "Failed"
        print(f"{rank}. {name} - Score: {score} ({status})") 