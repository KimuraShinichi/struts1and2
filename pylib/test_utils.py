# test_utils.py
import os
import re
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class LogHandler(FileSystemEventHandler):
    def __init__(self, log_file_path, start_pos):
        self.log_file_path = log_file_path
        self.start_pos = start_pos

    def on_modified(self, event):
        if event.src_path == self.log_file_path:
            with open(self.log_file_path, 'r') as log_file:
                log_file.seek(self.start_pos)
                new_logs = log_file.read()
                if new_logs:
                    print("New log entries:\n", new_logs)

@pytest.fixture(scope="module")
def driver():
    """Create and return a Selenium WebDriver instance."""
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def get_log_file_path():
    """Return the path to the Tomcat log file."""
    return f"{os.environ.get('CATALINA_HOME')}/logs/catalina.out"

def perform_test(driver, url, assertion):
    """Perform a test by making a request and applying an assertion."""
    start_pos, observer = setup_log_monitor(get_log_file_path())
    try:
        assertion(driver, url)
    except Exception as e:
        print(f"Request to {url} failed: {e}")
        check_logs(get_log_file_path(), start_pos)
        check_logs(get_log_file_path(), start_pos, re_pattern='(^.*Exception:.*$|^.*Exception from.*$)')
        pytest.fail(f"Test failed due to exception: {e}")
    finally:
        observer.stop()
        observer.join()

def get_file_end_position(file_path):
    """ ファイルの末尾の位置（ファイルサイズ）を取得する。 """
    with open(file_path, 'rb') as file:
        file.seek(0, os.SEEK_END)  # ファイルの末尾に移動
        end_position = file.tell()  # 現在の位置を取得
    return end_position

def setup_log_monitor(log_file_path):
    """Setup a log file monitor."""
    start_pos = get_file_end_position(log_file_path)
    event_handler = LogHandler(log_file_path, start_pos)
    observer = Observer()
    observer.schedule(event_handler, path=log_file_path, recursive=False)
    observer.start()
    return start_pos, observer

def check_logs(log_file_path, start_pos, re_pattern='^(?!.*)'):
    """Check and print logs that match the given regular expression pattern.
       By default, no logs are printed if re_pattern is set to '^(?!.*)'."""
    with open(log_file_path, 'r') as log_file:
        log_file.seek(start_pos)
        error_logs = log_file.read()

    # Compile the regular expression pattern
    pattern = re.compile(re_pattern, re.MULTILINE)

    # Find all lines matching the pattern
    matching_lines = pattern.findall(error_logs)

    if matching_lines:
        print(f"Logs matching the pattern '{re_pattern}':\n", "\n".join(matching_lines))
    else:
        if re_pattern != '^(?!.*)':
            print("No logs matching the pattern were found.")
