import sys


def main():
    # Header ausgeben
    print("=== Command Quest ===")

    # Programmname ist immer das erste Element
    program_name = sys.argv[0]

    # Argumente sind alles NACH dem Programmnamen
    arguments = sys.argv[1:]

    # Anzahl der Argumente (ohne Programmname)
    num_arguments = len(arguments)

    # Fall 1: Keine Argumente übergeben
    if num_arguments == 0:
        print("No arguments provided!")
    else:
        # Fall 2: Argumente vorhanden
        print(f"Arguments received: {num_arguments}")

        # Zeige jedes Argument einzeln
        for i, arg in enumerate(arguments, 1):
            print(f"Argument {i}: {arg}")

    # Zeige Programmname
    print(f"Program name: {program_name}")

    # Total arguments = Programmname + alle Argumente
    total = len(sys.argv)
    print(f"Total arguments: {total}")


main()
