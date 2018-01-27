import pytest

def pytest_addoption(parser):
	parser.addoption("--file", action="store", default="./input.txt", help="--file [FILENAME]")

@pytest.fixture
def input_file(request):
	return request.config.getoption("--file")