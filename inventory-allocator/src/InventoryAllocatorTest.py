import unittest

from InventoryAllocator import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):

    def test_basicOne(self):
        """
            Basic test from Github question
        """

        warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
        order = {'apple': 1}
        output = [{'owd': {'apple': 1}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_basicTwo(self):
        """
            Basic test from Github question
        """

        warehouses = [{'name': 'owd', 'inventory': {'apple': 5}},
                      {'name': 'dm', 'inventory': {'apple': 5}}]
        order = {'apple': 10}
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_basicThree(self):
        """
            Basic test from Github question
        """

        warehouses = [{'name': 'owd', 'inventory': {'apple': 0}}]
        order = {'apple': 1}
        output = []

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

        warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
        order = {'apple': 2}
        output = []

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_orderSplit(self):
        """
            Split order should take from multiple warehouses
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse2',
                      'inventory': {'product1': 5, 'product2': 2}},
                      {'name': 'warehouse3',
                      'inventory': {'product2': 2, 'product3': 5}}]
        order = {'product1': 7, 'product2': 4, 'product3': 4}
        output = [{'warehouse1': {'product1': 5}},
                  {'warehouse2': {'product1': 2, 'product2': 2}},
                  {'warehouse3': {'product2': 2, 'product3': 4}},]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_orderSplitMinimum(self):
        """
            Split order should take from multiple warehouses but 
            one warehouse is cheaper than multiple so it is minimum
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse2',
                      'inventory': {'product1': 5, 'product2': 2}},
                      {'name': 'warehouse3',
                      'inventory': {'product1': 5, 'product2': 2,
                      'product3': 5}}]
        order = {'product1': 5, 'product2': 2, 'product3': 4}
        output = [{'warehouse3': {'product1': 5, 'product2': 2,
                  'product3': 4}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_orderSplitMinimumTwo(self):
        """
            Split order should take from multiple warehouses but 
            one warehouse for product1 is cheaper than multiple for product1
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse2',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse3',
                      'inventory': {'product1': 10}},
                      {'name': 'warehouse4',
                      'inventory': {'product2': 2}}]
        order = {'product1': 10, 'product2': 1}
        output = [{'warehouse3': {'product1': 10}},
                  {'warehouse4': {'product2': 1}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_fullWarehouseOne(self):
        """
            Warehouse that can fullfill entire order with 1 product
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}}]
        order = {'product1': 5}
        output = [{'warehouse1': {'product1': 5}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_fullWarehouseTwo(self):
        """
            Warehouse that can fullfill entire order with 2 products
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5, 'product2': 6}}]
        order = {'product1': 5, 'product2': 6}
        output = [{'warehouse1': {'product1': 5, 'product2': 6}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_fullWarehouseThree(self):
        """
            Warehouse that can fullfill entire order with 2 products
            but one warehouse is cheaper than multiple.
            Full warehouse appears after partial warehouses
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse2',
                      'inventory': {'product2': 6}},
                      {'name': 'warehouse3',
                      'inventory': {'product1': 5, 'product2': 6}}]
        order = {'product1': 5, 'product2': 6}
        output = [{'warehouse3': {'product1': 5, 'product2': 6}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_fullWarehouseFour(self):
        """
            Warehouse that can fullfill entire order with 2 products
            but one warehouse is cheaper than multiple/
            Full warehouse appears before partial warehouses
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5, 'product2': 6}},
                      {'name': 'warehouse2',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse3',
                      'inventory': {'product2': 6}}]
        order = {'product1': 5, 'product2': 6}
        output = [{'warehouse1': {'product1': 5, 'product2': 6}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_invalidWarehouseQuantity(self):
        """
            Warehouse with 0 stock
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 0}},
                      {'name': 'warehouse2', 'inventory': {}}]
        order = {'product1': 5}
        output = []

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_invalidOrderQuantity(self):
        """
            Order with 0 stock
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}}]
        order = {'product1': 0}
        output = [{'warehouse1': {'product1': 0}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_emptyOrder(self):
        """
            No items in order
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}}]
        order = {}
        output = []

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_emptyWarehouse(self):
        """
            No items in warehouse
        """

        warehouses = []
        order = {'product1': 4}
        output = []

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_impossibleOrder(self):
        """
            Not enough inventory to fill order
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse2',
                      'inventory': {'product1': 5}}]
        order = {'product1': 5, 'product2': 5}
        output = []

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)

    def test_minimumOutput(self):
        """
            Should take closer warehouse if it can fill order
        """

        warehouses = [{'name': 'warehouse1',
                      'inventory': {'product1': 5}},
                      {'name': 'warehouse2',
                      'inventory': {'product1': 5}}]
        order = {'product1': 5}
        output = [{'warehouse1': {'product1': 5}}]

        allocateor = InventoryAllocator(order, warehouses)
        self.assertEqual(allocateor.getInventoryDistribution(), output)


if __name__ == '__main__':
    unittest.main()
