from sklearn.metrics import classification_report, confusion_matrix

def get_classification_metrics(y_true, y_pred):
    """
    Devuelve el classification report como dict.
    """
    return classification_report(y_true, y_pred, output_dict=True)

def get_confusion(y_true, y_pred, labels):
    """
    Devuelve la matriz de confusión.
    """
    return confusion_matrix(y_true, y_pred, labels=labels)

