# 6) Write a Python class to implement pow(x, n) 

class PowerCalculator:
    @staticmethod
    def pow(x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        for _ in range(n):
            result *= x
            
        return result

if __name__ == "__main__":
    calculator = PowerCalculator()
    print(calculator.pow(2, 10)) 
    print(calculator.pow(2.1, 3)) 
    print(calculator.pow(2, -2))   
