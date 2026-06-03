---
title: "第6章 有限脉冲响应(FIR)数字滤波器的设计"
source: "第6章 有限脉冲响应(FIR)数字滤波器的设计.pdf"
pages: 26
doc_type: book
language: zh
structure_source: llm_scan
parsed_at: 2026-05-28T07:14:02Z
---

<!-- pages: 1-4 -->
# 第 6 章 有限脉冲响应(FIR)数字滤波器的设计

本章内容与教材第7章内容相对应。
有限脉冲响应(FIR)数字滤波器最大的优点是容易设计成线性相位特性。在数字信号传输与处理及图像信号处理中，要求系统具有线性相位特性。但由于FIR滤波器为全零点系统，所以对同一幅频特性要求，用FIR滤波器实现要比用IIR滤波器实现阶数高得多。所以，一般在必须要求线性相位时，选用FIR滤波器。下面先总结线性相位FIR数字滤波器的特点(条件)，这些特点就是设计线性相位FIR滤波器的约束条件。

## 6.1 学习要点

### 6.1.1 线性相位概念与具有线性相位的FIR数字滤波器的特点

**1. 线性相位概念**

设 $H(\mathrm{e}^{\mathrm{j}\omega}) = \mathrm{FT}[h(n)]$ 为FIR滤波器的频响特性函数。$H(\mathrm{e}^{\mathrm{j}\omega})$ 可表示为
$$H(\mathrm{e}^{\mathrm{j}\omega}) = H_{\mathrm{g}}(\omega)\mathrm{e}^{\mathrm{j}\theta(\omega)}$$
$H_{\mathrm{g}}(\omega)$ 称为幅度函数，为 $\omega$ 的实函数。应注意 $H_{\mathrm{g}}(\omega)$ 与幅频特性函数 $|H(\mathrm{e}^{\mathrm{j}\omega})|$ 的区别，$|H(\mathrm{e}^{\mathrm{j}\omega})|$ 为 $\omega$ 的正实函数，而 $H_{\mathrm{g}}(\omega)$ 是一个可取负值的实函数。
$\theta(\omega)$ 称为相位特性函数，当 $\theta(\omega) = -\omega\tau$ 时，称为第一类(A类)线性相位特性；当 $\theta(\omega) = \theta_0 - \omega\tau$ 时，称为第二类(B类)线性相位特性。$\theta_0 = -\pi/2$ 是第二类线性相位特性常用的情况，所以本书仅考虑这种情况。

**2. 具有线性相位的FIR滤波器的特点（$h(n)$长度为 $N$）**

**1）时域特点**

A类
$$\begin{cases} h(n) = h(N-1-n) \quad h(n) \text{ 关于 } n = \frac{N-1}{2} \text{ 偶对称} \\ \theta(\omega) = -\omega \frac{N-1}{2} \end{cases} \tag{6.1.1}$$

B类
$$\begin{cases} h(n) = -h(N-1-n) \quad h(n) \text{ 关于 } n = \frac{N-1}{2} \text{ 奇对称} \\ \theta(\omega) = -\frac{\pi}{2} - \omega \frac{N-1}{2} \end{cases} \tag{6.1.2}$$

群延时，
$$\frac{\mathrm{d}\theta(\omega)}{\mathrm{d}\omega} = \tau = \frac{N-1}{2}$$

为常数，所以将A类和B类线性相位特性统称为恒定群延时特性。

**2）频域特点**

A类
$\begin{cases} N \text{为奇数(情况1)}: H_{\mathrm{g}}(\omega) \text{关于} \omega=0, \pi, 2\pi \text{三点偶对称} \\ N \text{为偶数(情况2)}: H_{\mathrm{g}}(\omega) \text{关于} \omega=\pi \text{奇对称}(H_{\mathrm{g}}(\pi)=0) \end{cases}$

B类
$\begin{cases} N \text{为奇数(情况3)}: H_{\mathrm{g}}(\omega) \text{关于} \omega=0, \pi, 2\pi \text{三点奇对称} \\ N \text{为偶数(情况4)}: H_{\mathrm{g}}(\omega) \text{关于} \omega=0, 2\pi \text{奇对称，关于} \omega=\pi \text{偶对称} \end{cases}$

**3）结论**

掌握以上特点，就可以得出如下结论，这些结论对FIR滤波器的设计很重要。
(1) 情况1：可以实现所有滤波特性(低通、高通、带通、带阻和点阻等)。
(2) 情况2：$H_{\mathrm{g}}(\pi)=0$，不能实现高通、带阻和点阻滤波器。
(3) 情况3：只能实现带通滤波器(因为 $H_{\mathrm{g}}(0)=H_{\mathrm{g}}(\pi)=H_{\mathrm{g}}(2\pi)=0$)。
(4) 情况4：不能实现低通、带阻和点阻滤波器。

### 6.1.2 FIR数字滤波器设计方法

教材中主要介绍了FIR-DF的3种设计方法，即窗函数法、频率采样法、等波纹最佳逼近法。

这3种设计方法的设计原理及设计步骤教材中讲得很清楚，本书不再重复，读者只要认真学习教材，并参考例题和习题解答，就可以掌握本章的知识和方法。

下面仅举一个例子，用窗函数设计法的概念证明一个重要的结论，使读者正确理解所谓的最佳设计法，其设计效果与设计的最佳准则有关，以一个最佳准则设计的最佳滤波器，在另一个最佳准则下可能就不是最佳的，甚至很差，以至于无实际应用价值。

**[例6.1.1]** 试证明在窗函数设计法中，当 $h(n)$ 长度 $N$ 值固定时，矩形窗设计结果满足频域最小均方误差逼近准则。

**解:** 仿照窗函数设计法的过程，设 $H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega})$ 表示期望逼近的理想滤波器频率响应，其单位脉冲响应为 $h_{\mathrm{d}}(n)$。用 $w(n)$ 表示窗函数，长度为 $N$；用 $h(n)$ 表示用窗函数法设计的实际FIR滤波器单位脉冲响应(即 $h(n)=h_{\mathrm{d}}(n)w(n)$)，其频率响应函数为 $H(\mathrm{e}^{\mathrm{j}\omega})$。

定义 $H(\mathrm{e}^{\mathrm{j}\omega})$ 与 $H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega})$ 的均方误差为
$$\varepsilon^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} | H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega}) - H(\mathrm{e}^{\mathrm{j}\omega}) |^2 \mathrm{d}\omega$$

本例题就是要求证明：当 $w(n)=R_N(n)$ 时，$\varepsilon^2$ 最小。由于证明的条件与窗函数 $w(n)$ 的类型(形状)有关，所以，将 $\varepsilon^2$ 转换到时域表示，有利于证明。证明如下：

(1) 令误差函数
$$E(\mathrm{e}^{\mathrm{j}\omega}) = H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega}) - H(\mathrm{e}^{\mathrm{j}\omega})$$

由于 $E(\mathrm{e}^{\mathrm{j}\omega})$ 为周期函数，所以可展开为幂级数
$$E(\mathrm{e}^{\mathrm{j}\omega}) = \sum_{n=-\infty}^{\infty} e(n) \mathrm{e}^{-\mathrm{j}\omega n}$$

(2) 用系数 $e(n)$ 表示均方误差 $\varepsilon^2$。
(3) 证明只有当 $w(n)=R_N(n)$，$h(n)=h_{\mathrm{d}}(n)R_n(n)$ 时，$\varepsilon^2$ 最小。
下面按三步证明：

(1) 因为
$$H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega}) = \sum_{n=-\infty}^{\infty} h_{\mathrm{d}}(n) \mathrm{e}^{-\mathrm{j}\omega n}, \quad H(\mathrm{e}^{\mathrm{j}\omega}) = \sum_{n=-\infty}^{\infty} h(n) \mathrm{e}^{-\mathrm{j}\omega n}$$
所以
$$E(\mathrm{e}^{\mathrm{j}\omega}) = H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega}) - H(\mathrm{e}^{\mathrm{j}\omega}) = \sum_{n=-\infty}^{\infty} [h_{\mathrm{d}}(n) - h(n)] \mathrm{e}^{-\mathrm{j}\omega n}$$
由于 $h(n)$ 长度为 $N$，即当 $n<0$ 或 $n \geqslant N$ 时，$h(n)=0$，所以
$$\begin{aligned} E(\mathrm{e}^{\mathrm{j}\omega}) &= \sum_{n=-\infty}^{-1} h_{\mathrm{d}}(n)\mathrm{e}^{-\mathrm{j}\omega n} + \sum_{n=N}^{\infty} h_{\mathrm{d}}(n)\mathrm{e}^{-\mathrm{j}\omega n} + \sum_{n=0}^{N-1} [h_{\mathrm{d}}(n) - h(n)] \mathrm{e}^{-\mathrm{j}\omega n} \\ &= \sum_{n=-\infty}^{\infty} e(n)\mathrm{e}^{-\mathrm{j}\omega n} \end{aligned}$$
故
$$e(n) = \begin{cases} h_{\mathrm{d}}(n) & n < 0, n \geqslant N \\ h_{\mathrm{d}}(n) - h(n) & 0 \leqslant n \leqslant N-1 \end{cases}$$

