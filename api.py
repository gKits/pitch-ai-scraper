from requests import get


request_url = (
    'https://pitchai-api-prod.proplayai.com/'
    'v1/Pitch/GetPitchReport?value=NTc1MDM'
)


def get_pitch_report(
    request_url: str,
    pitch_id: str,
    retry_counter: int = 0
):
    '''
    This method will make an API call and get the PitchAI

    :param: request_url: The URL to get the PitchAI pitch report
    :param: pitch_id: The Pitch ID

    :return: pitch_report: The pitch report data from the API response
    '''
    pitch_report = get(f'{request_url}{pitch_id}')

    if not pitch_report and retry_counter < 3:
        get_pitch_report(
            request_url=request_url,
            pitch_id=pitch_id,
            retry_counter=retry_counter+1
        )
    elif not pitch_report and retry_counter >= 3:
        return
    else:
        return pitch_report
