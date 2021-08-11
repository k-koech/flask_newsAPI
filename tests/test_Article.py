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
        self.new_article= Article("kELVIN",'How to watch the Tokyo Olympics','After a year-long delay due to the global COVID-19 pandemic, the games of the XXXII Olympiad are scheduled to begin in Tokyo this week','https://s.yimg.com/os/creatr-uploaded-images/2021-06/65c97580-d43c-11eb-beff-966c1caa7050','www.newske.com','2021-12-11',"https://www.engadget.com/how-to-watch-the-tokyo-olympics-134504180.html")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))