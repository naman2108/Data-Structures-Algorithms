class Solution:
    def ipv4(self, queryIP):
        s = queryIP.split('.')
        if len(s) != 4:
            return False
        for i in s:
            if not i.isdigit():
                return False
            if int(i) < 0 or int(i) > 255:
                return False
            if len(i) > 1 and i[0] == '0':
                return False
        return True

    def ipv6(self, queryIP):
        s = queryIP.split(':')
        if len(s) != 8:
            return False
        validchar = set('0123456789abcdefABCDEF')
        for i in s:
            
            if not i or len(i) > 4:
                return False
            for c in i:
                if c not in validchar:
                    return False    
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.ipv4(queryIP):
            return 'IPv4'
        elif self.ipv6(queryIP):
            return 'IPv6'
        
        return 'Neither'
    



        