(2) 因为 $E(\mathrm{e}^{\mathrm{j}\omega}) = \mathrm{FT}[e(n)]$，所以由帕塞瓦尔定理有
$$\begin{aligned} \varepsilon^2 &= \frac{1}{2\pi} \int_{-\pi}^{\pi} | E(\mathrm{e}^{\mathrm{j}\omega}) |^2 \mathrm{d}\omega = \sum_{n=-\infty}^{\infty} | e(n) |^2 \\ &= \sum_{n=-\infty}^{-1} | h_{\mathrm{d}}(n) |^2 + \sum_{n=N}^{\infty} | h_{\mathrm{d}}(n) |^2 + \sum_{n=0}^{N-1} | h_{\mathrm{d}}(n) - h(n) |^2 \end{aligned}$$

(3) 由(2)的结果知，$\varepsilon^2$ 的前面两个求和项与 $w(n)$ 无关，而第三个求和项为
$$\sum_{n=0}^{N-1} | h_{\mathrm{d}}(n) - h(n) | = \sum_{n=0}^{N-1} | h_{\mathrm{d}}(n) - w(n)h_{\mathrm{d}}(n) | \bigg|_{w(n)=R_N(n)} = \sum_{n=0}^{N-1} | h_{\mathrm{d}}(n) - h_{\mathrm{d}}(n) | = 0$$
由此证明，矩形窗设计确实满足频域最小均方误差准则。前面已提到，当 $H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega})$ 为理想频率响应特性(理想低通、带通等)时，矩形窗设计的FIR滤波器阻带最小衰减只有21 dB，不满足一般工程要求。所以，调用频域最小均方误差最佳逼近设计程序设计FIR滤波器时，使 $H_{\mathrm{d}}(\mathrm{e}^{\mathrm{j}\omega})$ 具有平滑的滚降特性，可使阻带衰减加大，通带内波纹减小。

## 6.2 教材第7章习题与上机题解答

**1. 已知FIR滤波器的单位脉冲响应为：**
(1) $h(n)$ 长度 $N=6$
$h(0)=h(5)=1.5$
$h(1)=h(4)=2$
$h(2)=h(3)=3$

(2) $h(n)$ 长度 $N=7$
$h(0)=-h(6)=3$
$h(1)=-h(5)=-2$
$h(2)=-h(4)=1$
$h(3)=0$

试分别说明它们的幅度特性和相位特性各有什么特点。

**解：**(1) 由所给 $h(n)$ 的取值可知，$h(n)$ 满足 $h(n)=h(N-1-n)$，所以FIR滤波器具有A类线性相位特性：
$$\theta(\omega) = -\omega \frac{N-1}{2} = -2.5\omega$$
由于 $N=6$ 为偶数(情况2)，所以幅度特性关于 $\omega=\pi$ 点奇对称。

(2) 由题中 $h(n)$ 值可知，$h(n)$ 满足 $h(n)=-h(N-1-n)$，所以FIR滤波器具有B类线性相位特性：
$$\theta(\omega) = -\frac{\pi}{2} - \omega \frac{N-1}{2} = -\frac{\pi}{2} - 3\omega$$
由于7为奇数(情况3)，所以幅度特性关于 $\omega=0, \pi, 2\pi$ 三点奇对称。

**2. 已知第一类线性相位FIR滤波器的单位脉冲响应长度为16，其16个频域幅度采样值中的前9个为：**
$H_{\mathrm{g}}(0)=12$，$H_{\mathrm{g}}(1)=8.34$，$H_{\mathrm{g}}(2)=3.79$，$H_{\mathrm{g}}(3)\sim H_{\mathrm{g}}(8)=0$
根据第一类线性相位FIR滤波器幅度特性 $H_{\mathrm{g}}(\omega)$ 的特点，求其余7个频域幅度采样值。

**解:** 因为 $N=16$ 是偶数(情况2)，所以FIR滤波器幅度特性 $H_{\mathrm{g}}(\omega)$ 关于 $\omega=\pi$ 点奇对称，即 $H_{\mathrm{g}}(2\pi-\omega) = -H_{\mathrm{g}}(\omega)$。其 $N$ 点采样关于 $k=N/2$ 点奇对称，即
$$H_{\mathrm{g}}(N-k) = -H_{\mathrm{g}}(k) \quad k=1,2,\cdots,15$$
综上所述，可知其余7个频域幅度采样值：
$H_{\mathrm{g}}(15)=-H_{\mathrm{g}}(1)=-8.34$，$H_{\mathrm{g}}(14)=-H_{\mathrm{g}}(2)=-3.79$，$H_{\mathrm{g}}(13)\sim H_{\mathrm{g}}(9)=0$

**3. 设FIR滤波器的系统函数为**
$$H(z) = \frac{1}{10}(1 + 0.9z^{-1} + 2.1z^{-2} + 0.9z^{-3} + z^{-4})$$
求出该滤波器的单位脉冲响应 $h(n)$，判断是否具有线性相位，求出其幅度特性函数和相位特性函数。

**解:** 对FIR数字滤波器，其系统函数为
$$H(z) = \sum_{n=0}^{N-1} h(n) z^{-n} = \frac{1}{10}(1 + 0.9z^{-1} + 2.1z^{-2} + 0.9z^{-3} + z^{-4})$$
所以其单位脉冲响应为
$$h(n) = \frac{1}{10}\{1, 0, 9, 2.1, 0.9, 1\}$$
由 $h(n)$ 的取值可知 $h(n)$ 满足：
$$h(n) = h(N-1-n) \quad N=5$$
所以，该FIR滤波器具有第一类线性相位特性。频率响应函数 $H(\mathrm{e}^{\mathrm{j}\omega})$ 为
$$\begin{aligned} H(\mathrm{e}^{\mathrm{j}\omega}) &= H_{\mathrm{g}}(\omega)\mathrm{e}^{\mathrm{j}\theta(\omega)} = \sum_{n=0}^{N-1} h(n) \mathrm{e}^{-\mathrm{j}\omega m} \\ &= \frac{1}{10}[1 + 0.9\mathrm{e}^{-\mathrm{j}\omega} + 2.1\mathrm{e}^{-\mathrm{j}2\omega} + 0.9\mathrm{e}^{-\mathrm{j}3\omega} + \mathrm{e}^{-\mathrm{j}4\omega}] \\ &= \frac{1}{10}(\mathrm{e}^{\mathrm{j}2\omega} + 0.9\mathrm{e}^{\mathrm{j}\omega} + 2.1 + 0.9\mathrm{e}^{-\mathrm{j}\omega} + \mathrm{e}^{-\mathrm{j}2\omega}) \mathrm{e}^{-\mathrm{j}2\omega} \end{aligned}$$

<!-- pages: 151-154 -->
# 第6章 有限脉冲响应(FIR)数字滤波器的设计

$$
= \frac{1}{10}(2.1 + 1.8 \cos\omega + 2 \cos2\omega)e^{-j2\omega}
$$

幅度特性函数为

$$
H_{\text{g}}(\omega) = \frac{2.1 + 1.8 \cos\omega + 2 \cos2\omega}{10}
$$

相位特性函数为

$$
\theta(\omega) = -\omega \frac{N-1}{2} = -2\omega
$$

4. 用矩形窗设计线性相位低通 FIR 滤波器，要求过渡带宽度不超过 $\pi/8 \text{ rad}$。希望逼近的理想低通滤波器频率响应函数 $H_{\text{d}}(\text{e}^{\text{j}\omega})$ 为

$$
H_{\text{d}}(\text{e}^{\text{j}\omega}) = 
$$
\begin{cases}
$$
\text{e}^{-\text{j}\omega\alpha} & 0 \leqslant |\omega| \leqslant \omega_{\text{c}} \\
0 & \omega_{\text{c}} < |\omega| \leqslant \pi
$$
\end{cases}
$$

$$
(1) 求出理想低通滤波器的单位脉冲响应 $h_{\text{d}}(n)$；
(2) 求出加矩形窗设计的低通 FIR 滤波器的单位脉冲响应 $h(n)$ 表达式，确定 $\alpha$ 与 $N$ 之间的关系；
(3) 简述 $N$ 取奇数或偶数对滤波特性的影响。

解：(1)

$$
$$
\begin{aligned}
$$
h_{\text{d}}(n) &= \frac{1}{2\pi} \int_{-\pi}^{\pi} H_{\text{d}}(\text{e}^{-\text{j}\omega}) \text{e}^{\text{j}\omega n} \text{d}\omega \\
&= \frac{1}{2\pi} \int_{-\omega_{\text{c}}}^{\omega_{\text{c}}} \text{e}^{-\text{j}\omega\alpha} \text{e}^{\text{j}\omega n} \text{d}\omega \\
&= \frac{\sin[\omega_{\text{c}}(n-\alpha)]}{\pi(n-\alpha)}
$$
\end{aligned}
$$

