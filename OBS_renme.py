import os
import time

def get_latest_file(directory):
    files = os.listdir(directory)
    if not files:
        return None
    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(directory, f)))
    return latest_file

def rename_new_file(directory, file_name):
    latest_file = get_latest_file(directory)
    if not latest_file:
        print("Нет файлов для переименования.")
        return
    
    file_path = os.path.join(directory, latest_file)
    file_extension = os.path.splitext(latest_file)[1]
    new_file_path = os.path.join(directory, file_name + file_extension)

    try:
        os.rename(file_path, new_file_path)
        print(f"Файл {latest_file} переименован в {file_name + file_extension}")
    except FileExistsError as e:
        print(f"Ошибка при переименовании {latest_file}: {e}")

directory = r"C:\Users\liza\Videos\dev_rename_OBS"
file_name = "new_video2"

rename_new_file(directory, file_name)
