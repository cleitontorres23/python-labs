def arg(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

#args = ('um', 2, 3)
#kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg4': 4}

#arg(*args)


def arg_mais_um(**kwargs):
    for i in kwargs:
        print(i)


kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um', 'arg4': 4}
arg_mais_um(**kwargs)