$$
(2) 为了满足线性相位条件，要求 $\alpha = \frac{N-1}{2}$，$N$ 为矩形窗函数长度。因为要求过渡带宽度 $\Delta\beta \leqslant \frac{\pi}{8} \text{ rad}$，所以要求 $\frac{4\pi}{N} \leqslant \frac{\pi}{8}$，求解得到 $N \geqslant 32$。加矩形窗函数，得到 $h(n)$：

$$
$$
\begin{aligned}
$$
h(n) &= h_{\text{d}}(n) R_{N}(n) = \frac{\sin[\omega_{\text{c}}(n-a)]}{\pi(n-a)} R_{N}(n) \\
$$
&= 
\begin{cases}
$$
\frac{\sin[\omega_{\text{c}}(n-a)]}{\pi(n-a)} & 0 \leqslant n \leqslant N-1, \ a = \frac{N-1}{2} \\
0 & \text{其它 } n
$$
\end{cases}
\end{aligned}
$$

$$
(3) $N$ 取奇数时，幅度特性函数 $H_{\text{g}}(\omega)$ 关于 $\omega=0, \pi, 2\pi$ 三点偶对称，可实现各类幅频特性；$N$ 取偶数时，$H_{\text{g}}(\omega)$ 关于 $\omega=\pi$ 奇对称，即 $H_{\text{g}}(\pi)=0$，所以不能实现高通、带阻和点阻滤波特性。

5. 用矩形窗设计一线性相位高通滤波器，要求过渡带宽度不超过 $\pi/10 \text{ rad}$。希望逼近的理想高通滤波器频率响应函数 $H_{\text{d}}(\text{e}^{\text{j}\omega})$ 为

(1) 求出该理想高通的单位脉冲响应 $h_{\text{d}}(n)$；
(2) 求出加矩形窗设计的高通 FIR 滤波器的单位脉冲响应 $h(n)$ 表达式，确定 $\alpha$ 与 $N$ 的关系；
(3) $N$ 的取值有什么限制？为什么？

解：(1) 直接用 $\text{IFT}[H_{\text{d}}(\text{e}^{\text{j}\omega})]$ 计算：

$h_{\text{d}}(n)$ 表达式中第 2 项 $\left( \frac{\sin[\omega_{\text{c}}(n-\alpha)]}{\pi(n-\alpha)} \right)$ 正好是截止频率为 $\omega_{\text{c}}$ 的理想低通滤波器的单位脉冲响应。而 $\delta(n-\alpha)$ 对应于一个线性相位全通滤波器：

$$
H_{\text{dap}}(\text{e}^{\text{j}\omega}) = \text{e}^{-\text{j}\omega\alpha}
$$

即高通滤波器可由全通滤波器减去低通滤波器实现。

(2) 用 $N$ 表示 $h(n)$ 的长度，则

$$
h(n) = h_{\text{d}}(n) R_{N}(n) = \left\{ \delta(n-\alpha) - \frac{\sin[\omega_{\text{c}}(n-\alpha)]}{\pi(n-\alpha)} \right\} R_{N}(n)
$$

为了满足线性相位条件：

$$
$$
h(n) = h(N-1-n)
$$

$$
要求满足

$$
\alpha = \frac{N-1}{2}
$$

(3) $N$ 必须取奇数。因为 $N$ 为偶数时(情况 2)，$H(\text{e}^{\text{j}\pi})=0$，不能实现高通。根据题中对过渡带宽度的要求，$N$ 应满足：$\frac{4\pi}{N} \leqslant \frac{\pi}{10}$，即 $N \geqslant 40$。取 $N=41$。

6. 理想带通特性为

(1) 求出该理想带通的单位脉冲响应 $h_{\text{d}}(n)$；
(2) 写出用升余弦窗设计的滤波器的 $h(n)$ 表达式，确定 $N$ 与 $\alpha$ 之间的关系；
(3) 要求过渡带宽度不超过 $\pi/16 \text{ rad}$。$N$ 的取值是否有限制？为什么？

上式第一项和第二项分别为截止频率 $\omega_{\text{c}}+B$ 和 $\omega_{\text{c}}$ 的理想低通滤波器的单位脉冲响应。所以，上面 $h_{\text{d}}(n)$ 的表达式说明，带通滤波器可由两个低通滤波器相减实现。

(2)

$$
$$
\begin{aligned}
$$
h(n) &= h_{\text{d}}(n) w(n) \\
&= \left\{ \frac{\sin[(\omega_{\text{c}}+B)(n-\alpha)]}{\pi(n-\alpha)} - \frac{\sin[\omega_{\text{c}}(n-\alpha)]}{\pi(n-\alpha)} \right\} \left[ 0.54 - 0.46 \cos\left( \frac{2\pi n}{N-1} \right) \right] R_{N}(n)
$$
\end{aligned}
$$

$$
为了满足线性相位条件，$\alpha$ 与 $N$ 应满足

实质上，即使不要求具有线性相位，$\alpha$ 与 $N$ 也应满足该关系，只有这样，才能截取 $h_{\text{d}}(n)$ 的主要能量部分，使引起的逼近误差最小。

(3) $N$ 取奇数和偶数时，均可实现带通滤波器。但升余弦窗设计的滤波器过渡带为 $8\pi/N$，所以，要求 $\frac{8\pi}{N} \leqslant \frac{\pi}{16}$，即要求 $N \geqslant 128$。

解：(1) 由题意可知

$$
h_1(n) = (-1)^n h(n) = \cos(\pi n) h(n) = \frac{1}{2} [\text{e}^{\text{j}\pi n} + \text{e}^{-\text{j}\pi n}] h(n)
$$

对 $h_1(n)$ 进行傅里叶变换，得到

$$
$$
\begin{aligned}
$$
H_1(\text{e}^{\text{j}\omega}) &= \sum_{n=-\infty}^{\infty} h_1(n) \text{e}^{-\text{j}\omega n} = \frac{1}{2} \sum_{n=-\infty}^{\infty} h(n) [\text{e}^{\text{j}\pi n} + \text{e}^{-\text{j}\pi n}] \text{e}^{-\text{j}\omega n} \\
&= \frac{1}{2} \left[ \sum_{n=-\infty}^{\infty} h(n) \text{e}^{-\text{j}(\omega-\pi)n} + \sum_{n=-\infty}^{\infty} h(n) \text{e}^{-\text{j}(\omega+\pi)n} \right] \\
&= \frac{1}{2} [H(\text{e}^{\text{j}(\omega-\pi)}) + H(\text{e}^{\text{j}(\omega+\pi)})]
$$
\end{aligned}
$$

$$
上式说明 $H_1(\text{e}^{\text{j}\omega})$ 就是 $H(\text{e}^{\text{j}\omega})$ 平移 $\pm\pi$ 的结果。由于 $H(\text{e}^{\text{j}\omega})$ 为低通滤波器，通带位于以 $\omega=0$ 为中心的附近邻域，因而 $H_1(\text{e}^{\text{j}\omega})$ 的通带位于以 $\omega=\pm\pi$ 为中心的附近，即 $h_1(n)$ 是一个高通滤波器。

这一证明结论又为我们提供了一种设计高通滤波器的方法(设高通滤波器通带为 $[\pi-\omega_{\text{c}}, \pi])$：
① 设计一个截止频率为 $\omega_{\text{c}}$ 的低通滤波器 $h_{\text{Lp}}(n)$。
② 对 $h_{\text{Lp}}(n)$ 乘以 $\cos(\pi n)$ 即可得到高通滤波器 $h_{\text{Hp}}(n) \cos(\pi n) = (-1)^n h_{\text{Lp}}(n)$。

$$
H_2(\text{e}^{\text{j}\omega}) = \frac{H(\text{e}^{\text{j}(\omega-\omega_0)}) + H(\text{e}^{\text{j}(\omega+\omega_0)})}{2}
$$

因为低通滤波器 $H(\text{e}^{\text{j}\omega})$ 通带中心位于 $\omega=2k\pi$，且 $H_2(\text{e}^{\text{j}\omega})$ 为 $H(\text{e}^{\text{j}\omega})$ 左右平移 $\omega_0$，所以 $H_2(\text{e}^{\text{j}\omega})$ 的通带中心位于 $\omega=2k\pi \pm \omega_0$ 处，所以 $h_2(n)$ 具有带通特性。这一结论又为我们提供了一种设计带通滤波器的方法。

8. 题 8 图中 $h_1(n)$ 和 $h_2(n)$ 是偶对称序列，$N=8$，设

$$
$$
\begin{aligned}
$$
H_1(k) &= \text{DFT}[h_1(n)] & k&=0,1,\cdots,N-1 \\
H_2(k) &= \text{DFT}[h_2(n)] & k&=0,1,\cdots,N-1
$$
\end{aligned}
$$

