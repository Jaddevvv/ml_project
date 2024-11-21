# Summary of 5_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

5.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.692914 |  nan        |
| auc       | 0.506345 |  nan        |
| f1        | 0.682625 |    0.216643 |
| accuracy  | 0.520367 |    0.512948 |
| precision | 0.547912 |    0.527806 |
| recall    | 1        |    0.216643 |
| mcc       | 0.024612 |    0.512948 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.692914 |  nan        |
| auc       | 0.506345 |  nan        |
| f1        | 0.630575 |    0.512948 |
| accuracy  | 0.520367 |    0.512948 |
| precision | 0.524699 |    0.512948 |
| recall    | 0.789981 |    0.512948 |
| mcc       | 0.024612 |    0.512948 |


## Confusion matrix (at threshold=0.512948)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              556 |             1857 |
| Labeled as 1 |              545 |             2050 |

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
