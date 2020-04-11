import subprocess


def ListBranches():
    subprocess.call(["git", "branch"])


def Main():
    ListBranches()


if __name__ == "__main__":
    Main()
