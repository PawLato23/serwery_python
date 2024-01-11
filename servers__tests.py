import unittest
from servers import Product


class MyTestCase(unittest.TestCase):
    def test_something(self):
        #Class Product:

            #__init__
        # isalnum()
        with self.assertRaises(ValueError):
            Product("", 2137)
        with self.assertRaises(ValueError):
            Product("a 1", 12)
        with self.assertRaises(ValueError):
            Product("!a1", 12)
        with self.assertRaises(ValueError):
            Product("a1%", 12)
        # price to float lub int
        Product("a1", int(123))
        Product("a1", float(123.123))
        with self.assertRaises(ValueError):
            Product("a1", "a")
        # przynajmniej 1 cyfra i 1 litera
        with self.assertRaises(ValueError):
            Product("a", 12)
        with self.assertRaises(ValueError):
            Product("ba", 2137)
        with self.assertRaises(ValueError):
            Product("1", 123131314124)
        with self.assertRaises(ValueError):
            Product("12", 2137)
        # format xxx000
        Product("xxx000", 2137)        
        with self.assertRaises(ValueError):
            Product("1a", 2137)
        with self.assertRaises(ValueError):
            Product("a1a", 2137)
        with self.assertRaises(ValueError):
            Product("aaaa1234asdf", 2137)
        with self.assertRaises(ValueError):
            Product("1123aasd2141", 2137)
            
            #__hash__ test unikatowosci
        self.assertNotEqual(hash(Product("a1", 1)), hash(Product("A1", 1)))
        
        p1 = Product("aaa2137", 12)
        p2 = Product("aab2", 13)
        p3 = Product("aaa2137", 12)
        p4 = Product("aaa2137", 100)
        p5 = Product("Fus123", 100)
        p6 = Product("Fus123", 100)
        
        self.assertEqual(hash(p1), hash(p1))
        self.assertEqual(hash(p2), hash(p2))
        self.assertEqual(hash(p1), hash(p3))
        self.assertEqual(hash(p5), hash(p6))
        self.assertNotEqual(hash(p1), hash(p2))
        self.assertNotEqual(hash(p1), hash(p4))
        self.assertNotEqual(hash(p1), hash(p5))
        self.assertNotEqual(hash(p3), hash(p4))
        self.assertNotEqual(hash(p4), hash(p5))
            
            #__eq__
        self.assertNotEqual(Product("a1", 1), Product("A1", 1))
        
        self.assertEqual(p1, p3)
        self.assertEqual(p5, p6)
        self.assertEqual(p6, p6)
        self.assertEqual(p5, p5)
        self.assertNotEqual(p1, p2)
        self.assertNotEqual(p1, p4)
        self.assertNotEqual(p1, p5)
        self.assertNotEqual(p1, p6)
        self.assertNotEqual(p2, p1)
        self.assertNotEqual(p2, p3)
        self.assertNotEqual(p2, p4)
        self.assertNotEqual(p2, p5)


if __name__ == '__main__':
    unittest.main()
