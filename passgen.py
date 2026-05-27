def confirmation():
    confirm = input("Do you want to continue? [Y/n]: ")
    if confirm == "y" or confirm == "Y":
        print("Press (Ctrl + C) to exit")
        return True
    else:
        return False


def gen_zeros(file_path) -> None:
    try:
        amount = int(input("Amount of zeros: "))
    except ValueError:
        print("You must enter integer number!")
        return
    if confirmation():
        with open(file_path, "w") as f:
            f.write("0" * amount)
            print("Success!")
    else:
        print("Aborting!")


def gen_numbers(file_path) -> None:
    try:
        a = int(input("Start count: "))
        b = int(input("End count: "))
        n = int(input("Amount of zeros: "))
    except ValueError:
        print("You must enter integer number!")
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
        location = input("Location of the output file: ")
        choice = input(
            "What do you want?\n[1] Fill file with zeros\n[2] Generate number passwords\n[1/2]: "
        )
        if choice == "1":
            gen_zeros(location)
        elif choice == "2":
            gen_numbers(location)
        else:
            print("Incorrect choice!!!")
    except KeyboardInterrupt:
        print("\nCancelled by user")
    except Exception as e:
        print(f"\n{e}")
        exit()
