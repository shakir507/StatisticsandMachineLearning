import os

# Define the base folder and subfolders for the Supervised Learning course
base_folder="/home/shakir-bilal/Videos/CourseraSpecializationMachineLearning/"
base_folder_supervised = base_folder+"Supervised_Machine_Learning_Regression_and_Classification"
week_folders_supervised = ["Week1", "Week2", "Week3"]
quizz_and_labs_subfolder_supervised = "QuizzandLabs"


# Define the base folder and subfolders for the Advanced Learning Algorithm course
base_folder_advanced = base_folder+"Advanced_Learning_Algorithms"
week_folders_advanced = ["Week1", "Week2", "Week3","Week4"]
quizz_and_labs_subfolder_advanced = "QuizzandLabs"


# Define the base folder and subfolders for the Unsupervised Learning course
base_folder_unsupervised = base_folder+"Unsupervised_Learning_Recommenders_Reinforcement_Learning"
week_folders_unsupervised = ["Week1", "Week2", "Week3"]
quizz_and_labs_subfolder_unsupervised = "QuizzandLabs"

# Ensure that both base folders exist
os.makedirs(base_folder_supervised, exist_ok=True)
os.makedirs(base_folder_unsupervised, exist_ok=True)

# Create a function to generate HTML list items for files
def generate_file_links(base_folder, week, files):
    links = ""
    for file in files:
        file_path = f"{base_folder}/{week}/{file}"
        links += f'<li><a href="file://{file_path}">{file}</a></li>\n'
    return links

# Week 1 content for Supervised Learning course
week_1_files_supervised = [
    "Welcome to machine learning.mp4", "Applications of machine learning.mp4", 
    "What is machine learning.mp4",
    "Supervised learning part 1.mp4", "Supervised learning part 2.mp4", 
    "Unsupervised learning part 1.mp4", "Unsupervised learning part 2.mp4",
    "Jupyter Notebooks.mp4", f"{quizz_and_labs_subfolder_supervised}/AllPythonLabs/C1_W1_Lab01_Python_Jupyter_Soln.ipynb",
    f"{quizz_and_labs_subfolder_supervised}/Supervised vs unsupervised learning.png",
    "Linear regression model part 1.mp4", "Linear regression model part 2.mp4",
    f"{quizz_and_labs_subfolder_supervised}/AllPythonLabs/C1_W1_Lab02_Model_Representation_Soln.ipynb", 
    "Cost function formula.mp4", "Cost function intuition.mp4",
    "Visualizing the cost function.mp4", "Visualization examples.mp4",
    f"{quizz_and_labs_subfolder_supervised}/AllPythonLabs/C1_W1_Lab03_Cost_function_Soln.ipynb", 
    f"{quizz_and_labs_subfolder_supervised}/Practice quiz: Regression.png",
    "Gradient descent.mp4", "Implementing gradient descent.mp4", 
    "Gradient descent intuition.mp4", "Learning rate.mp4",
    "Gradient descent for linear regression.mp4", "Running gradient descent.mp4",
    f"{quizz_and_labs_subfolder_supervised}/AllPythonLabs/C1_W1_Lab04_Gradient_Descent_Soln.ipynb", 
    f"{quizz_and_labs_subfolder_supervised}/Practice quiz: Train the model with gradient descent.png"
]

# Week 2 content for Supervised Learning course
week_2_files_supervised = [
    "Multiple features.mp4", "Vectorization part 1.mp4", "Vectorization part 2.mp4", 
    f"{quizz_and_labs_subfolder_supervised}/Python NumPy and vectorization Lab.zip",
    "Gradient descent for multiple linear regression.mp4", 
    f"{quizz_and_labs_subfolder_supervised}/Multiple linear regression Lab.zip", f"{quizz_and_labs_subfolder_supervised}/Practice quiz: Multiple linear regression.png",
    "Feature scaling part 1.mp4", "Feature scaling part 2.mp4",
    "Checking gradient descent for convergence.mp4", "Choosing the learning rate.mp4",
    f"{quizz_and_labs_subfolder_supervised}/Feature scaling and learning rate Lab.zip",
    "Feature engineering.mp4", "Polynomial regression.mp4",
    f"{quizz_and_labs_subfolder_supervised}/Feature engineering and Polynomial regression Lab.zip",
    f"{quizz_and_labs_subfolder_supervised}/Linear regression with scikit learn Lab.zip",
    f"{quizz_and_labs_subfolder_supervised}/Practice quiz: Gradient descent in practice.png",
    f"{quizz_and_labs_subfolder_supervised}/Programming Assignment: Week 2 practice lab: Linear regression.zip"
]

