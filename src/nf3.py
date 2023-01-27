import pandas as pd
from graph import Graph
def nf3():
    s = open("nf2.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    for i in u:
        print("Файл: ", i)
    print('Введите команду "NF3 NODE <filename>"')
    k5 = [str(i) for i in input().split()]
    if "NF3" in k5 and "NODE" in k5 and len(k5) == 3 and k5[2] in u:
        print("3 НФ - когда таблица для конвертации в граф находится в 2 НФ и ее атрибуты нетранзитивно зависимы(имеют ссылочную целостность).")
        # конвертация графа в таблицу
        df1 = pd.read_csv(f"{k5[2]}.csv")  # пишу считывание данных для показа
        m1 = []
        m2 = []
        k = list(df1.keys())
        e = str(input("Введите число для прогона:"))
        if e.isdigit():
            for j in range(len(df1)):
                kl = str(input("Введите столбец для отнесения его к одной из таблиц:"))
                if kl in k:
                    print("В какую таблицу относим? В первую или во вторую?")
                    s = str(input())
                    if s == "1":
                        m1.append(kl)
                    elif s == "2":
                        m2.append(kl)
                    else:
                        print("---------")

                else:
                    print("---------")

            df2 = df1[m1]
            df3 = df1[m2]
            name1 = str(input("Введите название графа1:"))
            df2.to_csv(f"{name1}.csv")
            with open("nf3.txt", "a+") as f:
                f.write(f'{name1}\n')
            name2 = str(input("Введите название графа2:"))
            df3.to_csv(f"{name2}.csv")
            with open("nf3.txt", "a+") as f:
                f.write(f'{name2}\n')

            if len(df2) != 0:
                graph = Graph(name1)
                graph.draw_graph()
            else:
                print("WRONG!")

            if len(df3) != 0:
                graph = Graph(name2)
                graph.draw_graph()
            else:
                print("WRONG!")

        else:
            exit("??????")

    else:
        print("WRONG!")
