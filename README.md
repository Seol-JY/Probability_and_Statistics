# Probability and Statistics
**Probability and Statistics with Python**
|Files|
|---|
|Frequency_Distribution.py|
|Confidence_Level_Simulation.py|
|Binomial_Distribution_Experiment.py|


## Frequency_Distribution
![1](https://i.imgur.com/wJpdlQx.png)  
  
**주어진 값을 분석해 도수분포표와 그래프를 출력**
```Python
sample = [11.8, 18.5, 17.4, ... ,16.8, 14.3, 22.1, 12.4, 23, 16.6, 19.8]
Rtn_list = Analyzer(sample)
mk_Table(Rtn_list)
mk_Histogram(Rtn_list)
```
|Object|설명|
|---|---|
|sample|분석할 데이터를 할당|
|Analyzer()|sample을 분석해 도수분포표를 구성하는 내용을 반환|
|mk_Table()|도수분포표 출력 함수|
|mk_Histogram()|도수분포그래프 출력 함수|

## Confidence_Level_Simulation
![2](https://i.imgur.com/aiSvwog.png)  
  
**신뢰수준 95%를 기반으로 확률 실험을 진행하며, 각 실험에 대한 크기, 점추정치, 표본표준편차, 신뢰구간 상한, 하한값을 가지는  
총 100가지의 실험의 결과를 표로 출력**  
```Python
def simulation(mean, deviation, confidence_level, size, trial):
  ...
  normal_lis = np.random.normal(mean, deviation, size)
  ...
...

ptn_Table(simulation(4, 1, 1.96, 100, 100))

```

|Object|설명|
|---|---|
|simulation()|실험 진행 함수|
|ptn_Table()|실험결과 출력 함수|
|confidence_level|1.96=95%, 2.58=99%|
|mean,deviation,size|평균, 표준편차, 개수|
|trial|시행횟수|

## Binomial_Distribution_Experiment
![3](https://i.imgur.com/ztO8EDV.png)  

**[GUI] 이항 분포 그래프 및 정규분포 그래프 작성**
```Python
window = tk.Tk()

window.title('Binomial Distribution Experiment')
window.geometry('1300x800')
window.resizable(True, True)
window.config(bg="white")
window.bind('<Return>', Binomial)

...

window.mainloop()
```
|Object|설명|
|---|---|
|ncr()|Combination|
|normalFunS()|1/(sd*((2*3.141592653589793))**(1/2)) * \2.718281828459045**(-(x-mu)**2/(2*sd**2))|
|exper_Binomial()|확률실험 수행|
|Binomial|그래프 생성|