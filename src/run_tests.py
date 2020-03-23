import os, pathlib, sys
import pytest

os.chdir(pathlib.Path.cwd() / 'src/tests')

sys.exit(pytest.main())
