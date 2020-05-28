grades_at_school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                    {'school_class': '5б', 'scores': [5,4,5,4,3]},
                    {'school_class': '10ы', 'scores': [2,3,2,4,2]}
                    ]

scores_sum = 0
for grade in grades_at_school:
    a = sum(grade['scores'])/len(grade['scores'])
    print(a)
    grade = sum(grade['scores'])
    #print(grade)
    scores_sum += grade

print(scores_sum/len(grades_at_school))

