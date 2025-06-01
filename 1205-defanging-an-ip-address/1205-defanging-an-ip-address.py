class Solution(object):
    def defangIPaddr(self, address):
        return  '[.]'.join(address.split('.'))