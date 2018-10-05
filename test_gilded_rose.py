# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        items = [Item('koko', 1, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

    def test_date_decreases_by_one(self):
        self.assertEqual(0, self.store.items[0].sell_in)

    def test_quality_decreases_by_one(self):
        self.assertEquals(0, self.store.items[0].quality)

    def test_quality_cant_be_negative(self):
        self.store.update_quality()

        self.assertTrue(self.store.items[0].quality >= 0)


class AgedBrieItem(unittest.TestCase):
    def test_quality_increases_by_one(self):
        items = [Item('Aged Brie', 1, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(2, self.store.items[0].quality)

    def test_quality_cannot_be_above_fifty(self):
        items = [Item('Aged Brie', 1, 50)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertTrue(self.store.items[0].quality <= 50)
    def test_aged_brie_less_than_zero_increases_by_one(self):
        items = [Item('Aged Brie', -1, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(2, self.store.items[0].quality)

class SulfurasItem(unittest.TestCase):
    def test_sell_in_is_constantly_eighty(self):
        items = [Item('Sulfuras, Hand of Ragnaros', 1, 80)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(80, self.store.items[0].quality)


class BackstagePassesItem(unittest.TestCase):
    def test_quality_inc_by_one_when_date_larger_than_ten(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 11, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(2, self.store.items[0].quality)


    def test_quality_does_not_exceed_50_when_date_larger_than_ten(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 11, 50)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertTrue(self.store.items[0].quality <= 50)


    def test_quality_inc_by_2_when_date_larger_than_five(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 6, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(3, self.store.items[0].quality)

    def test_quality_does_not_exceed_50_when_date_larger_than_five(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 6, 50)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertTrue(self.store.items[0].quality <= 50)

    def test_quality_inc_by_3_when_date_larger_than_zero(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 1, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(4, self.store.items[0].quality)

    def test_quality_does_not_exceed_50_when_date_larger_than_zero(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 1, 50)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertTrue(self.store.items[0].quality <= 50)

    def test_quality_is_zero_when_date_less_than_or_equals_zero(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 0, 1)]
        self.store = GildedRose(items)

        self.store.update_quality()

        self.assertEquals(0, self.store.items[0].quality)


class ItemTest(unittest.TestCase):
    def test_repr(self):
        item = Item('koko', 0, 0)

        expected_string = 'koko, 0, 0'
        actual_string = item.__repr__()
        self.assertEquals(expected_string, actual_string)

if __name__ == '__main__':
    unittest.main()
