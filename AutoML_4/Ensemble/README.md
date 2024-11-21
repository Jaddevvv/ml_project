# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                                       |   Weight |
|:--------------------------------------------|---------:|
| 27_CatBoost_GoldenFeatures_SelectedFeatures |        1 |
| 3_Default_Xgboost_SelectedFeatures          |        1 |
| 45_CatBoost_GoldenFeatures_SelectedFeatures |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.686131 |  nan        |
| auc       | 0.566672 |  nan        |
| f1        | 0.67068  |    0.395571 |
| accuracy  | 0.546326 |    0.515238 |
| precision | 0.657005 |    0.578409 |
| recall    | 1        |    0.189841 |
| mcc       | 0.111821 |    0.530055 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.686131 |  nan        |
| auc       | 0.566672 |  nan        |
| f1        | 0.455939 |    0.515238 |
| accuracy  | 0.546326 |    0.515238 |
| precision | 0.574532 |    0.515238 |
| recall    | 0.377928 |    0.515238 |
| mcc       | 0.10061  |    0.515238 |


## Confusion matrix (at threshold=0.515238)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1784 |              705 |
| Labeled as 1 |             1567 |              952 |

## Learning curves
![Learning curves](learning_curves.png)
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