# Week 3 content for Supervised Learning course
week_3_files_supervised = [
    "Motivations.mp4", f"{quizz_and_labs_subfolder_supervised}/Classification Lab.zip", 
    "Logistic regression.mp4", f"{quizz_and_labs_subfolder_supervised}/Sigmoid function and logistic regression Lab.zip",
    "Decision boundary.mp4", f"{quizz_and_labs_subfolder_supervised}/Decision boundary Lab.zip",
    "Cost function for logistic regression.mp4", f"{quizz_and_labs_subfolder_supervised}/Logistic loss Lab.zip",
    "Simplified Cost Function for Logistic Regression.mp4", f"{quizz_and_labs_subfolder_supervised}/Cost function for logistic regression Lab.zip",
    f"{quizz_and_labs_subfolder_supervised}/Practice quiz: Classification with logistic regression.png",
    "Gradient Descent Implementation.mp4", f"{quizz_and_labs_subfolder_supervised}/Gradient descent for logistic regression Lab.zip",
    f"{quizz_and_labs_subfolder_supervised}/Logistic regression with scikit learn Lab.zip",f"{quizz_and_labs_subfolder_supervised}/Practice quiz: Cost function for logistic regression.png",
    "The problem of overfitting.mp4", "Addressing overfitting.mp4", 
    f"{quizz_and_labs_subfolder_supervised}/Overfitting Lab.zip", 
    "Cost function with regularization.mp4", "Regularized linear regression.mp4", 
    "Regularized logistic regression.mp4", f"{quizz_and_labs_subfolder_supervised}/Regularization Lab.zip", 
    f"{quizz_and_labs_subfolder_supervised}/Practice quiz: The problem of overfitting.png",
    f"{quizz_and_labs_subfolder_supervised}/Week 3 practice lab logistic regression.zip", 
    "Andrew Ng and Fei-Fei Li on Human-Centered AI.mp4"
]

# Week 1 content for Advanced Learning Algorithms course
week_1_files_advanced = [
    "Welcome.mp4", "Neurons and the brain.mp4", 
    "Demand Prediction.mp4", "Example Recognizing Images.mp4", 
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Neural networks intuition.png",
    "Neural network layer.mp4", "More complex neural networks.mp4", 
    "Inference making predictions (forward propagation).mp4", 
    f"{quizz_and_labs_subfolder_advanced}/Neurons and Layers Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Neural network model.png",
    "Inference in Code.mp4", "Data in TensorFlow.mp4", 
    "Building a neural network.mp4", 
    f"{quizz_and_labs_subfolder_advanced}/Coffee Roasting in Tensorflow Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: TensorFlow implementation.png",
    "Forward prop in a single layer.mp4", "General implementation of forward propagation.mp4",
    f"{quizz_and_labs_subfolder_advanced}/CoffeeRoastingNumPy Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Neural network implementation in Python.png",
    "Is there a path to AGI.mp4", "Vectorization_How neural networks are implemented efficiently.mp4",
    "Vectorization_Matrix multiplication.mp4", "Vectorization_Matrix multiplication rules.mp4",
    "Vectorization_Matrix multiplication code.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Neural Networks for Binary Classification Programming Assignment.zip"
]

# Week 2 content for Advanced Learning Algorithms course
week_2_files_advanced = [
    "TensorFlow implementation.mp4", "Training Details.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Neural Network Training.png",
    "Alternatives to the sigmoid activation.mp4", "Choosing activation functions.mp4",
    "Why do we need activation functions.mp4", f"{quizz_and_labs_subfolder_advanced}/ReLU activation Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Activation Functions.png",
    "Multiclass.mp4", "Softmax.mp4", "Neural Network with Softmax output.mp4",
    "Improved implementation of softmax.mp4", "Classification with multiple outputs.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Softmax Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Multiclass Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Multiclass Classification.png",
    "Advanced Optimization.mp4", "Additional Layer Types.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Additional Neural Network Concepts.png",
    "What is a derivative.mp4", "Computation graph.mp4",
    "Larger neural network example.mp4", f"{quizz_and_labs_subfolder_advanced}/Derivatives Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Back propagation Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Neural Networks for Multiclass classification Programming Assignment.zip"
]

