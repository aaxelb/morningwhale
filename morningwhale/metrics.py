
from elasticsearch_metrics import metrics


# special-purpose metric class for gettin this running
class LogEvent(metrics.Metric):
    func_name = metrics.Keyword()
    log_level = metrics.Keyword()
    log_message_unformatted = metrics.Keyword()
    source_ref = metrics.Text()

    class Meta:
        source = metrics.MetaField(enabled=True)
