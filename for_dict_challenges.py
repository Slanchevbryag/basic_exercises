# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
list_of_st = []
record_of_st = {}
for student in students:
    list_of_st.append(student['first_name'])

list_of_name = set(list_of_st)

for name in list_of_name:
    record_of_st[name] = list_of_st.count(name)

print(record_of_st)

#for name in list_of_name:
#    collect = list_of_st.count(name)
#    print(f'{name}: {collect}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
list_of_st = []
oftentimes = 0
oft_name = None

for student in students:
    list_of_st.append(student['first_name'])

for name in list_of_st:
    collect = list_of_st.count(name)
    if collect >= oftentimes:
        oftentimes = collect
        oft_name = name
    
print(f'Самое частое имя среди учеников: {oft_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

nume_of_class = 1

for school_class in school_students:

    list_of_st = []
    oftentimes = 0
    oft_name = None

    for student in school_class:
        list_of_st.append(student['first_name'])

    for name in list_of_st:
        collect = list_of_st.count(name)
        if collect >= oftentimes:
            oftentimes = collect
            oft_name = name
    
    print(f'Самое частое имя в классе {nume_of_class}: {oft_name}')

    nume_of_class += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 
     'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for students_of_class in school:
    
    boys = 0
    girls = 0
    
    for list_of_st in students_of_class['students']:
        
        for name, male in is_male.items():

            if list_of_st['first_name'] == name and male == True:
                boys += 1

            if list_of_st['first_name'] == name and male == False:
                girls += 1

    print(f"Класс {students_of_class['class']} : девочки {girls}, мальчики {boys}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for students_of_class in school:
    
    boys = 0
    girls = 0
        
    for list_of_st in students_of_class['students']:
        
        for name, male in is_male.items():

            if list_of_st['first_name'] == name and male == True:
                boys += 1

            if list_of_st['first_name'] == name and male == False:
                girls += 1
                
        if boys >= most_of_boys:
            most_of_boys = boys
            class_boys = students_of_class['class']
        if girls >= most_of_girls:
            most_of_girls = girls
            class_girls = students_of_class['class']

print(f"Больше всего мальчиков в {class_boys} классе")
print(f"Больше всего девочек в {class_girls} классе")
