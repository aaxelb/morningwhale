from django.http import HttpResponse
from morningwhale.metrics import LogEvent


async def logged_event(request):
    log_record = request.GET

    source_lineno = log_record.get('lineno')
    source_filepath = log_record.get('pathname')

    LogEvent.record(
        func_name=log_record.get('funcName'),
        log_level=log_record.get('levelname'),
        log_message_unformatted=log_record.get('msg'),
        source_ref=f'{source_filepath}:{source_lineno}',
    )

    return HttpResponse(201, 'did it')
