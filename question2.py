import question1
import main
import random

if __name__ == "__main__":
    random.seed(345)
    inputs = [question1.create_random_input(3, m) for m in [4, 5, 6, 7]]
    results = [main.test_input(*input) for input in inputs]
    print(question1.to_table(results, inputs))
    print(inputs[3])