import random
import main

def create_random_input(k, m):
    return (k, m, [random.randint(0, m) for i in range(0, m)])

def to_table(results, inputs):
    out = f' File   k    m    FIFO    LRU  OPTFF\n'
    for i, result in enumerate(results):
        out += f'File{i+1}  30   {str(inputs[i][1]).rjust(3)}'
        for alg, v in result.items():
            out += str(v[0]).rjust(7)
        out += "\n"
    return out

if __name__ == "__main__":
    random.seed(123)
    inputs = [create_random_input(30, m) for m in [50, 100, 150, 200, 250]]
    results = [main.test_input(*input) for input in inputs]
    print(to_table(results, inputs))