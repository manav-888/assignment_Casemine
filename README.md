# NLP Web Application




## Setup Instructions


Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```
   git clone https://github.com/manav-888/manav-baisoya-wasserstoff-AiTask.git
   ```

2. **Create a Virtual Environment:**

   Note: We used Python 3.10.11 to create the virtual environment. Please ensure that you use the same Python version to avoid potential conflicts and ensure compatibility with the project dependencies.
   ```
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment:**
   ```
   . venv/bin/activate
   ```

5. **Install Requirements:**
   ```
   pip install -r requirements.txt

   ```
## Datasets
1. **Extract:**
   ```
   [IMDB Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
   ```
2. **Transform:**
- Perform data cleaning and preprocessing:
- Handle missing or null values.
- Normalize text (case folding, removing special characters).
- Tokenization and padding/truncating sequences as required.
- Remove stop words if applicable.
- Conduct Exploratory Data Analysis (EDA):
- Visualize class distributions.
- Analyze word/sentence lengths.

## Machine Learning & Deep Learning:

3. **Text Classification:**
 
- Fine-tune a pre-trained BERT model using your dataset for a classification task (e.g., sentiment analysis, topic categorization).
- Implement using PyTorch or TensorFlow (choose one).
- Train the model and evaluate its performance using metrics like accuracy, precision, recall, and F1-score.
- Optimize the model's hyperparameters to improve performance.
  Text Generation:
- Fine-tune a pre-trained GPT-2 model to generate text based on prompts from your dataset.
- Ensure the generated text is coherent and contextually relevant.
- Demonstrate the model's ability by generating examples based on sample prompts.
![image](https://github.com/user-attachments/assets/842cf770-7382-4d95-97a2-13a0926ed614)



