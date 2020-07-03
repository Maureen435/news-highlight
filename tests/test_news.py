import unittest
from app.models import Sources,Articles

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Sources('CNN','CNN News','Cable News Network that leads in providing news Worldwide','cnn.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Network that leads in providing news Worldwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new article = Articles('CNN','Memzo','The software World','A look at various software developers who have made the current technological world important and fruitful','mem.com','personal','Kenya','en')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'Memzo')
        self.assertEquals(self.new_source.title,'The software World')
        self.assertEquals(self.new_source.description,'A look at various software developers who have made the current technological world important and fruitful')
        self.assertEquals(self.new_source.url,'mem.com')
        self.assertEquals(self.new_source.category,'personal')
        self.assertEquals(self.new_source.country,'Kenya')
        self.assertEquals(self.new_source.language,'en')