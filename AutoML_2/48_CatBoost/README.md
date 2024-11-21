# Summary of 48_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
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

7.6 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691642  |  nan        |
| auc       | 0.525138  |  nan        |
| f1        | 0.682625  |    0.270406 |
| accuracy  | 0.527955  |    0.494879 |
| precision | 0.575492  |    0.55093  |
| recall    | 1         |    0.270406 |
| mcc       | 0.0467897 |    0.528822 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691642  |  nan        |
| auc       | 0.525138  |  nan        |
| f1        | 0.641927  |    0.494879 |
| accuracy  | 0.527955  |    0.494879 |
| precision | 0.528825  |    0.494879 |
| recall    | 0.81657   |    0.494879 |
| mcc       | 0.0426587 |    0.494879 |


## Confusion matrix (at threshold=0.494879)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              525 |             1888 |
| Labeled as 1 |              476 |             2119 |

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
