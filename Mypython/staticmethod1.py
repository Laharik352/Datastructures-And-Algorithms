class Student:

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

print(Student.is_full_name('Scott Robinson'))   # True
print(Student.is_full_name('Scott'))            # False