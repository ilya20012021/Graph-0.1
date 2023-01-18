import pandas as pd
from graph import Graph


def add_node():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print("Файл: ", i)
    print('Введите команду "ADD NODE <filename>"')
    k2 = [str(i) for i in input().split()]
    if "ADD" in k2 and "NODE" in k2 and len(k2) == 3 and k2[2] in u:
        # конвертация графа в таблицу
        df = pd.read_csv(f"{k2[2]}.csv")  # пишу считывание данных для показа
        if len(df) == 0:
            col = []
            s = str(input("Кол-во столбцов:"))
            if s.isdigit():
                s = int(s)
                for i in range(s):
                    x = str(input("Столбец:"))
                    col.append(x)
            else:
                exit("---------")

            s = str(input("Кол-во значений в столбце:"))

            for i in col:
                o = []
                if s.isdigit():
                    n = int(s)
                    for z in range(n):
                        e = str(input("Введите значение:"))
                        o.append(e)
                df[i] = o

            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df.to_csv(f"{k2[2]}.csv")
            # конвертор таблицы в граф с экранированием и сохранением
            graph = Graph(k2[2])
            graph.draw_graph()

        else:
            print("----")


    else:
        print("WRONG!")
