import pytest
import subprocess
import time


@pytest.fixture(scope="session", autouse=True)
def launch_server():
    process = subprocess.Popen(["python3", "main.py"])
    time.sleep(1)

    yield

    process.terminate()
    process.wait()
