import unittest
from app.models import Source

class   SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Surce class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source= Source("ABC",'Kenya News','SOURCE OF BREAKING NEWS','HTTPS//:WWW.ABC.COM','English',"Kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


