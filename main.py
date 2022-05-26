# ДЗ №3 Парты и школьники


kidsinclass1 = int(input(20))
kidsinclass2 = input(27)
kidsinclass3 = input(30)

answer1 = kidsinclass1 // 2
answer2 = kidsinclass2 % 2
answer3 = kidsinclass3 // 2

print('Ответ1', answer1)
print('Ответ2', answer2)
print('Ответ3', answer3)

answer_final = answer1 + answer2 + answer3
print('Количество парт:', answer_final)

# Во втором классе нечетное количество учеников. Следовательно, нужно прибавить еще одну парту для ученика без пары
