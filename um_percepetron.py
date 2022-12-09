data = [
    # Matriz vai no show?
    #longe, caro, amigos, vai
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0]
]

class Percepetron(object):
    matrix: list
    max_epoque: int

    weights: list
    bias: int = 0.1
    w0: float

    def __init__(self, matrix: list):
        self.matrix = matrix
        self.weights = len(matrix[:-1])*[0.0]
        self.max_epoque = 10
        self.w0 = 0.0

    def predict(self, line: list):
        x_data = line[:-1]

        # Pega cada Xn * Wn e soma em Z
        # sendo Xn cada elemento do data
        # e Wn os pesos
        z = sum(map(lambda x, w: x * w, x_data, self.weights)) + self.w0
        if z > 0:
            predicted = 1
        else:
            predicted = 0
        
        return predicted

    def adjust_weights(self, predicted: int, line: list):
        y = line[-1]
        print(self.weights, self.w0)
        for n in range(len(self.weights)):
            delta_w = self.bias * (y-predicted) * line[n]
            self.weights[n] = self.weights[n] + delta_w
        
        self.w0 = self.bias * (y-predicted) * 1
        print(self.weights, self.w0)

    def fit(self):
        for epoque in range(self.max_epoque):
            changed = False
            for num_line, line in enumerate(self.matrix):
                y = line[-1]
                predicted = self.predict(line)
                
                if predicted != y:
                    print(f"Line: {num_line}")
                    print(f"Epoque: {epoque}")
                    self.adjust_weights(predicted, line)
                    changed = True
                            
            if not changed:
                break

    def __repr__(self) -> str:
        out = f"Pesos: {self.weights, self.w0}\n"
        out += f"Bias: {self.bias}"
        return out

    def __str__(self) -> str:
        out = f"Pesos: {self.weights, self.w0}\n"
        out += f"Bias: {self.bias}"
        return out

new_percept = Percepetron(data)
new_percept.fit()

print(new_percept)