class Allergies(object):
    def __init__(self, code):
        decoderDic = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatose',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats' 
        }

        allergyList = []

        shift = 1

        while shift <= 128:
            if (shift & code != 0):
                allergyList.append(decoderDic[shift])
            shift = shift << 1
            
        
        self.lst = allergyList

    def is_allergic_to(self,member): 
        return True if member in self.lst else False

