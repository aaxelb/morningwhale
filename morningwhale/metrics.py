
from elasticsearch_metrics import metrics


class LoggedEvent(metrics.Metric):
    func_name = metrics.Keyword()
    log_level = metrics.Keyword()
    log_message_unformatted = metrics.Keyword()
    source_ref = metrics.Text()
