import sys
import argparse


def main():
    # sysargv_method()
    argparse_method()


def argparse_method():
    parser = argparse.ArgumentParser(descriotion="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()
    
    for _ in range(int(args.n)):
        print("meow")


def sysargv_method():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        for _ in range(int(sys.argv[2])):
            print("meow")
    else:
        print("usage: meows.py")


if __name__ == "__main__":
    main()