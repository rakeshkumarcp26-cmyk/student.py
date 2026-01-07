import os

def show_grade_criteria():
    print("--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------\n")


def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    # Read Jenkins parameters
    name = os.getenv("name", "UNKNOWN")
    dept = os.getenv("dept", "UNKNOWN")
    sem = os.getenv("sem", "0")

    m1 = int(os.getenv("m1", 0))
    m2 = int(os.getenv("m2", 0))
    m3 = int(os.getenv("m3", 0))

    show_grade_criteria()

    print("--- Student Details ---")
    print(f"Name: {name}")
    print(f"Department: {dept}")
    print(f"Semester: {sem}\n")

    print("--- Subject Marks ---")
    print(f"Subject 1: {m1}")
    print(f"Subject 2: {m2}")
    print(f"Subject 3: {m3}\n")

    avg = (m1 + m2 + m3) / 3
    print(f"Average Marks: {avg}")
    print(f"Final Grade: {calculate_grade(avg)}")


if __name__ == "__main__":
    main()
