def activity_selection(start, finish):

    activities = sorted(
        zip(start, finish),
        key=lambda x: x[1]
    )

    count = 1
    last_finish = activities[0][1]

    for i in range(1, len(activities)):

        if activities[i][0] >= last_finish:

            count += 1
            last_finish = activities[i][1]

    return count


print(
    activity_selection(
        [1,3,0,5,8,5],
        [2,4,6,7,9,9]
    )
)
