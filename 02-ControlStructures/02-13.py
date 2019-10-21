x = 0
y = 0
if x==0 and y==0:
    print(f"Punkt P({x},{y}) leży na początku układu współrzędnych")
elif x==0 and (y>0 or y<0):
    print(f"Punkt P({x},{y}) leży na osi Y")
elif (x>0 or x<0) and y==0:
    print(f"Punkt P({x},{y}) leży na osi X")
elif x>0 and y>0:
    print(f"Punkt P({x},{y}) leży w I ćwiartce")
elif x>0 and y<0:
    print(f"Punkt P({x},{y}) leży w II ćwiartce")
elif x<0 and y<0:
    print(f"Punkt P({x},{y}) leży w III ćwiartce")
elif x<0 and y>0:
    print(f"Punkt P({x},{y}) leży w IV ćwiartce")