$$

**题 8 图**

$$
$$
h_2(n) = h_1((n+4))_8 R_8(n)
$$

$$
由 DFT 的循环移位性质可得

$$
$$
\begin{aligned}
$$
H_2(k) &= W_8^{-k \cdot 4} H_1(k) = \text{e}^{\text{j}\pi k} H_1(k) = (-1)^k H_1(k) \\
$$
|H_2(k)| &= |W_8^{-k \cdot 4} H_1(k)| = |H_1(k)|
\end{aligned}
$$

$$
\begin{aligned}
h_1(n) &= h_1(N-1-n) \\
h_2(n) &= h_2(N-1-n)
\end{aligned}
$$

$$
所以，用 $h_1(n)$ 和 $h_2(n)$ 构成的低通滤波器具有线性相位。直接计算 $\text{FT}[h_1(n)]$ 和 $\text{FT}[h_2(n)]$ 也可以得到同样的结论。

设

$$
$$
\begin{aligned}
$$
H_1(\text{e}^{\text{j}\omega}) &= \text{FT}[h_1(n)] = H_{1\text{g}}(\omega) \text{e}^{\text{j}\theta_1(\omega)} \\
H_2(\text{e}^{\text{j}\omega}) &= \text{FT}[h_2(n)] = H_{2\text{g}}(\omega) \text{e}^{\text{j}\theta_2(\omega)} \\
\theta_1(\omega) = \theta_2(\omega) &= -\frac{1}{2}(N-1)\omega = -\frac{7}{2}\omega
$$
\end{aligned}
$$

$$
所以，群延时为

$$
\tau_2 = \tau_1 = -\frac{\text{d}\theta_1(\omega)}{\text{d}\omega} = \frac{7}{2}
$$

9. 对下面的每一种滤波器指标，选择满足 FIRDF 设计要求的窗函数类型和长度。

<!-- pages: 9-12 -->
# 第6章 有限脉冲响应(FIR)数字滤波器的设计

（1）阻带衰减为20 dB，过渡带宽度为1 kHz，采样频率为12 kHz；
（2）阻带衰减为50 dB，过渡带宽度为2 kHz，采样频率为20 kHz；
（3）阻带衰减为50 dB，过渡带宽度为500 Hz，采样频率为5 kHz。

解：我们知道，根据阻带最小衰减选择窗函数类型，根据过渡带宽度计算窗函数长度。为了观察方便，重写出教材第211页中表7.2.2。

**教材表 7.2.2 6种窗函数的基本参数**

| 窗函数类型 | 旁瓣峰值 $\alpha_p$/dB | 过渡带宽度 $B_t$ | 阻带最小衰减 $\alpha_s$ /dB |
| :--- | :---: | :---: | :---: | :---: |
| | | **近似值** | **精确值** | |
| 矩形窗 | -13 | $\frac{4\pi}{N}$ | $\frac{1.8\pi}{N}$ | -21 |
| 三角窗 | -25 | $\frac{8\pi}{N}$ | $\frac{6.1\pi}{N}$ | -25 |
| 汉宁窗 | -31 | $\frac{8\pi}{N}$ | $\frac{6.2\pi}{N}$ | -44 |
| 哈明窗 | -41 | $\frac{8\pi}{N}$ | $\frac{6.6\pi}{N}$ | -53 |
| 布莱克曼窗 | -57 | $\frac{12\pi}{N}$ | $\frac{11\pi}{N}$ | -74 |
| 凯塞窗($\beta=7.865$) | -57 | | $\frac{10\pi}{N}$ | -80 |

结合本题要求和教材表7.2.2，选择结果如下：
（1）矩形窗满足本题要求。过渡带宽度1 kHz对应的数字频率为 $B=200\pi/12000=\pi/60$，精确过渡带满足：$1.8\pi/N \leqslant \pi/60$，所以要求 $N \geqslant 1.8\times60=108$。
（2）选哈明窗，过渡带宽度2 kHz对应的数字频率为 $B=4000\pi/20000=\pi/5$，精确过渡带满足：$6.6\pi/N \leqslant \pi/5$，所以要求 $N \geqslant 6.6\times5=33$。
（3）选哈明窗，过渡带宽度500 Hz对应的数字频率为 $B=1000\pi/5000=\pi/5$，精确过渡带满足：$6.6\pi/N \leqslant \pi/5$，所以要求 $N \geqslant 6.6\times5=33$。

10. 利用矩形窗、升余弦窗、改进升余弦窗和布莱克曼窗设计线性相位FIR低通滤波器。要求希望逼近的理想低通滤波器通带截止频率 $\omega_c = \pi/4$ rad，$N=21$。求出分别对应的单位脉冲响应。

(3) 加窗得到FIR滤波器单位脉冲响应 $h(n)$：
- 升余弦窗：
$$
w_{\text{Hn}}(n) = 0.5\left(1-\cos\frac{2\pi n}{N-1}\right)R_N(n) \tag{3}
$$
$$
h_{\text{Hn}}(n) = h_d(n)w_{\text{Hn}}(n) = \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{2\pi(n-10)}\left(1-\cos\frac{2\pi n}{20}\right)R_{21}(n) \tag{4}
$$
- 改进升余弦窗：
$$
w_{\text{Hm}}(n) = \left(0.54-0.46\cos\frac{2\pi n}{N-1}\right)R_N(n) \tag{5}
$$
$$
h_{\text{Hm}}(n) = h_d(n)w_{\text{Hm}}(n) = \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{\pi(n-10)}\left(0.54-0.46\cos\frac{2\pi n}{20}\right)R_{21}(n) \tag{6}
$$
- 布莱克曼窗：
$$
h_{\text{Bl}}(n) = h_d(n)w_{\text{Bl}}(n) \\
= \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{\pi(n-10)}\left(0.42-0.5\cos\frac{2\pi n}{20}+0.08\cos\frac{4\pi n}{20}\right)R_{21}(n) \tag{7}
$$

11. 将技术要求改为设计线性相位高通滤波器，重复题10。
解：方法一 将题10解答中的逼近理想低通滤波器($H_d(e^{j\omega})$、$h_d(n)$)改为如下理想高通滤波器即可。
$$
$$
H_d(e^{j\omega}) = \begin{cases}
$$
e^{-j10\omega} & \frac{3\pi}{4} \leqslant |\omega| \leqslant \pi \\
0 & 0 \leqslant |\omega| < \frac{3\pi}{4}
$$
\end{cases} \tag{8}
$$
$$
\begin{aligned}
$$
h_d(n) &= \frac{1}{2\pi}\int_{-\pi}^{\pi} H_d(e^{j\omega})d\omega \\
&= \frac{1}{2\pi}\int_{-\pi}^{-3\pi/4} e^{-j10\omega} d\omega + \int_{3\pi/4}^{\pi} e^{-j10\omega} e^{j\omega n} d\omega \\
&= \frac{\sin[\pi(n-10)]}{\pi(n-10)} - \frac{\sin\left[\frac{3\pi}{4}(n-10)\right]}{\pi(n-10)} \\
&= \delta(n-10) - \frac{\sin\left[\frac{3\pi}{4}(n-10)\right]}{\pi(n-10)}
$$
\end{aligned} \tag{9}
$$
$$
上式中 $\delta(n-10)$ 对应于全通滤波器。上式说明，高通滤波器的单位脉冲响应等于全通滤波器的单位脉冲响应减去低通滤波器的单位脉冲响应。
仿照10题，用矩形窗、升余弦窗、改进升余弦窗和布莱克曼窗对上面所求的 $h_d(n)$ 加窗即可。
计算与绘图程序与题10解中类同，只要将其中的 $h(n)$ 用本题的高通 $h(n)$ 替换即可。
方法二 根据第7题(1)的证明结论设计。
（1）先设计通带截止频率为 $\pi/4$ 的低通滤波器。对四种窗函数所得FIR低通滤波器单位脉冲响应为题9解中的 $h_{\text{R}}(n)$、$h_{\text{Hn}}(n)$、$h_{\text{Hm}}(n)$ 和 $h_{\text{Bl}}(n)$。
（2）对低通滤波器单位脉冲响应乘以 $\cos\pi n$ 可得到高通滤波器单位脉冲响应：
- 矩形窗：
$$
h_1(n) = h_{\text{R}}(n)\cos\pi n = \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{\pi(n-10)}\cos\pi n \ R_{21}(n) \tag{10}
$$
- 升余弦窗：
$$
$$
\begin{aligned}
$$
h_2(n) &= h_{\text{Hn}}(n)\cos\pi n = (-1)^n h_{\text{Hn}}(n) \\
&= \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{2\pi(n-10)}\left(1-\cos\frac{2\pi n}{20}\right)\cos\pi n \ R_{21}(n)
$$
\end{aligned} \tag{11}
$$
$$
- 改进升余弦窗：
$$
$$
\begin{aligned}
$$
h_3(n) &= h_{\text{Hn}}(n)\cos\pi n \\
&= \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{\pi(n-10)}\left(0.54-0.46\cos\frac{2\pi n}{20}\right)\cos\pi n \ R_{21}(n)
$$
\end{aligned} \tag{12}
$$
$$
- 布莱克曼窗：
$$
h_4(n) = \frac{\sin\left[\frac{\pi}{4}(n-10)\right]}{\pi(n-10)}\left(0.42-0.5\cos\frac{2\pi n}{20}+0.08\cos\frac{4\pi n}{20}\right)\cos\pi n \ R_{21}(n) \tag{13}
$$

