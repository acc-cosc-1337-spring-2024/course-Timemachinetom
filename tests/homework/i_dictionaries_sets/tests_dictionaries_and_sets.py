import unittest
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1
prog1 = set ({'Student1', 'Student2', 'Student3'})
prog2=  set ({'Student3', 'Student4', 'Student5'})
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


    def test_get_students_who_took_prog1_and_prog2(self):
        self.assertEqual ({'Student3'}, get_students_who_took_prog1_and_prog2(prog1, prog2))

    def test_get_students_who_took_prog1_or_prog2(self):
        self.assertEqual ({'Student1', 'Student2','Student3', 'Student4', 'Student5'}, get_students_who_took_prog1_or_prog2(prog1, prog2))

    def test_get_students_who_took_prog1_not_prog_2(self):
        self.assertEqual ({'Student1', 'Student2'}, get_students_who_took_prog1_not_prog_2(prog1, prog2))

    def test_get_students_who_took_prog2_not_prog_1(self):
        self.assertEqual ({'Student4', 'Student5'}, get_students_who_took_prog2_not_prog_1(prog1, prog2))