def help():
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("CREATE NODE <filename> - создание графа. Создание пустой таблицы в виде графа для дальнейшей работы с ним.")
    print("ADD NODE <filename> - заполнение графа. Один из этапов работы с графовым представлением таблицы с данными. В этом этапе мы заполняем наш граф данными.")
    print("DEL NODE <filename> - удаление данных в графе. Очистка графа от ненужных/устаревших данных.")
    print("UPDATE NODE <filename> - обновление данных.")
    print("CONCATE NODE <filename1> <filename2> - склейка таблиц. По-другому говоря, полное объединение таблиц.")
    print("JOIN NODE <filename1> <filename2> - объединение таблиц. Операции JOIN, как в языке SQL: inner,left,right")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")