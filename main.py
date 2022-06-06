from json import dump
from workflows.get_pitch_report import get_pitch_report_workflow
from workflows.get_kinematics_data import get_kinamtics_data_workflow


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

pitch_report = get_pitch_report_workflow(
    request_url=request_url,
    pitch_url='https://pitchai.proplayai.com/shared/report/pitch/NTc1MDM%3D',
    headers=headers
)

if pitch_report:
    kine = get_kinamtics_data_workflow(
        pitch_report=pitch_report
    )
    with open('j.json', 'w') as write:
        dump(kine, write, indent=4)
