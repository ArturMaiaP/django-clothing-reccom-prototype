import unittest

from api.chatbot.entity import EntityExtractor

class TestEntityExtractor(unittest.TestCase):
    def setUp(self) -> None:
        self.ner = EntityExtractor()

    def test_pattern(self):
        patterns = [
            ["animal_print", ["animal", "animal print", "animal-print"]],
            ["geometric", ["geometric", "argyle"]],
            ["camouflage", ["camouflage"]],
            ["checked", ["checked", "plaid"]],
            ["floral", ["flower", "floral"]],
            ["paisley", ["paisley"]],
            ["plain", ["plain"]],
            ["dots", ["dot", "dots", "dotted", "polka dots"]],
            ["striped", ["stripe", "stripes", "striped"]],
            ["tie_dyed", ["tie dyed", "tie-dyed", "tie-dye", "tie dye"]],
        ]
        for key, texts in patterns:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "pattern"]])
    def test_fabric(self):
        fabrics = [
            ["denim", ["denim", "jean", "jeans"]],
            ["knitted", ["knit", "knitted", "whool"]],
            ["laced", ["lace", "lacy", "laced", "jacquard"]],
            ["glossy", ["leather", "glossy", "faux leather"]],
            ["velvet", ["velvet", "plushy"]],
            ["general", ["cotton", "jersey", "silk", "satin"]],
        ]
        for key, texts in fabrics:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "fabric"]])
    def test_size(self):
        sizes = [
            ["maxi", ["long", "longer", "max", "maxi"]],
            ["midi", ["mid", "midi"]],
            ["mini", ["mini", "short"]],
        ]
        for key, texts in sizes:
            for text in texts:
                self.assertListEqual(self.ner.extract(text), [[key, "size"]])
    def test_type(self):
        types = [
            ["straight", ["pencil", "straight", "bubble", "tulip"]],
            ["pleated", ["pleat", "pleated", "pleats", "a-line", "a line", "yoke", "panel", "tiered", "gathered", "godet"]],
            ["skewed", ["skewed", "wrap", "hankerchief", "sarong", "assymetric"]],
        ]
        for key, texts in types:
            for text in texts:
                print("Test",text)
                self.assertListEqual(self.ner.extract(text), [[key, "type"]])

if __name__ == '__main__':
    unittest.main()