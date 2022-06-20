import argparse
from json import dump
from workflows.get_pitch_report import get_pitch_report_workflow
from workflows.get_kinematics_data import get_kinamtics_data_workflow


def parser() -> argparse.Namespace:
    '''
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        'pitchURL',
        type=str,
        help='an url leading to a pitch report'
    )
    parser.add_argument(
        '-p', '--path',
        type=str,
        help='the path were the .json file is saved'
    )
    args = parser.parse_args()

    return args
    

def main():
    '''
    This is the main method

    :param:
    :return:
    '''
    request_url = (
    'https://pitchai-api-prod.proplayai.com/v1/Pitch/'
    'GetUnsubscribedUserPitchReport?value={}='
    )


    headers = {
        'Authority': 'pitchai-api-prod.proplayai.com',
        'Referer': 'https://pitchai.proplayai.com/',
        'ProplayAIAPIKey': 'e38bbd45-4375-4b20-bda0-bdbc5f3123b2',
        'Path': '/v1/Pitch/GetUnsubscribedUserPitchReport?value={}='
    }

    args = parser

    pitch_report = get_pitch_report_workflow(
        request_url=request_url,
        pitch_url=args['pitchURL'],
        headers=headers
    )

    kinematics_data = get_kinamtics_data_workflow(pitch_report=pitch_report)

    with open('kinematics.json', 'w') as write:
        dump(
            kinematics_data,
            write,
            indent=4
        )


if __name__ == "__main__":
    main()
