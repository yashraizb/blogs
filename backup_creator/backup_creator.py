import traceback as tb
import os
import pathlib
import shutil


def is_backup_required(location: str, src: str, dest: str, dir: bool):
    """
        This function will check whether the file/folder needs to be backed up or not
    Args:
        location: absolute path of the file/folder(item) which is being processed
        src: parent location where this item is present
        dest: destination location where this needs to backed up
        dir: boolean value whether the passed location is of file or a folder
    returns
        bool | None
    """
    try:
        dest_backup = location.replace(src, dest)
        is_exists = os.path.exists(dest_backup)
        is_modified = False
        # print("{} exists: {}".format(dest_backup, is_exists))
        if is_exists:
            if dir:
                return None
            src_last_mod = pathlib.Path(location).stat().st_mtime
            dest_last_mod = pathlib.Path(dest_backup).stat().st_mtime
            is_modified = (src_last_mod != dest_last_mod)
            return is_modified
        else:
            return True
    except Exception as error:
        print("is_backup_required error is: {}".format(error))
        raise error


def create_backup(source_location, destination_location):
    """
        This function will create backup of source location to the destination location
    Args:
        source_location: source location of the data to be backed up
        destination_location: destination location where data will be backed up
    returns:
        None
    """
    try:
        dirs = [source_location]
        files = []
        
        while len(dirs) > 0:
            
            location = dirs.pop(0)

            for obj in os.scandir(location):
                src_absolute_path = location + "/" + obj.name
                dest_absolute_path = src_absolute_path.replace(source_location, destination_location)
                # print("proccessing {}".format(src_absolute_path))
                is_required = is_backup_required(src_absolute_path, source_location, destination_location, dir=obj.is_dir())
                # print("backup required: {}".format(is_required))
                if obj.is_file() and is_required:
                    shutil.copy2(src_absolute_path, dest_absolute_path)
                    print("Backing up: {} --> {}".format(src_absolute_path, dest_absolute_path))
                elif obj.is_dir():
                    if is_required != None:
                        shutil.copytree(src_absolute_path, dest_absolute_path)
                        print("Backing up: {} --> {}".format(src_absolute_path, dest_absolute_path))
                    else:
                        dirs.append(src_absolute_path) 
    except Exception as error:
        print("Error is: {}".format(error))
        print("trace: {}".format(tb.format_exc()))

if __name__ == "__main__":
    while True:
        choice = input("Press Y to start the backup, or Q to quit: ")
        if choice.lower() == "q":
            exit()
        elif choice.lower() != "y":
            print("Invalid choice")
            continue
        source_location = input("Enter the source location: ")
        
        if not os.path.exists(source_location):
            print("Error: source location does not exists")
            continue
        if not os.path.isdir(source_location):
            print("Error: source location is not a directory")
            continue

        destination_location = input("Enter the destination location: ")

        if not os.path.exists(destination_location):
            print("Error: destination location does not exists")
            continue
        
        if not os.path.isdir(destination_location):
            print("Error: destination location is not a directory")
            continue
            
        create_backup(source_location, destination_location)