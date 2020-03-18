import os, pathlib, sys
import pytest

os.chdir(pathlib.Path.cwd() / 'tests')

sys.exit(pytest.main())
