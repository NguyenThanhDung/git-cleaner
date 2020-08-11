import subprocess
import sys


def list_branches():
    # subprocess.call(["git", "branch"])
    command = ["git", "branch"]
    p = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.stderr:
        print("error:", p.stderr, file=sys.stderr)
    else:
        branches = p.stdout.split()
        branches.remove(b"*")
        for branch in branches:
            print(branch)


def main():
    list_branches()


if __name__ == "__main__":
    main()
