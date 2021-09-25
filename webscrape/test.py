from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class Test(unittest.TestCase):
    #bs = None
    def setUpClass():
        url = "https://www.careopinion.org.au/"
        Test.bs = BeautifulSoup(urlopen(url),'html.parser')
    
    def test_title(self):
        get_title = Test.bs.find('title').get_text()
        self.assertEqual('Care Opinion',get_title);

    def test_content(self):
        pagecontent = Test.bs.find('div',{'id':'container'})
        self.assertIsNotNone(pagecontent)



if __name__ == "__main__":
    unittest.main()