# Week 3 content for Advanced Learning Algorithms course
week_3_files_advanced = [
    "Deciding what to try next.mp4", "Evaluating a model.mp4",
    "Model selection and training cross validation test sets.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Model Evaluation and Selection Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Advice for applying machine learning.png",
    "Diagnosing bias and variance.mp4", "Regularization and bias variance.mp4",
    "Establishing a baseline level of performance.mp4", "Learning curves.mp4",
    "Deciding what to try next revisited.mp4", "Bias variance and neural networks.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Diagnosing Bias and Variance Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Bias and variance.png",
    "Iterative loop of ML development.mp4", "Error analysis.mp4",
    "Adding data.mp4", "Transfer learning using data from a different task.mp4",
    "Full cycle of a machine learning project.mp4", 
    "Fairness bias and ethics.mp4", 
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Machine learning development process.png",
    "Error metrics for skewed datasets.mp4", 
    "Trading off precision and recall.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Advice for Applying Machine Learning Programming Assignment.zip"
]

# Week 4 content for Advanced Learning Algorithms course
week_4_files_advanced = [
    "Decision tree model.mp4", "Learning Process.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Decision trees.png",
    "Measuring purity.mp4", "Choosing a split Information Gain.mp4",
    "Putting it together.mp4", "Using one-hot encoding of categorical features.mp4",
    "Continuous valued features.mp4", "Regression Trees.mp4",
    f"{quizz_and_labs_subfolder_advanced}/Decision Trees Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Decision tree learning.png",
    "Using multiple decision trees.mp4", "Sampling with replacement.mp4",
    "Random forest algorithm.mp4", "XGBoost.mp4",
    "When to use decision trees.mp4", f"{quizz_and_labs_subfolder_advanced}/Tree Ensembles Lab.zip",
    f"{quizz_and_labs_subfolder_advanced}/Practice quiz: Tree ensembles.png",
    f"{quizz_and_labs_subfolder_advanced}/Decision Trees Programming Assignment.zip",
    "Andrew Ng and Chris Manning on Natural Language Processing.mp4"
    ]


# Week 1 content for Unsupervised Learning course
week_1_files_unsupervised = [
    "Welcome.mp4", "What is clustering.mp4",
    "K-means intuition.mp4", "K-means algorithm.mp4", "Optimization objective.mp4",
    "Initializing K-means.mp4", "Choosing the number of clusters.mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/ClusteringQuizz.png",
    f"{quizz_and_labs_subfolder_unsupervised}/k-means Programming Assignment.zip",
    "AnomalyDetection_Finding unusual events.mp4", "AnomalyDetection_Gaussian (normal) distribution.mp4",
    "Anomaly detection algorithm.mp4", "Developing and evaluating an anomaly detection system.mp4",
    "Anomaly detection vs supervised learning.mp4", "Choosing what features to use.mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/Anomaly detection.png",
    f"{quizz_and_labs_subfolder_unsupervised}/Anomaly Detection Programming Assignment.zip"
]

# Week 2 content for Unsupervised Learning course
week_2_files_unsupervised = [
    "Making recommendations.mp4", "Using per-item features.mp4", 
    "Collaborative filtering algorithm.mp4", "Binary labels_ favs likes and clicks.mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/Collaborative Filtering.png",
    "RecommenderSystemImplementationDetail_Mean normalization.mp4", "TensorFlow implementation of collaborative filtering.mp4",
    "Finding related items.mp4", f"{quizz_and_labs_subfolder_unsupervised}/Collaborative Filtering Recommender Systems Programming Assignment.zip",
    f"{quizz_and_labs_subfolder_unsupervised}/Recommender systems implementation.png",
    "Collaborative filtering vs Content-based filtering.mp4", 
    "Deep learning for content-based filtering.mp4",
    "Recommending from a large catalogue.mp4", "Ethical use of recommender systems.mp4",
    "TensorFlow implementation of content-based filtering.mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/Content-based filtering.png",
    f"{quizz_and_labs_subfolder_unsupervised}/Deep Learning for Content-Based Filtering Programming Assignment.zip",
    "PCA_Reducing the number of features (optional).mp4", "PCA algorithm (optional).mp4", "PCA in code (optional).mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/PCA and data visualization Lab.zip"
]

