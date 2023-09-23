do_list = []
done_list = []
pending_list = []
while True:
    while True:
        a = '''***** MAIN MENU *****
1)- Create a new to-do list.
2)- Update current to-do list.
3)- Track your to-do list
4)- Exit '''
        print(a)
        n = input("Enter choice: ")
        if n in ["1","2","3","4"]:
            break
        else:
            print("Wrong choice!")   
            p = input("<--Press Enter-->")
            continue     
    if n == "1":
        while True:
            try:
                b = int(input("Enter total number of activities: "))
                break
            except ValueError:
                print("Invalid input! Please enter 'integer' value")
                p = input("<--Press Enter-->")
                continue
        for i in range(1,b+1):
            c = input("Enter activity: ")
            do_list.append(c)
            pending_list.append(c)
        print("To-do list is created")
        p = input("<--Press Enter-->")
    elif n == "2":
        while True:
            q = '''***** UPDATE LIST *****
1)- Task you want to add in list.
2)- Task you completed.
3)- Back'''
            print(q)
            m = input("Enter choice: ")
            if m not in ["1","2","3"]:
                print("Wrong choice")
                p = input("<--Press Enter-->")
                continue
            if m == "2":
                e = input("Enter task you completed: ")
                if e in do_list:
                    if e not in done_list:
                        done_list.append(e)
                    if e in pending_list:
                        pending_list.remove(e)
                    else:
                        print("Given task is already completed")
                        p = input("<--Press Enter-->")
                        continue
                    print("Task marked as completed")
                    p = input("<--Press Enter-->")
                else:
                    print("Given task is not mentioned in to-do list")
                    p = input("<--Press Enter-->")
            elif m == "1":
                f = input("Enter task you want to add in to-do list: ")
                if f in do_list:
                    print("Task is already mentioned in to-do list")
                    p = input("<--Press Enter-->")
                else:
                    do_list.append(f)
                    pending_list.append(f)
                    print("Task added to list")
                    p = input("<--Press Enter-->")
            else:
                break
    elif n == "3":
        while True:
            l = '''***** TRACKING YOUR TO-DO LIST *****
1)- Display to-do list.
2)- Display tasks completed.
3)- Display tasks pending.
4)- Back'''
            print(l)
            z = input("Enter choice: ")
            if z not in ["1","2","3","4"]:
                print("Wrong choice!")
                p = input("<--Press Enter-->")
                continue
            if z == "1":
                print("To-do list is as follows: ")
                for i in do_list:
                    print(i)
                p = input("<--Press Enter-->")
            elif z == "2":
                print("Completed tasks are as follows: ")
                for i in done_list:
                    print(i)
                p = input("<--Press Enter-->")
            elif z == "3":
                print("Pending tasks are as follows: ")
                for i in pending_list:
                    print(i)
                p = input("<--Press Enter-->")
            else:
                break
    else:
        break 