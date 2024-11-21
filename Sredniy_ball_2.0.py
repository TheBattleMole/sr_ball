grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_alf = list(students)
students_alf.sort()
sr_ball = []
for i in grades:
    sr_ball.append(sum(i)/len(i))
itog = dict(zip(students_alf, sr_ball))
print(itog)