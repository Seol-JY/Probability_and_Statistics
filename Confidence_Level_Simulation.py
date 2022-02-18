import numpy as np
import os


def ptn_Table(value):                       # to make Table
    top = '┌─────────────────────────────┐'
    title = '│ Confidence Level Simulation │'
    bottom = '└─────────────────────────────┘'
    print(f' {top:^111}')
    print(f' {title:^111}')
    print(f' {bottom:^111}')
    print(f'    ┌─────────────┬──────────┬────────────────┬──────────────┬────────────────┬────────────────┬────────────┐')
    print(f'    │     num     │   size   │ point_estimate │ 표본표준편차 │ confidence_min │ confidecne_max │ unreliable │')
    for i in range(len(value[0])):
        print(f'    ├─────────────┼──────────┼────────────────┼──────────────┼────────────────┼────────────────┼────────────┤')
        print(
            f'    │  exper{i+1:>4}  │{value[0][i][0]:>9} │         {value[0][i][1]:>1.4f} │       {value[0][i][2]:>1.4f} │         {value[0][i][3]:>1.4f} │         {value[0][i][4]:1.4f} │      {value[0][i][5]}     │')
    print(f'    └─────────────┴──────────┴────────────────┴──────────────┴────────────────┴────────────────┴────────────┘')
    print(f'    ┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐')
    print(
        f'    │    모평균: {value[1][0]:<4}    모 표준편차: {value[1][1]:<4}                                                                  │')
    print(f'    └───────────────────────────────────────────────────────────────────────────────────────────────────────┘')


def simulation(mean, deviation, confidence_level, size, trial):  # for Simulation
    rtn_list = []
    for i in range(trial):
        normal_lis = np.random.normal(mean, deviation, size)
        point_estimate = sum(normal_lis)/size
        sp_deviation = (
            sum([(point_estimate - value)**2 for value in normal_lis]) / size)**0.5
        confidence_min = point_estimate - \
            sp_deviation*confidence_level/(size**0.5)
        confidence_max = point_estimate + \
            sp_deviation*confidence_level/(size**0.5)
        if not(confidence_min <= mean and mean <= confidence_max):
            unreliable = "X"
        else:
            unreliable = "O"
        rtn_list.append([size, point_estimate, sp_deviation, confidence_min,
                        confidence_max, unreliable])  # 점 추정치 표본표준편차 신뢰구간 최저/최고
    info = [mean, deviation]
    return (rtn_list, info)


ptn_Table(simulation(4, 1, 1.96, 100, 100))
os.system("pause")
