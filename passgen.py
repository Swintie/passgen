from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def confirmation() -> bool:
    confirm = input("Do you want to continue? [Y/n]: ").lower()
    if confirm in ("yes", "y", ""):
        print("Press (Ctrl + C) to exit")
        return True
    else:
        return False


dictionaries = {
    "1": ascii_lowercase,
    "2": ascii_uppercase,
    "3": digits,
    "4": punctuation,
}


def select_dict() -> str:
    selection = input(
        f"Select a dictionary(es):\n"
        f"[1] {ascii_lowercase}\n"
        f"[2] {ascii_uppercase}\n"
        f"[3] {digits}\n"
        f"[4] {punctuation}\n"
        f"Your choice: "
    )
    return selection


def gen_ascii_pass() -> None:  # This generator isn't ideal but it's working at least
    try:
        length = int(input("Password length: "))
    except ValueError:
        print("You must enter an integer value")
        return
    work_dir = "".join(dictionaries[i] for i in select_dict() if i in dictionaries)
    if not work_dir:
        print("Dictionary is empty")
        return
    password = ""
    for i in range(length):
        password += choice(work_dir)
    print(password)


def gen_zeros(file_path) -> None:
    try:
        amount = int(input("Amount of zeros: "))
    except ValueError:
        print("You must enter an integer value!")
        return
    chunk = 100000000  # It takes around 100MB RAM per writing
    chunks_amount = amount // chunk
    zeros_left = amount % chunk
    if confirmation():
        with open(file_path, "w") as f:
            for i in range(chunks_amount):
                f.write("0" * chunk)
            f.write("0" * zeros_left)
            print("Success!")
    else:
        print("Aborting!")


def gen_numbers(file_path) -> None:
    try:
        a = int(input("Start range: "))
        b = int(input("End range: "))
        n = int(input("Total digits (width): "))
    except ValueError:
        print("You must enter an integer value!")
        return
    if confirmation():
        with open(file_path, "w") as f:
            for i in range(a, b + 1):
                f.write(str(i).zfill(n) + "\n")
            print("Success!")
    else:
        print("Aborting!")


if __name__ == "__main__":
    try:
        option = input(
            "Select an option\n[1] Fill file with zeros\n[2] Generate number passwords\n[3] Generate custom password\n: "
        )
        if option == "1":
            location = input("Location of the output file: ")
            gen_zeros(location)
        elif option == "2":
            location = input("Location of the output file: ")
            gen_numbers(location)
        elif option == "3":
            gen_ascii_pass()
        else:
            print("Incorrect option!!!")
    except KeyboardInterrupt:
        print("\nCancelled by user")
    except Exception as e:
        print(f"\n{e}")
