class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        is_negative = False
        if b < 0:
            b = self.subtract(b, 0)
            is_negative = not is_negative
        if a < 0:
            a = self.subtract(a, 0)
            is_negative = not is_negative
        for _ in range(b):
            result = self.add(result, a)
        if is_negative:
            result = self.subtract(result,0)
        return result

    def divide(self, a, b):
        result = 0
        is_negative = False
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        if a < 0:
            a = self.subtract(a,0)
            is_negative = not is_negative
        if b < 0:
            b = self.subtract(b,0)
            is_negative = not is_negative
        while a >= b:
            a = self.subtract(b, a)
            result = self.add(result,1)
        if is_negative:
            result = self.subtract(result,0)
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        is_negative = a < 0
        a = a if not is_negative else self.subtract(a,0)
        b = b if b > 0 else self.subtract(b,0)
        while a >= b:
            a = self.subtract(b,a)
        if is_negative:
            a = self.subtract(a,0)
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division:", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))