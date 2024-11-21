# Summary of 34_RandomForest_SelectedFeatures

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 40
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

31.4 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691296  |  nan        |
| auc       | 0.533695  |  nan        |
| f1        | 0.669324  |    0.240275 |
| accuracy  | 0.525759  |    0.503189 |
| precision | 0.574959  |    0.534103 |
| recall    | 1         |    0.240275 |
| mcc       | 0.0569789 |    0.474487 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691296  |  nan        |
| auc       | 0.533695  |  nan        |
| f1        | 0.491979  |    0.503189 |
| accuracy  | 0.525759  |    0.503189 |
| precision | 0.533395  |    0.503189 |
| recall    | 0.45653   |    0.503189 |
| mcc       | 0.0528641 |    0.503189 |


## Confusion matrix (at threshold=0.503189)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1483 |             1006 |
| Labeled as 1 |             1369 |             1150 |

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
