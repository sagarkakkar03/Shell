import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write('$ ')
        command = sys.stdin.readline().strip()
        if command == "exit":
            break
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
    pass



if __name__ == "__main__":
    main()
