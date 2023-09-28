class Solution:
    def ipv4(self, s):
        s = s.split('.')
        if len(s) != 4:
            return False
        for i in s:
            if not i.isdigit():
                return False
            if not 0 <= int(i) <= 255:
                return False
            if len(i) > 1 and i[0] == '0':
                return False
        return True

    def ipv6(self, s):
        s = s.split(':')
        if len(s) != 8:
            return False
        valid_chars = "0123456789ABCDEFabcdef"
        for i in s:
            if not i or len(i) > 4:
                return False
            for c in i:
                if c not in valid_chars:
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if ':' in queryIP:
            if self.ipv6(queryIP):
                return 'IPv6'
        elif '.' in queryIP:
            if self.ipv4(queryIP):
                return 'IPv4'
        return 'Neither'
               
               
        