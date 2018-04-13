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

    def test_short_fn_doc(self):
        self.assertLessEqual(len(pythontrainer.short_fn_doc(print).splitlines()), 20)

    def test_list_objs_to_dict(self):
        self.assertIsInstance(pythontrainer.list_objs_to_dict([str, bool]), dict)

    def test_list_of_methods(self):
        str_methods = pythontrainer.list_of_methods(str)
        self.assertIsInstance(str_methods, list)
        self.assertIn(str.upper, str_methods)

def main():
    unittest.main(exit=False)

if __name__ == '__main__':
    main()
