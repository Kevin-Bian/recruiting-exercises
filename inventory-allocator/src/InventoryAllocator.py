#!/usr/bin/python
from collections import OrderedDict

class InventoryAllocator:
    def __init__(self, order, warehouses):
        self.orderMap = order
        self.warehousesList = warehouses
        self.warehousesData = {}
        self.processWarehousesData()
        
    def processWarehousesData(self):
        for warehouse in self.warehousesList:
            warehouseName = warehouse["name"]
            warehouseInventory = warehouse["inventory"]
            self.warehousesData[warehouseName] = warehouseInventory
        
    def getInventoryDistributionList(self, inventoryDistribution):
        inventoryDistributionList = []
        for warehouse, inventory in inventoryDistribution.items():
            inventoryDistributionList.append({warehouse: inventory})
        print(inventoryDistributionList)
        return inventoryDistributionList
                
    def getInventoryDistribution(self):
        inventoryDistribution = {}
        
        for item, quantity in self.orderMap.items():
            currItemInventory = {}
            
            for warehouse in self.warehousesList:
                warehouseName = warehouse["name"]
                warehouseInventory = warehouse["inventory"]
                if item in warehouseInventory:
                    warehouseQuantity = warehouseInventory[item]
                    if warehouseQuantity > 0:
                      
                        if quantity > warehouseQuantity:
                            currItemInventory[warehouseName] = warehouseQuantity
                            quantity -= warehouseQuantity
                            self.warehousesData[warehouseName][item] = 0
                        else:
                            self.warehousesData[warehouseName][item] -= quantity  
                            currItemInventory[warehouseName] = quantity
                            quantity = 0
                            break

            if quantity == 0:
                for warehouse, quantity in currItemInventory.items():
                    if warehouse not in inventoryDistribution:
                        inventoryDistribution[warehouse] = {}
                    if quantity not in inventoryDistribution[warehouse]:
                        inventoryDistribution[warehouse][item] = 0
                    inventoryDistribution[warehouse][item] = quantity
            else:
                return []

        return self.getInventoryDistributionList(inventoryDistribution)
