import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
import unittest
from scripts.features.reader import Reader


class TestReader(unittest.TestCase):

    def test_file_iterator(self):
        reader = Reader()
        for p in reader.post_iterator():
            print(p.title)


if __name__ == "__main__":
    unittest.main()
