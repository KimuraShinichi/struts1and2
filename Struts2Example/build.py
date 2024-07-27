# build.py

from pathlib import Path
import sys

# 'pylib' フォルダへの絶対パスを指定
pylib_dir = r"C:\kimura363\pylib"
sys.path.append(pylib_dir)

from runner import Runner
from deploy import deploy
from native2ascii import native2ascii

def build(runner, build):
    runner.clear(f"{build}")
    runner.create_directory(f"{build}/WEB-INF")
    runner.create_directory(f"{build}/WEB-INF/classes")
    runner.create_directory(f"{build}/WEB-INF/lib")
    runner.create_directory(f"{build}/css")
    runner.copy_recursive_preserve("src/main/webapp/WEB-INF/web.xml", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/main/resources/struts.xml", f"{build}/WEB-INF/classes")
    runner.copy_recursive_preserve("src/main/resources/log4j2.xml", f"{build}/WEB-INF/classes")
    runner.copy_recursive_preserve("src/main/webapp/WEB-INF/jsp/*", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/main/webapp/css/*", f"{build}/css")
    runner.copy_recursive_preserve("src/main/webapp/index.jsp", f"{build}")
    runner.copy_recursive_preserve("src/main/webapp/*.jsp", f"{build}")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/*", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-tomcat-8.5.100/*", f"{build}/WEB-INF/lib")
    for path in runner.list_relative_paths("src/main/java"):
        if path.name.endswith(".java"):
            # java ファイルの文字コードが UTF-8 で保存されていることを想定しています。
            runner.run(f"javac -encoding UTF-8 -d {build}/WEB-INF/classes -cp {build}/WEB-INF/lib/* {path}")
    runner.copy_recursive_preserve("src/main/resources/ApplicationResources.properties", f"{build}/WEB-INF/classes/com/example/web")
    native2ascii(Path(f"src/main/resources/ApplicationResources_ja_JP.UTF8"), Path(f"{build}/WEB-INF/classes/ApplicationResources_ja_JP.properties"), opt="-encoding UTF8")
    native2ascii(Path(f"src/main/resources/ApplicationResources_ja_JP.UTF8"), Path(f"{build}/WEB-INF/classes/ApplicationResources_ja.properties"), opt="-encoding UTF8")

    runner.run(f"tree /F {build}")
    runner.run(f"jar -cvf {build}.war -C {build} .")
    return f"{build}.war"

if __name__ == "__main__":
    try:
        runner = Runner()
        war_file = build(runner, "Struts2Example")
        deploy(runner, war_file)
    except Exception as e:
        print(f"Error occurred: {e}")
        runner.run(f"pause")
    runner.run(f"pause")
