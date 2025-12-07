import subprocess, os, sys, shutil
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
    External = "external"
    PWD = "pwd"
    CHANGE_DIRECTORY = "cd"

def command_type(cmd: str) -> str:
    for ctype in CommandType:
        if ctype.value == cmd:
            return ctype   
    return ctype.UNKNOWN

def handle_type(args: str):
    path = shutil.which(args.strip())
    if args.strip() == "echo":
        sys.stdout.write("echo is a shell builtin" + "\n")
    elif args.strip() == "exit":
        sys.stdout.write("exit is a shell builtin" + "\n")
    elif args.strip() == "type":
        sys.stdout.write("type is a shell builtin" + "\n")
    elif args.strip() == "pwd":
        sys.stdout.write("pwd is a shell builtin" + "\n")
    elif path:
        sys.stdout.write(f"{args.strip()} is {path}" + "\n")
    else:
        sys.stdout.write(f"{args.strip()}: not found" + "\n")
    return

def handle_pwd(args: str):
    current_path = os.getcwd()
    sys.stdout.write(current_path + "\n")

def handle_external(cmd: str, args: str):
    program_length = len(args.split()) + 1
    path = shutil.which(cmd)
    subprocess.run([cmd, *args.split()], executable=path)
    return path

def handle_cd(args: str):
    path = args.strip()
    try:
        os.chdir(path)
    except FileNotFoundError:
        sys.stdout.write(f"cd: {path}: No such file or directory" + "\n")
    

def handle_exit(args: str):
    sys.exit(0)

def handle_echo(args: str):
    sys.stdout.write(args + "\n")

def handle_unknown(args: str):
    sys.stdout.write(args + ": command not found" + "\n")

def handle_command(cmd: str, command_type: str, args: str):
    handler_name = f"handle_{command_type.value}"
    if handler_name == "handle_unknown":
        path = shutil.which(cmd)
        if not path:
            return handle_unknown(cmd)
        handle_external(cmd, args)
    else:    
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
