"""Модуль вычисления"""

from information_system_design import usecase


def calculate_with_all(*args, **kwargs):
    return usecase.use_calculate_with_all(*args, **kwargs)


def calculate_with_several(*args, **kwargs):
    return usecase.use_calculate_with_several(*args, **kwargs)
