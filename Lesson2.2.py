my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
rig = []

for i in my_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            rig.append(f"'{int(i):02}'")
        else:
            rig.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        rig.append(i)
print(rig)
print(" ".join(rig))
