from os.path import dirname, abspath


def create_df(name: str, *args):
    cur_line = 1
    with open(f"{dirname(abspath('main.py'))}\{name}.txt", "w") as f:
        for i in args:
            f.write(f"{cur_line}: {i}\n")
            cur_line += 1


def add_to_df(name, *args):
    cur_line = 1
    with open(f"{dirname(abspath('main.py'))}/{name}.txt", "r"):
        pass
    with open(f"{dirname(abspath('main.py'))}/{name}.txt", "a") as f:
        for i in args:
            f.write(f"{cur_line}: {i}\n")
            cur_line += 1
