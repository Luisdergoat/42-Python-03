import sys


def main():
    print("=== Command Quest ===")

    program_name = sys.argv[0]

    arguments = sys.argv[1:]

    num_arguments = len(arguments)

    if num_arguments == 0:
        print("No arguments provided!")
    else:

        print(f"Arguments received: {num_arguments}")

        for i, arg in enumerate(arguments, 1):
            print(f"Argument {i}: {arg}")

    print(f"Program name: {program_name}")

    total = len(sys.argv)
    print(f"Total arguments: {total}")


main()
