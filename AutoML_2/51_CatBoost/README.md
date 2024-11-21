# Summary of 51_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
- **rsm**: 0.9
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

29.5 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.690607  |  nan        |
| auc       | 0.533298  |  nan        |
| f1        | 0.682625  |    0.289987 |
| accuracy  | 0.53115   |    0.50983  |
| precision | 0.614035  |    0.575168 |
| recall    | 1         |    0.289987 |
| mcc       | 0.0566981 |    0.50983  |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.690607  |   nan       |
| auc       | 0.533298  |   nan       |
| f1        | 0.577089  |     0.50983 |
| accuracy  | 0.53115   |     0.50983 |
| precision | 0.541765  |     0.50983 |
| recall    | 0.617341  |     0.50983 |
| mcc       | 0.0566981 |     0.50983 |


## Confusion matrix (at threshold=0.50983)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1058 |             1355 |
| Labeled as 1 |              993 |             1602 |

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
