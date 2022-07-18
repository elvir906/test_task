def appearance(intervals):
    # создание списка четных номеров временных интервалов ученика
    nums_pupil = [
        num*2 for num in range(0, round(len(intervals.get('pupil')) / 2))
    ]

    # создание списка четных номеров временных интервалов учителя
    nums_tutor = [
        num*2 for num in range(0, round(len(intervals.get('tutor')) / 2))
    ]

    # генерация множества из секунд временного отрезка урока
    lesson_time = set([i for i in range(
        intervals.get('lesson')[0], intervals.get('lesson')[1]
    )])

    # генерация множества из секунд временного отрезка ученика
    full_pupil_time = {}
    for num in nums_pupil:
        pupil_time = set([i for i in range(
            intervals.get('pupil')[num], intervals.get('pupil')[num + 1]
        )])
        full_pupil_time = pupil_time.union(full_pupil_time)

    # генерация множества из секунд временного отрезка учителя
    full_tutor_time = {}
    for num in nums_tutor:
        tutor_time = set([i for i in range(
            intervals.get('tutor')[num], intervals.get('tutor')[num + 1]
        )])
        full_tutor_time = tutor_time.union(full_tutor_time)

    # вычисление временных пересечений
    tutor_pupil_intersection = full_tutor_time.intersection(full_pupil_time)
    result_intersection = tutor_pupil_intersection.intersection(
        lesson_time
    )

    return len(result_intersection)


tests = [
    {
        'data': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390,
                      1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443,
                      1594666473]
        },
        'answer': 3117
    },

    {
        'data': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807,
                      1594704542, 1594704512, 1594704513,
                      1594704564, 1594705150, 1594704581,
                      1594704582, 1594704734, 1594705009,
                      1594705095, 1594705096, 1594705106,
                      1594706480, 1594705158, 1594705773,
                      1594705849, 1594706480, 1594706500,
                      1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579,
                      1594706641],
            'tutor': [1594700035, 1594700364, 1594702749,
                      1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },

    {
        'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068,
                      1594696341]
        },
        'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        appearance(test['data'])
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], (f'Error on test case {i}, '
                                               f'got {test_answer}, '
                                               f'expected {test["answer"]}')
