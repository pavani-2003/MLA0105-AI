import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_weights(input_size, hidden_size, output_size):
    np.random.seed(42)
    weights_input_hidden = 2 * np.random.random((input_size, hidden_size)) - 1
    weights_hidden_output = 2 * np.random.random((hidden_size, output_size)) - 1
    return weights_input_hidden, weights_hidden_output

def forward_pass(inputs, weights_input_hidden, weights_hidden_output):
    hidden_layer_input = np.dot(inputs, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    return hidden_layer_output, predicted_output

def train_neural_network(inputs, labels, epochs, learning_rate):
    input_size = inputs.shape[1]
    hidden_size = 4  # Adjust as needed
    output_size = 1

    weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)

    for epoch in range(epochs):
        # Forward pass
        hidden_layer_output, predicted_output = forward_pass(inputs, weights_input_hidden, weights_hidden_output)

        # Backpropagation
        output_error = labels - predicted_output
        output_delta = output_error * sigmoid_derivative(predicted_output)

        hidden_layer_error = output_delta.dot(weights_hidden_output.T)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

        # Update weights
        weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
        weights_input_hidden += inputs.T.dot(hidden_layer_delta) * learning_rate

        if epoch % 1000 == 0:
            print(f"Error after {epoch} epochs: {np.mean(np.abs(output_error))}")

    return weights_input_hidden, weights_hidden_output

if __name__ == "__main__":
    # Example usage with an XOR problem
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([[0], [1], [1], [0]])

    epochs = 10000
    learning_rate = 0.1

    trained_weights_input_hidden, trained_weights_hidden_output = train_neural_network(inputs, labels, epochs, learning_rate)

    # Test the trained neural network
    _, predictions = forward_pass(inputs, trained_weights_input_hidden, trained_weights_hidden_output)
    print("Predictions:")
    print(predictions)
