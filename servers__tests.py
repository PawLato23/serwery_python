import unittest
from servers import Product, ListServer, MapServer, Client, TooManyProductsFoundError


class Product_test(unittest.TestCase):
    def test_Product_init(self):
        with self.assertRaises(ValueError):
            Product("", 2137)
        with self.assertRaises(ValueError):
            Product("a 1", 12)
        with self.assertRaises(ValueError):
            Product("!a1", 12)
        with self.assertRaises(ValueError):
            Product("a1%", 12)
        with self.assertRaises(ValueError):
            Product("a1", "a")
        with self.assertRaises(ValueError):
            Product("a1", -2)
        with self.assertRaises(ValueError):
            Product("a", 12)
        with self.assertRaises(ValueError):
            Product("ba", 2137)
        with self.assertRaises(ValueError):
            Product("1", 123131314124)
        with self.assertRaises(ValueError):
            Product("12", 2137)
        with self.assertRaises(ValueError):
            Product("1a", 2137)
        with self.assertRaises(ValueError):
            Product("a1a", 2137)
        with self.assertRaises(ValueError):
            Product("aaaa1234asdf", 2137)
        with self.assertRaises(ValueError):
            Product("1123aasd2141", 2137)
        p1 = Product("aaa2137", 12)
        self.assertEqual(p1.get_name(), "aaa2137")
        a = p1.get_name() + "a"
        self.assertEqual(p1.get_name(), "aaa2137")
        self.assertEqual(p1.get_price(), 12)
        a = p1.get_price() + 100
        self.assertEqual(p1.get_price(), 12)
        self.assertEqual(p1.get(), ("aaa2137", 12))  # krotki są niemutowalne
        self.assertEqual(Product("a1", 0), ("a1",0))    
        
    def test_Product_hash_eq(self):
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

    def test_ListServer_init(self):
        prod_list = [Product("a1", 1), Product("b2", 2), Product("c3", 3)]

        sl1 = ListServer(prod_list)
        self.assertEqual(sl1.products, [Product("a1",1), Product("b2", 2), Product("c3",3)])
        with self.assertRaises(TypeError):
            ListServer(1)

    def test_ListServer_get_entries(self):
        prod_list1 = [Product("ab12", 1), Product("Bb231", 4), Product("CB33", 3), Product("ac1241", 4),
                      Product("GIjs12", 1)]
        prod_list2 = [Product("ab12", 1), Product("Bb231", 2), Product("CB33", 3), Product("ac124", 4),
                      Product("GI12", 1), Product("AI12", 5)]
        sl1 = ListServer(prod_list1)
        self.assertEqual(sl1.get_entries(2), [Product("ab12", 1), Product("CB33", 3), Product("Bb231", 4)])
        self.assertEqual(sl1.get_entries(3), [])
        self.assertEqual(sl1.get_entries(4), [Product("GIjs12", 1)])
        sl2 = ListServer(prod_list2)
        with self.assertRaises(TooManyProductsFoundError):
            res = sl2.get_entries(2)

    def test_MapServer_init(self):
        prod_list = [Product("a1", 1), Product("b2", 2), Product("c3", 3)]

        sm1 = MapServer(prod_list)
        self.assertDictEqual(sm1.products, {"a1": Product("a1", 1), "c3": Product("c3", 3), "b2": Product("b2", 2)})
        with self.assertRaises(TypeError):
            MapServer(1)

    def test_MapServer_get_entries(self):
        prod_list1 = [Product("ab12", 1), Product("Bb231", 4), Product("CB33", 3), Product("ac1241", 4),
                      Product("GIjs12", 1)]
        prod_list2 = [Product("ab12", 1), Product("Bb231", 2), Product("CB33", 3), Product("ac124", 4),
                      Product("GI12", 1), Product("AI12", 5)]
        sm1 = MapServer(prod_list1)
        self.assertEqual(sm1.get_entries(2), [Product("ab12", 1), Product("CB33", 3), Product("Bb231", 4)])
        self.assertEqual(sm1.get_entries(3), [])
        self.assertEqual(sm1.get_entries(4), [Product("GIjs12", 1)])
        sm2 = MapServer(prod_list2)
        with self.assertRaises(TooManyProductsFoundError):
            res = sm2.get_entries(2)

    def test_Client(self):
        prod_list1 = [Product("ab12", 1), Product("Bb231", 4), Product("CB33", 3), Product("ac1241", 4),
                      Product("GIjs12", 1)]
        prod_list2 = [Product("ab12", 1), Product("Bb231", 2), Product("CB33", 3), Product("ac124", 4),
                      Product("GI12", 1), Product("AI12", 5)]
        sl = ListServer(prod_list1)
        sm = MapServer(prod_list2)
        c1 = Client(sl)
        c2 = Client(sl)
        c3 = Client(sm)
        self.assertEqual(c1.get_total_price(2), 8)
        self.assertEqual(c2.get_total_price(2), 8)
        self.assertEqual(c2.get_total_price(3), None)
        self.assertEqual(c3.get_total_price(2), None)
        self.assertEqual(c3.get_total_price(4), None)
        
if __name__ == '__main__':
    unittest.main()

