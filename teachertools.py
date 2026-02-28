def average_mark(*marks:list[int | float]):
    sum_of_marks:float = 0
    amount:int = 0
    average_mark:float = 0
    for i in range(len(marks)):
        sum_of_marks += marks[i]
        amount += 1
    average_mark = sum_of_marks / amount
    return average_mark

def is_enter(completed_mark, *marks):
    completed:int = 0
    for i in range(len(marks)):
        if marks[i] >= completed_mark:
            completed += 1
    return completed

def students(*students:list) -> None:
    print("------- STUDENTS -------\n\n")
    for i in range(len(students)):
        print(f"----  {students[i]}  ----\n")

def get_students_file(*students:list) -> None:
    with open("students.txt", "w", encoding="UTF-8") as file:
        file.write("------- STUDENTS -------\n\n")
        for i in range(len(students)):
            file.write(f"----  {students[i]}  ----\n")

def schedual(schedual:dict[str, str | int | float]) -> None:
    print("------- SCHEDUAL -------")
    for lesson, time in schedual.items():
        print(f"{lesson} - {time}\n")

def get_schedual_file(schedual:dict[str, str | int | float]) -> None:
    with open("schedual.txt", "w", encoding="UTF-8") as file:
        print("------- SCHEDUAL -------\n\n")
        for lesson, time in schedual.items():
            file.write(f"{lesson} - {time}\n")
            print(f"{lesson} - {time}\n")
