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
    search_file,
    copy_file,
    move_file,
    file_info,
    count_files,
    open_folder,
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

    elif command.startswith("search file "):
        keyword = command.replace("search file ", "")
        return search_file(keyword)
    elif command.startswith("copy file "):
        try:
            parts = command.split()

            old_name = parts[2]
            new_name = parts[3]

            return copy_file(old_name, new_name)

        except:
            return "Use: copy file old_name new_name"


    elif command.startswith("move file "):
        try:
            parts = command.split()

            old_name = parts[2]
            new_name = parts[3]

            return move_file(old_name, new_name)

        except:
            return "Use: move file old_name new_name"


    elif command.startswith("file info "):
        filename = command.replace("file info ", "")
        return file_info(filename)


    elif command == "count files":
        return count_files()


    elif command == "open folder":
        return open_folder()

    elif command.startswith("create folder "):
        folder = command.replace("create folder ", "")
        return create_folder(folder)

    elif command == "list folders":
        return list_folders()

    elif command.startswith("delete folder "):
        folder = command.replace("delete folder ", "")
        return delete_folder(folder)
    elif command == "list files":
        print("DEBUG: list files block")
        return list_files()
    return None