import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write('$ ')
        command = sys.stdin.readline().strip()
        if command == "exit":
            break
        elif command[:4] == "echo":
            output = command[5:]
            sys.stdout.write(f"{output}\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
    pass



if __name__ == "__main__":
    main()
