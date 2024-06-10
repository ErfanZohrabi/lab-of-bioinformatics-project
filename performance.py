import sys
import numpy as np

def read_positive_list(posi_file):
    with open(posi_file) as file:
        return set(line.strip() for line in file)

def process_entries(eval_file, positive_set, threshold):
    tp, tn, fp, fn = 0, 0, 0, 0
    fp_list, fn_list = [], []
    
    with open(eval_file) as file:
        for line in file:
            entry, e_val = line.rstrip().split()
            e_val = float(e_val)
            
            if e_val <= threshold:
                if entry in positive_set:
                    tp += 1
                else:
                    fp += 1
                    fp_list.append(entry)
            else:
                if entry in positive_set:
                    fn += 1
                    fn_list.append(entry)
                else:
                    tn += 1
    
    return tp, tn, fp, fn, fp_list, fn_list

def calculate_metrics(tp, tn, fp, fn):
    conf_matrix = np.array([[tp, fp], [fn, tn]])
    acc = (tp + tn) / np.sum(conf_matrix)
    mcc_denominator = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    mcc = ((tn * tp) - (fp * fn)) / mcc_denominator if mcc_denominator != 0 else 0
    tpr = tp / (tp + fn) if (tp + fn) != 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) != 0 else 0
    return conf_matrix, acc, mcc, tpr, fpr

def main(eval_file, posi_file, threshold):
    positive_set = read_positive_list(posi_file)
    tp, tn, fp, fn, fp_list, fn_list = process_entries(eval_file, positive_set, threshold)
    conf_matrix, acc, mcc, tpr, fpr = calculate_metrics(tp, tn, fp, fn)
    
    print("Matrix:", conf_matrix)
    print("ACC:", acc)
    print("MCC:", mcc)
    print("TPR:", tpr)
    print("FPR:", fpr)
    print("Threshold:", threshold)
    print("FP entries:", fp_list)
    print("FN entries:", fn_list)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <eval_file> <posi_file> <threshold>")
        sys.exit(1)

    eval_file = sys.argv[1]
    posi_file = sys.argv[2]
    threshold = float(sys.argv[3])
    
    main(eval_file, posi_file, threshold)
