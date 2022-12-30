import sys

def mul(val1, val2):
    return int(val1) * int(val2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python3 ./calculator.py number1 number2')
        sys.exit(1)

    val1 = sys.argv[1]
    val2 = sys.argv[2]
    
    result = mul(val1, val2)
    print(result)