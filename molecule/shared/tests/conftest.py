import os
import pytest

@pytest.fixture
def scenario():
    implementation = "{}_pyenv_root".format(os.environ['TEST_CASE'])
    return pytest.importorskip(implementation)