# Week 3 content for Unsupervised Learning course
week_3_files_unsupervised = [
    "What is Reinforcement Learning.mp4", "Mars rover example.mp4",
    "The Return in reinforcement learning.mp4", "Making decisions Policies in reinforcement learning.mp4",
    "Review of key concepts.mp4", f"{quizz_and_labs_subfolder_unsupervised}/Reinforcement learning introduction.png",
    "State-action value function definition.mp4", "State-action value function example.mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/State-action value function (optional lab).zip",
    "Bellman Equation.mp4", "Random (stochastic) environment (Optional).mp4",
    f"{quizz_and_labs_subfolder_unsupervised}/State-action value function.png",
    "Example of continuous state space applications.mp4", "Lunar lander.mp4",
    "Learning the state-value function.mp4", "Algorithm refinement Improved neural network architecture.mp4",
    "Algorithm refinement_ ϵ-greedy policy.mp4", "Algorithm refinement Mini-batch and soft updates (Optional).mp4",
    "The state of reinforcement learning.mp4", f"{quizz_and_labs_subfolder_unsupervised}/Continuous state spaces.png",
    f"{quizz_and_labs_subfolder_unsupervised}/Reinforcement Learning Programming Assignment.zip",
    "Summary and thank you.mp4", "Andrew Ng and Chelsea Finn on AI and Robotics.mp4",
]

#Certificate of completion
certificates=["SpecializationCertificate.pdf","Supervised Machine Learning: Regression and Classification Certificate.pdf","Advanced Learning Algorithms Certificate.pdf","Unsupervised Learning, Recommenders, Reinforcement Learning.pdf"]

# Generate the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Machine Learning Courses</title>
</head>
<body>
    <h1>Machine Learning Courses</h1>
    
    <h2>Supervised Machine Learning: Regression and Classification</h2>
    <h3>Week 1</h3>
    <ul>
        {generate_file_links(base_folder_supervised, week_folders_supervised[0], week_1_files_supervised)}
    </ul>
    <h3>Week 2</h3>
    <ul>
        {generate_file_links(base_folder_supervised, week_folders_supervised[1], week_2_files_supervised)}
    </ul>
    <h3>Week 3</h3>
    <ul>
        {generate_file_links(base_folder_supervised, week_folders_supervised[2], week_3_files_supervised)}
    </ul>

    <h2>Advanced Learning Algorithms</h2>
    <h3>Week 1</h3>
    <ul>
        {generate_file_links(base_folder_advanced, week_folders_advanced[0], week_1_files_advanced)}
    </ul>
    <h3>Week 2</h3>
    <ul>
        {generate_file_links(base_folder_advanced, week_folders_advanced[1], week_2_files_advanced)}
    </ul>
    <h3>Week 3</h3>
    <ul>
        {generate_file_links(base_folder_advanced, week_folders_advanced[2], week_3_files_advanced)}
    </ul>
    <h3>Week 4</h3>
    <ul>
        {generate_file_links(base_folder_advanced, week_folders_advanced[3], week_4_files_advanced)}
    </ul>

    <h2>Unsupervised Learning, Recommenders, Reinforcement Learning</h2>
    <h3>Week 1</h3>
    <ul>
        {generate_file_links(base_folder_unsupervised, week_folders_unsupervised[0], week_1_files_unsupervised)}
    </ul>
    <h3>Week 2</h3>
    <ul>
        {generate_file_links(base_folder_unsupervised, week_folders_unsupervised[1], week_2_files_unsupervised)}
    </ul>
    <h3>Week 3</h3>
    <ul>
        {generate_file_links(base_folder_unsupervised, week_folders_unsupervised[2], week_3_files_unsupervised)}
    </ul>
    <h2>Certificates</h2>
    <ul>
        {generate_file_links(base_folder, "Certificates", certificates)}
    </ul>
</body>
</html>
"""

# Save the HTML content to a file
output_file_path = os.path.join(base_folder, "machine_learning_courses.html")
with open(output_file_path, "w") as file:
    file.write(html_content)

print(f"HTML file has been generated successfully at {output_file_path}.")
