import unittest
import pythontrainer

class TestCase(unittest.TestCase):
    """This is only a bunch of tests"""

    def test_list_builtins(self):
        """this is a test"""
        list_of_builtins = pythontrainer.list_builtins()
        self.assertIsInstance(list_of_builtins, list)
        self.assertIn('print', list_of_builtins)
        self.assertIn('max', list_of_builtins)
        self.assertNotIn('__name__', list_of_builtins)
        self.assertNotIn('Exception', list_of_builtins)

    def test_api_function(self):
        """test that api(obj) returns the public api of obj"""
        str_api = pythontrainer.api(str)
        self.assertIn('lower', str_api)
        self.assertNotIn('__class__', str_api)

    def test_create_obscured_doc(self):
        obscured_doc = pythontrainer.create_obscured_doc(print, 'print')
        self.assertIn('(value,', obscured_doc)
        self.assertNotIn('print', obscured_doc)

    def test_builtins_data(self):
        data = pythontrainer.BUILTINS_DATA
        self.assertIn('introspection', data)
        self.assertIn(type, data['introspection'])
        self.assertIn('types', data)



def main():
    unittest.main(exit=False)

if __name__ == '__main__':
    main()
