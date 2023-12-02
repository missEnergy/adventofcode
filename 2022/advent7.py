from csv import reader


class Dir:
    def __init__(self, path, parent_dir):
        self.path = path
        self.parent_dir = parent_dir
        self.dirs = []
        self.files = []

    def add_dir(self, dir):
        self.dirs.append(dir)

    def add_file(self, file):
        self.files.append(file)

    def get_child_dir(self, child_path):
        for dir in self.dirs:
            if dir.path == child_path:
                return dir
        raise ValueError(f"{child_path} not present in dirs")


class File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name


total_size = 0


def get_size_of_dir(dir, ts):
    file_sizes = 0
    for file in dir.files:
        file_sizes = file_sizes + file.size
    dir_sizes = 0
    for i in dir.dirs:
        dir_size, ts = get_size_of_dir(i, ts)
        if dir_size <= 100000:
            ts = ts + dir_size
        dir_sizes = dir_sizes + dir_size
    return file_sizes + dir_sizes, ts


def print_dir(dir, indent=""):
    print(f"{indent}- {dir.path} (dir, size={get_size_of_dir(dir)})")
    new_indent = indent + "\t"
    for file in dir.files:
        print(f"{new_indent}- {file.name} (file, size={file.size})")
    for i in dir.dirs:
        print_dir(i, new_indent)


root_dir = Dir("/", None)
current_dir = root_dir
with open("advent7.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        command = row[0]
        print(command)
        if command == "$ cd ..":
            current_dir = current_dir.parent_dir
        elif command.startswith("$ cd"):
            current_dir = current_dir.get_child_dir(command.replace("$ cd ", ""))
        elif command == "$ ls":
            print("do nothing")
        elif command.startswith("dir"):
            current_dir.add_dir(Dir(command.replace("dir ", ""), current_dir))
        else:
            size, name = command.split(" ")
            current_dir.add_file(File(size, name))

_, total_size = get_size_of_dir(root_dir, total_size)
print(total_size)
