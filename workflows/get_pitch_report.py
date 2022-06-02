from typing import Dict
from requests import get
from logging import error, info


def get_pitch_report_workflow(
    request_url: str,
    pitch_url: str,
    headers: Dict
):
    '''
    This method get the pitch report

    :param: request_url: The request url
    :param: pitch_url: The URL leading to the pitch report
    :param: headers: The request headers
    :return:
    '''
    return get_pitch_id(
        request_url=request_url,
        pitch_url=pitch_url,
        headers=headers
    )


def get_pitch_id(
    request_url: str,
    pitch_url: str,
    headers: Dict
):
    '''
    This method will extract the pitch ID from the pitch URL

    :request_url: The non-final request url missing the pitch ID
    :param: pitch_url: The default URL leading to the pitch report
    :headers: headers: The non-final request headers missing the pitch ID
    :return:
    '''
    try:
        pitch_id = pitch_url.split('/')[-1].replace('%3D', '')
        info('Extracted pitch id {} from {}'.format(
            pitch_id,
            pitch_url
            )
        )
        return add_pitch_id_to_request_url_and_headers(
            request_url=request_url,
            pitch_id=pitch_id,
            headers=headers
        )

    except TypeError:
        return error('{} is not a valid url'.format(pitch_url))


def add_pitch_id_to_request_url_and_headers(
    request_url: str,
    pitch_id: str,
    headers: Dict
):
    '''
    This method will add the pitch ID into the request URL and headers

    :request_url: The non-final request url missing the pitch ID
    :param: pitch_url: The default URL leading to the pitch report
    :headers: headers: The non-final request headers missing the pitch ID
    :return:
    '''
    headers['Path'] = headers['Path'].format(pitch_id)
    info('Added pitch id {} to request URL and request headers'.format(
        pitch_id
        )
    )
    return get_pitch_report(
        request_url=request_url.format(pitch_id),
        headers=headers
    )


def get_pitch_report(
    request_url: str,
    headers: Dict,
    retry_counter: int = 0
):
    '''
    This method will make an API call and get the PitchAI

    :param: request_url: The final request URL
    :param: headers: The final request headers
    :return:
    '''
    pitch_report = get(
        url=request_url,
        headers=headers
    ).json()

    if not pitch_report and retry_counter < 3:
        get_pitch_report(
            request_url=request_url,
            headers=headers,
            retry_counter=retry_counter+1
        )

    elif not pitch_report and retry_counter >= 3:
        return error('No pitch report found at {}'.format(
            request_url
            )
        )

    else:
        return pitch_report_no_empty(
            pitch_report=pitch_report
        )


def pitch_report_no_empty(
    pitch_report: Dict
):
    '''
    This method will check if the pitch report isn't empty

    :param: pitch_report: The pitch report data
    :return:
    '''
    if 'kinematics' in pitch_report['result']:
        info('Got pitch report')
        return pitch_report
    else:
        return error('Pitch report does not contain kinematics data')
