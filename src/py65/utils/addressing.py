import re

class AddressParser(object):
    """Parse user input into addresses or ranges of addresses.
    """

    def __init__(self, maxwidth=16, radix=16, labels={}):
        """Maxwidth is the maximum width of an address in bits.
        Radix is the default radix to use when one is not specified
        as a prefix of any input.  Labels are a dictionary of label
        names that can be substituted for addresses.
        """
        self.radix = radix
        self.labels = labels
        self.maxwidth = maxwidth
        
    def _get_maxwidth(self):
        return self._maxwidth    

    def _set_maxwidth(self, width):
        self._maxwidth = width
        self._maxaddr = pow(2, width) - 1

    maxwidth = property(_get_maxwidth, _set_maxwidth)
              
    def label_for(self, address, default=None):
        """Given an address, return the corresponding label or a default.
        """
        for label, label_address in self.labels.iteritems():
            if label_address == address:
                return label
        return default

    def number(self, num):
        """Parse a string containing a label or number into an address.
        """
        if num.startswith('$'):
            return int(num[1:], 16)

        elif num.startswith('+'):
            return int(num[1:], 10)

        elif num.startswith('%'):
            return int(num[1:], 2)

        elif num in self.labels:
            return self.labels[num]
      
        else:
            matches = re.match('^([^\s+-]+)\s*([+\-])\s*([$+%]?\d+)$', num)
            if matches:
                label, sign, offset = matches.groups()

                if label not in self.labels:
                    raise KeyError("Label not found: %s" % label)

                base = self.labels[label]
                offset = self.number(offset)

                if sign == '+':
                    address = base + offset
                else:
                    address = base - offset

                if address < 0:
                    address = 0
                if address > self._maxaddr:
                    address = self._maxaddr
                return address

            else:
                try:
                    return int(num, self.radix)
                except ValueError:
                    raise KeyError("Label not found: %s" % num)

    def range(self, addresses):
        """Parse a string containing an address or a range of addresses
        into a tuple of (start address, end address)
        """
        matches = re.match('^([^:,]+)\s*[:,]+\s*([^:,]+)$', addresses)
        if matches:
            start, end = map(self.number, matches.groups(0))
        else:
            start = end = self.number(addresses)

        if start > end:
            start, end = end, start            
        return (start, end)
