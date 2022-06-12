import unittest
import example

class Test_Example_File(unittest.TestCase):

    def test_Suman_1(self):
        self.assertEqual(example.Suman(10,20), 30)


    def test_Suman_2(self):
        self.assertEqual(example.Suman(20, 20), 50)

    def test_Suman_Cube_1(self):
        self.assertGreater(example.Suman_Cube(3), 20)



if __name__ == '__main__':
    unittest.main()
