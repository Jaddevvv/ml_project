# Summary of 45_CatBoost_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
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

26.7 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.687197  |  nan        |
| auc       | 0.559906  |  nan        |
| f1        | 0.669609  |    0.358255 |
| accuracy  | 0.545927  |    0.511485 |
| precision | 0.666667  |    0.674213 |
| recall    | 1         |    0.131475 |
| mcc       | 0.0991268 |    0.545339 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.687197  |  nan        |
| auc       | 0.559906  |  nan        |
| f1        | 0.486218  |    0.511485 |
| accuracy  | 0.545927  |    0.511485 |
| precision | 0.564237  |    0.511485 |
| recall    | 0.427154  |    0.511485 |
| mcc       | 0.0960529 |    0.511485 |


## Confusion matrix (at threshold=0.511485)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1658 |              831 |
| Labeled as 1 |             1443 |             1076 |

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
