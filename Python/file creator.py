import os
l = os.listdir()
l.remove(__file__.rsplit("\\", 1)[-1])

l = (int(i.rsplit(".", 1)[0].rsplit("-")[0]) for i in l if i.endswith(".py"))

s = max(l)

with open(str(s+1)+".py", "w") as f:
    pass
