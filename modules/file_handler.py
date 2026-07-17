from files import (
    create_file,
    write_file,
    read_file,
    list_files,
    delete_file,
    append_file,
    create_folder,
    list_folders,
    delete_folder,
    rename_file,
)


def handle_file(command):

    print("Received:", command)

    if command.startswith("create file "):
        filename = command.replace("create file ", "")
        return create_file(filename)

    elif command.startswith("write file "):
        try:
            parts = command.split(" ", 3)
            filename = parts[2]
            text = parts[3]
            return write_file(filename, text)
        except:
            return "Use: write file filename text"

    elif command.startswith("read file "):
        filename = command.replace("read file ", "")
        return read_file(filename)

    elif command == "list files":
        return list_files()

    elif command.startswith("delete file "):
        filename = command.replace("delete file ", "")
        return delete_file(filename)

    elif command.startswith("append file "):
        data = command.replace("append file ", "")
        filename = data.split(" ")[0]
        text = data.replace(filename, "").strip()
        return append_file(filename, text)

    elif command.startswith("rename file "):
        try:
            parts = command.split()

            old_name = parts[2]
            new_name = parts[3]

            return rename_file(old_name, new_name)

        except:
            return "Use: rename file old_name new_name"

    elif command.startswith("create folder "):
        folder = command.replace("create folder ", "")
        return create_folder(folder)

    elif command == "list folders":
        return list_folders()

    elif command.startswith("delete folder "):
        folder = command.replace("delete folder ", "")
        return delete_folder(folder)

    return None