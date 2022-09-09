class solution:
    """A class used to covert a roman numeral to an integer
    """
    def romanToInt(self, s: str) -> int:
        
        """The method defined is used to iterate and perform the correct conversions
        to the passed Roman numeral

        Args:
            s (str): when calling the method, a string of Roman numeral is to be passed to the method 

        Returns:
            int: The method returns an integer as the conversion from roman numeral to integer as it is requred to do so.
        """
        
        # Convert all the strings passed to uppercase for correct indexing
        s = s.upper()
        
        # The conversion reference from roman to integer
        # keys represents the Roman string while values represent the coresponding integer value 
        numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        # Covert the roman string to a list 
        s_list = list(s)
        num = []
        conv = []
        for x in s:
            num.append(numerals[x])
        ind = 0
        while True:
            try:
                if num[ind] < num[ind+1]:
                    conv.append(num[ind+1] - num[ind])
                    num.pop(ind)
                    num.pop(ind)
                else:
                    ind+= 1
                    
            except IndexError:
                break
            
        integer = sum(conv + num)
        return integer
    
# create a solution instance
sol = solution()
sol.romanToInt("vii")