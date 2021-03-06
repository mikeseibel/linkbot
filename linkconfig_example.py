# LinkBot Configuration

import os
from ast import literal_eval

API_TOKEN = os.environ.get('API_TOKEN')
LOG_FILE = os.environ.get('LOG_FILE', 'linkbot.log')
JIRA_HOST = os.environ.get('JIRA_HOST')
UW_SAML_CREDENTIALS = os.environ.get('UW_SAML_CREDENTIALS')
SERVICE_NOW_HOST = os.environ.get('SERVICE_NOW_HOST')
SERVICE_NOW_CREDENTIALS = os.environ.get('SERVICE_NOW_CREDENTIALS')


LINKBOTS = []


if SERVICE_NOW_HOST and SERVICE_NOW_CREDENTIALS:
    LINKBOTS.append({
        'LINK_CLASS': 'ServiceNowBot',
        'HOST': SERVICE_NOW_HOST,
        'AUTH': literal_eval(SERVICE_NOW_CREDENTIALS)
    })

if JIRA_HOST:
    if UW_SAML_CREDENTIALS:
        LINKBOTS.append({
            'LINK_CLASS': 'JiraLinkBot',
            'HOST': JIRA_HOST,
            'AUTH': literal_eval(UW_SAML_CREDENTIALS)
        })
    else:
        LINKBOTS += [
            {
                'MATCH': 'req[0-9]+',
                'LINK': '<{}/u_simple_requests.do?sysparm_type=labels'
                '&sysparm_table=u_simple_requests'
                '&sysparm_query=number=%s|%s>'.format(JIRA_HOST)
            },
            {
                'MATCH': 'inc[0-9]+',
                'LINK': '<{}/incident.do?sys_id=%s|%s>'.format(JIRA_HOST)
            },
            {
                'MATCH': '[Kk][Bb][0-9]+',
                'LINK': '<{}/nav_to.do?uri=/kb_view.do?'
                'sysparm_article=%s|%s>'.format(JIRA_HOST),
            },
        ]
