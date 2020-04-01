import unittest
from package import json


class MyTestCase(unittest.TestCase):
    def test_json1(self):
        res = {'glossary': {'title': 'exampleglossary', 'GlossDiv': {'title': 'S', 'GlossList': {
            'GlossEntry': {'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'StandardGeneralizedMarkupLanguage',
                           'Acronym': 'SGML', 'Abbrev': 'ISO8879:1986',
                           'GlossDef': {'para': 'Ameta-markuplanguage,usedtocreatemarkuplanguagessuchasDocBook.',
                                        'GlossSeeAlso': ['GML', 'XML']}, 'GlossSee': 'markup'}}}}}
        a = json.get_json(res)
        b = json.parse_json(a)[0]
        c = json.get_json(b)
        self.assertEqual(a, c)

    def test_json2(self):
        res = {'glossary': {'title': 'exampleglossary', 'GlossDiv': {'title': 'S', 'GlossList': {
            'GlossEntry': {'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'StandardGeneralizedMarkupLanguage',
                           'Acronym': 'SGML', 'Abbrev': 'ISO8879:1986',
                           'GlossDef': {'para': 'Ameta-markuplanguage,usedtocreatemarkuplanguagessuchasDocBook.',
                                        'GlossSeeAlso': ['GML', 'XML']}, 'GlossSee': 'markup'}}}}}
        a = json.get_json(res)
        b = json.parse_json(a)[0]
        self.assertEqual(res, b)


if __name__ == '__main__':
    unittest.main()
