"""Top-level package for monte_carlo."""

from . bitstring import BitString

# import math
# import numpy as np

# class BitString:
#     """
#     Simple class to implement a config of bits
#     """
#     def __init__(self, N):
#         """
#         Initialize a BitString with N bits.
        
#         Parameters
#         ----------
#         N : int
#             Number of bits in the BitString
#         """
#         self.N = N
#         self.config = np.zeros(N, dtype=int) 

#     def __repr__(self):
#         """Return string representation of the BitString as a sequence of 0s and 1s."""
#         out = ""
#         for i in self.config:
#             out += str(i)
#         return out

#     def __eq__(self, other):
#         """Check equality of two BitStrings."""
#         return all(self.config == other.config)
    
#     def __len__(self):
#         """Return the number of bits in the BitString."""
#         return len(self.config)

#     def on(self):
#         """Return the count of bits that are on (1)."""
#         return np.sum(self.config)
    
#     def off(self):
#         """Return the count of bits that are off (0)."""
#         return len(self)-self.on()
    
#     def flip_site(self,i):
#         """
#         Flip the bit at site i
        
#         Parameters
#         ----------
#         i : int
#             Index of the bit to flip
#         """
#         try:
#             self.config[i] = (self.config[i] + 1) % 2  
#         except ValueError:
#             print("problem with i", i)
    
#     def int(self):
#         """
#         Return the integer corresponding to BitString
        
#         Returns
#         -------
#         int
#             Decimal integer representation of the binary BitString
#         """
#         out = 0
#         for idx, i in enumerate(reversed(self.config)):
#             if i==1:
#                 out += 2**idx
#                 # print(i, idx, i*(2**idx), out)
#         return out
 

#     def set_config(self, s:list[int]):
#         """
#         Set the configuration of the BitString.
        
#         Parameters
#         ----------
#         s : list[int]
#             List of bits (must match length N)
            
#         Raises
#         ------
#         ValueError
#             If the provided config has wrong size
#         """
#         try:
#             assert(len(s) == self.N)
#         except:
#             raise ValueError("provided config wrong size: ", len(s), " ", self.N)

#         self.config = s
#         return
        
#     def set_int_config(self, dec:int):
#         """
#         Convert a decimal integer to binary and set as configuration.
    
#         Parameters
#         ----------
#         dec : int
#             Input integer to convert to binary
            
#         Raises
#         ------
#         ValueError
#             If the integer requires more bits than N
#         """
#         digits_needed = math.ceil(math.log(dec+1,2))
#         try:
#             assert(self.N >= digits_needed)
#         except:
#             raise ValueError("not enough digits!")
            
#         config = np.array([0 for i in range(self.N)])
#         # bs = Bitconfig(digits)
    
#         # for i in range(digits_needed):
#         tmp = dec*1
#         for i in reversed(range(self.N-digits_needed, self.N)):
#             # print(tmp%2)
#             config[i] = tmp%2
#             tmp = tmp//2
#         self.set_config(config)
#         return 
