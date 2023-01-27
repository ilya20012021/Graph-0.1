import add_node
import concatenation
import create
import delete
import info
import join
import nf1
import nf2
import nf4
import nf5
import upd
import nf3

n = 1

while n != 0:
    m = ["Создать граф(нажмите 1)", "добавить ноды(нажмите 2)", "удалить ноды(нажмите 3)", "обновить ноды(нажмите 4)","склеивание графов(нажмите 5)","объединение графов(нажмите 6)","Приведение 1 НФ(нажмите 7)","Приведение 2 НФ(нажмите 8)","Приведение 3 НФ(нажмите 9)","Приведение 4 НФ(нажмите 10)","Приведение 5 НФ(нажмите 11)","справочная информация(--help)"]
    for i in m:
        print(i)

    s = str(input())
    if s == "1":
        create.create_node()
    elif s == "2":
        add_node.add_node()
    elif s == "3":
        delete.del_node()
    elif s == "4":
        upd.update_node()
    elif s == "5":
        concatenation.concate()
    elif s == "6":
        join.join()
    elif s == "7":
        nf1.nf1()
    elif s == "8":
        nf2.nf2()
    elif s == "9":
        nf3.nf3()
    elif s == "10":
        nf4.nf4()
    elif s == "11":
        nf5.nf5()
    elif s == "--help":
        info.help()
    else:
        print("???")
    ans = ["да", "нет"]
    ans_n = "/".join(ans)
    print(f"Хотите ли вы продолжить работу с данным ПО?{ans_n}")
    s = str(input("Введите ответ:"))
    if s == ans[0]:
        n += 1
    elif s == ans[1]:
        break
    else:
        print("Ничего непонятно")
