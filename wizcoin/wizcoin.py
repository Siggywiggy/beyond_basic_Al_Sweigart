class WizCoinException(Exception):
    """The wizcoin module raises this when the module is misused."""
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self._galleons = galleons
        self.sickles  = sickles
        self.knuts    = knuts
        # NOTE: __init__() methods NEVER have a return statement.

    def __repr__(self):
        """Returns a string of an expression that re-creates this object. Can use this call to copy this object!"""
        return f'{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})'

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return f'{self.galleons}g, {self.sickles}s, {self.knuts}k'
    # read-only property

    @property
    def total(self):
        """Total value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    # Note that there is no setter or deleter method for `total`.

    @property
    def galleons(self):
        """Returns the number of galleon coins in this object."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException('galleons attr must be set to an int, not a ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons attr must be a positive int, not ' + value.__class__.__qualname__)
        self._galleons = value

    def __add__(self, other):
        """Adds the coin amounts in two WizCoin objects together."""
        if not isinstance(other, WizCoin): # we check if both of the classes are the same type!
            return NotImplemented # try calling other methods => python calls __add__ which also returns NotImplemented
        # resulting in raising a TypeError!

        return WizCoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # Multiplying by a negative int results in negative
            # amounts of coins, which is invalid.
            raise WizCoinException('cannot multiply with negative integers')

        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __sub__(self, other):
        if other.__class__ is self.__class__:
            if self.__galleons < other.galleons or self.__sickles < other.sickles or self.__knuts < other.knuts:
                # Coins objects represent an amount of physical coins, not a
                # monetary value, so there can't be negative coins.
                raise WizCoinException(
                    'subtracting %s from %s would result in negative quantity of coins' % (other, self))
            return WizCoin(self.__galleons - other.galleons,
                         self.__sickles - other.sickles,
                         self.__knuts - other.knuts)
        else:
            return NotImplemented






purse = WizCoin(12,0,13)
print(purse.galleons)
purse.galleons = 34
print(purse.galleons)
print(purse.total)
#purse.total = 10000 # NO SETTER!
print(repr(purse))
print(str(purse))
print(f'my purse contains {purse}')
tipJar = WizCoin(0, 0, 37)

print(purse + tipJar) # sums both of the objects and creates a new object basically!

#print(purse + 40) # returns NOT IMPLEMENTED instead of an exception

print(purse * 2)

#print(purse * -2) # cant multiply with negative numbers

print(purse - tipJar)

