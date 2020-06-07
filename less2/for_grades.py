grades_at_school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                    {'school_class': '5б', 'scores': [5,4,5,4,3]},
                    {'school_class': '10ы', 'scores': [2,3,2,4,2]}
                    ]

scores_sum = 0
for grade in grades_at_school:
    a = sum(grade['scores'])/len(grade['scores'])
    print(a)
    grades_sum = sum(grade['scores'])
    #print(grades_sum)
    scores_sum += grades_sum

print(scores_sum/len(grades_at_school))

