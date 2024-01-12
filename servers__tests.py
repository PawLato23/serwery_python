import unittest
from servers import Product, ListServer, MapServer


class Product_test(unittest.TestCase):
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
        # price to float lub int >0
        Product("a1", int(123))
        Product("a1", float(123.123))
        with self.assertRaises(ValueError):
            Product("a1", "a")
        with self.assertRaises(ValueError):
            Product("a1", -2)
        with self.assertRaises(ValueError):
            Product("a1", 0)
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
            
            #get, get_name, get_price  - testy enkapsulacji
        self.assertEqual(p1.get_name(), "aaa2137")
        a = p1.get_name() + "a"
        self.assertEqual(p1.get_name(), "aaa2137")
        self.assertEqual(p1.get_price(), 12)
        a = p1.get_price() + 100
        self.assertEqual(p1.get_price(), 12)
        self.assertEqual(p1.get(), ("aaa2137", 12)) #krotki są niemutowalne
        
        #Server inherited classes:
        prod_list = [Product("a1",1), Product("b2", 2), Product("c3",3)]
        new_prod1 = Product("d4",4)
        new_prod2 = Product("e5",5)
        
        #CLASS listServer
            # __init__
        sl1 = ListServer(prod_list)
        sl2 = ListServer()
        self.assertEqual(sl1.LIST, [Product("a1",1), Product("b2", 2), Product("c3",3)])
        self.assertEqual(sl2.LIST, [])
        with self.assertRaises(TypeError):
            ListServer(1)
        with self.assertRaises(TypeError):
            ListServer([new_prod1, "aj"])
            
            # add
        sl1.add(new_prod1)
        sl2.add(new_prod1)
        self.assertEqual(sl1.LIST, [Product("a1",1), Product("b2", 2), Product("c3",3), new_prod1])
        self.assertEqual(sl2.LIST, [new_prod1])
        sl1.add(new_prod2)
        sl2.add(new_prod2)
        self.assertEqual(sl1.LIST, [Product("a1",1), Product("b2", 2), Product("c3",3), new_prod1, new_prod2])
        self.assertEqual(sl2.LIST, [new_prod1, new_prod2])
        with self.assertRaises(ValueError):
            sl1.add("aj")
                
        #CLASS MapServer
            # __init__
        sm1 = MapServer(prod_list)
        sm2 = MapServer()
        self.assertDictEqual(sm1.MAP, {"a1":Product("a1",1), "c3":Product("c3",3), "b2":Product("b2", 2)})
        self.assertDictEqual(sm2.MAP, dict({}))
        with self.assertRaises(TypeError):
            MapServer(1)
        with self.assertRaises(TypeError):
            MapServer([new_prod1, "aj"])
                
            # add
        sm1.add(new_prod1)
        sm2.add(new_prod1)
        self.assertDictEqual(sm1.MAP, {"a1":Product("a1",1), "c3":Product("c3",3), "b2":Product("b2", 2), new_prod1.get_name():new_prod1})
        self.assertDictEqual(sm2.MAP, dict({new_prod1.get_name():new_prod1}))
        sm1.add(new_prod2)
        sm2.add(new_prod2)
        self.assertDictEqual(sm1.MAP, {"a1":Product("a1",1), "c3":Product("c3",3), "b2":Product("b2", 2), new_prod1.get_name():new_prod1, new_prod2.get_name():new_prod2})
        self.assertDictEqual(sm2.MAP, dict({new_prod1.get_name():new_prod1, new_prod2.get_name():new_prod2}))
        with self.assertRaises(ValueError):
            sm1.add("aj")
            
        
if __name__ == '__main__':
    unittest.main()

