import os, pathlib, sys
import pytest

os.chdir(pathlib.Path.cwd() / 'src/tests')
os.environ["mars"] = str(pathlib.Path.cwd()) + '/MARS/Mars4_5_mod.jar'

sys.exit(pytest.main())
