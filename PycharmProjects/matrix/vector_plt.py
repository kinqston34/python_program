import matplotlib.pyplot as plt
import seaborn
seaborn.reset_orig()
def plot_a_vector(x,y):
    x0,y0 = 0,0     #定義向量起始點
    dx,dy = x,y     #定義向量終點
    max_val = max(abs(dx),abs(dy))+2
    plt.xlim(-max_val,max_val) #設定x軸 xlim(left,right)
    plt.ylim(-max_val, max_val)
    ax = plt.gca()  #設定坐標軸 ，如沒有建立一個
    ax.spines['top'].set_color('none')     # 設定上面線條
    ax.spines['right'].set_color('none')    # 設定下面線條
    #將兩邊設定到原點
    ax.xaxis.set_ticks_position('bottom')   #set_t_p ={'top', 'bottom', 'both', 'default', 'none'}
    ax.spines['bottom'].set_position(('data', 0))  #設定以零為準
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    #標註文字
    adjust= (0.5 if dx >= 0 else -3)
    ax.annotate('({}, {})'.format(dx,dy),xy=(dx,dy),xytext = (dx+adjust,dy)) #annotat(註解樣式,註解點,註解顯示調整)
    #劃出向量
    plt.arrow(x0,y0,dx,dy,length_includes_head = True,head_width=0.3)
    tick = 3 #設定刻度
    plt.xticks(range(-max_val + 1,max_val - 1, tick)) #tick: 刻度
    plt.yticks(range(-max_val + 1,max_val - 1, tick))
    return ax
plt.subplot(2,2,1)
plot_a_vector(8,8)
plt.subplot(2,2,2)
plot_a_vector(-5,6)
plt.subplot(2,2,3)
plot_a_vector(-3,-6)
plt.subplot(2,2,4)
plot_a_vector(8,-5)
plt.show()
