# Summary of 16_CatBoost_GoldenFeatures_RandomFeature

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

37.6 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.68848   |  nan        |
| auc       | 0.549007  |  nan        |
| f1        | 0.669324  |    0.259501 |
| accuracy  | 0.53754   |    0.505034 |
| precision | 0.77193   |    0.649089 |
| recall    | 1         |    0.259501 |
| mcc       | 0.0778185 |    0.505034 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.68848   |  nan        |
| auc       | 0.549007  |  nan        |
| f1        | 0.48829   |    0.505034 |
| accuracy  | 0.53754   |    0.505034 |
| precision | 0.550573  |    0.505034 |
| recall    | 0.438666  |    0.505034 |
| mcc       | 0.0778185 |    0.505034 |


## Confusion matrix (at threshold=0.505034)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1587 |              902 |
| Labeled as 1 |             1414 |             1105 |

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
