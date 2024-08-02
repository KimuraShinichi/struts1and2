import os
import zipfile
import sys

def extract_jar(jar_path, dest_path):
    # 絶対パスを生成
    abs_jar_path = os.path.abspath(jar_path)
    abs_dest_path = os.path.abspath(dest_path)
    
    # JARファイル名を含む展開先ディレクトリを生成
    jar_dir_name = os.path.basename(jar_path) + ".extracted"
    extract_dir = os.path.join(abs_dest_path, jar_dir_name)
    os.makedirs(extract_dir, exist_ok=True)
    
    # JARファイルを展開
    with zipfile.ZipFile(abs_jar_path, 'r') as jar:
        jar.extractall(extract_dir)
        print(f'Extracted {jar_path} to {extract_dir}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <jar_path> <dest_path>')
        sys.exit(1)
    
    jar_path = sys.argv[1]
    dest_path = sys.argv[2]
    extract_jar(jar_path, dest_path)

