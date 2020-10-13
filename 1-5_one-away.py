import unittest

def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    
    # replace edit check
    if len(string1) == len(string2):
        replaceFlag = False
        for i, c in enumerate(string1):
            if string2[i] != c:
                if not replaceFlag:        # consume replace edit
                    replaceFlag = True
                else:                      # replace edit already consumed
                    return False

        return True

    # add check
    if len(string1) < len(string2):
        addFlag = False
        i = 0  # string1 pointer
        j = 0  # string2 pointer
        
        while i < len(string1):
            if string1[i] != string2[j]: # mismatching char
                if not addFlag:          # consume our add edit
                    addFlag = True       
                else:                    # add edit already consumed
                    return False    
                j += 1                   # increment only longer string

            else:                        # same char, increment both pointers
                i += 1
                j += 1

        return True   

    # remove check
    if len(string1) > len(string2):
        replaceFlag = False
        i = 0  # string1 pointer
        j = 0  # string2 pointer

        while j < len(string2):
            if string1[i] != string2[j]: # mismatching char
                if not addFlag:          # consume our add edit
                    addFlag = True       
                else:                    # add edit already consumed
                    return False    
                i += 1                   # increment only longer string

            else:                        # same char, increment both pointers
                i += 1
                j += 1

        return True  


class TestMethods(unittest.TestCase):
    def test_same_string(self):
        self.assertTrue(one_away('place', 'place'))

    def test_add_char(self):
        self.assertTrue(one_away('place', 'places'))

    def test_remove_char(self):
        self.assertTrue(one_away('places', 'place'))

    def test_replace_char(self):
        self.assertTrue(one_away('plade', 'plaze'))

    def test_multireplace_same_char(self):
        self.assertFalse(one_away('aaab', 'cccb'))
    
    def test_multireplace_diff_char(self):
        self.assertFalse(one_away('acs', 'ztp'))

    def test_two_edit(self):
        self.assertFalse(one_away('baa', 'baass'))

    def test_add_and_replace(self):
        self.assertFalse(one_away('bass', 'passt'))

    def test_add_and_remove(self):
        self.assertFalse(one_away('bassp', 'asspt'))

if __name__ == '__main__':
    unittest.main()
