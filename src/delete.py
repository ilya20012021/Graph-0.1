import pandas as pd
from graph import Graph


def del_node():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print("Файл: ", i)
    print('Введите команду "DEL NODE <filename>"')
    k3 = [str(i) for i in input().split()]
    if "DEL" in k3 and "NODE" in k3 and len(k3) == 3 and k3[2] in u:
        # конвертация графа в таблицу
        df = pd.read_csv(f"{k3[2]}.csv")  # пишу считывание данных для показа
        s = str(input("Введите значение:"))
        c = str(input("Введите имя столбца:"))
        k1 = list(df.keys())
        if c in k1:
            df = df[df[c] != s]
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df.to_csv(f"{k3[2]}.csv")
            # конвертор таблицы в граф с экранированием и сохранением
            graph = Graph(k3[2])
            graph.draw_graph()
        else:
            print("WRONG NAME!")

    else:
        print("WRONG!")
