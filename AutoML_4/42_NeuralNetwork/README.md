# Summary of 42_NeuralNetwork

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

33.5 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693793  |  nan        |
| auc       | 0.507536  |  nan        |
| f1        | 0.669324  |    0.276245 |
| accuracy  | 0.509585  |    0.497851 |
| precision | 0.555556  |    0.538228 |
| recall    | 1         |    0.276245 |
| mcc       | 0.0218281 |    0.538228 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693793  |  nan        |
| auc       | 0.507536  |  nan        |
| f1        | 0.589023  |    0.497851 |
| accuracy  | 0.509585  |    0.497851 |
| precision | 0.509112  |    0.497851 |
| recall    | 0.69869   |    0.497851 |
| mcc       | 0.0182642 |    0.497851 |


## Confusion matrix (at threshold=0.497851)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              792 |             1697 |
| Labeled as 1 |              759 |             1760 |

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
