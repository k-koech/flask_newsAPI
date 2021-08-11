import unittest
from app.models import Article

class   ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article= Article("ABC",'Kenya News','SOURCE OF BREAKING NEWS','HTTPS//:WWW.ABC.COM','English',"Kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))