import json
from azure.ai.formrecognizer._models import AnalyzeResult


def get_invoice_analyzed_result_from_json(path_to_json : str) -> AnalyzeResult :
    with open(path_to_json, 'rb') as fp:
        analyzed_invoice = json.load(fp)
        
    return AnalyzeResult.from_dict(analyzed_invoice)