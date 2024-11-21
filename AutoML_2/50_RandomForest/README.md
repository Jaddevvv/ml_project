# Summary of 50_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.5
- **min_samples_split**: 20
- **max_depth**: 5
- **eval_metric_name**: logloss
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

10.8 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691245  |  nan        |
| auc       | 0.535563  |  nan        |
| f1        | 0.682625  |    0.257052 |
| accuracy  | 0.533546  |    0.519623 |
| precision | 0.596491  |    0.60854  |
| recall    | 1         |    0.257052 |
| mcc       | 0.0709503 |    0.533951 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691245  |  nan        |
| auc       | 0.535563  |  nan        |
| f1        | 0.555217  |    0.519623 |
| accuracy  | 0.533546  |    0.519623 |
| precision | 0.548739  |    0.519623 |
| recall    | 0.56185   |    0.519623 |
| mcc       | 0.0650365 |    0.519623 |


## Confusion matrix (at threshold=0.519623)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1214 |             1199 |
| Labeled as 1 |             1137 |             1458 |

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
