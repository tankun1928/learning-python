hours =  float(input("How many hours do you submit late? "))
print()
score = float(input("What is your estimated score? "))
if hours == 0:
     score = score
elif hours <= 24:
     score = (score * 20/100) - score
     score = abs(score)
elif hours <= 48:
     score = (score * 50/100) - score
     score = abs(score)
else:
     score = score * 0   
     score = float(score)
print("Your expected score is %.1f" % score)

