### Author: Kevin Bian, qiqikevin@outlook.com, Python 3.8.5
## My solution

Main idea behind the solution is to take what is similar to a greedy algorithm approach. We will loop over all the warehouses and fill as many products/items from the order as we can. 

From the FAQ, we are given the **additional constraint that one warehouse is cheaper than multiple.**

Therefore, whenever we encounter a warehouse that can join two previously seperated ones, we will pick it instead to fill the order.

1. Loop through warehouses
   1. Loop through items
      1. Update the order by taking as much of the item as possible from the current warehouse.
      2. We can either split up the order or join previously split orders (if the current warehouse can fill an entire item)
   2. Check if the current warehouse can fully fill the order (if so we are done)
2. Check if the order is complete and return the result if so

```
warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
order = {'apple': 1}
output = [{'owd': {'apple': 1}}]

allocateor = InventoryAllocator(order, warehouses)

# This will return the answer
solution = allocateor.getInventoryDistribution() 
```


## Testing

To run tests cd into the inventory-allocator/src folder. Then run

```
python3 InventoryAllocatorTest.py
```

Tests include
- Basic tests from question
- Matches, no matches, partial matches
- Orders that split and take multiple warehouses
- Orders that split that take the minimum warehouses since it is cheaper
- Warehouse that can fit the entire order should always be used
- Invalid quantities (for warehouse stock, order quantity, order items, etc.)
- Empty and impossible cases (order and warehouse)
- Minimum output and making sure cheapest list is produced
- And many more... (please see InventoryAllocatorTest.py comments)



## Problem

The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution). 

Your task is to implement a function that will to produce the cheapest shipment.

The first input will be an order: a map of items that are being ordered and how many of them are ordered. For example an order of apples, bananas and oranges of 5 units each will be 

`{ apple: 5, banana: 5, orange: 5 }`

The second input will be a list of object with warehouse name and inventory amounts (inventory distribution) for these items. For example, the inventory across two warehouses called owd and dm for apples, bananas and oranges could look like

`[ 
    {
    	name: owd,
    	inventory: { apple: 5, orange: 10 }
    }, 
    {
    	name: dm:,
    	inventory: { banana: 5, orange: 10 } 1
]`

You can assume that the list of warehouses is pre-sorted based on cost. The first warehouse will be less expensive to ship from than the second warehouse.

You can use any language of your choice to write the solution (internally we use Typescript/Javascript, Python, and some Java). Please write unit tests with your code, a few are mentioned below, but these are not comprehensive. Fork the repository and put your solution inside of the src directory and include a way to run your tests!

## Examples

### Order can be shipped using one warehouse

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[{ owd: { apple: 1 } }]`

### Order can be shipped using multiple warehouses

Input: `{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]`  
Output: `[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]`

### Order cannot be shipped because there is not enough inventory

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]`  
Output: `[]`

Input: `{ apple: 2 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[]`

## FAQs
**If an order can be completely shipped from one warehouse or shipped from multiple warehouses, which option is cheaper?**
  We can assume that shipping out of one warehouse is cheaper than shipping from multiple warehouses.

## What are we looking for

We'll evaluate your code via the following guidelines in no particular order:

1. **Readability**: naming, spacing, consistency
2. **Correctness**: is the solution correct and does it solve the problem
3. **Test Code Quality**: Is the test code comperehensive and covering all cases.
4. **Tool/Language mastery**: is the code using up to date syntax and techniques. 
