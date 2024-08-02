import os
import sys
import subprocess

def find_and_do(jar_dir, do_script, dest_dir):
    abs_jar_dir = os.path.abspath(jar_dir)
    abs_do_script = os.path.abspath(do_script)
    abs_dest_dir = os.path.abspath(dest_dir)

    for root, dirs, files in os.walk(abs_jar_dir):
        for file in files:
            if file.endswith(".jar"):
                jar_path = os.path.join(root, file)
                print(f'Executing {do_script} on {jar_path} with destination {abs_dest_dir}')
                subprocess.run([sys.executable, abs_do_script, jar_path, abs_dest_dir])

def main():
    # デフォルト値
    default_jar_dir = 'lib'
    default_do_script = '../pylib/extract_jar.py'
    default_dest_dir = '.lib-extracted'

    # 引数の数をチェック
    jar_dir = default_jar_dir
    do_script = default_do_script
    dest_dir = default_dest_dir

    if len(sys.argv) == 2:
        jar_dir = sys.argv[1]
    elif len(sys.argv) == 3:
        jar_dir = sys.argv[1]
        do_script = sys.argv[2]
    elif len(sys.argv) == 4:
        jar_dir = sys.argv[1]
        do_script = sys.argv[2]
        dest_dir = sys.argv[3]
    elif len(sys.argv) > 4:
        print(f'Usage: {sys.argv[0]} [<jar_dir> <do_script> <dest_dir>]')
        sys.exit(1)

    find_and_do(jar_dir, do_script, dest_dir)

if __name__ == "__main__":
    main()

