erin_gpa=4.5
erin_score=75

if erin_gpa>=3.5:
    if 50<=erin_score<=65:
        print("partial scholarship")
    elif erin_score>65:
        print("full scholarship")
    else:
        print("no scholarship")
else:
    print("no scholarship")