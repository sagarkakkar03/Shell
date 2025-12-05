import sys
from enum import Enum

def parse_command(command: str) -> tuple[str, str]:
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
    TYPE = "type"

def command_type(cmd: str) -> str:
    for ctype in CommandType:
        if ctype.value == cmd:
            return ctype   
    return ctype.UNKNOWN

def handle_type(args: str):
    if args.strip() == "echo":
        sys.stdout.write("echo is a shell builtin" + "\n")
    elif args.strip() == "exit":
        sys.stdout.write("exit is a shell builtin" + "\n")
    elif args.strip() == "cat":
        sys.stdout.write("cat is a shell builtin" + "\n")
    elif args.strip() == "type":
        sys.stdout.write("type is a shell builtin" + "\n")
    else:
        sys.stdout.write(f"{args.strip()}: not found" + "\n")
    return

def handle_exit(args: str):
    sys.exit(0)

def handle_echo(args: str):
    sys.stdout.write(args + "\n")

def handle_unknown(args: str):
    sys.stdout.write(args + ": command not found" + "\n")

def handle_command(cmd: str, command_type: str, args: str):
    handler_name = f"handle_{command_type.value}"
    if handler_name == "handle_unknown":
        return handle_unknown(cmd)
    return globals()[handler_name](args)

def main():
    while True:
        sys.stdout.write('$ ')
        command = sys.stdin.readline()
        cmd, args = parse_command(command) 
        cmd_type = command_type(cmd)
        handle_command(cmd, cmd_type, args)
    pass




if __name__ == "__main__":
    main()
