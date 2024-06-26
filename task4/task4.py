import sys

def read_file(file_path):
    with open(file_path,'r') as file:
        nums=file.readlines()
        numbers=[int(num) for num in nums]
    return numbers

def find_median(numbers):
    sorted_numbers=numbers.sort()
    median= len(numbers)//2
    print(sum(abs(n - numbers[median]) for n in numbers))

if __name__=="__main__":
    if len(sys.argv)!=2:
        print('Неверное количество аргументов')
        sys.exit(1)
    file_path=sys.argv[1]

    numbers=read_file(file_path)
    find_median(numbers)