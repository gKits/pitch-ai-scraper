from workflows.get_pitch_report import get_pitch_report_workflow


request_url = (
    'https://pitchai-api-prod.proplayai.com/v1/Pitch/GetPitchReport?value={}='
)

headers = {
    'Authority': 'pitchai-api-prod.proplayai.com',
    'Referer': 'https://pitchai.proplayai.com/',
    'ProplayAIAPIKey': 'e38bbd45-4375-4b20-bda0-bdbc5f3123b2',
    'Path': '/v1/Pitch/GetPitchReport?value={}='
}


print(get_pitch_report_workflow(
    request_url=request_url,
    pitch_url='https://pitchai.proplayai.com/shared/report/pitch/NTc1MDM%3D',
    headers=headers
    )
)
