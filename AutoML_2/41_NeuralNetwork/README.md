# Summary of 41_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 16
- **learning_rate**: 0.08
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

8.3 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.694123  |  nan        |
| auc       | 0.500061  |  nan        |
| f1        | 0.682625  |    0.301056 |
| accuracy  | 0.520367  |    0.457272 |
| precision | 0.524443  |    0.511593 |
| recall    | 1         |    0.301056 |
| mcc       | 0.0184268 |    0.457272 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.694123  |  nan        |
| auc       | 0.500061  |  nan        |
| f1        | 0.673286  |    0.457272 |
| accuracy  | 0.520367  |    0.457272 |
| precision | 0.520286  |    0.457272 |
| recall    | 0.953757  |    0.457272 |
| mcc       | 0.0184268 |    0.457272 |


## Confusion matrix (at threshold=0.457272)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              131 |             2282 |
| Labeled as 1 |              120 |             2475 |

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
