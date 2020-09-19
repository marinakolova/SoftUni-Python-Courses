class Gladiator:
    def __init__(self, gladiator_name, skills):
        self.gladiator_name = gladiator_name
        self.skills = skills
        self.total_skills = self.get_total_skills_amount()

    def get_total_skills_amount(self):
        return sum(list(self.skills.values()))


gladiators_list = []

data = input()

while not data == 'Ave Cesar':
    splitted_data = data.split(' -> ')

    gladiators_names_list = list(map(lambda gl: gl.gladiator_name, gladiators_list))

    if len(splitted_data) == 3:
        name = splitted_data[0]
        technique = splitted_data[1]
        skill = int(splitted_data[2])

        if not name in gladiators_names_list:
            gladiator = Gladiator(name, {technique: skill})
            gladiators_list.append(gladiator)
        else:
            gladiator = list(filter(lambda gl: gl.gladiator_name == name, gladiators_list))[0]
            if technique in gladiator.skills.keys():
                if gladiator.skills[technique] < skill:
                    gladiator.skills[technique] = skill
                    gladiator.total_skills = gladiator.get_total_skills_amount()
            else:
                gladiator.skills.update({technique: skill})
                gladiator.total_skills = gladiator.get_total_skills_amount()


    else:
        fighter_1 = data.split(' vs ')[0]
        fighter_2 = data.split(' vs ')[1]

        if fighter_1 in gladiators_names_list and fighter_2 in gladiators_names_list:
            fighter_1_techiques_list = list(filter(lambda gl: gl.gladiator_name == fighter_1, gladiators_list))[
                0].skills.keys()
            fighter_2_techiques_list = list(filter(lambda gl: gl.gladiator_name == fighter_2, gladiators_list))[
                0].skills.keys()
            common_skills = list(set(fighter_1_techiques_list).intersection(set(fighter_2_techiques_list)))

            if common_skills:
                fighter_1_obj = list(filter(lambda gl: gl.gladiator_name == fighter_1, gladiators_list))[0]
                fighter_2_obj = list(filter(lambda gl: gl.gladiator_name == fighter_2, gladiators_list))[0]

                total_skills_1 = fighter_1_obj.get_total_skills_amount()
                total_skills_2 = fighter_2_obj.get_total_skills_amount()

                if total_skills_1 < total_skills_2:
                    gladiators_list.remove(fighter_1_obj)
                elif total_skills_2 < total_skills_1:
                    gladiators_list.remove(fighter_2_obj)

    data = input()

ordered_gladiators = sorted(gladiators_list, key=lambda gl: (-gl.total_skills, gl.gladiator_name))

for gladiator in ordered_gladiators:
    print(f'{gladiator.gladiator_name}: {gladiator.get_total_skills_amount()} skill')
    for techique, skill in sorted(gladiator.skills.items(), key=lambda kvp: kvp[1], reverse=True):
        print(f'- {techique} <!> {skill}')
