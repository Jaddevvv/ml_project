# Summary of 40_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 8
- **learning_rate**: 0.05
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

7.6 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.692839  |  nan        |
| auc       | 0.504739  |  nan        |
| f1        | 0.682625  |    0.438035 |
| accuracy  | 0.520367  |    0.497325 |
| precision | 1         |    0.558261 |
| recall    | 1         |    0.438035 |
| mcc       | 0.0198681 |    0.527569 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.692839  |  nan        |
| auc       | 0.504739  |  nan        |
| f1        | 0.66415   |    0.497325 |
| accuracy  | 0.520367  |    0.497325 |
| precision | 0.521176  |    0.497325 |
| recall    | 0.915222  |    0.497325 |
| mcc       | 0.0191185 |    0.497325 |


## Confusion matrix (at threshold=0.497325)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              231 |             2182 |
| Labeled as 1 |              220 |             2375 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
