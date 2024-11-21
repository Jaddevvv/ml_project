# Summary of 35_RandomForest_SelectedFeatures

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
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

30.6 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.69129   |  nan        |
| auc       | 0.531838  |  nan        |
| f1        | 0.669324  |    0.213014 |
| accuracy  | 0.523762  |    0.505899 |
| precision | 0.618357  |    0.561326 |
| recall    | 1         |    0.213014 |
| mcc       | 0.0569668 |    0.479824 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.69129   |  nan        |
| auc       | 0.531838  |  nan        |
| f1        | 0.472695  |    0.505899 |
| accuracy  | 0.523762  |    0.505899 |
| precision | 0.533433  |    0.505899 |
| recall    | 0.424375  |    0.505899 |
| mcc       | 0.0497224 |    0.505899 |


## Confusion matrix (at threshold=0.505899)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1554 |              935 |
| Labeled as 1 |             1450 |             1069 |

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
