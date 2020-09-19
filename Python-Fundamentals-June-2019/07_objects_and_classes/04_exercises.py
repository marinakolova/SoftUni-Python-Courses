class Exercise:

    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


if __name__ == '__main__':
    exercises = []
    while True:
        inp = input()
        if inp == 'go go go':
            break

        inp = inp.split(' -> ')
        inp_topic = inp[0]
        inp_course_name = inp[1]
        inp_judge_contest_link = inp[2]
        inp_problems = [x.strip() for x in inp[3].split(', ')]
        exercises.append(Exercise(inp_topic, inp_course_name, inp_judge_contest_link, inp_problems))

    for ex in exercises:
        print(f'Exercises: {ex.topic}')
        print(f'Problems for exercises and homework for the "{ex.course_name}" course @ SoftUni.')
        print(f'Check your solutions here: {ex.judge_contest_link}')
        for i, p in enumerate(ex.problems, 1):
            print(f'{i}. {p}')
