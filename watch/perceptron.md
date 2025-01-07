

A perceptron is a type of artificial neuron introduced by Frank Rosenblatt in 1958. It is a mathematical model used in machine learning for binary classification tasks. It mimics the structure and function of a biological neuron, which consists of dendrites (inputs), a cell body (processing unit), and an axon (output).

The biological neuron receives signals through its dendrites, processes them in the cell body, and generates an output signal through the axon. Similarly, the perceptron takes weighted inputs, sums them up, applies an activation function, and produces an output. However, a perceptron is a simplified abstraction of a biological neuron and lacks the complexity and adaptability of its biological counterpart.

---

The perceptron computes the output using the following equation:

\[
y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)
\]

Where:
- \( x_i \): Input features (e.g., \( x_1, x_2, \dots, x_n \)).
- \( w_i \): Weights associated with each input \( x_i \).
- \( b \): Bias term, allowing the decision boundary to shift.
- \( \sum_{i=1}^{n} w_i x_i + b \): Weighted sum of inputs and bias.
- \( f \): Activation function, often a step function that outputs \( 1 \) or \( 0 \) based on the threshold.

The perceptron is used for binary classification tasks where data can be linearly separated.

---

The perceptron learning rule adjusts weights iteratively to minimize classification errors. The update rule is defined as:

\[
w_i \leftarrow w_i + \Delta w_i
\]

\[
\Delta w_i = \eta (y_{\text{true}} - y_{\text{pred}}) x_i
\]

Where:
- \( \eta \): Learning rate, controlling the step size for weight updates.
- \( y_{\text{true}} \): True label of the input data.
- \( y_{\text{pred}} \): Predicted output of the perceptron.
- \( x_i \): Corresponding input feature.

Weights are updated only when the perceptron makes a misclassification.

---

The perceptron typically uses a **step function** as its activation function:

\[
f(z) =
\begin{cases} 
1, & \text{if } z \geq 0 \\
0, & \text{if } z < 0
\end{cases}
\]

This function outputs a binary result (\( 1 \) or \( 0 \)) depending on whether the weighted sum of inputs is above or below a threshold.

---

The perceptron training process involves the following steps:
1. **Initialize weights and bias** to small random values.
2. **For each training sample**:
   - Compute the weighted sum: \( z = \sum_{i=1}^{n} w_i x_i + b \).
   - Apply the step function: \( y_{\text{pred}} = f(z) \).
   - Compare \( y_{\text{pred}} \) with \( y_{\text{true}} \) (ground truth).
   - Update weights and bias using the learning rule if \( y_{\text{pred}} \neq y_{\text{true}} \).
3. Repeat until the perceptron correctly classifies all training examples or a maximum number of iterations is reached.

---

**The limitations of the perceptron**
1. **Linear Separability**: The perceptron can only solve problems that are linearly separable, such as AND and OR, but fails for non-linearly separable problems like XOR.
2. **Fixed Learning Rate**: The learning process may be slow or unstable for inappropriate learning rate values.
3. **No Hidden Layers**: A single-layer perceptron lacks the capability to model complex relationships or hierarchical features in data.
4. **Step Function**: The discrete step function limits the perceptron's ability to model continuous or probabilistic outputs, unlike modern neural networks with smoother activation functions.

These limitations led to the development of more advanced architectures, such as multi-layer perceptrons (MLPs) with backpropagation and non-linear activation functions.