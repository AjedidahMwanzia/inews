import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(123,'The Times News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at The times','https://www.thetimes.co.uk/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()