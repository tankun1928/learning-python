for st in range(1,4):
    # do something
    print("Student %d:" % st)
    # 1) get 5 inputs + sum
    total = 0 # reset to 0 for every student
    for sb in range(1,6):
        score = int(input("\tSubject %d: " % sb))
        total += score

    # 2) show total score
    print("Total score of student %d is %d." % (st, total))