12. 利用窗函数(哈明窗)法设计一数字微分器，逼近题12图所示的理想微分器特性，并绘出其幅频特性。


**题12图**

（2）对3种不同的长度 $N=20$，$40$ 和 $41$，用MATLAB计算单位脉冲响应 $h(n)$ 和幅频特性函数，并绘图的程序 `ex712.m` 如下：

<!-- pages: 13-16 -->

% ex712. m: 用哈明窗设计线性相位 FIR 微分器
```matlab
clear all; close all;
N1 = 20; n = 0: N1 - 1; tou = (N1 - 1)/2;
h1n = sin((n - tou) * pi) ./ (pi * (n - tou) .^ 2) .* (hamming(N1))';
N2 = 40; n = 0: N2 - 1; tou = (N2 - 1)/2;
h2n = sin((n - tou) * pi) ./ (pi * (n - tou) .^ 2) .* (hamming(N2))';
N3 = 41; n = 0: N3 - 1; tou = (N3 - 1)/2;
h3n = sin((n - tou) * pi) ./ (pi * (n - tou) .^ 2) .* (hamming(N3))';
h3n((N3 - 1)/2 + 1) = 0;      % 因为该点分母为零，无定义，所以赋值0
% 以下为绘图部分(省略)
```
程序运行结果即数字微分器的单位脉冲响应和幅频特性函数曲线如题 12 解图所示。由图可见，当滤波器长度 N 为偶数时，逼近效果好。但 N = 奇数时(本程序中 N = 41)，逼近误差很大。这一结论与教材给出的理论一致(对第二类线性相位滤波器，N = 奇数时不能实现高通滤波特性)。


**图 12.1:** N=20设计的h(n)

**图 12.2:** N=20设计的幅频特性

**图 12.3:** N=40设计的h(n)

**图 12.4:** N=40设计的幅频特性

**图 12.5:** N=41设计的h(n)

**图 12.6:** N=41设计的幅频特性

题 12 解图

也可以采用调用等波纹最佳逼近法设计函数 remez 来设计 FIR 数字微分器的方法。$hn = remez(N-1, f, m, \text{'differentialiator'})$ 设计 $N-1$ 阶 FIR 数字微分器，返回的单位脉冲响应向量 $hn$ 具有奇对称特性。在大多数工程实际中，仅要求在频率区间 $0 \leqslant \omega \leqslant \omega_p$ 上逼近理想微分器的频率响应特性，而在区间 $\omega_p < \omega \leqslant \pi$ 上频率响应特性不作要求，或要求为零。对微分器设计，在区间 $\omega_p < \omega \leqslant \pi$ 上频率响应特性要求为零时，调用参数 $f = [0, \omega_p/\pi, (\omega_p + B)/\pi, 1]$，$m = [0, \omega_p/\pi, 0, 0]$，其中 $B$ 为过渡带宽度(即无关区)，$\omega_p$ 不能太靠近 $\pi$，$B$ 也不能太小，否则设计可能失败。调用等波纹最佳逼近法设计函数 remez 设计本题要求的 FIR 数字微分器的程序 ex712b. m 如下：
```matlab
% ex712b. m: 调用 remez 函数设计 FIR 微分器
Wp = 0.9; B = 0.09;   % 设置微分器边界频率(关于 $\pi$ 归一化)
N = 40; f = [0, wp, wp + B, 1]; m = [0, wp, 0, 0];
hn = remez(N - 1, f, m, 'differentiator');   % 调用 remez 函数设计 FIR 微分器
% 以下为绘图部分(省略)
```
请读者运行该程序，观察设计效果。

13. 用窗函数法设计一个线性相位低通 FIRDF，要求通带截止频率为 $\pi/4$ rad，过渡带宽度为 $8\pi/51$ rad，阻带最小衰减为 45 dB。
    (1) 选择合适的窗函数及其长度，求出 $h(n)$ 的表达式。
    (2*) 用 MATLAB 画出损耗函数曲线和相频特性曲线。

解：(1) 根据教材 7.2.2 节所给步骤进行设计。
① 根据对阻带衰减及过渡带的指标要求，选择窗函数的类型，并估计窗口长度 $N$。由习题 9 中教材表 7.2.2，本题应选择哈明窗。因为过渡带宽度 $B_t = 8\pi/51$，所以窗口长度 $N$ 为 $N \geqslant 6.6\pi/B_t = 42.075$，取 $N=43$。窗函数表达式为
$$ w_{\text{Hm}}(n) = \left( 0.54 - 0.46 \cos \frac{2\pi n}{N - 1} \right) R_N(n) $$
② 构造希望逼近的频率响应函数 $H_d(e^{j\omega})$：
$$ H_d(e^{j\omega}) = H_{dg}(\omega) e^{-j\omega(N-1)/2} = \begin{cases} e^{-j\omega \tau} & 0 \leqslant | \omega | < \omega_c \\ 0 & \omega_c \leqslant | \omega | \leqslant \pi \end{cases} $$
式中
$$ \tau = \frac{N-1}{2} = 21, \omega_c = \omega_p + \frac{B_t}{2} = \frac{\pi}{4} + \frac{4\pi}{51} = 0.0833\pi $$
③ 求 $h_d(n)$：
$$ h_d(n) = \frac{1}{2\pi} \int_{-\pi}^{\pi} H_d(e^{j\omega}) e^{j\omega n} d\omega = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} e^{-j\omega \tau} e^{j\omega n} d\omega = \frac{\sin[\omega_c(n - \tau)]}{\pi(n - \tau)} $$
④ 加窗：
$$ h(n) = h_d(n) w(n) = \frac{\sin[\omega_c(n - \tau)]}{\pi(n - \tau)} \left( 0.54 - 0.46 \cos \frac{2\pi n}{N - 1} \right) R_N(n) $$
(2) 调用 MATLAB 函数设计及绘图程序 ex713. m 如下：
```matlab
% ex713. m: 调用 fir1 设计线性相位低通 FIR 滤波器并绘图
wp = pi/4; Bt = 8 * pi/51;
wc = wp + Bt/2; N = ceil(6.6 * pi/Bt);
hmn = fir1(N - 1, wc/pi, hamming(N));
rs = 60; a = 1; mpplot(hmn, a, rs)  % 调用自编函数 mpplot 绘制损耗函数和相频特性曲线
```
程序运行结果即损耗函数和相频特性曲线如题 13 解图所示，请读者运行程序查看 $h(n)$ 的数据。


**题 13 解图:** (a) 损耗函数曲线 (b) 相频特性曲线

14. 要求用数字低通滤波器对模拟信号进行滤波，要求：通带截止频率为 10 kHz，阻带截止频率为 22 kHz，阻带最小衰减为 75 dB，采样频率为 $F_s = 50$ kHz。用窗函数法设计数字低通滤波器。
    (1) 选择合适的窗函数及其长度，求出 $h(n)$ 的表达式。
    (2*) 用 MATLAB 画出损耗函数曲线和相频特性曲线。

