# Summary of 54_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 8
- **learning_rate**: 0.01
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

35.8 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693185  |  nan        |
| auc       | 0.515146  |  nan        |
| f1        | 0.682625  |    0.125255 |
| accuracy  | 0.519968  |    0.479323 |
| precision | 0.586319  |    0.552144 |
| recall    | 1         |    0.125255 |
| mcc       | 0.0357423 |    0.551368 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693185  |  nan        |
| auc       | 0.515146  |  nan        |
| f1        | 0.668505  |    0.479323 |
| accuracy  | 0.519968  |    0.479323 |
| precision | 0.520507  |    0.479323 |
| recall    | 0.934104  |    0.479323 |
| mcc       | 0.0170278 |    0.479323 |


## Confusion matrix (at threshold=0.479323)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              180 |             2233 |
| Labeled as 1 |              171 |             2424 |

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
