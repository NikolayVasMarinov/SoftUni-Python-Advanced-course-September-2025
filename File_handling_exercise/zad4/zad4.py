import os

def get_files(folder, level=1) -> None:
    if level == -1:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            file_name, file_extension = os.path.splitext(f)

            if file_extension not in files:
                files[file_extension] = []

            files[file_extension].append(file_name)

        else:
            get_files(f, level - 1)


files: dict[str, list[str]] = {}

get_files("..\\")

files = dict(sorted(files.items(), key=lambda x: (x[0])))

for extension, file_list in files.items():
    file_list.sort()

    print(extension)
    for file in file_list:
        print(f"   - {file}{extension}")