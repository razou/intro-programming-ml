def accuracy(true_positives, false_positives, true_negatives, false_negatives):
    numerator = true_positives + true_negatives
    denominator = true_positives + true_negatives + false_positives + false_negatives
    return numerator / denominator


def sensitivity(true_positives, false_negatives):
    try:
        return true_positives / (true_positives + false_negatives)
    except ZeroDivisionError:
        return float('nan')


def specificity(true_negatives, false_positives):
    try:
        return true_negatives / (true_negatives + false_positives)
    except ZeroDivisionError:
        return float('nan')


def pos_pred_val(true_positives, false_positives):
    try:
        return true_positives / (true_positives + false_positives)
    except ZeroDivisionError:
        return float('nan')


def neg_pred_val(true_negatives, false_negatives):
    try:
        return true_negatives / (true_negatives + false_negatives)
    except ZeroDivisionError:
        return float('nan')


def get_stats(true_positives, false_positives, true_negatives, false_negatives, to_print=True):
    accur = accuracy(true_positives, false_positives, true_negatives, false_negatives)
    sens = sensitivity(true_positives, false_negatives)
    spec = specificity(true_negatives, false_positives)
    ppv = pos_pred_val(true_positives, false_positives)
    if to_print:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return accur, sens, spec, ppv
