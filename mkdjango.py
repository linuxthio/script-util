import os
import sys

projet = sys.argv[1]
app = sys.argv[2]

os.system(f"django-admin startproject {projet} .")
os.system(f"django-admin startapp {app}")


def ecrire(pp, n, l):
    f = open(pp, "r")
    ll = []
    for e in f:
        ll.append(str(e))
    m = ll[:n]
    m = m[:] + l[:] + ["\n"]
    m = m[:] + ll[n:]
    f.close()
    return m


l = [f'    "{app}.apps.{app.title()}Config",']

# ecrire(f, 50, l)


def chg(pp, n, l):
    d = ecrire(pp, n, l)
    with open(pp, "w") as f:
        for e in d:
            f.write(e)


chg(f"./{projet}/settings.py", 39, l)
chg(f"./{projet}/urls.py", 18, [f"from {app} import views"])
chg(f"./{projet}/urls.py", 22, ['    path("", view=views.index),'])
