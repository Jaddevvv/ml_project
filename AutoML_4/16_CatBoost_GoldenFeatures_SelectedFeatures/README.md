# Summary of 16_CatBoost_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 8
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

21.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.687796 |  nan        |
| auc       | 0.554872 |  nan        |
| f1        | 0.669324 |    0.196861 |
| accuracy  | 0.542732 |    0.499965 |
| precision | 0.728972 |    0.631479 |
| recall    | 1        |    0.196861 |
| mcc       | 0.086452 |    0.542071 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.687796  |  nan        |
| auc       | 0.554872  |  nan        |
| f1        | 0.539791  |    0.499965 |
| accuracy  | 0.542732  |    0.499965 |
| precision | 0.546602  |    0.499965 |
| recall    | 0.533148  |    0.499965 |
| mcc       | 0.0855923 |    0.499965 |


## Confusion matrix (at threshold=0.499965)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1375 |             1114 |
| Labeled as 1 |             1176 |             1343 |

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
