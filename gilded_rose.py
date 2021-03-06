# -*- coding: utf-8 -*-
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def isGeneralItem(self, item):
        return item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros"

    def updateBackstagePass(self, item):
    	item.quality += 1
        if item.sell_in < 11:
            item.quality = item.quality + 1
        if item.sell_in < 6:
	        item.quality = item.quality + 1

		item.quality = min(50, item.quality)

    def update_quality(self):
        for item in self.items:
            if self.isGeneralItem(item):
                if item.quality > 0:
                    item.quality -= 1
            else:
                if item.quality < 50:
                    if item.name == "Aged Brie" :
                        item.quality += 1
                    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                        self.updateBackstagePass(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
