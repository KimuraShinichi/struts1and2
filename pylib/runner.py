#Part-1
import os
import shutil
import subprocess
from pathlib import Path
import glob

class Runner():
    def __init__(self):
        self.counter = 0

    def __run_system_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            return result.stdout, result.stderr, result.returncode
        except subprocess.CalledProcessError as e:
            raise subprocess.CalledProcessError(returncode=e.returncode, cmd=e.cmd, output=e.stdout, stderr=e.stderr)

    def __prompt(self, command):
        self.counter += 1
        print(f"{self.counter}> {command}")

    def run(self, command):
        self.__prompt(command)
        try:
            stdout, stderr, returncode = self.__run_system_command(command)
            if stderr:
                print(f"標準エラー:\n{stderr}")
            if stdout:
                print(f"標準出力:\n{stdout}")
            return returncode
        except subprocess.CalledProcessError as e:
            print(f"コマンドの終了ステータス: {e.returncode} - コマンドの実行に失敗しました:\n {e.cmd}")
            if e.output:
                print(f"標準出力:\n{e.output}")
            if e.stderr:
                print(f"標準エラー:\n{e.stderr}")
            raise

    def create_directory(self, path):
        command = f"mkdir -p {path}"
        self.__prompt(command)
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            print(f"Error: {e} - {command}")

    def clear(self, path):
        """
        指定されたディレクトリとその内容をすべて削除します.

        :param path: 削除するディレクトリのパス
        """
        command = f"rm -rf {path}"
        self.__prompt(command)
        try:
            shutil.rmtree(path)
        except OSError as e:
            print(f"Error: {e} - Failed to delete {path}")

    def __copy_preserve_timestamps(self, src, dst):
        """
        指定されたパスのファイルまたはディレクトリをdstディレクトリへコピーします。
        ファイルの更新日時を保持します.

        :param src: コピーするファイルまたはディレクトリのソースパス
        :param dst: コピー先のディレクトリパスまたはファイルパス
        """
        src_path = Path(src)
        dst_path = Path(dst)

        if src_path.is_file():
            if dst_path.is_dir():
                shutil.copy2(src_path, dst_path / src_path.name)
            else:
                shutil.copy2(src_path, dst_path)
        elif src_path.is_dir():
            if dst_path.is_dir():
                shutil.copytree(src_path, dst_path / src_path.name, copy_function=shutil.copy2)
            else:
                raise ValueError(f"Destination {dst} is not a directory.")
        else:
            raise ValueError(f"Source {src} is neither a file nor a directory.")

# Part-2
    def __concatenate_args(self, *args):
        """
        可変引数 args を空白文字で区切って連結した文字列を返します.

        :param args: 可変長の引数
        :return: 連結された文字列
        """
        return " ".join(args)

    def copy_recursive_preserve(self, *args):
        """
        Linux の cp -pr コマンドと同様に処理します。
        最後の引数はコピー先のディレクトリまたはファイルパスとなります.
        :param args: コマンドライン引数のように、ソースパスとディスティネーションパスのリスト
        """

        command = f"cp -pr {self.__concatenate_args(*args)}"
        self.__prompt(command)
        if len(args) < 2:
            raise ValueError("At least two arguments are required: source(s) and destination.")

        dst = Path(args[-1])
        src_patterns = args[:-1]

        expanded_sources = []
        for pattern in src_patterns:
            expanded_sources.extend(glob.glob(pattern))

        if not dst.exists():
            os.makedirs(dst)

        for src in expanded_sources:
            src_path = Path(src)
            if not src_path.exists():
                raise FileNotFoundError(f"Source path {src} does not exist.")
            self.__copy_preserve_timestamps(src_path, dst)

    def list_relative_paths(self, directory):
        """
        指定されたディレクトリ以下の全てのファイルを列挙し、指定されたディレクトリパスから始まる相対パスを返します。

        :param directory: 探索する基点ディレクトリ
        :return: ファイルの相対パスのリスト
        """
        base_path = Path(directory)
        relative_paths = []

        for path in base_path.rglob('*'):
            if path.is_file():
                relative_paths.append(path.relative_to("."))

        return relative_paths

# サンプル使用法
if __name__ == "__main__":
    runner = Runner()
    runner.run("dir")

    # src/java下のすべての .java ファイルの相対パスを出力
    for path in runner.list_relative_paths("src/java"):
        if path.name.endswith(".java"):
            print(path)

    # 仮のビルドディレクトリパス
    build = "build_directory"

    # ビルドディレクトリを作成
    runner.create_directory(build)

    # src/main/webapps/index.jsp を ビルドディレクトリにコピー
    runner.copy_recursive_preserve("src/main/webapp/index.jsp", f"{build}")
