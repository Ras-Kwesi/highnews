import unittest
from app.models import Source,Articles

class SourcesTest(unittest.TestCase):
    '''
    Thest to see whether the  Class of Movie
    Can instantiate an object
    '''
    def setUp(self):
         '''
         Seting up an instance that can be ran as test for object
         '''

         self.newSources = Source('BBC','https//; bbc-news.com/123',"Sports","english",'USA',"Ronaldo scores HatTrick in Derby")

    def test_source(self):
         '''
         Test to see if our test objects would recognizable in the app
         '''

         self.assertTrue(isinstance(self.newSources,Source))



class ArticlesTest(unittest.TestCase):

    def setUp(self):

        self.newArticles = Articles('Man of the Year', 'Forbes','Kwesi Makonnen graces cover of Forbes Man of the Year award','https:// forbes.com/kwesi-ras', 'www.forbes.com/kwesiM.png', '1/11/2027')

    def test_article(self):

        self.assertTrue(isinstance(self.newArticles,Articles))
