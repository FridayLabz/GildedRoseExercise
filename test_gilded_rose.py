# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_item_date_decreases_by_one(self):
        items = [Item('koko', 1, 0)]
        store = GildedRose(items)
        
        store.update_quality()
        
        self.assertEqual(0, store.items[0].sell_in)
    
    def test_item_quality_decreases_by_one(self):
        items = [Item('koko', 1, 1)]
        store = GildedRose(items)
        
        store.update_quality()
        
        self.assertEquals(0, store.items[0].quality)
    
    def test_item_quality_cant_be_negative(self):
        items = [Item('koko', 1, 0)]
        store = GildedRose(items)
        
        store.update_quality()
        
        self.assertTrue(store.items[0].quality >= 0)
        
    

class ItemTest(unittest.TestCase):
    def test_repr(self):
        item = Item('koko', 0, 0)
        
        expected_string = 'koko, 0, 0'
        actual_string = item.__repr__()
        self.assertEquals(expected_string, actual_string)

if __name__ == '__main__':
    unittest.main()
