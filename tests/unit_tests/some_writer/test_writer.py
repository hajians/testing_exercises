import os
import shutil
import tempfile
import unittest


class TestWriter(unittest.TestCase):
    def setUp(self) -> None:
        # This method is called before the tests are run.
        self.tmp_dirname = "writer"
        self.tmp_dirpath = tempfile.mkdtemp(self.tmp_dirname)

    def tearDown(self) -> None:
        # This method is called after the tests are run.
        shutil.rmtree(self.tmp_dirpath)

    def test_writer(self):
        # Check if the temporary folder is created.
        assert os.path.exists(self.tmp_dirpath)
