import subprocess
from pathlib import Path

def native2ascii(src, dest, opt="-encoding UTF8"):
    """
    native2ascii コマンドを実行する関数。
    
    :param src: 入力ファイルのパス (Path オブジェクト)
    :param dest: 出力ファイルのパス (Path オブジェクト)
    :param opt: native2ascii コマンドのオプション
    """
    # オプションを分割してリストに変換
    opt_list = opt.split()

    # コマンドをリストとして作成
    command = ["native2ascii", *opt_list, str(src), str(dest)]

    try:
        # コマンドを実行
        result = subprocess.run(command, check=True, text=True)
        print("Command executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print("native2ascii command not found. Please ensure it is installed and in your PATH.")

# 例の使用法
if __name__ == "__main__":
    src = Path("path/to/source/file")
    dest = Path("path/to/destination/file")

    # native2ascii 関数を呼び出し
    native2ascii(src, dest, opt="-encoding UTF8")
