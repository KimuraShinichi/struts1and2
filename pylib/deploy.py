# deploy.py

from runner import Runner
from contextlib import contextmanager
import os
import platform
import psutil
import socket
import subprocess
import time

def is_tomcat_running_by_process():
    """
    プロセスベースでTomcatが実行中かどうかを判定します。

    :return: (Tomcatが実行中の場合はTrue、プロセスID), 否定は (False, None)
    """
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] == 'java.exe':
                cmdline = " ".join(proc.info['cmdline']).lower()
                if 'tomcat' in cmdline:
                    print(f"Detected Tomcat process: PID={proc.info['pid']}, Cmdline={cmdline}")
                    return True, proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, Exception) as e:
            print(f"Could not access process info: {e}")

    return False, None

def is_tomcat_running_by_port(host='localhost', port=8080):
    """
    ネットワークベースでTomcatが実行中かどうかを判定する。

    :param host: 接続先ホスト
    :param port: Tomcatのポート番号
    :return: Tomcatが実行中の場合はTrue、そうでない場合はFalse
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # 1秒のタイムアウトを設定
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, socket.gaierror):
            return False

def stop_tomcat(tomcat_path):
    """
    Tomcat を停止します。

    :param tomcat_path: Tomcatのホームディレクトリ
    """
    try:
        print("Stopping Tomcat...")
        if platform.system() == "Windows":
            stop_script = os.path.join(tomcat_path, "bin", "catalina.bat")
        else:
            stop_script = os.path.join(tomcat_path, "bin", "catalina.sh")
        subprocess.run([stop_script, "stop"], check=True)
        while is_tomcat_running_by_port():
            time.sleep(1)  # ポートが閉じるのを待つ
        print("Tomcat stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop Tomcat using script {stop_script}: {e}")
        raise

@contextmanager
def on_dir(tmp_current_dir, to_do):
    # 現在の作業ディレクトリを保存
    current_dir = os.getcwd()

    try:
        # 一時的に指定されたディレクトリに移動
        os.chdir(tmp_current_dir)
        print(f"---- on_dir: {tmp_current_dir}")
        # to_do を実行
        yield
    finally:
        # to_do の実行後、元のディレクトリに戻る
        os.chdir(current_dir)

def get_abspath_from_script_dir(relative_path):
    """
    このスクリプトファイルの親ディレクトリからの相対パスを絶対パスで返します。
    """
    script_path = os.path.realpath(__file__)
    parent_dir = os.path.dirname(script_path)
    absolute_path = os.path.abspath(os.path.join(parent_dir, relative_path))
    return absolute_path

def start_tomcat(tomcat_path):
    """
    Tomcat を起動します。

    :param tomcat_path: Tomcatのホームディレクトリ
    """
    try:
        print("Starting Tomcat...")
        if platform.system() == "Windows":
            startup_script = os.path.join(tomcat_path, "bin", "catalina.bat")
        else:
            startup_script = os.path.join(tomcat_path, "bin", "catalina.sh")
        with on_dir(get_abspath_from_script_dir('..'), subprocess.run([startup_script, "start"], check=True)):
            pass
        print("Tomcat started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Tomcat using script {startup_script}: {e}")
        raise

def deploy(runner, war_file):
    runner = Runner()
    try:
        # Tomcat ディレクトリを CATALINA_HOME に指定
        tomcat_home = get_abspath_from_script_dir('../tomcat/apache-tomcat-8.5.100')
        os.environ['CATALINA_HOME'] = tomcat_home

        # WAR ファイルが存在するか確認
        if not os.path.exists(war_file):
            raise FileNotFoundError(f"{war_file} not found.")

        # Tomcat デプロイメントディレクトリを指定
        tomcat_home_directory = f"{os.environ.get('CATALINA_HOME')}"
        tomcat_deploy_directory = os.path.join(tomcat_home_directory, "webapps")

        # デプロイメントディレクトリの存在を確認
        if not os.path.exists(tomcat_deploy_directory):
            raise FileNotFoundError(f"Tomcat deployment directory {tomcat_deploy_directory} does not exist.")

        # Tomcat が実行中かどうかを確認
        print("Checking if Tomcat is running...")
        running, pid = is_tomcat_running_by_process()
        if running or is_tomcat_running_by_port():
            stop_tomcat(tomcat_home_directory)

        # WAR ファイルを Tomcat の webapps ディレクトリにコピー
        try:
            runner.copy_recursive_preserve(war_file, tomcat_deploy_directory)
            print(f"Successfully copied {war_file} to {tomcat_deploy_directory}")
        except Exception as e:
            print(f"Failed to copy {war_file} to {tomcat_deploy_directory}: {e}")
            return

        # Tomcat を起動
        start_tomcat(tomcat_home_directory)
    
    except Exception as e:
        print(f"Error occurred during deployment: {e}")

if __name__ == "__main__":
    runner = Runner()
    war_file = "StrutsExample.war"
    deploy(runner, war_file)
