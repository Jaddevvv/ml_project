# Summary of 49_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.5
- **min_samples_split**: 20
- **max_depth**: 3
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

9.1 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.690442  |  nan        |
| auc       | 0.537972  |  nan        |
| f1        | 0.682625  |    0.290688 |
| accuracy  | 0.532149  |    0.495919 |
| precision | 0.617647  |    0.572317 |
| recall    | 1         |    0.290688 |
| mcc       | 0.0650987 |    0.520084 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.690442  |  nan        |
| auc       | 0.537972  |  nan        |
| f1        | 0.647616  |    0.495919 |
| accuracy  | 0.532149  |    0.495919 |
| precision | 0.53108   |    0.495919 |
| recall    | 0.829672  |    0.495919 |
| mcc       | 0.0532591 |    0.495919 |


## Confusion matrix (at threshold=0.495919)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              512 |             1901 |
| Labeled as 1 |              442 |             2153 |

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
