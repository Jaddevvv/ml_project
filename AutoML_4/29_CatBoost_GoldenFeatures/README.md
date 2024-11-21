# Summary of 29_CatBoost_GoldenFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 9
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

40.5 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.688371  |  nan        |
| auc       | 0.556091  |  nan        |
| f1        | 0.669342  |    0.395221 |
| accuracy  | 0.546326  |    0.498891 |
| precision | 0.666667  |    0.631442 |
| recall    | 1         |    0.260163 |
| mcc       | 0.0926463 |    0.498891 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.688371  |  nan        |
| auc       | 0.556091  |  nan        |
| f1        | 0.547951  |    0.498891 |
| accuracy  | 0.546326  |    0.498891 |
| precision | 0.549262  |    0.498891 |
| recall    | 0.546645  |    0.498891 |
| mcc       | 0.0926463 |    0.498891 |


## Confusion matrix (at threshold=0.498891)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1359 |             1130 |
| Labeled as 1 |             1142 |             1377 |

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
