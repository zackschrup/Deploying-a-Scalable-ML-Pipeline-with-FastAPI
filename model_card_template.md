# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

- RandomForestClassifier
- SCikit-learn

## Intended Use

- The intended use is to predict if income exceeds $50K

## Training Data

- Adult Census Income Dataset

## Evaluation Data

The model was evaluated using a test set from the Adult Census Income dataset. The dataset was split into training and testing subsets with an 80/20 split and a random seed of 42 to ensure reproducability. The test set was not used in the evaluation data.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

Precision: 0.7419
Recall: 0.6384
F1: 0.6863

## Ethical Considerations

Some considerations for this data set include potential biases across some demographic groups. These predictions also should not be the main consideration for employment, loans, or other financial decisions.

## Caveats and Recommendations

THis model was trained on the Adult Census Income dataset. This data might not generalize well to data outside of this dataset. The dataset also represents a specific historical demographic so it might not reflect accuratly oncurrent or future trends.

The models performance does vary across different groups. Some groups have many less observational datapoints which can cause predictions to be unreliable.

Future improvements could include collecting more data, improving the parameter tuning to get more accurate predictions, and evaluating fairness across demographic groups.