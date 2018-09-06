import unittest
from app.models import Source,Articles


class ArticlesTest(unittest.TestCase):

    def setUp(self):

        self.newArticles = Articles('Man of the Year', 'Forbes','Kwesi Makonnen graces cover of Forbes Man of the Year award','https:// forbes.com/kwesi-ras', 'www.forbes.com/kwesiM.png', '1/11/2027')

    def test_article(self):

        self.assertTrue(isinstance(self.newArticles,Articles))