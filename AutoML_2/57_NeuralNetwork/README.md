# Summary of 57_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.08
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

34.1 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.692637  |  nan        |
| auc       | 0.50713   |  nan        |
| f1        | 0.682625  |    0.37063  |
| accuracy  | 0.520367  |    0.512101 |
| precision | 0.530913  |    0.522739 |
| recall    | 1         |    0.37063  |
| mcc       | 0.0255324 |    0.522739 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.692637  |  nan        |
| auc       | 0.50713   |  nan        |
| f1        | 0.661785  |    0.512101 |
| accuracy  | 0.520367  |    0.512101 |
| precision | 0.521411  |    0.512101 |
| recall    | 0.905588  |    0.512101 |
| mcc       | 0.0194498 |    0.512101 |


## Confusion matrix (at threshold=0.512101)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              256 |             2157 |
| Labeled as 1 |              245 |             2350 |

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
