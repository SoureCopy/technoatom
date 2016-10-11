from generator import events
import logging

event = events(8, 3)

class WSGIapp:
    def __init__(self, enviroment, start_response):
        self.enviroment = enviroment
        self.start_response = start_response
        self.headers = [('Content-type', 'text/plain; charset=utf-8')]

    def __iter__(self):
        logging.debug('Wait for response')
        if self.enviroment.get('PATH_INFO', '/') == '/':
            result = next(event)
            if result:
                yield from self.ok_response('200 OK', result)
            else:
                yield from self.no_content_response('204 No Content', 'NO CONTENT')
        else:
            self.not_found_response()
        logging.debug('Done')

    def not_found_response(self):
        logging.debug('Create response')
        logging.debug('Send headers')
        self.start_response('404 Not Found', self.headers)

    def no_content_response(self, status, message):
        logging.debug('Create response')
        logging.debug('Send headers')
        self.start_response(status, self.headers)
        logging.debug('Headers is sent')
        logging.debug('Send body')
        yield ('%s\n' % message).encode('utf-8')

    def ok_response(self, status, message):
        logging.debug('Create response')
        logging.debug('Send headers')
        self.start_response(status, self.headers)
        logging.debug('Headers is sent')
        logging.debug('Send body')
        yield ('%s\n' % message).encode('utf-8')

    def not_response(self, message):
        logging.debug('Problems with Path')
        logging.debug('Send headers')
        self.start_response('404 Not FOUND', self.headers)
        logging.debug('Headers is sent')

