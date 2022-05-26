#ДЗ №3 Парты и школьники



class1 = int(input(20))
class2 = int(input(27))
class3 = int(input(30))




answer1 = class1 // 2
answer2 = class2 % 2
answer3 = class3 // 2

print('Ответ1', answer1)
print('Ответ2', answer2)
print('Ответ3', answer3)

answer_final = answer1 + answer2 + answer3
print('Количество парт:', answer_final)

# Во втором классе нечетное количество учеников. Следовательно, нужно прибавить еще одну парту для ученика без пары