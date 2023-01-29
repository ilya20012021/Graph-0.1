import pandas as pd
from graph import Graph
def nf1():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print("Файл: ", i)
    print('Введите команду "NF1 NODE <filename>"')
    k5 = [str(i) for i in input().split()]
    if "NF1" in k5 and "NODE" in k5 and len(k5) == 3 and k5[2] in u:
        print("Каждый из ранее созданных графов находится в первой нормальной форме.")
        print("1 НФ - когда таблица для конвертации в граф не содержит атрибута/атрибутов, который имеет/имеют  в ячейке/ячейках несколько значений.")
        # конвертация графа в таблицу
        df1 = pd.read_csv(f"{k5[2]}.csv")  # пишу считывание данных для показа
        df1 = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]
        name = str(input("Введите имя графа для сохранения:"))
        df1.to_csv(f"{name}.csv")
        with open("nf1.txt", "a+") as f:
            f.write(f'{name}\n')
        # конвертор таблицы в граф с экранированием и сохранением
        if len(df1) != 0:
            graph = Graph(name)
            graph.draw_graph()
        else:
            print("WRONG!")

    else:
        print("WRONG!")