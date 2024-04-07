def get_students_who_took_prog1_and_prog2(prog1, prog2):
    students = prog1.intersection(prog2)
    return students

def get_students_who_took_prog1_or_prog2(prog1, prog2):
    students = prog1.union(prog2)
    return students

def get_students_who_took_prog1_not_prog_2(prog1, prog2):
    students = prog1.difference(prog2)
    return students

def get_students_who_took_prog2_not_prog_1(prog1, prog2):
    students = prog2.difference(prog1)
    return students
