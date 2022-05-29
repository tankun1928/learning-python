todo = {}

while True:
    inp = input("To do: ")
    n = len(inp)
    if n > 0:
        k = inp
        detail = input("* details: ")
        todo[k] = detail
    else:
        break

print("You have  %d thing(s) to do:" % len(todo))
for k in sorted(todo.keys()):
    print(k)
    print("*", todo[k])