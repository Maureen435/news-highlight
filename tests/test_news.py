import unittest
from app.models import Sources,Articles

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Sources('bbc-news','BBC News','Boris Johnson says the televised format will give the public direct engagement with decision-makers','http://www.bbc.co.uk-politics-53275395','general','U.K','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'bbc-news')
        self.assertEquals(self.new_source.name,'BBC News')
        self.assertEquals(self.new_source.description,'Boris Johnson says the televised format will give the public direct engagement with decision-makers')
        self.assertEquals(self.new_source.url,'http://www.bbc.co.uk-politics-53275395')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.K')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new article = Articles(self,id,author,title,description,url,category,country,language)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'id')
        self.assertEquals(self.new_source.name,'author')
        self.assertEquals(self.new_source.title,'title')
        self.assertEquals(self.new_source.description,'description')
        self.assertEquals(self.new_source.url,'url')
        self.assertEquals(self.new_source.category,'category')
        self.assertEquals(self.new_source.country,'country')
        self.assertEquals(self.new_source.language,'language')

if __name__ == '__main__':
    unittest.main()