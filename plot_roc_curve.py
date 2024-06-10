# plot_roc_curve.py

"""
This script plots the ROC curve and calculates the AUC (Area Under the Curve) 
from given TPR (True Positive Rate) and FPR (False Positive Rate) lists.
The script takes as input two lists: one for TPR values and another for FPR values, 
previously computed with the performance_and_TPR_FPR.py script.

Functions:
- plot_roc_curve(tpr_list, fpr_list): Plots the ROC curve using matplotlib.
- calculate_auc(tpr_list, fpr_list): Calculates the AUC using the trapezoidal rule.
- main(): Main function to execute the script, including predefined TPR and FPR values.
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_roc_curve(tpr_list, fpr_list):
    """
    Plots the ROC curve using TPR and FPR lists.

    Parameters:
    tpr_list (list): List of True Positive Rate values.
    fpr_list (list): List of False Positive Rate values.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(fpr_list, tpr_list, color='blue', lw=2, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Random')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()

def calculate_auc(tpr_list, fpr_list):
    """
    Calculates the AUC (Area Under the Curve) using the trapezoidal rule.

    Parameters:
    tpr_list (list): List of True Positive Rate values.
    fpr_list (list): List of False Positive Rate values.

    Returns:
    float: Calculated AUC value.
    """
    sorted_indices = np.argsort(fpr_list)
    sorted_fpr = np.array(fpr_list)[sorted_indices]
    sorted_tpr = np.array(tpr_list)[sorted_indices]
    auc = np.trapz(sorted_tpr, sorted_fpr)
    return max(0.0, min(auc, 1.0))  # Ensures AUC is within [0, 1] range

def main():
    """
    Main function to execute the script. Defines TPR and FPR lists, calculates AUC,
    and plots the ROC curve.
    """
    tpr_list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.994, 0.994, 0.989, 0.984, 0.984, 0.984, 0.973, 0.946, 0.936, 0.930, 0.920, 0.909, 0.872, 0.813]
    fpr_list = [0.462, 0.040, 0.003, 0.0003, 0.7379, 0.3514, 0.1757, 0.03514, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    auc = calculate_auc(tpr_list, fpr_list)
    print("AUC:", auc)

    plot_roc_curve(tpr_list, fpr_list)

if __name__ == '__main__':
    main()

"""
Caption
This Python script, named plot_roc_curve.py, is designed to plot the ROC (Receiver Operating Characteristic) curve and compute the AUC (Area Under the Curve) from given lists of TPR (True Positive Rate) and FPR (False Positive Rate) values.

Key Components:
plot_roc_curve(tpr_list, fpr_list): A function that generates and displays the ROC curve using matplotlib.
calculate_auc(tpr_list, fpr_list): A function that calculates the AUC by integrating the area under the ROC curve using the trapezoidal rule.
main(): The main function that initializes predefined TPR and FPR values, calculates the AUC, and calls the plotting function to display the ROC curve.
The script ensures the AUC value is within the valid range [0, 1], correcting potential numerical inaccuracies.

"""