解：(1) 根据教材 7.2.2 节所给步骤进行设计。
① 根据对阻带衰减及过渡带的指标要求，选择窗函数的类型，并估计窗口长度 $N$。
本题要求设计的 FIRDF 指标：
通带截止频率：
$$ \omega_p = \frac{2\pi f_p}{F_s} = 2\pi \times \frac{10\,000}{50\,000} = \frac{2\pi}{5} \text{ rad} $$
阻带截止频率：
$$ \omega_s = \frac{2\pi f_s}{F_s} = 2\pi \times \frac{22\,000}{50\,000} = \frac{22\pi}{25} \text{ rad} $$
阻带最小衰减：
$$ \alpha_s = 75 \text{ dB} $$
由习题 9 中教材表 7.2.2 可知，本题应选凯塞窗($\beta = 7.865$)。窗口长度 $N \geqslant 10\pi/B_t = 10\pi/(\omega_s - \omega_p) = 20.833$，取 $N=21$。窗函数表达式为
$$ w_k(n) = \frac{I_0(\beta)}{I_0(\alpha)} R_{21}(n), \beta = 7.865 $$
② 构造希望逼近的频率响应函数 $H_d(e^{j\omega})$：
$$ H_d(e^{j\omega}) = H_{dg}(\omega) e^{-j\omega(N-1)/2} = \begin{cases} e^{-j\omega \tau} & 0 \leqslant | \omega | < \omega_c \\ 0 & \omega_c \leqslant | \omega | \leqslant \pi \end{cases} $$
式中，$\tau = (N-1)/2 = 10, \omega_c = (\omega_p + \omega_s)/2 = 16\pi/25$。
③ 求 $h_d(n)$：
$$ h_d(n) = \frac{1}{2\pi} \int_{-\pi}^{\pi} H_d(e^{j\omega}) e^{j\omega n} d\omega = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} e^{-j\omega \tau} e^{j\omega n} d\omega = \frac{\sin[\omega_c(n - \tau)]}{\pi(n - \tau)} $$
④ 加窗：
$$ h(n) = h_d(n) w(n) = \frac{\sin[\omega_c(n - \tau)]}{\pi(n - \tau)} w_k(n) $$
(2) 调用 MATLAB 函数设计及绘图程序 ex714. m 如下：
```matlab
% ex714. m: 调用 fir1 设计线性相位低通 FIR 滤波器并绘图
Fs = 50000; fp = 10000; fs = 22000; rs = 75;
wp = 2 * pi * fp / Fs; ws = 2 * pi * fs / Fs; Bt = ws - wp;
wc = (wp + ws)/2; N = ceil(10 * pi/Bt);
hmn = fir1(N - 1, wc/pi, kaiser(N, 7.865));
rs = 100; a = 1; mpplot(hmn, a, rs)  % 调用自编函数 mpplot 绘制损耗函数和相频特性曲线
```
程序运行结果即损耗函数和相频特性曲线如题 14 解图所示，请读者运行程序查看 $h(n)$ 的数据。


**题 14 解图:** (a) 损耗函数曲线 (b) 相频特性曲线

15. 利用频率采样法设计线性相位 FIR 低通滤波器，给定 $N=21$，通带截止频率 $\omega_c = 0.15\pi$ rad。求出 $h(n)$，为了改善其频率响应(过渡带宽度、阻带最小衰减)，应采取什么

<!-- pages: 163-166 -->

第6章 有限脉冲响应(FIR)数字滤波器的设计

措施？
解：(1) 确定希望逼近的理想低通滤波频率响应函数 $H_d(e^{j\omega})$：
$$
$$
H_d(e^{j\omega}) = \begin{cases}
e^{-j\omega a} & 0 \leqslant |\omega| < 0.15\pi \\
0 & 0.15\pi \leqslant |\omega| \leqslant \pi
\end{cases}
$$
$$
其中，$a = (N-1)/2 = 10$。
② 采样：
$$
H_d(k) = H_d(e^{j\frac{2\pi}{N}k}) = \begin{cases}
e^{-j\frac{N-1}{N}\pi k} = e^{-j\frac{20}{21}\pi k} & k = 0, 1, 20 \\
$$
0 & 2 \leqslant k \leqslant 19
\end{cases}
$$
$$
③ 求 $h(n)$：
$$
$$
\begin{aligned}
$$
h(n) &= \text{IDFT}[H_d(k)] = \frac{1}{N} \sum_{k=0}^{N-1} H_d(k) W_N^{-kn} \\
&= \frac{1}{21} [1 + e^{-j\frac{20}{21}\pi} W_{21}^{-n} + e^{-j\frac{20}{21}\pi W_{21}^{-20n}}] R_{21}(n) \\
&= \frac{1}{21} [1 + e^{j\frac{20}{21}\pi(n-10)} + e^{-j\frac{400}{21}\pi} e^{j\frac{40}{21}\pi n}] R_{21}(n)
$$
\end{aligned}
$$
$$
因为
$$
e^{-j\frac{400}{21}\pi} = e^{j\frac{20}{21}\pi}, \quad e^{j\frac{40}{21}\pi n} = e^{j(\frac{42\pi}{21} - \frac{2\pi}{21})n} = e^{-j\frac{2\pi}{21}n}
$$
所以
$$
h(n) = \frac{1}{21} [1 + e^{j\frac{2\pi}{21}(n-10)} + e^{-j\frac{2\pi}{21}(n-10)}] = \frac{1}{21} \left[1 + 2 \cos\left(\frac{2\pi}{21}(n-10)\right)\right] R_{21}(n)
$$

损耗函数曲线绘图程序 `ex715.m` 如下：
```matlab
% 程序 ex715.m
N = 21; n = 0: N-1;
hn = (1 + 2 * cos(2 * pi * (n - 10) / N)) / N;
rs = 20; a = 1; mpplot(hn, a, rs) % 调用自编函数 mpplot 绘制损耗函数和相频特性曲线
```
运行程序绘制损耗函数曲线如题 15 解图所示，请读者运行程序查看 `hn` 的数据。
为了改善阻带衰减和通带波纹，应加过渡带采样点，为了使边界频率更精确，过渡带更窄，应加大采样点数 $N$。


**题 15 解图：** 损耗函数曲线。

16. 重复题 15，但改为用矩形窗函数法设计。将设计结果与题 15 进行比较。
解：直接调用 `fir1` 设计，程序为 `ex716.m`。
```matlab
% 调用 fir1 求解 16 题的程序 ex716.m
N = 21; wc = 0.15;
hn = fir1(N - 1, wc, boxcar(N)); % 选用矩形窗函数（与上面求解中相同）
rs = 20; a = 1; mpplot(hn, a, rs) % 调用自编函数 mpplot 绘制损耗函数和相频特性曲线
```
运行程序绘制损耗函数曲线如题 16 解图所示。与题 15 解图比较，过渡带宽度相同，但矩形窗函数法设计的 FIRDF 阻带最小衰减约为 20 dB，而 15 题设计结果约为 16 dB。


**题 16 解图：** 损耗函数曲线。

17. 利用频率采样法设计线性相位 FIR 低通滤波器，设 $N=16$，给定希望逼近的滤波器的幅度采样值为
$$
$$
H_{dg}(k) = \begin{cases}
1 & k = 0, 1, 2, 3 \\
0.389 & k = 4 \\
0 & k = 5, 6, 7
\end{cases}
$$
$$
解：由希望逼近的滤波器幅度采样 $H_{dg}(k)$ 可构造出 $H_d(e^{j\omega})$ 的采样 $H_d(k)$：
$$
$$
H_d(k) = \begin{cases}
$$
e^{-j\frac{N-1}{N}\pi k} = e^{-j\frac{15}{16}\pi k} & k = 0, 1, 2, 3, 13, 14, 15 \\
0.389 e^{-j\frac{15}{16}\pi k} & k = 4, 12 \\
$$
0 & k = 5, 6, 7, 8, 9, 11
\end{cases}
$$
$$
\begin{aligned}
$$
h(n) &= \text{IDFT}[H_d(k)] = \frac{1}{16} \sum_{k=0}^{15} H_d(k) W_{16}^{-kn} R_{16}(n) \\
&= \frac{1}{16} [1 + e^{-j\frac{15}{16}\pi} e^{j\frac{\pi}{8}n} + e^{-j\frac{15}{16}2\pi} e^{j\frac{\pi}{8}2n} + e^{-j\frac{15}{16}3\pi} e^{j\frac{\pi}{8}3n} + 0.389 e^{-j\frac{15}{16}4\pi} e^{j\frac{\pi}{8}4n} \\
&\quad + e^{-j\frac{15}{16}15\pi} e^{j\frac{\pi}{8}15n} + e^{-j\frac{15}{16}14\pi} e^{j\frac{\pi}{8}14n} + e^{-j\frac{15}{16}13\pi} e^{j\frac{\pi}{8}13n} + 0.389 e^{-j\frac{15}{16}12\pi} e^{j\frac{\pi}{8}12n}] R_{16}(n) \\
&= \frac{1}{16} \left\{1 + 2 \cos\left[\frac{\pi}{8} \left(n - \frac{15}{2}\right)\right] + 2 \cos\left[\frac{\pi}{4} \left(n - \frac{15}{2}\right)\right] \right. \\
&\quad \left. + 2 \cos\left[\frac{3\pi}{8} \left(n - \frac{15}{2}\right)\right] + 0.778 \cos\left[\frac{\pi}{2} \left(n - \frac{15}{2}\right)\right]\right\}
$$
\end{aligned}
$$

$$
18. 利用频率采样法设计线性相位 FIR 带通滤波器，设 $N=33$，理想幅度特性 $H_d(\omega)$ 如题 18 图所示。


**题 18图：** 理想幅度特性 $H_d(\omega)$ 图。

