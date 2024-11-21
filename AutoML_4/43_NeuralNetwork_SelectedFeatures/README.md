# Summary of 43_NeuralNetwork_SelectedFeatures

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 8
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

33.4 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693586  |  nan        |
| auc       | 0.504716  |  nan        |
| f1        | 0.669324  |    0.117631 |
| accuracy  | 0.509185  |    0.499132 |
| precision | 0.513384  |    0.499562 |
| recall    | 1         |    0.117631 |
| mcc       | 0.0175772 |    0.499132 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693586  |  nan        |
| auc       | 0.504716  |  nan        |
| f1        | 0.551132  |    0.499132 |
| accuracy  | 0.509185  |    0.499132 |
| precision | 0.510315  |    0.499132 |
| recall    | 0.599047  |    0.499132 |
| mcc       | 0.0175772 |    0.499132 |


## Confusion matrix (at threshold=0.499132)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1041 |             1448 |
| Labeled as 1 |             1010 |             1509 |

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
