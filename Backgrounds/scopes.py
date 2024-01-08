global_var = 'I am global variable'

def f1() -> None:
    print (global_var)

    # global global_var
    # global_var = 'Changed by f1'
    # print (global_var)

def f2() -> None:
    local_var_f2 = 'I am local at f2'
    


def f3() -> None:
    local_var_f3 = 'I am local at f3'

    def change_local_var_f3() -> None:
        nonlocal local_var_f3
        local_var_f3 += '. Changed!'

    change_local_var_f3()
    print (local_var_f3)



# print (global_var)
# print (local_var_f2)
# f1()
# f3()