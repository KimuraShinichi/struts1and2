# カレントディレクトリ下に .lib-extracted として展開済の jar ファイルについて class 名とメソッド名パターンからメソッドシグネチャを抽出して一覧表示。
import os
import sys
import subprocess
import re

def find_class_file(class_name, lib_extracted):
    class_files = []
    for root, dirs, files in os.walk(lib_extracted):
        for file in files:
            if class_name in file:
                class_files.append(os.path.join(root, file))
    return class_files

def main(class_name, method_name_pattern, lib_extracted='.lib-extracted'):
    CFS_JAR = '../download/cfr-0.152.jar'  # Path to the CFR jar file

    # Find the class file
    class_files = find_class_file(class_name, lib_extracted)
    if not class_files:
        print(f'Class file for {class_name} not found.')
        return

    method_name_regex = re.compile(method_name_pattern)
    
    # Decompile and search for method signatures
    for class_file in class_files:
        result = subprocess.run(['java', '-jar', CFS_JAR, class_file], capture_output=True, text=True)
        if result.returncode != 0:
            print(f'Error decompiling {class_file}: {result.stderr}')
            continue

        # Search for the method signature
        for line in result.stdout.splitlines():
            if ' public ' in line and method_name_regex.search(line):
                print(line)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(f'Usage: {sys.argv[0]} <class_name> <method_name_pattern> [lib_extracted]')
        sys.exit(1)
    
    class_name = sys.argv[1]
    method_name_pattern = sys.argv[2]
    lib_extracted = sys.argv[3] if len(sys.argv) == 4 else '.lib-extracted'
    main(class_name, method_name_pattern, lib_extracted)

