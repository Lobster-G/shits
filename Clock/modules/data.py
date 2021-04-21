cur_line = 1


def create_df(name: str, *args):
    global cur_line
    with open(f"{name}.txt", "w") as f:
        for i in args:
            f.write(f"{cur_line}: {i}\n")
            cur_line += 1


def add_to_df(name, *args):
    global cur_line
    with open(f"{name}.txt", "r"):
        pass
    with open(f"{name}.txt", "a") as f:
        for i in args:
            f.write(f"{cur_line}: {i}\n")
            cur_line += 1
