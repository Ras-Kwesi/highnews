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




