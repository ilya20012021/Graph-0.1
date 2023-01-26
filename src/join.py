import pandas as pd
from graph import Graph


def join():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print("Файл: ", i)
    print('Введите команду "JOIN NODE <filename1> <filename2>"')
    k5 = [str(i) for i in input().split()]
    if "JOIN" in k5 and "NODE" in k5 and len(k5) == 4 and k5[2] in u and k5[3] in u:
        # конвертация графа в таблицу
        df1 = pd.read_csv(f"{k5[2]}.csv")  # пишу считывание данных для показа
        df2 = pd.read_csv(f"{k5[3]}.csv")
        how = ["inner","left","join"]
        how1 = str(input("Введите вид объединения:"))
        cols = list(df2.keys())
        c = str(input("Введите имя столбца, по которому будет происходить объединение:"))
        if how1 in how and c in cols:
            df3 = df1.merge(df2,how=how1,on=c)
            df3 = df3.loc[:, ~df3.columns.str.contains('^Unnamed')]
            name = str(input("Введите название графа:"))
            df3.to_csv(f"{name}.csv")
            # конвертор таблицы в граф с экранированием и сохранением
            if len(df3) != 0:
                graph = Graph(name)
                graph.draw_graph()
            else:
                print("WRONG!")
        else:
            print("WRONG!")

    else:
        print("WRONG!")