解：由题 18 图可得到理想幅度采样值为
$$
H_{dg}(k) = H_d\left(\frac{2\pi}{N}k\right) = \begin{cases}
$$
1 & k = 7, 8, 25, 26 \\
0 & k = 0 \sim 6, k = 9 \sim 24, k = 27 \sim 32
\end{cases}
$$
$$
$$
H_d(k) = H_d(e^{j\frac{2\pi}{N}k}) = \begin{cases}
e^{-j\frac{32}{33}\pi k} & k = 7, 8, 25, 26 \\
0 & \text{其它 } k \text{ 值}
$$
\end{cases}
$$
$$
\begin{aligned}
$$
h(n) &= \text{IDFT}[H_d(k)] = \frac{1}{33} \sum_{k=0}^{32} H_d(k) W_{33}^{-kn} R_{33}(n) \\
&= \frac{1}{33} [e^{-j\frac{32}{33}7\pi} e^{j\frac{2\pi}{33}7n} + e^{-j\frac{32}{33}8\pi} e^{j\frac{2\pi}{33}8n} + e^{-j\frac{32}{33}25\pi} e^{j\frac{2\pi}{33}25n} + e^{-j\frac{32}{33}26\pi} e^{j\frac{2\pi}{33}26n}] \\
&= \frac{1}{33} \left\{\left[\cos \frac{14\pi}{33}(n-16)\right] + \cos\left[\frac{16\pi}{33}(n-16)\right]\right\} R_{33}(n)
$$
\end{aligned}
$$

$$
19*. 设信号 $x(t) = s(t) + v(t)$，其中 $v(t)$ 是干扰，$s(t)$ 与 $v(t)$ 的频谱不混叠，其幅度谱如题 19* 图所示。要求设计数字滤波器，将干扰滤除，指标是允许 $|s(f)|$ 在 $0 \leqslant f \leqslant 15$ kHz 频率范围中幅度失真为 $\pm 2\%$ ($\delta_1 = 0.02$)；$f > 20$ kHz，衰减大于 40 dB ($\delta_2 = 0.01$)；希望分别设计性价比最高的 FIR 和 IIR 两种滤波器进行滤除干扰。请选择合适的滤波器类型和设计方法进行设计，最后比较两种滤波器的幅频特性、相频特性和阶数。


**题 19*图：** 信号 $x(t)$ 的幅度谱 $|s(f)|$ 和 $|v(f)|$。

解：本题以模拟频率给定滤波器指标，所以，程序中先要计算出对应的数字边界频率，然后再调用 MATLAB 工具箱函数 `fir1` 设计数字滤波器。由题意确定滤波器指标（边界频率以模拟频率给出）：
$$
f_p = 15 \text{ kHz}, \delta_1 = 0.02, \alpha_p = -20 \lg \frac{1-\delta_2}{1+\delta_2} \text{ dB}
$$
$$
f_s = 20 \text{ kHz}, \delta_2 = 0.01, \alpha_s = 40 \text{ dB}
$$
(1) 确定相应的数字滤波器指标。根据信号带宽，取系统采样频率 $F_s = 80$ kHz。
$$
\omega_p = \frac{2\pi f_p}{F_s}, \delta_1 = 0.02, \alpha_p = -20 \lg \frac{1-\delta_2}{1+\delta_2} \text{ dB}
$$
$$
\omega_s = \frac{2\pi f_s}{F_s}, \delta_2 = 0.01, \alpha_s = 40 \text{ dB}
$$

(2) 设计数字低通滤波器。为了设计性价比最高的 FIR 和 IIR 滤波器，IIR 滤波器选择椭圆滤波器，FIR 滤波器采用等波纹最佳逼近法设计。设计程序为 `ex719.m`。
```matlab
% ex719.m: 设计性价比最高的 FIR 和 IIR 滤波器
Fs = 80000; fp = 15000; fs = 20000;
deltal = 0.02; rp = -20 * log10((1 - deltal) / (1 + deltal));
delta2 = 0.01; rs = 40;
wp = 2 * fp / Fs; ws = 2 * fs / Fs; % 计算数字边界频率（关于 π 归一化）
% 椭圆 DF 设计
[Ne, wpe] = ellipord(wp, ws, rp, rs); % 调用 ellipord 计算椭圆 DF 阶数 N 和通带截止频率 wp
[Be, Ae] = ellip(Ne, wpe, rs, wp); % 调用 ellip 计算椭圆 DF 系统函数系数向量 Be 和 Ae
% 用等波纹最佳逼近法设计 FIRDF
f = [wp, ws]; m = [1, 0]; rip = [deltal, delta2];
[Nr, fo, mo, w] = remezord(f, m, rip);
hn = remez(Nr, fo, mo, w);
% 以下为绘图部分（省略）
```
程序运行结果：椭圆 DF 阶数 Ne=5，损耗函数曲线和相频特性曲线如题图 19* 解图 (a) 所示。采用等波纹最佳逼近法设计的 FIRDF 阶数 Nr=29，损耗函数曲线和相频特性曲线如题 19* 解图 (b) 图所示。由图可见，IIRDF 阶数低得多，但相位特性存在非线性，FIRDF 具有线性相位特性。


**题 19* 解图：** (a) IIR 滤波器（椭圆）的损耗函数曲线和相频特性曲线。


**题 19* 解图：** (b) FIR 滤波器（等波纹）的损耗函数曲线和相频特性曲线。

<!-- pages: 21-24 -->

第 6 章 有限脉冲响应 (FIR) 数字滤波器的设计

## 20*. 调用 MATLAB 工具箱函数 fir1 设计线性相位低通 FIR 滤波器，要求希望逼近的理想低通滤波器通带截止频率 $\omega_c = \pi/4$ rad，滤波器长度 $N=21$。分别选用矩形窗、Hanning 窗、Hamming 窗和 Blackman 窗进行设计，绘制用每种窗函数设计的单位脉冲响应 $h(n)$ 及其损耗函数曲线，并进行比较，观察各种窗函数的设计性能。


**图 1:** 矩形窗设计的 $h(n)$


**图 2:** 矩形窗设计的损耗函数


**图 3:** hanning 窗设计的 $h(n)$


**图 4:** hanning 窗设计的损耗函数


**图 5:** hamming 窗设计的 $h(n)$


**图 6:** hamming 窗设计的损耗函数


**图 7:** blackman 窗设计的 $h(n)$


**图 8:** blackman 窗设计的损耗函数

**题 20* 解图**

**解:** 本题设计程序 `ex720.m` 如下：

```matlab
% ex720.m: 调用 fir1 设计线性相位低通 FIR 滤波器
clear; close all;
N=21; wc=1/4; n=0: 20;
hrn=fir1(N-1, wc, boxcar(N)); % 用矩形窗函数设计
hnn=fir1(N-1, wc, hanning(N)); % 用 hanning 窗设计
hmn=fir1(N-1, wc, hamming(N)); % 用 hamming 窗函数设计
hbn=fir1(N-1, wc, blackman(N)); % 用 blackman 窗函数设计
% 以下为绘图部分 (省略)
```

程序运行结果：用矩形窗、Hanning 窗、Hamming 窗和 Blackman 窗设计的单位脉冲响应 $h(n)$ 及其损耗函数曲线如题 20* 解图所示。由图可见，滤波器长度 $N$ 固定时，矩形窗设计的滤波器过渡带最窄，阻带最小衰减也最小；blackman 窗设计的滤波器过渡带最宽，阻带最小衰减最大。

## 21*. 将要求改成设计线性相位高通 FIR 滤波器，重作题 20。

**解:** 本题的设计程序除了在每个 `fir1` 函数的调用参数中加入滤波器类型参数 “high” 外，与第 20 题的程序完全相同，请读者修改并运行程序，完成本题。

## 22*. 调用 MATLAB 工具箱函数 `remezord` 和 `remez` 设计线性相位低通 FIR 滤波器，实现对模拟信号的采样序列 $x(n)$ 的数字低通滤波处理。指标要求：采样频率为 16 kHz；通带截止频率为 4.5 kHz，通带最小衰减为 1 dB；阻带截止频率为 6 kHz，阻带最小衰减为 75 dB。列出 $h(n)$ 的序列数据，并画出损耗函数曲线。

**解:** 本题设计程序 `ex722.m` 如下：

```matlab
% ex722.m: 调用 remezord 和 remez 设计线性相位低通 FIR 滤波器
Fs=16000; f=[4500, 6000]; % 采样频率，边界频率为模拟频率(Hz)
m=[1, 0];
rp=1; rs=75; dat1=(10^(rp/20)-1)/(10^(rp/20)+1); dat2=10^(-rs/20);
rip=[dat1, dat2];
[M, fo, mo, w]=remezord(f, m, rip, Fs); M=M+1; % 边界频率为模拟频率(Hz)时必须加入采样频率 Fs
hn=remez(M, fo, mo, w)
% 以下为绘图部分 (省略)
```

程序运行结果：

$h(n) =[$
$-0.0023 \quad 0.0026 \quad 0.0207 \quad 0.0131 \quad -0.0185 \quad 0.0032 \quad 0.0278 \quad -0.0306$
$-0.0176 \quad 0.0705 \quad -0.0402 \quad -0.1075 \quad 0.2927 \quad 0.6227 \quad 0.2927 \quad -0.1075$
$-0.0402 \quad 0.0705 \quad -0.0176 \quad -0.0306 \quad 0.0278 \quad 0.0032 \quad -0.0185 \quad 0.0131$
$0.0207 \quad 0.0026 \quad -0.0023]$

