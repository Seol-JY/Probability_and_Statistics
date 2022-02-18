# tkinter
import tkinter as tk
# font 사용
import tkinter.font
# 그래프를 그리기위한  matplotlib
import matplotlib.pyplot as plt
# matplotlib를 tkinter 내에서 사용 가능하도록
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 확률 실험을 위한 난수 추출용
import secrets
# 경과 시간 측정을 위해
import time
# Combination 계산을 위해
import operator as op
from functools import reduce  # ,,
from tkinter import ttk


def ncr(n, r):                                                                    # nCr 계산 함수
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def normalFunS(x, mu, sd):
    output = 1/(sd*((2*3.141592653589793))**(1/2)) * \
        2.718281828459045**(-(x-mu)**2/(2*sd**2))
    return output


# 확률실험을 수행하는 함수
def exper_Binomial(_event=None):
    num = int(number.get())
    prob = float(probability.get())
    # sample의 크기를 가져옴
    rs_value = int(rs.get())
    # 확률을 가지는 임의추출을 만들기 위해
    r_sample = [1 for _ in range(int(prob*1000))]
    tmp = [0 for _ in range(int(1000-prob*1000))]
    r_sample += tmp
    prob_list = []
    for _ in range(rs_value):
        prob_list.append([secrets.choice(r_sample)
                         for _ in range(num)].count(1))
    exper_data = []
    for i in range(num+1):
        exper_data.append(prob_list.count(i)/rs_value)
    return exper_data, prob_list


# 확률실험 과정을 설명하는 새창 생성
def newWindow(value):
    window2 = tk.Toplevel(window)
    window2.title('Experiment Result')
    window2.geometry('500x800')
    window2.resizable(True, True)
    window2.config(bg="white")

    ptn = tk.Text(window2)
    ptn.configure(state='normal')
    ptn.place(x=7, y=10, width=480, height=700)
    for i, j in enumerate(value):
        ptn.insert('current', f'{j:>3}')
        if i % 14-13 == 0:
            ptn.insert('current', '\n')
    ptn.configure(state='disabled')

    window2.mainloop()


def Binomial(_event=None):

    x = time.time()
    num = int(number.get())
    prob = float(probability.get())
    data = [ncr(num, i)*(prob**i)*((1-prob)**(num-i))
            for i in range(num+1)]        # 이론값 그래프 y축

    figure = plt.Figure(figsize=(10, 4.5), dpi=100)
    ax = figure.add_subplot(111)

    ax.plot(data, label="Simulation")

    ax.plot([normalFunS(x, num*prob, (num*prob*(1-prob))**(1/2))
            for x in range(0, num+1)], label="Normal Distribution")

    if autoint.get() == 1:
        # value = 실험값 그래프 y축
        value = exper_Binomial()
        ax.plot(value[0], label="Experimental")

    ax.set_xlabel("x")
    ax.set_ylabel("P(X=x)")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(loc="best")

    chart_type = FigureCanvasTkAgg(figure, window)
    chart_type.get_tk_widget().place(x=35, y=170)
    y = time.time()
    tme['text'] = f'{(y-x):0.2f}초'
    if autoint.get() == 1:
        newWindow(value[1])


window = tk.Tk()

window.title('Binomial Distribution Experiment')
window.geometry('1300x800')
window.resizable(True, True)
window.config(bg="white")
window.bind('<Return>', Binomial)

font = tkinter.font.Font(family="맑은 고딕", size=18, weight="bold")
tit = tk.Label(window, text='                           Binomial Distribution Experiment                           ',
               borderwidth=1, relief='flat', font=font, bg="#F5F5F5")
tit.place(x=-2, y=-2, width=1300, height=80)


figure = plt.Figure(figsize=(10, 4.5), dpi=100)
ax = figure.add_subplot(111)
ax.plot()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
chart_type = FigureCanvasTkAgg(figure, window)
chart_type.get_tk_widget().place(x=35, y=170)


font2 = tkinter.font.Font(family="맑은 고딕", size=14,
                          weight="bold", slant="italic")
font3 = tkinter.font.Font(family="맑은 고딕", size=12)

txt1 = tk.Label(window, text='n = ', relief="flat", font=font2, bg="white")
txt1.place(x=235, y=120, width=50, height=45)

number = tk.Entry(window, relief="groove", borderwidth=0.5, bg="#F5F5F5")
number.place(x=285, y=125, width=100, height=45)

txt2 = tk.Label(window, text='p = ', relief="flat", font=font2, bg="white")
txt2.place(x=435, y=120, width=50, height=45)
probability = tk.Entry(window, relief="groove", borderwidth=0.5, bg="#F5F5F5")
probability.place(x=485, y=125, width=100, height=45)

txt3 = tk.Label(window, text='RS =', relief="flat", font=font3, bg="white")
txt3.place(x=610, y=122, width=50, height=45)
rs = tk.Entry(window, relief="groove", borderwidth=0.5, bg="#F5F5F5")
rs.place(x=665, y=125, width=100, height=45)

btn = tk.Button(window, text='Go', relief="groove", command=Binomial)
btn.place(x=820, y=125, width=110, height=45)

tme = tk.Label(window, text='경과 시간', borderwidth=2,
               relief='flat')     # 시간 표시 라벨
tme.place(x=940, y=125, width=91, height=45)

# 체크박스의 선택여부를 나타내는 변수
autoint = tk.IntVar()
action = ttk.Checkbutton(window, text='확률실험 진행', variable=autoint)   # 체크박스
action.place(x=154, y=100)

window.mainloop()
