grades = [
    [ "Bobby", "87" ],
    [ "Charles", "100" ],
    [ "Eric", "64" ],
    [ "Charles", "22" ]
]

def bestAverageGrade(grades):

    avgs = {}
    best = 0

    for row in grades:

        student = row[0]
        grade = int(row[1])

        if student not in avgs.keys():

            avgs[student] = grade
            #best = grade if grade > best else best

        else:

            newAvg = round((avgs[student] + grade) / 2)
            avgs[student] = newAvg
            #best = newAvg if newAvg > best else best

    for stu in avgs:

        best = int(avgs[stu]) if int(avgs[stu]) > best else best

    return best


print(bestAverageGrade(grades))

'''
if the key exists
    add the new grade and divide by 2, that way we're only maintaining the avg

keep track of previous high
'''