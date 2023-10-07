import argparse
import os


def replace_words_in_yaml(file_path: str, args: dict):
    print("Replacing words in yaml file. Path: ", file_path)

def replace_words_in_yml(file_path: str, args: dict):
    print("Replacing words in yml file. Path: ", file_path)

def replace_words_in_tf(file_path: str, args: dict):
    print("Replacing words in tf file. Path: ", file_path)
    with open(file_path, "r+") as file:
        for line in file:
            splited = line.split()
            for word in splited:
                word = word.lower()
                if word in args:
                    print("Replacing word: " + word + " with: " + args[word])
                    splited[2] = str(args[word])
                    line = line.replace(splited[2], args[word]) 
                    file.writelines(line) 
                    break


def replace(file_path: str, args: dict):
    if os.path.isfile(file_path):
        if file_path.endswith(".yaml"):
            replace_words_in_yaml(file_path, args)
        elif file_path.endswith(".yml"):
            replace_words_in_yml(file_path, args)
        elif file_path.endswith(".tf"):
            replace_words_in_tf(file_path, args)

    if os.path.isdir(file_path):
        for file in os.listdir(file_path):
            replace(file, args)

    else:
        print("File not found. (Path: " + file_path + "))")


def main():
    parser = argparse.ArgumentParser(
        prog="main",
        description="Replace words in a file with other words.",
        epilog="Simples epilog."
    )
    parser.add_argument(
        "--path", "-p",
        help="Path to file."
    )
    parser.add_argument(
        "--squad", "-s",
        help="New value to replace on Squad tag."
    )
    parser.add_argument(
        "--vs",
        help="New value to replace on VS tag."
    )
    parser.add_argument(
        "--product",
        help="New value to replace on Product tag."
    )
    parser.add_argument(
        "--env", "-e",
        help="New value to replace on Environment tag."
    )

    args = parser.parse_args()
    print(vars(args))
    if args.path:
        print("Path to file: " + args.path)
        replace(args.path, vars(args))
                
    else:
        print("No path to file.")

if __name__ == "__main__":
    main()