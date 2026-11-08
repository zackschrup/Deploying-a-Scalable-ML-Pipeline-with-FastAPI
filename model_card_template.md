# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

For this project I used a RandomForestClassifier implemented with the scikit-learn ML Library. The model is trained to predict if a persons annual income is more or less than $50,000 based on demographic and employment features from the provided Adult Census Income dataset.  

## Intended Use

The intended use of this model is to predict if an individuals income exceeds $50K based on demographic and employment features.

## Training Data

The model was trained using the Adult Census Income Dataset from the UCI ML Repository. The datset included demographic, education, and occupation, among other peices of data.
## Evaluation Data

The model was evaluated using a test set from the Adult Census Income dataset. The dataset was split into training and testing subsets with an 80/20 split and a random seed of 42 to ensure reproducability. The test set was not used in the evaluation data.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The model was evaluated using precision, which it scored a 0.7419, Recall, which it scored 0.6384, and F1, which it scored 0.6863. Precision measures the proportion of positive predictions that were correct, recall measures tha proportion of positive cases that were identified correctly, and the F1 score provides a balance between the two previous metrics.

Precision: 0.7419
Recall: 0.6384
F1: 0.6863

## Ethical Considerations

Some considerations for this data set include potential biases across some demographic groups. These predictions also should not be the main consideration for employment, loans, or other financial decisions.

## Caveats and Recommendations

This model was trained on the Adult Census Income dataset. This data might not generalize well to data outside of this dataset. The dataset also represents a specific historical demographic so it might not reflect accuratly oncurrent or future trends.

The models performance does vary across different groups. Some groups have many less observational datapoints which can cause predictions to be unreliable.

Future improvements could include collecting more data, improving the parameter tuning to get more accurate predictions, and evaluating fairness across demographic groups.