
facts = {'A', 'B'}

rules = [
    ({'A', 'B'}, 'C'),
    ({'C'}, 'D'),
    ({'D'}, 'E')
]

goal = 'E'

def forward_chaining(facts, rules, goal):
    while True:
        new_fact = False

        for conditions, result in rules:
            if conditions.issubset(facts) and result not in facts:
                facts.add(result)
                print("Derived:", result)
                new_fact = True

                if result == goal:
                    print("Goal reached:", goal)
                    return

        if not new_fact:
            break

    print("Goal not found")

forward_chaining(facts, rules, goal)
