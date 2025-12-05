import sys

def parse command(command: str) -> tuple[str, str]:
    command = command.strip()
    if not command:
        return ("", "")
    parts = command.split(" ", 1)
    if len(parts) == 1:
        return (parts[0], "")
    else:
        return (parts[0], parts[1])

class CommandType(Enum):
    EXIT = "exit"
    ECHO = "echo"
    CAT = "cat"
    UNKNOWN = "unknown"

def command_type(cmd: str) -> str:
    for ctype in CommandType:
        if ctype.value == cmd:
            reutrn ctype   
    return ctype.UNKNOWN

def handle_exit(args: str):
    sys.exit(0)

def handle_echo(args: str):
    sys.stdout.write(args + "\n")


def handle_command(command_type: str, args: str):
    handler_name = f"handle_{command_type.value}"
    return globals()[handler_name](args)

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write('$ ')
        command = sys.stdin.readline()
        cmd, args = parse command(command) 
        command_type = command_type(cmd)
        handle_command(command_type, args)
    pass




if __name__ == "__main__":
    main()
