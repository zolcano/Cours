from os.path import *
from datetime import datetime

def get_file_size(file_path):
    if os.path.isfile(file_path):
        return os.path.getsize(file_path)
    else:
        return None

def get_last_modified(file_path):
    if os.path.isfile(file_path):
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp)
    else:
        return None

def main():
    file1 = input("Entrez le chemin du premier fichier : ")
    file2 = input("Entrez le chemin du deuxième fichier : ")

    size1 = get_file_size(file1)
    size2 = get_file_size(file2)

    if size1 is not None:
        print(f"Taille de {file1}: {size1} octets")
    else:
        print(f"{file1} n'est pas un fichier existant.")

    if size2 is not None:
        print(f"Taille de {file2}: {size2} octets")
    else:
        print(f"{file2} n'est pas un fichier existant.")

    last_modified1 = get_last_modified(file1)
    last_modified2 = get_last_modified(file2)

    if last_modified1 and last_modified2:
        if last_modified1 > last_modified2:
            print(f"{file1} a été modifié plus récemment le {last_modified1}.")
        else:
            print(f"{file2} a été modifié plus récemment le {last_modified2}.")
    else:
        print("Impossible de déterminer le fichier le plus récent.")

if __name__ == "__main__":
    main()
