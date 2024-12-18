# Summary of 17_CatBoost_GoldenFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
- **rsm**: 1.0
- **loss_function**: Logloss
- **eval_metric**: Logloss
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

24.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.68916  |  nan        |
| auc       | 0.547592 |  nan        |
| f1        | 0.669342 |    0.394771 |
| accuracy  | 0.539137 |    0.509121 |
| precision | 0.701754 |    0.621433 |
| recall    | 1        |    0.222613 |
| mcc       | 0.08263  |    0.509121 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.68916  |  nan        |
| auc       | 0.547592 |  nan        |
| f1        | 0.472578 |    0.509121 |
| accuracy  | 0.539137 |    0.509121 |
| precision | 0.556812 |    0.509121 |
| recall    | 0.41048  |    0.509121 |
| mcc       | 0.08263  |    0.509121 |


## Confusion matrix (at threshold=0.509121)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1666 |              823 |
| Labeled as 1 |             1485 |             1034 |

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
