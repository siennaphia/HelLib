class SimpleLinearRegression:
    def __init__(self):
        self.weight = 0.0
        self.bias = 0.0

    def predict(self, x):
        return self.weight * x + self.bias

    def update_parameters(self, x, y, learning_rate):
        prediction = self.predict(x)
        error = prediction - y
        self.weight -= learning_rate * (2 * x * error)
        self.bias -= learning_rate * (2 * error)

# Instantiate Model
model = SimpleLinearRegression()

# Training Loop
epochs = 1000
learning_rate = 0.01
for epoch in range(epochs):
    for xi, yi in zip([1.0, 2.0, 3.0], [2.0, 4.0, 6.0]):
        model.update_parameters(xi, yi, learning_rate)

    if (epoch + 1) % 100 == 0:
        prediction = model.predict(4.0)
        print(f'Epoch [{epoch+1}/{epochs}], Prediction for x=4: {prediction:.4f}')
