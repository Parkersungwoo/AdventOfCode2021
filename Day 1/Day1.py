
def part_one(input):
    pass



def part_two(input):
    count = 0
    prev_sum = input[0] + input[1] + input[2]
    for i in range(1, len(input) - 2):
        current_sum = input[i] + input[i+1] + input[i+2]
        
        if current_sum > prev_sum:
            count += 1
    return count

def initialize(input):
    collection = []
    while True:
        line = input_stream.readline()
        if not line:
            break
        collection.add(int(line))
    return collection

def __main__():
    input_stream = open('input2.txt', 'r')
    print(part_two(initialize(input_stream)))
    input_stream.close()