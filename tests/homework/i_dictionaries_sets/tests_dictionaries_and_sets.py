import unittest
#from src.homework.i_dictionaries_sets import get_p_distance

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        inventory_dictionary = {}
        inventory_dictionary['Widget1'] = 10
        self.assertEqual (inventory_dictionary['Widget1'], 10)
        inventory_dictionary['Widget1'] += 25
        self.assertEqual (inventory_dictionary['Widget1'], 35)
        inventory_dictionary['Widget1'] += -10
        self.assertEqual (inventory_dictionary['Widget1'], 25)
    
    def remove_inventory_widget(self):
        inventory_dictionary = {}
        inventory_dictionary['widget1'] = 10
        inventory_dictionary['widget2'] = 25
        del inventory_dictionary['widget1']
        length = len(inventory_dictionary)
        self.assertEqual (length, 1)