import tkinter as tk
import tkinter.ttk as ttk
import GCD_LCM

#创建窗口
window = tk.Tk()
window.title("my window")
window.geometry("350x200")



#检查输入的内容是否为数字
def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False

reg = window.register(correct)



#创建两个tab标签，用于切换两种计算页面
tab = ttk.Notebook(window)

#tab里需要一个child，也就是frame作为容器
frame1 = tk.Frame(tab)
tab1 = tab.add(frame1, text = "最大公因数")

#创建3个输入框
f1_inpbox1 = tk.Entry(frame1)
f1_inpbox1.pack()
f1_inpbox2 = tk.Entry(frame1)
f1_inpbox2.pack()
f1_inpbox3 = tk.Entry(frame1)
f1_inpbox3.pack()

#检查3个输入框输入的内容是否为数字
f1_inpbox1.config(validate="key", validatecommand=(reg,"%P"))
f1_inpbox2.config(validate="key", validatecommand=(reg,"%P"))
f1_inpbox3.config(validate="key", validatecommand=(reg,"%P"))

#调用自定义函数
def start_count1():
    num1 = GCD_LCM.my_prime_factorization(int(f1_inpbox1.get()))
    num2 = GCD_LCM.my_prime_factorization(int(f1_inpbox2.get()))
    num3 = GCD_LCM.my_prime_factorization(int(f1_inpbox3.get()))
    a =  GCD_LCM.gcd_count(num1,num2,num3)
    label1.config(text="最大公因数为：" + str(a))

f1_btn1 = tk.Button(frame1, text="开始计算", command=start_count1)
f1_btn1.pack()

label1 = tk.Label(frame1, text="")
label1.pack()



frame2 = tk.Frame(tab)
tab2 = tab.add(frame2, text = "最小公倍数")

f2_inpbox1 = tk.Entry(frame2)
f2_inpbox1.pack()
f2_inpbox2 = tk.Entry(frame2)
f2_inpbox2.pack()
f2_inpbox3 = tk.Entry(frame2)
f2_inpbox3.pack()

f2_inpbox1.config(validate="key", validatecommand=(reg,"%P"))
f2_inpbox2.config(validate="key", validatecommand=(reg,"%P"))
f2_inpbox3.config(validate="key", validatecommand=(reg,"%P"))

def start_count2():
    num1 = GCD_LCM.my_prime_factorization(int(f2_inpbox1.get()))
    num2 = GCD_LCM.my_prime_factorization(int(f2_inpbox2.get()))
    num3 = GCD_LCM.my_prime_factorization(int(f2_inpbox3.get()))
    a =  GCD_LCM.lcm_count(num1,num2,num3)
    label2.config(text="最小公倍数为：" + str(a))

f2_btn1 = tk.Button(frame2, text="开始计算", command=start_count2)
f2_btn1.pack()

label2 = tk.Label(frame2, text="")
label2.pack()


tab.pack(expand=True, fill=tk.BOTH)



window.mainloop()