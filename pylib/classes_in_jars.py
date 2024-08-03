# カレントディレクトリ直下の .lib-extracted フォルダ内に展開済の jar ファイル内容を一覧表示。

import os

def find_and_transform(lib_extracted):
    result = []
    for root, dirs, files in os.walk(lib_extracted):
        for file in files:
            file_path = os.path.join(root, file)
            transformed_path = file_path.replace(lib_extracted + '/', '', 1).replace('.extracted/', '\t')
            result.append(transformed_path)
    return result

def main(lib_extracted):
    transformed_paths = find_and_transform(lib_extracted)
    for path in transformed_paths:
        print(path)

if __name__ == "__main__":
    lib_extract = '.lib-extracted'  # Replace with your directory if needed
    main(lib_extract)

