
def dispatcher(event):
    text = 'Hello! I\'ll repeat anything you say to me.'
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = event['request']['original_utterance']
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text + '1',
            # Don't finish the session after this response.
            'end_session': 'false'
        },
    }
