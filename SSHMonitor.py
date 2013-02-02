import os
from urllib import urlencode
from urllib2 import urlopen, HTTPError
from xml.etree.ElementTree import XML
import logging

rejectedData[]
acceptedData[]
_last_meta_data = {}

__all__ = ['Error', 'get_remaining', 'get_reset_time', 'verify', 'post', 'Prowl', 'LogHandler']



class Error(ValueError):
    print ValueError
    pass



"""
Parameters:
    key -- An API key, or a list of API keys to post to.
    message -- The message to send.
    priority -- Integer from -2 to 2 inclusive.
    url -- Requires Prowl 1.2 The URL which should be attached to the notification.
    app -- App identifier to send as.
    event -- Event identifier to send as.
    providerkey -- Provider API key if you have been whitelisted.
"""
def sendNotification(key, message, priority=None, url=None, app=None, event=None, providerkey=None):

    API_URL_BASE = 'https://api.prowlapp.com/publicapi/'
    DEFAULT_PRIORITY = 0
    DEFAULT_APP = 'py:%s' % __name__
    DEFAULT_EVENT = 'default'

    data = {
            'apikey': key if isinstance(key, basestring) else ','.join(key),
            'priority': priority or DEFAULT_PRIORITY,
            'application': app or DEFAULT_APP,
            'event': event or DEFAULT_EVENT,
            'description': message
            }

    if url is not None:
        data['url'] = url

    if providerkey is not None:
        data['providerkey'] = providerkey

    method = 'add'

    """Make the raw request to the Prowl API."""

    # Catch the errors and treat them just like the normal response.
    try:
        res = urlopen(API_URL_BASE + method, urlencode(data) if data else None)
    except HTTPError as res:
        pass

    xml = XML(res.read())
    if xml.tag != 'prowl':
        raise Error('malformed response: unexpected tag %r' % xml.tag)
    children = xml.getchildren()
    if len(children) != 1:
        raise Error('malformed response: too many children')
    node = children[0]
    status, data, text = node.tag, node.attrib, node.text

    if status not in ('success', 'error'):
        raise Error('malformed response: unknown status %r' % node.tag)

    if 'code' not in node.attrib:
        raise Error('malformed response: no response code')

    if status == 'error' and not text:
        raise Error('malformed response: no error message with code %d' % data['code'])

    data = dict((k, int(v)) for k, v in data.items())
    _last_meta_data.update(data)



""" parse the timestamp from the line of data given """
def getTimeStamp():



""" parse the host from the line of data given """
def getHost(line):



""" parse the user from the line of data given """
def getUser(line):



""" purge old data if it's something like 3 days old """
def purgeData():



""" write the current data to the filesystem to survive a reboot """
def saveData():



""" Put new data into acceptedData[], but only new data. discard old data, and return the new data. """
def getNewAcceptedData():



""" Put new data into rejectedData[], but only new data. discard old data, and return the new data. """
def getNewRejectedData():
    output_invalid_user = os.system("grep -i 'sshd' /var/log/system.log | grep 'Invalid user'")
    output_disconnect = os.system("grep -i 'sshd' /var/log/system.log | grep 'Received disconnect'")
    output_auth_falure = os.system("grep -i 'sshd' /var/log/system.log | grep 'authentication error'")


if __name__ == '__main__':


























