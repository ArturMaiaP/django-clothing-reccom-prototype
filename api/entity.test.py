import unittest

from chatbot.entity import EntityExtractor

class TestEntityExtractor(unittest.TestCase):
    def setUp(self) -> None:
        self.ner = EntityExtractor()

    def test_pattern(self):
        patterns = [
            ["a_line", ["a-line", "a -line", "a- line", "a - line", "a line"]],
            ["dots", ["dot", "dots", "dotted"]],
            ["Floral", ["flower", "floral"]],
            ["Printed", ["print", "printed"]],
            ["Stripes", ["stripe", "stripes", "striped"]],
        ]
        for key, texts in patterns:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "pattern"]])
    def test_fabric(self):
        fabrics = [
            ["denim", ["denim"]],
            ["faux", ["faux"]],
            ["faux_leather", ["faux leather"]],
            ["knit", ["knit", "knitted"]],
            ["Lacy", ["lace", "lacy", "laced"]],
            ["leather", ["leather"]],
        ]
        for key, texts in fabrics:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "fabric"]])
    def test_size(self):
        sizes = [
            ["maxi", ["long", "longer"]],
            ["midi", ["mid"]],
            ["mini", ["mini"]],
        ]
        for key, texts in sizes:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "size"]])
    def test_format(self):
        formats = [
            ["pencil", ["pencil"]],
            ["Pleated", ["pleat", "pleated"]],
            ["skater", ["skater"]],
        ]
        for key, texts in formats:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "format"]])

if __name__ == '__main__':
    unittest.main()