单位脉冲响应 $h(n)$ 及其损耗函数曲线如题 22* 解图所示。


**题 22* 解图**

## 23*. 调用 MATLAB 工具箱函数 `remezord` 和 `remez` 设计线性相位高通 FIR 滤波器，实现对模拟信号的采样序列 $x(n)$ 的数字高通滤波处理。指标要求：采样频率为 16 kHz；通带截止频率为 5.5 kHz，通带最小衰减为 1 dB；过渡带宽度小于等于 3.5 kHz，阻带最小衰减为 75 dB。列出 $h(n)$ 的序列数据，并画出损耗函数曲线。

**解:** 滤波器的阻带截止频率 $f_s=5500-3500=2000$ Hz。本题设计程序 `ex723.m` 如下：

```matlab
% ex723.m: 调用 remezord 和 remez 设计线性相位高通 FIR 滤波器
Fs=16000; f=[2000, 5500]; % 采样频率，边界频率为模拟频率(Hz)
m=[0, 1];
rp=1; rs=75; dat1=(10^(rp/20)-1)/(10^(rp/20)+1); dat2=10^(-rs/20);
rip=[dat2, dat1];
[M, fo, mo, w]=remezord(f, m, rip, Fs); % 边界频率为模拟频率(Hz)时必须加入采样频率 Fs
hn=remez(M, fo, mo, w)
```

程序运行结果：滤波器长度为 $N=M+1=11$，单位脉冲响应 $h(n)$ 及其损耗函数曲线如题 23* 解图所示，请读者运行程序查看 $h(n)$ 的数据。


**(a) 单位脉冲响应**


**(b) 损耗函数**

**题 23* 解图**

## 24*. 用窗函数法设计一个线性相位低通 FIR 滤波器，要求通带截止频率为 $0.3\pi$ rad，阻带截止频率为 $0.5\pi$ rad，阻带最小衰减为 40 dB。选择合适的窗函数及其长度，求出并显示所设计的单位脉冲响应 $h(n)$ 的数据，并画出损耗函数曲线和相频特性曲线，请检验设计结果。试不用 `fir1` 函数，直接按照窗函数设计法编程设计。

**解:** 直接按照窗函数设计法的设计程序 `ex724.m` 如下：

```matlab
% ex724.m: 直接按照窗函数设计法编程设计线性相位低通 FIR 滤波器
wp=0.3 * pi; ws=0.5 * pi; rs=40; % 指标参数
Bt=ws-wp; % 过渡带宽度
N=ceil(6.2 * pi/Bt); % 选 hanning 窗，求 wn 长度 N
wc=(wp+ws)/2; r=(N-1)/2; % 理想低通截止频率 wc
n=0: N-1; hdn=sin(wc * (n-r))./(pi * (n-r)); % 计算理想低通的 hdn
hdn(16)=wc/pi; % 在 n=(N-1)/2=15 点为 0/0 型，直接赋值
wn=0.5 * (1-cos(2 * pi * n/(N-1))); % 求窗函数序列 wn
hn=hdn.* wn % 加窗
% 以下为绘图部分 (省略)
```

程序运行结果：单位脉冲响应 $h(n)$ 及其损耗函数曲线如题 24* 解图所示，请读者运行程序查看 $h(n)$ 的数据。


**(a) 单位脉冲响应**


**(b) 损耗函数**

**题 24* 解图**

## 25*. 调用 MATLAB 工具箱函数 `fir1` 设计线性相位高通 FIR 滤波器。要求通带截止频率为 $0.6\pi$ rad，阻带截止频率为 $0.45\pi$，通带最大衰减为 0.2 dB，阻带最小衰减为 45 dB。显示所设计的单位脉冲响应 $h(n)$ 的数据，并画出损耗函数曲线。

**解:** 本题设计程序 `ex725.m` 如下：

```matlab
% ex725.m: 调用 fir1 设计线性相位高通 FIR 滤波器
wp=0.6 * pi; ws=0.45 * pi; rs=45; % 指标参数
wc=(wp+ws)/2; % 理想低通截止频率 wc
Bt=wp-ws; % 过渡带宽度
N1=ceil(6.6 * pi/Bt); % hamming 窗 w(n) 长度
N=N1+mod(N1+1, 2); % 如果 N1 为偶数加 1，保证 N=奇数
hn=fir1(N-1, wc/pi, 'high', hamming(N)) % 计算 hn
subplot 221; yn='h(n)'; tstem(hn, yn) % 调用自编函数 tstem 绘制 hn 波形
subplot 222; A=1; myplot(hn, A); % 调用自编函数 myplot 绘制损耗函数曲线
```

程序运行结果：滤波器长度 $N=45$。单位脉冲响应 $h(n)$ 及其损耗函数曲线如题 25* 解图所示。请读者运行程序查看 $h(n)$ 的数据。


**损耗函数曲线**

**题 25* 解图**

## 26*. 调用 MATLAB 工具箱函数 `fir1` 设计线性相位带通 FIR 滤波器。要求通带截止频率为 $0.55\pi$ rad 和 $0.7\pi$ rad，阻带截止频率为 $0.45\pi$ rad 和 $0.8\pi$ rad，通带最大衰减为

<!-- pages: 25-26 -->
# 第6章 有限脉冲响应(FIR)数字滤波器的设计

0.15 dB，阻带最小衰减为 40 dB。显示所设计的单位脉冲响应 h(n)的数据，并画出损耗函数曲线。

解：本题设计程序 ex726.m 如下：

```matlab
%ex726.m：调用 fir1 设计线性相位带通 FIR 滤波器
wpl=0.55*pi; wpu=0.7*pi; wsl=0.45*pi; wsu=0.8*pi; rs=40; %指标参数
wc=[(wpl+wsl)/2, (wpu+wsu)/2];      %理想带通截止频率 wc
Bt=wpl-wsl;                          %过渡带宽度
N=ceil(6.2*pi/Bt);                   %hanning 窗 wn 长度
hn=fir1(N-1, wc/pi, hanning(N))     %计算 hn
subplot 221; yn='h(n)'; tstem(hn, yn) %调用自编函数 tstem 绘制 hn 波形
subplot 222; A=1; myplot(hn, A);     %调用自编函数 myplot 绘制损耗函数曲线
```
程序运行结果：滤波器长度 N=62。单位脉冲响应 h(n)及其损耗函数曲线如题 26*解图所示。请读者运行程序查看 h(n)的数据。


**题26*解图**

27*．调用 remezord 和 remez 函数完成题 25* 和 26* 所给技术指标的滤波器的设计，并比较设计结果（主要比较滤波器阶数的高低和幅频特性）。

解：本题设计程序 ex727.m 如下：

```matlab
%ex727.m：调用 remezord 和 remez 设计线性相位高通和带通 FIR 滤波器
%按照题 25 指标设计高通滤波器
f=[0.45, 0.6]; m=[0, 1]; rp=0.2; rs=45;       %指标参数
dat1=(10^(rp/20)-1)/(10^(rp/20)+1); dat2=10^(-rs/20); rip=[dat2, dat1];
[M25, fo, mo, w]=remezord(f, m, rip); %M=M+1;
hn25=remez(M25, fo, mo, w)
subplot 221; yn='h(n)'; tstem(hn25, yn); title('(a)') %调用自编函数 tstem 绘制 hn25 波形
subplot 222; A=1; myplot(hn25, A); title('(b)') %调用自编函数 myplot 绘制损耗函数曲线

%按照题 26 指标设计带通滤波器
f=[0.45, 0.55, 0.7, 0.8]; m=[0, 1, 0]; rp=0.15; rs=40; %指标参数
dat1=(10^(rp/20)-1)/(10^(rp/20)+1); dat2=10^(-rs/20); rip=[dat2, dat1, dat2];
[M26, fo, mo, w]=remezord(f, m, rip); M26=M26+1;
hn26=remez(M26, fo, mo, w)
subplot 223; yn='h(n)'; tstem(hn26, yn); title('(c)') %调用自编函数 tstem 绘制 hn26 波形
subplot 224; A=1; myplot(hn26, A); title('(d)') %调用自编函数 myplot 绘制损耗函数曲线
```
程序运行结果：满足题 25 和 26 所给技术指标的滤波器长度分别为 N25=M25+1=29，N26= M26+1=42。高通滤波器的单位脉冲响应 h(n)及其损耗函数曲线如题 27*解图（a）和（b）所示。带通滤波器的单位脉冲响应 h(n)及其损耗函数曲线如题 27*解图（c）和（d）所示。请读者运行程序查看 h(n)的数据。

remez 设计的高通滤波器阶数为窗函数法的 64.44%，remez 设计的带通滤波器阶数为窗函数法的 67.74%。


**题27*解图**