# Summary of 5_Default_NeuralNetwork_SelectedFeatures

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

27.6 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693501  |  nan        |
| auc       | 0.517011  |  nan        |
| f1        | 0.669324  |    0.324426 |
| accuracy  | 0.51877   |    0.516727 |
| precision | 0.543357  |    0.516727 |
| recall    | 1         |    0.324426 |
| mcc       | 0.0467309 |    0.516727 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.693501  |  nan        |
| auc       | 0.517011  |  nan        |
| f1        | 0.361758  |    0.516727 |
| accuracy  | 0.51877   |    0.516727 |
| precision | 0.543357  |    0.516727 |
| recall    | 0.271139  |    0.516727 |
| mcc       | 0.0467309 |    0.516727 |


## Confusion matrix (at threshold=0.516727)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             1915 |              574 |
| Labeled as 1 |             1836 |              683 |

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
