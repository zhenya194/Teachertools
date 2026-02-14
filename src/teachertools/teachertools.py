def average_mark(*marks:list[int | float]):
    sum_of_marks:float = 0
    amount:int = 0
    average_mark:float = 0
    for i in range(len(marks)):
        sum_of_marks += marks[i]
        amount += 1
    average_mark = sum_of_marks / amount
    return average_mark
