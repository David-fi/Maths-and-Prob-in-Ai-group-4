import numpy as np  # Importing numpy for array operations

class SoftmaxLayer:
    def __init__(self):
        # Prepare to store the output of the softmax function
        self.output = None

    def forward(self, logits):
        """
        Perform the forward pass to calculate softmax probabilities.
        
        Parameters:
        logits (np.array): Scores from the previous layer, shaped (batch_size, num_classes).

        Returns:
        np.array: Probabilities for each class, same shape as input.
        """
        # Subtract the max to keep numbers stable
        z_max = np.max(logits, axis=1, keepdims=True)
        shifted_logits = logits - z_max
        exp_shifted = np.exp(shifted_logits)

        # Divide by sum of exponents to get probabilities
        sum_exp = np.sum(exp_shifted, axis=1, keepdims=True)
        self.output = exp_shifted / sum_exp
        return self.output

    def backward(self, true_labels):
        """
        Perform the backward pass to calculate gradient of the loss.
        
        Parameters:
        true_labels (np.array): One-hot encoded true class labels.

        Returns:
        np.array: Gradient of the loss with respect to logits.
        """
        # Get the number of samples to average the gradient
        num_samples = true_labels.shape[0]

        # Calculate the gradient for softmax combined with cross-entropy
        gradient = (self.output - true_labels) / num_samples
        return gradient

if __name__ == "__main__":
    # Example usage of SoftmaxLayer

    # Define example logits, representing class scores
    logits_example = np.array([[2.0, 1.0, 0.1],
                               [1.0, 2.0, 0.1]])

    # Define the true labels in one-hot encoding
    true_labels_example = np.array([[1, 0, 0],
                                    [0, 1, 0]])

    # Instantiate the softmax layer
    softmax_layer = SoftmaxLayer()

    # Forward pass to get probability distributions
    softmax_output = softmax_layer.forward(logits_example)
    print("Softmax Probabilities:\n", softmax_output)

    # Backward pass to compute gradient
    loss_gradient = softmax_layer.backward(true_labels_example)
    print("Gradient of Loss w.r.t Logits:\n", loss_gradient)
