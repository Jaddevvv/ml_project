# Summary of 39_RandomForest_SelectedFeatures

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.6
- **min_samples_split**: 20
- **max_depth**: 4
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

8.4 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691125  |  nan        |
| auc       | 0.528399  |  nan        |
| f1        | 0.682733  |    0.405937 |
| accuracy  | 0.52516   |    0.442886 |
| precision | 0.61194   |    0.576954 |
| recall    | 1         |    0.245877 |
| mcc       | 0.0563735 |    0.547931 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.691125  |  nan        |
| auc       | 0.528399  |  nan        |
| f1        | 0.678735  |    0.442886 |
| accuracy  | 0.52516   |    0.442886 |
| precision | 0.522571  |    0.442886 |
| recall    | 0.968015  |    0.442886 |
| mcc       | 0.0430666 |    0.442886 |


## Confusion matrix (at threshold=0.442886)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              118 |             2295 |
| Labeled as 1 |               83 |             2512 |

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
