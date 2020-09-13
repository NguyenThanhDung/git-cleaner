from subprocess import Popen, PIPE


def list_branches():
    command = ["git", "branch"]
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        print("error:", stderr)
    else:
        branches = stdout.split()
        branches.remove(b"*")
        for branch in branches:
            print(branch)


def main():
    list_branches()


if __name__ == "__main__":
    main()
