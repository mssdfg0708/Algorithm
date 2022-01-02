def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        possible = True
        learned = []

        for s in skill_tree:
            necessary = []

            # 스킬 트리가 필요한 스킬
            if s in skill:
                for s_skill in skill:
                    if s_skill == s:
                        break
                    necessary.append(s_skill)
                for n in necessary:
                    if n not in learned:
                        possible = False
                        break
            if possible:
                learned.append(s)

        if possible:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
