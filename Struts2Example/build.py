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

def build(runner, build):
    runner.clear(f"{build}")
    runner.create_directory(f"{build}/WEB-INF")
    runner.create_directory(f"{build}/WEB-INF/classes")
    runner.create_directory(f"{build}/WEB-INF/lib")
    runner.create_directory(f"{build}/css")
    runner.copy_recursive_preserve("src/main/webapp/WEB-INF/web.xml", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/main/resources/struts.xml", f"{build}/WEB-INF/classes")
    runner.copy_recursive_preserve("src/main/resources/log4j2.xml", f"{build}/WEB-INF/classes")
    runner.copy_recursive_preserve("src/main/webapp/WEB-INF/jsp/", f"{build}/WEB-INF")
    runner.copy_recursive_preserve("src/main/webapp/css/*", f"{build}/css")
    runner.copy_recursive_preserve("src/main/webapp/index.jsp", f"{build}")
    runner.copy_recursive_preserve("src/main/webapp/*.jsp", f"{build}")
    #runner.copy_recursive_preserve("lib/lib-struts-6.1.1/*", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-beanutils-1.9.4.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-collections-3.2.2.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-digester-2.1.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-fileupload-1.4.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-lang3-3.10.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-logging-1.2.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/commons-text-1.10.0.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/freemarker-2.3.31.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/javassist-3.29.0-GA.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/ognl-3.3.4.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/struts2-config-browser-plugin-6.1.1.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/struts2-core-6.1.1.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/struts2-json-plugin-6.1.1.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-struts-6.1.1/xstream-1.4.19.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-log4j-2.20.0/log4j-api-2.20.0.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-log4j-2.20.0/log4j-core-2.20.0.jar", f"{build}/WEB-INF/lib")
    runner.copy_recursive_preserve("lib/lib-tomcat-8.5.100/*", f"{build}/WEB-INF/lib")
    for path in runner.list_relative_paths("src/main/java"):
        if path.name.endswith(".java"):
            # java ファイルの文字コードが UTF-8 で保存されていることを想定しています。
            runner.run(f"javac -encoding UTF-8 -d {build}/WEB-INF/classes -cp \"{build}/WEB-INF/lib/*\" {path}")
    runner.copy_recursive_preserve("src/main/resources/ApplicationResources.properties", f"{build}/WEB-INF/classes/com/example/web")
    native2ascii(Path(f"src/main/resources/ApplicationResources_ja_JP.UTF8"), Path(f"{build}/WEB-INF/classes/ApplicationResources_ja_JP.properties"), opt="-encoding UTF8")
    native2ascii(Path(f"src/main/resources/ApplicationResources_ja_JP.UTF8"), Path(f"{build}/WEB-INF/classes/ApplicationResources_ja.properties"), opt="-encoding UTF8")

    #runner.run(f"tree /F {build}")
    runner.run(f"tree {build}")
    runner.run(f"jar -cvf {build}.war -C {build} .")
    return f"{build}.war"

if __name__ == "__main__":
    try:
        runner = Runner()
        war_file = build(runner, "Struts2Example")
        deploy(runner, war_file)
    except Exception as e:
        print(f"Error occurred: {e}")
        #runner.run(f"pause")
    #runner.run(f"pause")
