import random
import math
import os


def mk_Table(Rtn_list):

    Rel_total = 0
    Freq_total = 0

    print()
    print(' '*63, end="")
    print('┌──────────────────────────────┐')
    print(' '*63, end="")
    print('│ Frequency Distribution Table │')
    print(' '*63, end="")
    print('└──────────────────────────────┘')
    print(' ┌──────────────┬─────────────────┬─────────────────┬──────────────────┬─────────────────────┬──────────────────┬─────────────────────┬─────────────────┐')
    print(' │    Number    │      Class      │    Frequency    │    Rel. Freq.    │    Percentage(%)    │   Accum. Freq.   │  Accum. Rel. Freq.  │    Class Mark   │')
    for decomposed_list in Rtn_list:
        Rel_total += decomposed_list[4]
        Freq_total += decomposed_list[3]
        print(' ├──────────────┼─────────────────┼─────────────────┼──────────────────┼─────────────────────┼──────────────────┼─────────────────────┼─────────────────┤')
        print(f' │ No.{decomposed_list[0]:>10}│{decomposed_list[1]:^8}~{decomposed_list[2]:^8}│{decomposed_list[3]:>17}│{decomposed_list[4]:>18.3f}│{decomposed_list[5]:>19.2f} %│{Freq_total:>18}│{Rel_total:>21.2f}│{decomposed_list[6]:>17}│')
    print(' ├──────────────┼─────────────────┼─────────────────┼──────────────────┼─────────────────────┼──────────────────┼─────────────────────┼─────────────────┤')
    percentage_total = Rel_total*100
    print(
        f' │     Total    │                 │{Freq_total:>17}│{Rel_total:>18.2f}│ {percentage_total:>18.2f} %│                  │                     │                 │')
    print(' └──────────────┴─────────────────┴─────────────────┴──────────────────┴─────────────────────┴──────────────────┴─────────────────────┴─────────────────┘')


def Analyzer(sample):
    # The Number of Sample
    nos = len(sample)
    noc = round(nos**(1/2)) if nos <= 200 else round(1 +
                                                     3.3*math.log10(nos))   # The Number of Class

    # List for Return
    Rtn_list = []

    # Initial Class Value
    icv = min(sample)-0.5

    Class_Interval = float(math.ceil((max(sample) - min(sample)) / noc))

    for no in range(1, noc+1):
        Analyzed_Value = []    # List Element: [Number, Most_Class_Value, Least_Class_Value, Frequency, Relative_Frequency, Percentage, Class Mark]
        # 0. Number
        Analyzed_Value.append(no)
        # 1. Most_Class_Value
        Analyzed_Value.append(icv)
        icv += Class_Interval
        # 2. Least_Class_Value
        Analyzed_Value.append(icv)
        tmp = [i for i in sample if icv - Class_Interval <= i < icv]
        # 3. Frequency
        Analyzed_Value.append(len(tmp))
        # 4. Relative_Frequency
        Analyzed_Value.append(len(tmp)/nos)
        # 5. Percentage
        Analyzed_Value.append(len(tmp)/nos*100)
        # 6. Class Mark
        Analyzed_Value.append(icv - Class_Interval/2)

        # Add to Return List
        Rtn_list.append(Analyzed_Value)

    return Rtn_list


def mk_Histogram(Rtn_list):
    # 그래프 높이들을 저장할 리스트
    boundary = []
    # 그래프 마지막 줄 출력을 위한 변수
    pixels_last = 0

    print()

    for decomposed_list2 in Rtn_list:
        # Percentage값을 가져온다
        tmp = decomposed_list2[5]
        bry = int(25 - (tmp//4 + (0 if tmp % 4 < 2 else 1))
                  )                  # 그래프 높이 계산
        boundary.append(bry)

    pixels = [[' 1.0 ─┐'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              [' 0.8 ─┤'],
              ['      ┤'],    # 그래프 출력을 위한 2차원 배열
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              [' 0.6 ─┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              [' 0.4 ─┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              [' 0.2 ─┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              ['      ┤'],
              ['   0 ─┴'],
              ['       ']]

    for tp in boundary:
        if tp == 25:
            # 그래프 x축 구성 (그래프의 높이가 0일때)
            pixels[25].append('─────────')
            for tp2 in range(0, tp):
                # 공백
                pixels[tp2].append('         ')
        else:
            # 그래프 최상단
            pixels[tp].append(' ┌─────┐ ')
            for tp2 in range(0, tp):
                # 공백
                pixels[tp2].append('         ')
            for tp2 in range(tp+1, 25):
                pixels[tp2].append(' │     │ ')
            # 그래프 x축 구성
            pixels[25].append('─┴─────┴─')

        # 그래프 맨 마지막줄 구성
        pixels[26].append(f'{Rtn_list[pixels_last][6]:^9}')
        pixels_last += 1

    print()
    print(' '*(6+9*len(boundary)//2-18), end='')
    print('┌──────────────────────────────────┐')
    print(' '*(6+9*len(boundary)//2-18), end='')
    print('│ Frequency Distribution Histogram │')
    print(' '*(6+9*len(boundary)//2-18), end='')
    print('└──────────────────────────────────┘')

    for tp in pixels:                                                        # 그래프 출력
        for i in tp:
            print(i, end='')
        print()

    print()


#os.system('color F0')
os.system('cls')

sample = [11.8, 18.5, 17.4, 17.4, 24.8, 16.3, 20.8, 13.5, 6, 8.9, 5.7, 16.1, 19, 8.5, 22.6, 12.5, 19, 19.6, 15.7, 20.3, 2, 12.9, 29, 11.4, 16, 5, 8.3, 15, 13.5, 11.8, 23.3, 21.4, 5.5, 17.1, 7.3, 5.5, 10.3, 19.4, 19.8, 14, 19.9,
          15.1, 26.4, 14.4, 10.1, 22.4, 15.6, 21, 14.9, 11.9, 13.4, 6.5, 10, 6.8, 20.1, 5.5, 11.9, 15.3, 21.4, 23.5, 17.8, 6.5, 2, 13.5, 17.6, 18.2, 14.9, 20.7, 15.3, 10.4, 18.2, 21.2, 9.4, 18.1, 16.8, 14.3, 22.1, 12.4, 23, 16.6, 19.8]

Rtn_list = Analyzer(sample)

mk_Table(Rtn_list)
mk_Histogram(Rtn_list)

os.system('pause')
os.system('cls')
