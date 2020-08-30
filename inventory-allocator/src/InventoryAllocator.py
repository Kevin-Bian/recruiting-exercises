class InventoryAllocator:

    """
    Class for storing order and warehouse data and allocating inventory
    Author: Kevin Bian

    ...

    Attributes:
        order : object
            An object representing the order 
            ex. { apple: 1, banana: 2 }
        warehouses : list
            A list of warehouse objects with name and inventory
            ex. [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]

    Methods:
        getInventoryDistributionList(inventoryDistribution)
            Given inventory distribution dict returns the distribution as a list
        
        canFillEntireOrder(currWarehouseDistribution)
            Given distribution of current warehouse, determines if warehouse can fill
            the entire order
            
        isOrderComplete(currOrder)
            Given current order, check if it is complete
            
        getInventoryDistribution()
            Returns the cheapest shipment distribution
    """

    def __init__(self, order, warehouses):
        self.orderMap = order
        self.warehousesList = warehouses

    def getInventoryDistributionList(self, inventoryDistribution):
        """

        Returns inventory distribution list given inventoryDistribution dict

        Args:
            inventoryDistribution: dict of warehouse to map of products to get from warehouse

        Returns:
            A list of cheapest shipment
        """

        inventoryDistributionList = []
        for (warehouseName, itemMap) in inventoryDistribution.items():
            
            # Builds the list entry if an item is grabbed from warehouse
            if itemMap != {}:
                inventoryDistributionList.append({warehouseName: itemMap})
        return inventoryDistributionList

    def canFillEntireOrder(self, currWarehouseDistribution):
        """

        Checks if the entire order can be filled by a single warehouse

        Args:
            currWarehouseDistribution: product distribution of warehouse to check

        Returns:
            Boolean indicating if warehouse can fill entire order
        """

        for (item, quantity) in self.orderMap.items():
            if item not in currWarehouseDistribution:
                return False
            if quantity > currWarehouseDistribution[item]:
                return False
            else:
                
                # Set the distribution to quantity we need to prevent getting too much
                currWarehouseDistribution[item] = quantity
        return True

    def isOrderComplete(self, currOrder):
        """

        Checks if we are done with the order

        Args:
            currOrder: map of item to quantity representing currently filled order

        Returns:
            Boolean indicating if order is complete
        """

        for (item, quantity) in currOrder.items():

            # Checks if we still have products to get
            if quantity > 0:
                return False
        return True

    def getInventoryDistribution(self):
        """

        Returns the cheapest shipment object (called inventory distribution) 

        Returns:
            Dict of warehouse to map of products to get from the warehouse
        """

        inventoryDistribution = {}
        currOrder = dict(self.orderMap)

        for warehouse in self.warehousesList:
            currWarehouseItems = {}
            currWarehouseDistribution = {}
            currWarehouseName = warehouse['name']
            currWarehouseInventory = warehouse['inventory']

            if currWarehouseName not in inventoryDistribution:
                inventoryDistribution[currWarehouseName] = {}

            for (item, quantity) in self.orderMap.items():
                if item in currWarehouseInventory:

                    # Current warehouse can fill entire item
                    if currWarehouseInventory[item] >= self.orderMap[item]:

                        # From FAQ, for order, shipping from one warehouse is cheaper than multiple
                        # First we check how many times the item was split up in past warehouses
                        previousEncounters = 0
                        for (warehouse, itemTable) in inventoryDistribution.items():
                            if item in itemTable:
                                previousEncounters += 1

                        # If it was split up (more than one warehouse), delete from those entries since
                        # Shipping from one warehouse is cheapaer than multiple
                        if previousEncounters > 1:
                            for (warehouse, itemTable) in inventoryDistribution.items():
                                if item in itemTable:
                                    del inventoryDistribution[warehouse][item]
                                    if not inventoryDistribution[warehouse]:
                                        del inventoryDistribution[warehouse]
                        inventoryDistribution[currWarehouseName][item] = self.orderMap[item]
                        currWarehouseItems[item] = self.orderMap[item]
                        currOrder[item] = 0
                    else:

                        # Current warehouse can fill part of the item
                        # Grab whatever we can from current warehouse and update currOrder
                        if currOrder[item] > 0 and currWarehouseInventory[item] > 0:

                            # Ensure that we don't take too much of the product
                            inventoryDistribution[currWarehouseName][item] = min(currWarehouseInventory[item], currOrder[item])
                            currWarehouseItems[item] = currWarehouseInventory[item]
                            currOrder[item] -= currWarehouseInventory[item]
                    currWarehouseDistribution[item] = currWarehouseInventory[item]

            # Return the current warehouse distirbution if current warehouse can fill whole order
            if self.canFillEntireOrder(currWarehouseDistribution):
                if currWarehouseDistribution != {}:
                    return [{currWarehouseName: currWarehouseDistribution}]

        # Account for edge cases where order isn't complete
        if not self.isOrderComplete(currOrder):
            return []
        return self.getInventoryDistributionList(inventoryDistribution)
