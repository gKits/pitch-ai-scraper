from typing import Dict, List
from logging import error, info
from json import loads


def get_kinamtics_data_workflow(
    pitch_report: Dict
):
    '''
    This method will get the kinematics data from the pitch report data

    :param: pitch_report: The pitch report data
    :return:
    '''
    return get_frame_by_frame_data_and_key_list(
        pitch_report=pitch_report
    )


def get_frame_by_frame_data_and_key_list(
    pitch_report: Dict
):
    '''
    This method will get the frame-by-frame data

    :param: pitch_report: The pitch report data
    :return:
    '''
    try:
        key_list = loads(
            pitch_report['result']['kinematics']
        )['angle_list']
        frame_data = loads(
            pitch_report['result']['kinematics']
        )['frames']
    except (KeyError, TypeError, IndexError):
        return error('Unknow error')

    if frame_data:
        info('Retrived frame data')
        return sort_data_by_key_list(
            frame_data=frame_data,
            key_list=key_list
        )
    else:
        return error('Frame data is missing')


def sort_data_by_key_list(
    frame_data: Dict,
    key_list: List
):
    '''
    This method will sort the kinematics data by the key list

    :param: frame_data: The frame-by-frame kinematics data
    :param: key_list: The list with the key names
    :return:
    '''
    try:
        vel_ang_plot = {}
        for key in key_list:
            vel_ang_plot[key] = {
                'velocity': [],
                'angle': []
            }
        for frame in frame_data:
            for i, key in enumerate(key_list):
                vel_ang_plot[key]['velocity'].append(frame['velocity'][i])
                vel_ang_plot[key]['angle'].append(frame['angle'][i])

        return vel_ang_plot
    except (KeyError, TypeError, IndexError):
        return error('Unknow error')
