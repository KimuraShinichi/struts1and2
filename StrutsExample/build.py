# build.py

from pathlib import Path
import sys

# 'pylib' フォルダへの絶対パスを指定
#pylib_dir = r"C:\kimura363\pylib"
pylib_dir = "../pylib"
sys.path.append(pylib_dir)

from runner import Runner
from deploy import deploy
from native2ascii import native2ascii

import pytest

def build(runner, build):
    runner.clear(build)
    runner.create_directory(f"{build}/WEB-INF")
    runner.create_directory(f"{build}/WEB-INF/classes")
    runner.create_directory(f"{build}/WEB-INF/lib")
    runner.create_directory(f"{build}/WEB-INF/dtds")
    runner.create_directory(f"{build}/css")
    runner.copy_recursive_preserve("src/WEB-INF/web.xml", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/WEB-INF/struts-config.xml", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/WEB-INF/validator-rules.xml", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/WEB-INF/validation.xml", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/WEB-INF/dtds/*", f"{build}/WEB-INF/dtds")
    runner.copy_recursive_preserve("src/WEB-INF/tld/*", f"{build}/WEB-INF/tld")
    runner.copy_recursive_preserve("src/jsp/*", f"{build}")
    runner.copy_recursive_preserve("src/css/*", f"{build}/css")
    runner.copy_recursive_preserve("lib/lib-struts-1.3.10/*", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-tomcat-8.5.100/*", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-log4j-1.2.17/*", f"{build}/WEB-INF/lib")
    for path in runner.list_relative_paths("src/java"):
        if path.name.endswith(".java"):
            # java ファイルの文字コードが UTF-8 で保存されていることを想定しています。
            runner.run(f"javac -encoding UTF-8 -d {build}/WEB-INF/classes -cp \"{build}/WEB-INF/lib/*\" {path}")
    runner.copy_recursive_preserve("src/resources/ApplicationResources.properties", f"{build}/WEB-INF/classes/com/example/web")
    native2ascii(Path(f"src/resources/ApplicationResources_ja.UTF8"), Path(f"{build}/WEB-INF/classes/com/example/web/ApplicationResources_ja.properties"), opt="-encoding UTF8")
    native2ascii(Path(f"src/resources/ApplicationResources_ja_JP.UTF8"), Path(f"{build}/WEB-INF/classes/com/example/web/ApplicationResources_ja_JP.properties"), opt="-encoding UTF8")
    runner.copy_recursive_preserve("src/resources/log4j.properties", f"{build}/WEB-INF/classes")

    #runner.run(f"tree /F {build}")
    runner.run(f"tree {build}")
    runner.run(f"jar -cvf {build}.war -C {build} .")
    return f"{build}.war"

if __name__ == "__main__":
    try:
        runner = Runner()
        war_file = build(runner, "StrutsExample")
        deploy(runner, war_file)
        pytest.main(["-s", "test/test_StrutsExample.py"])
    except Exception as e:
        print(f"Error occurred: {e}")
        #runner.run(f"pause")
