---
title: "第3章 离散傅里叶变换(DFT)及其快速算法(FFT)"
source: "第3章 离散傅里叶变换(DFT)及其快速算法(FFT).pdf"
pages: 35
doc_type: book
language: zh
structure_source: llm_scan
parsed_at: 2026-05-28T06:49:19Z
---

<!-- pages: 1-4 -->

# 第3章 离散傅里叶变换(DFT)及其快速算法(FFT)

本章内容与教材第3、4章内容相对应。
本章是全书的重点之一，更是学习数字信号处理技术的重点内容之一。这是因为 DFT（或 FFT)在数字信号处理这门学科中起着不一般的作用，它开拓了用数字方法在计算机上在频域对信号进行处理的先例，使处理方法更加灵活，能完成模拟信号处理完不成的许多功能，增加了若干新颖的处理内容。
离散傅里叶变换(DFT)也是一种时域到频域的变换，能够表征信号的频域特性，和已学过的 FT 和 ZT 有着密切的联系。但是它有不同于 FT 和 ZT 的物理概念和重要性质，只有很好地掌握了这些概念和性质，才能正确地应用 DFT/FFT，在各种不同的信号处理中充分灵活地发挥作用。
FFT 仅是 DFT 的一种快速算法，重要的物理概念在 DFT 部分，因此一定要掌握 DFT 的基本理论；对于 FFT，只要掌握它的基本快速算法原理和使用方法即可。

## 3.1 学习要点与重要公式

### 3.1.1 学习要点

(1) DFT 的定义和物理意义，DFT 和 FT、ZT 之间的关系；
(2) DFT 的重要性质和定理：隐含周期性、循环移位性质、共轭对称性、实序列 DFT 的特点、循环卷积定理、离散巴塞伐尔定理；
(3) 频率域采样定理；
(4) FFT 的基本原理及其应用。

### 3.1.2 重要公式

1）定义
$$
X(k) = \text{DFT}[x(n)]_N = \sum_{n=0}^{N-1} x(n)W_N^{kn} \quad k = 0, 1, \dots, N-1
$$
$$
x(n) = \text{IDFT}[X(k)]_N = \frac{1}{N} \sum_{k=0}^{N-1} X(k)W_N^{-kn} \quad n = 0, 1, \dots, N-1
$$
2）隐含周期性
$$
$$
X(k + mN) = \sum_{n=0}^{N-1} x(n)W_N^{(k+mN)n} = \sum_{n=0}^{N-1} x(n)W_N^{kn} = X(k)
$$
$$
3）线性性质
若 $y(n) = ax_1(n) + bx_2(n)$， 则 $Y(k) = \text{DFT}[y(n)] = aX_1(k) + bX_2(k)$
4）时域循环移位性质
$$
\text{DFT}[x((n+m))_NR_N(n)] = W_N^{-km}X(k)
$$
5）频域循环移位性质
$$
\text{DFT}[W_N^{nm}x(n)] = X((k+m))_NR_N(k)
$$
6）循环卷积定理
循环卷积：
$$
y_c(n) = \left[ \sum_{m=0}^{L-1} h(m)x((n-m))_L \right]R_L(n) = h(n) \circledast x(n)
$$
循环卷积的矩阵表示：
$$
\begin{bmatrix} y_c(0) \\ y_c(1) \\ y_c(2) \\ \vdots \\ y_c(L-1) \end{bmatrix} = \begin{bmatrix} x(0) & x(L-1) & x(L-2) & \dots & x(1) \\ x(1) & x(0) & x(L-1) & \dots & x(2) \\ x(2) & x(1) & x(0) & \dots & x(3) \\ \vdots & \vdots & \vdots & & \vdots \\ x(L-1) & x(L-2) & x(L-3) & \dots & x(0) \end{bmatrix} \begin{bmatrix} h(0) \\ h(1) \\ h(2) \\ \vdots \\ h(L-1) \end{bmatrix}
$$
循环卷积定理：若
$$
$$
y_c(n) = h(n) \circledast x(n)
$$
$$
则
$$
Y_c(k) = \text{DFT}[y_c(n)]_L = H(k)X(k) \quad k = 0, 1, 2, \dots, L-1
$$
其中 $H(k) = \text{DFT}[h(n)]_L, X(k) = \text{DFT}[x(n)]_L$
6）离散巴塞伐尔定理
$$
\sum_{n=0}^{N-1} |x(n)|^2 = \frac{1}{N} \sum_{k=0}^{N-1} |X(k)|^2
$$
7）共轭对称性质
(1) 长度为 $N$ 的共轭对称序列 $x_{\text{ep}}(n)$ 与反共轭对称序列 $x_{\text{op}}(n)$：
$$
$$
\begin{aligned}
$$
x_{\text{ep}}(n) &= x_{\text{ep}}^*(N-n) \\
x_{\text{op}}(n) &= -x_{\text{op}}^*(N-n)
$$
\end{aligned}
$$
$$
序列 $x(n)$ 的共轭对称分量与共轭反对称分量：
$$
$$
\begin{aligned}
$$
x_{\text{ep}}(n) &= \frac{1}{2}[x(n) + x^*(N-n)] \\
x_{\text{op}}(n) &= \frac{1}{2}[x(n) - x^*(N-n)]
$$
\end{aligned}
$$
$$
(2) 如果 $x(n) = x_r(n) + \text{j}x_i(n)$
且 $X(k) = X_{\text{ep}}(k) + X_{\text{op}}(k)$
则 $X_{\text{ep}}(k) = \text{DFT}[x_r(n)], \quad X_{\text{op}}(k) = \text{DFT}[\text{j}x_i(n)]$
(3) 如果 $x(n) = x_{\text{ep}}(n) + x_{\text{op}}(n)$
且 $X(k) = X_r(k) + \text{j}X_i(k)$
则 $X_r(k) = \text{DFT}[x_{\text{ep}}(n)], \text{j}X_i(k) = \text{DFT}[x_{\text{op}}(n)]$
(4) 实序列 DFT 及 FT 的特点：假设 $x(n)$ 是实序列，$X(k) = \text{DFT}[x(n)]$，则
$$
$$
X(k) = X^*(N-k)
$$
$$
$$
|X(k)| = |X(N-k)|, \quad \theta(k) = -\theta(N-k)
$$

$$
## 3.2 频率域采样

我们知道，时域采样和频域采样各有相应的采样定理。频域采样定理包含以下内容：
(1) 设 $x(n)$ 是任意序列，$X(e^{j\omega}) = \text{FT}[x(n)]$，对 $X(e^{j\omega})$ 等间隔采样得到
$$
X_N(k) = X(e^{j\omega}) \mid_{\omega = \frac{2\pi}{N}k} \quad k = 0, 1, 2, 3, \dots, N-1
$$
则
$$
x_N(n) = \text{IDFT}[X_N(k)] = \sum_{n=-\infty}^{\infty} x(n + iN)R_N(n)
$$
(2) 如果 $x(n)$ 的长度为 $M$，只有当频域采样点数 $N \geqslant M$ 时，$x_N(n) = x(n)$，否则 $\widetilde{x}_N(n) = \sum_{n=-\infty}^{\infty} x(n + iN)$ 会发生时域混叠，$x_N(n) \neq x(n)$。
通过频率域采样得到频域离散序列 $x_N(k)$，再对 $x_N(k)$ 进行 IDFT 得到的序列 $x_N(n)$ 应是原序列 $x(n)$ 以采样点数 $N$ 为周期进行周期化后的主值区序列，这一概念非常重要。
(3) 如果在频率域采样的点数满足频率域采样定理，即采样点数 $N$ 大于等于序列的长度 $M$，则可以用频率采样得到的离散函数 $X(k)$ 恢复原序列的 Z 变换 $X(z)$，公式为
$$
$$
X(z) = \sum_{k=0}^{N-1} X(k)\varphi_k(z)
$$
$$
式中
$$
\varphi_k(z) = \frac{1}{N} \frac{1 - z^{-N}}{1 - W_N^{-k}z^{-1}}
$$
上面第一式称为 $z$ 域内插公式，第二式称为内插函数。

## 3.3 循环卷积和线性卷积的快速计算以及信号的频谱分析

### 3.3.1 循环卷积的快速计算

如果两个序列的长度均不很长，可以直接采用循环卷积的矩阵乘法计算其循环卷积；如果序列较长，可以采用快速算法。快速算法的理论基础是循环卷积定理。设 $h(n)$ 的长度为 $N$，$x(n)$ 的长度为 $M$，计算 $y_c(n) = h(n) \circledast x(n)$ 的快速算法如下：
(1) 计算 $\left. \begin{aligned} H(k) &= \text{FFT}[h(n)] \\ X(k) &= \text{FFT}[x(n)] \end{aligned} \right\} \quad k = 0, 1, 2, 3, \dots, L-1, L = \max[N, M]$
(2) 计算 $Y_c(k) = H(k)X(k) \quad k = 0, 1, 2, \dots, L-1$
(3) 计算 $y_c(n) = \text{IDFT}[Y_c(k)]_L \quad n = 0, 1, 2, \dots, L-1$
说明：如上计算过程中的 DFT 和 IDFT 均采用 FFT 算法时，才称为快速算法，否则比直接在时域计算循环卷积的运算量大 3 倍以上。

### 3.3.2 线性卷积的快速计算——快速卷积法

序列 $h(n)$ 和 $x(n)$ 的长度分别为 $N$ 和 $M$，$L = N + M - 1$，求 $y(n) = h(n) * x(n)$ 的方法如下：
(1) 在 $h(n)$ 的尾部加 $L - N$ 个零点，在 $x(n)$ 的尾部加 $L - M$ 个零点；
(2) 计算 $L$ 点的 $H(k) = \text{FFT}[h(n)]$ 和 $L$ 点的 $X(k) = \text{FFT}[x(n)]$；
(3) 计算 $Y(k) = H(k)X(k)$；
(4) 计算 $Y(n) = \text{IFFT}[Y(k)]，\quad n = 0, 1, 2, 3, \dots, L - 1$。
但当 $h(n)$ 和 $x(n)$ 中任一个的长度很长或者无限长时，需用书上介绍的重叠相加法和重叠保留法。

### 3.3.3 用 DFT/FFT 进行频谱分析

对序列进行 $N$ 点的 DFT/FFT 就是对序列频域的 $N$ 点离散采样，采样点的频率为 $\omega_k = 2\pi k / N, k = 0, 1, 2, \dots, N - 1$。
对信号进行频谱分析要关心三个问题：频谱分辨率、频谱分析范围和分析误差。
DFT 的分辨率指的是频域采样间隔 $2\pi/N$，用 DFT/FFT 进行频谱分析时，在相邻采样点之间的频谱是不知道的，因此频率分辨率是一个重要指标，希望分辨率高，即 $2\pi/N$ 要小，DFT 的变换区间 $N$ 要大。当然，截取信号的长度要足够长。但如果截取的长度不够长，而依靠在所截取的序列尾部加零点，增加变换区间长度，也不会提高分辨率。例如，分析周期序列的频谱，只观察了一个周期的 1/4 长度，用这些数据进行 DFT，再通过尾部增加零点，加大 DFT 的变换区间 $N$，也不能分辨出是周期序列，更不能得到周期序列的精确频率。
用 DFT/FFT 对序列进行频谱分析，频谱分析范围为 $\pi$；用 DFT/FFT 对模拟信号进行频谱分析，频谱分析范围为采样频率的一半，即 $0.5F_s$。
用 DFT/FFT 对信号进行谱分析的误差表现在三个方面，即混叠现象、栅栏效应和截断效应。截断效应包括泄漏和谱间干扰。

## 3.4 例题

[例 3.4.1] 设 $x(n)$ 为存在傅里叶变换的任意序列，其 Z 变换为 $X(z)$，$X(k)$ 是对 $X(z)$ 在单位圆上的 $N$ 点等间隔采样，即
$$
X(k) = X(z) \mid_{z=e^{j\frac{2\pi}{N}k}} \quad k = 0, 1, \dots, N-1
$$
求 $X(k)$ 的 $N$ 点离散傅里叶逆变换(记为 $x_N(n)$)与 $x(n)$ 的关系式。
解：由题意知
$$
X(k) = X(e^{j\omega}) \mid_{\omega = \frac{2\pi}{N}k}
$$
即 $X(k)$ 是对 $X(e^{j\omega})$ 在 $[0, 2\pi]$ 上的 $N$ 点等间隔采样。由于 $X(e^{j\omega})$ 是以 $2\pi$ 为周期的，所以采样序列
$$
\widetilde{X}(k) = X(e^{j\omega}) \mid_{\omega = \frac{2\pi}{N}k} = X((k))_N
$$

<!-- pages: 5-8 -->

即\(\widetilde{X}(k)\)以 \(N\) 为周期。所以它必然与一周期序列 \(\widetilde{x}(n)_N\) 相对应，\(\widetilde{X}(k)\) 为 \(\widetilde{x}(n)_N\) 的 DFS 系数。

$$
\widetilde{x}(n)_N = \frac{1}{N}\sum_{k=0}^{N-1}\widetilde{X}(k)\mathrm{e}^{\mathrm{j}\frac{2\pi}{N}kn}
$$

为了导出 \(\widetilde{x}(n)_N\) 与 \(x(n)\) 之间的关系，应将上式中的 \(\widetilde{X}(k)\) 用 \(x(n)\) 表示：

$$
\widetilde{X}(k) = X(z)\big|_{z=\mathrm{e}^{\mathrm{j}\frac{2\pi}{N}k}} = \sum_{n=-\infty}^{\infty} x(k)z^{-n}\big|_{z=\mathrm{e}^{\mathrm{j}\frac{2\pi}{N}kn}} = \sum_{n=-\infty}^{\infty} x(n)\mathrm{e}^{-\mathrm{j}\frac{2\pi}{N}kn}
$$

所以

$$
\widetilde{x}_N(n) = \frac{1}{N}\sum_{k=0}^{N-1} \left( \sum_{m=-\infty}^{\infty} x(m)\mathrm{e}^{-\mathrm{j}\frac{2\pi}{N}km} \right) \mathrm{e}^{\mathrm{j}\frac{2\pi}{N}kn} = \sum_{m=-\infty}^{\infty} x(m) \frac{1}{N} \sum_{k=0}^{N-1} \mathrm{e}^{\mathrm{j}\frac{2\pi}{N}k(n-m)}
$$

因为

$$
\frac{1}{N} \sum_{k=0}^{N-1} \mathrm{e}^{\mathrm{j}\frac{2\pi}{N}k(n-m)} = \begin{cases} 1 & m = n + rN, \ r \text{ 为整数} \\ 0 & \text{其它} m \end{cases}
$$

$$
\widetilde{x}_N(n) = \sum_{r=-\infty}^{\infty} x(n + rN)
$$

即 \(\widetilde{x}_N(n)\) 是 \(x(n)\) 的周期延拓序列。由 DFT 与 DFS 的关系可得出
$$
$$
\begin{aligned}
$$
x_N(n) &= \text{IDFT}[X(k)] = \widetilde{x}_N(n)R_N(n) \\
&= \sum_{r=-\infty}^{\infty} x(n - rN)R_N(n)
$$
\end{aligned}
$$
\(x_N(n)=\text{IDFT}[X(k)]\) 为 \(x(n)\) 的周期延拓序列（以 \(N\) 为延拓周期）的主值序列。以后这一结论可以直接引用。

$$
[例 3.4.2] 已知
$$x(n) = R_8(n), X(\mathrm{e}^{\mathrm{j}\omega}) = \text{FT}[x(n)]$$
$$
对 \(X(\mathrm{e}^{\mathrm{j}\omega})\) 采样得到 \(X(k)\)，
$$X(k) = X(\mathrm{e}^{\mathrm{j}\omega})\big|_{\omega=\frac{2\pi}{6}k} \qquad k = 0, 1, \cdots, 5$$
求
$$x_6(n) = \text{IDFT}[X(k)] \qquad n = 0, 1, 2, \cdots, 5$$

**解：** 直接根据频域采样概念得到
$$x_6(n) = \sum_{l=-\infty}^{\infty} x(n + 6l) \cdot R_6(n) = R_6(n) + R_2(n)$$

[例 3.4.3] 令 \(X(k)\) 表示 \(x(n)\) 的 \(N\) 点 DFT，分别证明：
(1) 如果 \(x(n)\) 满足关系式
$$x(n) = -x(N - 1 - n)$$
则
$$X(0) = 0$$
(2) 当 \(N\) 为偶数时，如果
$$x(n) = x(N - 1 - n)$$
则
$$X\left(\frac{N}{2}\right) = 0$$

[例 3.4.4] 有限时宽序列的 \(N\) 点离散傅里叶变换相当于其 \(Z\) 变换在单位圆上的 \(N\) 点等间隔采样。我们希望求出 \(X(z)\) 在半径为 \(r\) 的圆上的 \(N\) 点等间隔采样，即
$$\hat{X}(k) = X(z)\big|_{z=r\mathrm{e}^{\mathrm{j}\frac{2\pi}{N}kn}} \qquad k = 0, 1, \cdots, N-1$$
$$
试给出一种用 DFT 计算得到 \(\hat{X}(k)\) 的算法。

$$
[例 3.4.5] 长度为 \(N\) 的一个有限长序列 \(x(n)\) 的 \(N\) 点 DFT 为 \(X(k)\)。另一个长度为 \(2N\) 的序列 \(y(n)\) 定义为
$$y(n) = \begin{cases} x\left(\frac{n}{2}\right) & n \text{ 为偶数} \\ 0 & n \text{ 为奇数} \end{cases}$$
试用 \(X(k)\) 表示 \(y(n)\) 的 \(2N\) 点离散傅里叶变换 \(Y(k)\)。

**解：** 该题可以直接按 DFT 定义求解。
$$
$$
\begin{aligned}
$$
Y(k) &= \sum_{n=0}^{2N-1} y(n)W_{2N}^{kn} = \sum_{n=\text{偶数}}^{2N-1} x\left(\frac{n}{2}\right)W_{2N}^{kn} \\
$$
&= \sum_{l=0}^{N-1} x(l)W_{2N}^{k(2l)} \\
$$
&= \sum_{l=0}^{N-1} x(l)W_N^{kl} \qquad k = 0, 1, \cdots, 2N-1 \\
&= X(k) \qquad k = 0, 1, \cdots, 2N-1 \\
$$
&= X((k))_N R_{2N}(k)
\end{aligned}
$$
$$
上面最后一步采用的是 \(X(k)\) 以 \(N\) 为周期的概念。

$$
[例 3.4.6] 用 DFT 对模拟信号进行谱分析，设模拟信号 \(x_{\text{a}}(t)\) 的最高频率为 \(200\ \text{Hz}\)，以奈奎斯特频率采样得到时域离散序列 \(x(n) = x_{\text{a}}(nT)\)，要求频率分辨率为 \(10\ \text{Hz}\)。假设模拟信号频谱 \(X_{\text{a}}(\mathrm{j}\varOmega)\) 如图 3.4.1 所示，试画出 \(X(\mathrm{e}^{\mathrm{j}\omega}) = \text{FT}[x(n)]\) 和 \(X(k) = \text{DFT}[x(n)]\) 的谱线图，并标出每个 \(k\) 值对应的数字频率 \(\omega_k\) 和模拟频率 \(f_k\) 的取值。

$$

**图 3.4.1**

$$
**解：** 因为最高频率 \(f_{\text{max}} = 200\ \text{Hz}\)，频率分辨率 \(F = 10\ \text{Hz}\)，所以采样频率 \(f_{\text{s}}\) 为
$$f_{\text{s}} = 2f_{\text{max}} = 400\ \text{次/s}, \quad T = \frac{1}{f_{\text{s}}} = \frac{1}{400}\ \text{s}$$
观察时间
$$T_{\text{p}} = \frac{1}{F} = 0.1\ \text{s}$$
采样点数
$$N = T_{\text{p}}f_{\text{s}} = 0.1 \times 400 = 40\ \text{个}$$
$$
所以，对 \(x_{\text{a}}(t)\) 进行采样得
$$x(n) = x_{\text{a}}(nT) \qquad n = 0, 1, \cdots, 39$$
$$X(\mathrm{e}^{\mathrm{j}\omega}) = \text{FT}[x(n)] = \frac{1}{T} \sum_{k=-\infty}^{\infty} X_{\text{a}}\left(\mathrm{j}\frac{\omega}{T} - \mathrm{j}\frac{2\pi}{T}k\right)$$
$$X(k) = \text{DFT}[x(n)] = X(\mathrm{e}^{\mathrm{j}\frac{2\pi}{N}k}) \qquad k = 0, 1, \cdots, 39$$
$$
\(X_{\text{a}}(\mathrm{j}f)\)、\(X(\mathrm{e}^{\mathrm{j}\omega})\) 及 \(X((k))_N\) 分别如图 3.4.2(a)、(b)、(c) 所示。当 \(f_{\text{s}} = 2f_{\text{max}}\) 时，\(f = f_{\text{max}}\) 对应 \(\omega = 2\pi fT = \frac{2\pi f_{\text{max}}}{2f_{\text{max}}} = \pi\)，由 \(\omega = \pi = \frac{2\pi}{N}k\)，可求得 \(k = \frac{N}{2}\)；当 \(f_{\text{s}} > 2f_{\text{max}}\) 时，\(f_{\text{max}}\) 对应的数字频率 \(\omega = 2\pi f_{\text{max}}T < \pi\)。\(X_{\text{a}}(\mathrm{j}f)\) 与 \(X(k)\) 的对应关系（由图 3.4.2(a)、(c) 可看出）为
$$TX(k) = X_{\text{a}}(\mathrm{j}kF) \qquad k = 0, 1, \cdots, \frac{N}{2}$$
$$F = \frac{f_{\text{s}}}{N} = \frac{1}{NT} = \frac{1}{T_{\text{p}}}\ \text{Hz}$$


**图 3.4.2**

<!-- pages: 9-12 -->

该例题主要说明了模拟信号 $x_a(t)$ 的时域采样序列 $x(n)$ 的 $N$ 点离散傅里叶变换 $X(k)$ 与 $x_a(t)$ 的频谱 $X_a(jf)$ 之间的对应关系。只有搞清该关系，才能由 $X(k)$ 看出 $X_a(jf)$ 的频谱特征。否则，即使计算出 $X(k)$，也搞不清 $X(k)$ 的第 $k$ 条谱线对应于 $X_a(jf)$ 的哪个频率点的采样，这样就达不到谱分析的目的。实际中，$X(k)$ 求出后，也可以将横坐标换算成模拟频率，换算公式为 $f_k = kF = k/(NT)$。直接作出 $X_a(kF) = X_a(f_k) = TX(k)$ 谱线图。

**[例 3.4.7]** 已知 $x(n)$ 长度为 $N$，$X(z) = \text{ZT}[x(n)]$。要求计算 $X(z)$ 在单位圆上的 $M$ 个等间隔采样。假定 $M<N$，试设计一种计算 $M$ 个采样值的方法，它只需计算一次 $M$ 点 DFT。

**解：** 这是一个典型的频域采样理论应用问题。根据频域采样、时域周期延拓以及 DFT 的惟一性概念，容易解答该题。

由频域采样理论知道，如果

$$X(k) = X(z) \big|_{z=e^{j\frac{2\pi}{M}k}} \quad k = 0, 1, \cdots, M-1$$

即 $X(k)$ 是 $X(z)$ 在单位圆上的 $M$ 点等间隔采样，则

$$x_M(n) = \text{IDFT}[X(k)] = \sum_{r=-\infty}^{\infty} x(n + rM)R_M(n)$$

当然

即首先将 $x(n)$ 以 $M$ 为周期进行周期延拓，取主值区序列 $x_M(n)$，最后进行 $M$ 点 DFT 则可得到 $X(k) = X(e^{j\frac{2\pi}{M}k}), k=0, 1, \cdots, M-1$。

应当注意，$M<N$，所以周期延拓 $x(n)$ 时，有重叠区，$x_M(n)$ 在重叠区上的值等于重叠在 $n$ 点处的所有序列值相加。

显然，由于频域采样点数 $M<N$，不满足频域采样定理，所以，不能由 $X(k)$ 恢复 $x(n)$，即丢失了 $x(n)$ 的频谱信息。

**[例 3.4.8]** 已知序列
$$x(n) = \{1, 2, 2, 1\}, \quad h(n) = \{3, 2, -1, 1\}$$
(1) 计算 5 点循环卷积 $y_5(n) = x(n) \circledast h(n)$；
(2) 用计算循环卷积的方法计算线性卷积 $y(n) = x(n) * h(n)$。

**解：** (1) 这里是 2 个短序列的循环卷积计算，可以用矩阵相乘的方法（即用教材第 82 页式(3.2.7)）计算，也可以用类似于线性卷积的列表法。因为要求 5 点循环卷积，因此每个序列尾部加一个零值点，按照教材式(3.2.7)写出

$$
$$
\begin{bmatrix}
y_5(0) \\
y_5(1) \\
y_5(2) \\
y_5(3) \\
y_5(4)
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 1 & 2 & 2 \\
2 & 1 & 0 & 1 & 2 \\
2 & 2 & 1 & 0 & 1 \\
1 & 2 & 2 & 1 & 0 \\
0 & 1 & 2 & 2 & 1
\end{bmatrix}
\begin{bmatrix}
3 \\
2 \\
-1 \\
1 \\
0
\end{bmatrix}
=
\begin{bmatrix}
4 \\
9 \\
9 \\
6 \\
2
\end{bmatrix}
$$

$$
得到 $y_5(n) = \{4, 9, 9, 6, 2\}$。注意上面矩阵方程右边第一个 $5 \times 5$ 矩阵称为 $x(n)$ 的循环矩阵，它的第一行是 $x(n)$ 的 5 点循环倒相，第二行是第一行的向右循环移一位，第三行是第二行向右循环移一位，依次类推。

用列表法可以省去写矩阵方程，下面用列表法解：

| 3 | 2 | -1 | 1 | 0 |  |
|---|---|---|---|---|---|
| 1 | 0 | 1 | 2 | 2 | $y_5(0)=4$ |
| 2 | 1 | 0 | 1 | 2 | $y_5(1)=9$ |
| 2 | 2 | 1 | 0 | 1 | $y_5(2)=9$ |
| 1 | 2 | 2 | 1 | 0 | $y_5(3)=6$ |
| 0 | 1 | 2 | 2 | 1 | $y_5(4)=2$ |

表中的第一行是 $h(n)$ 序列，第 2、3、4、5、6 行的前五列即是 $x(n)$ 的循环矩阵的对应行。同样得到 $y_5(n) = \{4, 9, 9, 6, 2\}$。

(2) 我们知道只有当循环卷积的长度大于等于线性卷积结果的长度时，循环卷积的结果才能等于线性卷积的结果。该题目中线性卷积的长度为 $L=4+4-1=7$，因此循环卷积的长度可选 $L=7$，这样两个序列的尾部分别加 3 个零点后，进行 7 点循环卷积，其结果就是线性卷积的结果。即

$$
$$
\begin{bmatrix}
y(0) \\
y(1) \\
y(2) \\
y(3) \\
y(4) \\
y(5) \\
y(6)
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 2 & 2 \\
2 & 1 & 0 & 0 & 0 & 1 & 2 \\
2 & 2 & 1 & 0 & 0 & 0 & 1 \\
1 & 2 & 2 & 1 & 0 & 0 & 0 \\
0 & 1 & 2 & 2 & 1 & 0 & 0 \\
0 & 0 & 1 & 2 & 2 & 1 & 0 \\
0 & 0 & 0 & 1 & 2 & 2 & 1
\end{bmatrix}
\begin{bmatrix}
3 \\
2 \\
-1 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}
=
\begin{bmatrix}
3 \\
8 \\
9 \\
6 \\
2 \\
1 \\
1
\end{bmatrix}
$$

$$
得到

$$y(n) = x(n) * h(n) = \{3, 8, 9, 6, 2, 1, 1\}$$

**[例 3.4.9]** 已知实序列 $x(n)$ 和 $y(n)$ 的 DFT 分别为 $X(k)$ 和 $Y(k)$，试给出一种计算一次 IDFT 就可得出 $x(n)$ 和 $y(n)$ 的计算方法。（选自 2004 年北京交通大学硕士研究生入学试题。）

**[例 3.4.10]** 已知 $x(n) (n=0, 1, 2, \cdots, 1023)$, $h(n) (n=0, 1, 2, \cdots, 15)$。在进行线性卷积时，每次只能进行 16 点线性卷积运算。试问为了得到 $y(n) = x(n) * h(n)$ 的正确结果，原始数据应作怎样处理，并如何进行运算。（选自 1996 年西安电子科技大学硕士研究生入学试题。）

**解：** 将 $x(n)$ 进行分组后，采用书上介绍的重叠相加法。

$x(n)$ 的长度为 1024 点，按照 16 分组，共分 64 组，记为 $x_i(n), i=0, 1, 2, \cdots, 63$。即
$$x(n) = \sum_{i=0}^{63} x_i(n - 16i), \quad x_i(n) = x(n + 16i)R_{16}(n)$$
$$y(n) = x(n) * h(n) = \sum_{i=0}^{63} y_i(n - 16i)$$
式中，$y_i(n) = x_i(n) * h(n), i=0, 1, 2, \cdots, 63$。可以用 FFT 计算 16 点的线性卷积 $y_i(n)$。最后结果 $y(n)$ 的长度为 $1024+16-1=1039$。

**[例 3.4.11]** $x(n)$ 是一个长度 $M=142$ 的信号序列，即：$x(n)=0$，当 $n<0$ 或 $n \geqslant M$ 时。现希望用 $N=100$ 的 DFT 来分析频谱。试问：如何通过一次 $N=100$ 的 DFT 求得 $X(e^{j\omega}) \big|_{\omega = \frac{2\pi}{N}k}, k=0, 1, 2, \cdots, 99$；这样进行频谱分析是否存在误差？（选自 2006 年西安交通大学硕士研究生入学试题。）

**解：** 通过频率域采样得到频域离散函数，再对其进行 IDFT 得到的序列应是原序列 $x(n)$ 以 $N$ 为周期进行周期化后的主值序列。按照这一概念，在频域 $0\sim 2\pi$ 采样 100 点，那么相应的时域应以 100 为周期进行延拓后截取主值区。该题要求用一次 100 点的 DFT 求得，可以用下式计算：
$$X_{100}(k) = \text{DFT}\left[ \sum_{i=-\infty}^{\infty} x(n + 100i)R_{100}(n) \right]$$
式中，$k$ 对应的频率为 $\omega_k = \frac{2\pi k}{100}$ rad。这样进行频谱分析存在误差，误差是因为时域混叠引起的。

## 3.5 教材第 3 章习题与上机题解答

1. 计算以下序列的 $N$ 点 DFT，在变换区间 $0 \leqslant n \leqslant N-1$ 内，序列定义为
(1) $x(n) = 1$
(2) $x(n) = \delta(n)$
(3) $x(n) = \delta(n - n_0) \quad 0 < n_0 < N$
(4) $x(n) = R_m(n) \quad 0 < m < N$
(5) $x(n) = e^{j\frac{2\pi}{N}mn} \quad 0 < m < N$
(6) $x(n) = \cos\left( \frac{2\pi}{N}mn \right) \quad 0 < m < N$
(7) $x(n) = e^{j\omega_0 n} R_N(n)$
(8) $x(n) = \sin(\omega_0 n) R_N(n)$
(9) $x(n) = \cos(\omega_0 n) R_N(N)$
(10) $x(n) = nR_N(n)$

**解：**

(1) 
$$
$$
\begin{aligned}
$$
X(k) &= \sum_{n=0}^{N-1} 1 \cdot W_N^{kn} = \sum_{n=0}^{N-1} e^{-j\frac{2\pi}{N}kn} = \frac{1 - e^{-j\frac{2\pi}{N}kN}}{1 - e^{-j\frac{2\pi}{N}k}} \\
$$
&= \begin{cases}
N & k = 0 \\
$$
0 & k = 1, 2, \cdots, N-1
$$
\end{cases}
\end{aligned}
$$

$$
(2) 
$$X(k) = \sum_{n=0}^{N-1} \delta(n)W_N^{kn} = \sum_{n=0}^{N-1} \delta(n) = 1 \quad k = 0, 1, \cdots, N-1$$

(3) 
$$
$$
\begin{aligned}
X(k) &= \sum_{n=0}^{N-1} \delta(n - n_0)W_N^{kn} \\
$$
&= W_N^{kn_0} \sum_{n=0}^{N-1} \delta(n - n_0) = W_N^{kn_0} \quad k = 0, 1, \cdots, N-1
$$
\end{aligned}
$$

$$
(4) 
$$
$$
\begin{aligned}
$$
X(k) &= \sum_{n=0}^{m-1} W_N^{kn} = \frac{1 - W_N^{km}}{1 - W_N^k} = e^{-j\frac{\pi}{N}(m-1)k} \frac{\sin\left( \frac{\pi}{N}mk \right)}{\sin\left( \frac{\pi}{N}k \right)} R_N(k)
$$
\end{aligned}
$$

$$
(5) 
$$
$$
\begin{aligned}
$$
X(k) &= \sum_{n=0}^{N-1} e^{j\frac{2\pi}{N}mn} W_N^{kn} = \sum_{n=0}^{N-1} e^{j\frac{2\pi}{N}(m-k)n} = \frac{1 - e^{-j\frac{2\pi}{N}(m-k)N}}{1 - e^{-j\frac{2\pi}{N}(m-k)}} \\
$$
&= \begin{cases}
N & k = m \\
0 & k \neq m
\end{cases}
$$
, \quad 0 \leqslant k \leqslant N-1
$$
\end{aligned}
$$

$$
(7) 
$$
$$
\begin{aligned}
$$
X_7(k) &= \sum_{n=0}^{N-1} e^{j\omega_0 n} W_N^{kn} = \sum_{n=0}^{N-1} e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)n} = \frac{1 - e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)N}}{1 - e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)}} \\
&= e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)\frac{N-1}{2}} \frac{\sin\left[ \left( \omega_0 - \frac{2\pi}{N}k \right) \frac{N}{2} \right]}{\sin\left[ \frac{\left( \omega_0 - \frac{2\pi}{N}k \right)}{2} \right]} \quad k = 0, 1, \cdots, N-1
$$
\end{aligned}
$$
$$
或
$$X_7(k) = \frac{1 - e^{j\omega_0 N}}{1 - e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)}} \quad k = 0, 1, \cdots, N-1$$

(8) 解法一 直接计算：
$$
$$
\begin{aligned}
$$
x_8(n) &= \sin(\omega_0 n)R_N(n) = \frac{1}{2j} \left[ e^{j\omega_0 n} - e^{-j\omega_0 n} \right] R_N(n) \\
X_8(n) &= \sum_{n=0}^{N-1} x_8(n) W_N^{kn} = \frac{1}{2j} \sum_{n=0}^{N-1} \left[ e^{j\omega_0 n} - e^{-j\omega_0 n} \right] e^{-j\frac{2\pi}{N}kn} \\
&= \frac{1}{2j} \left[ \sum_{n=0}^{N-1} e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)n} - \sum_{n=0}^{N-1} e^{-j\left( \omega_0 + \frac{2\pi}{N}k \right)n} \right] \\
&= \frac{1}{2j} \left[ \frac{1 - e^{j\omega_0 N}}{1 - e^{j\left( \omega_0 - \frac{2\pi}{N}k \right)}} - \frac{1 - e^{-j\omega_0 N}}{1 - e^{-j\left( \omega_0 + \frac{2\pi}{N}k \right)}} \right]
$$
\end{aligned}
$$

$$
<!-- pages: 13-16 -->
# 第3章 离散傅里叶变换(DFT)及其快速算法(FFT)

**解法二** 由 DFT 的共轭对称性求解。
因为
$$x_7(n) = e^{j\omega_0 n}R_N(n) = [\cos(\omega_0 n) + j\sin(\omega_0 n)]R_N(n)$$
所以
$$x_8(n) = \sin(\omega_0 n)R_N(n) = \text{Im}[x_7(n)]$$
所以
$$\text{DFT}[jx_8(n)] = \text{DFT}[j\text{Im}[x_7(n)]] = X_{7o}(k)$$
即
$$X_8(k) = -jX_{7o}(k) = -j\frac{1}{2}[X_7(k) - X_7^*(N-k)]$$
结果与解法一所得结果相同。此题验证了共轭对称性。

**(9) 解法一** 直接计算：
$$x_9(n) \cos(\omega_0 n)R_N(n) = \frac{1}{2}[e^{j\omega_0 n} + e^{-j\omega_0 n}]$$
$$X_9(k) = \sum_{n=0}^{N-1} x_9(n)W_N^{kn}$$
$$= \frac{1}{2} \sum_{n=0}^{N-1} [e^{j\omega_0 n} + e^{-j\omega_0 n}]e^{-j\frac{2\pi}{N}kn}$$
$$= \frac{1}{2} \left[ \frac{1-e^{j\omega_0 N}}{1-e^{j(\omega_0 - \frac{2\pi}{N}k)}} + \frac{1-e^{-j\omega_0 N}}{1-e^{-j(\omega_0 + \frac{2\pi}{N}k)}} \right]$$

**解法二** 由 DFT 共轭对称性可得同样结果。
因为
$$x_9(n) = \cos(\omega_0 n)R_N(n) = \text{Re}[x_7(n)]$$
所以
$$X_9(k) = X_{7e}(k) = \frac{1}{2}[X_7(k) + X_7^*(N-k)]$$
$$= \frac{1}{2} \left[ \frac{1-e^{j\omega_0 N}}{1-e^{j(\omega_0 - \frac{2\pi}{N}k)}} + \frac{1-e^{-j\omega_0 N}}{1-e^{-j(\omega_0 + \frac{2\pi}{N}k)}} \right]$$

**(10) 解法一**
$$X(k) = \sum_{n=0}^{N-1} n W_N^{kn} \quad k=0, 1, \cdots, N-1$$
上式直接计算较难，可根据循环移位性质来求解 $X(k)$。因为 $x(n)=nR_N(n)$，所以
$$x(n) - x((n-1))_N R_N(n) + N\delta(n) = R_N(n)$$
等式两边进行 DFT，得到
$$X(k) - X(k)W_N^k + N = N\delta(k)$$
故
$$X(k) = \frac{N[\delta(k)-1]}{1-W_N^k} \quad k=1, 2, \cdots, N-1$$
当 $k=0$ 时，可直接计算得出 $X(0)$ 为
$$X(0) = \sum_{n=0}^{N-1} n W_N^0 = \sum_{n=0}^{N-1} n = \frac{N(N-1)}{2}$$
这样，$X(k)$ 可写成如下形式：
$$X(k) = \begin{cases} \frac{N(N-1)}{2} & k=0 \\ \frac{-N}{1-W_N^k} & k=1, 2, \cdots, N-1 \end{cases}$$

**解法二**
$k=0$ 时，
$$X(k) = \sum_{n=0}^{N-1} n = \frac{N(N-1)}{2}$$
$k \neq 0$ 时，
$$X(k) = 0 + W_N^k + 2W_N^{2k} + 3W_N^{3k} + \cdots + (N-1)W_N^{(N-1)k}$$
$$W_N^k X(k) = 0 + W_N^{2k} + 2W_N^{3k} + 3W_N^{4k} + \cdots + (N-2)W_N^{(N-1)k} + (N-1)$$
$$X(k) - W_N^k X(k) = \sum_{m=1}^{N-1} W_N^{km} - (N-1)$$
$$= \sum_{n=0}^{N-1} W_N^{kn} - 1 - (N-1) = -N$$
所以，$X(k) = \frac{-N}{1-W_N^k}$，$k \neq 0$，即
$$X(k) = \begin{cases} \frac{N(N-1)}{2} & k=0 \\ \frac{-N}{1-W_N^k} & k=1, 2, \cdots, N-1 \end{cases}$$

**2. 已知下列 $X(k)$，求 $x(n)=\text{IDFT}[X(k)]$**
(1)
$$X(k) = \begin{cases} \frac{N}{2}e^{j\theta} & k=m \\ \frac{N}{2}e^{-j\theta} & k=N-m \\ 0 & \text{其它}k \end{cases}$$
(2)
$$X(k) = \begin{cases} -\frac{N}{2}e^{j\theta} & k=m \\ j\frac{N}{2}e^{-j\theta} & k=N-m \\ 0 & \text{其它}k \end{cases}$$
其中，$m$ 为正整数，$0<m<N/2$，$N$ 为变换区间长度。

(2)
$$x(n) = \frac{1}{N} \left[ -\frac{N}{2} j e^{j\theta} W_N^{-mn} + \frac{N}{2} j e^{-j\theta} W_N^{-(N-m)n} \right]$$
$$= \frac{1}{2j} [ e^{j(\frac{2\pi}{N}mn + \theta)} - e^{-j(\frac{2\pi}{N}mn + \theta)} ]$$
$$= \sin\left(\frac{2\pi}{N}mn + \theta\right) \quad n=0, 1, \cdots, N-1$$


**图(a):** 序列 $x_1(n)$


**图(b):** 序列 $x_2(n)$


**图(c):** 循环卷积结果 $y(n)=x_1(n) \circledast x_2(n)$

题3解图

**4. 证明 DFT 的对称定理，即假设 $X(k)=\text{DFT}[x(n)]$，证明**
$$\text{DFT}[X(n)] = Nx(N-k)$$
**证：** 因为
$$X(k) = \sum_{n=0}^{N-1} x(n)W_N^{kn}$$
所以
$$\text{DFT}[X(n)] = \sum_{n=0}^{N-1} X(n)W_N^{kn} = \sum_{n=0}^{N-1} \left[ \sum_{m=0}^{N-1} x(m)W_N^{mn} \right] W_N^{kn}$$
$$= \sum_{m=0}^{N-1} x(m) \sum_{n=0}^{N-1} W_N^{n(m+k)}$$
由于
$$\sum_{n=0}^{N-1} W_N^{n(m+k)} = \begin{cases} N & m = N-k \\ 0 & m \neq N-k, 0 \leq m \leq N-1 \end{cases}$$
所以
$$\text{DFT}[X(n)] = Nx(N-k) \quad k=0, 1, \cdots, N-1$$

**5. 如果 $X(k)=\text{DFT}[x(n)]$，证明 DFT 的初值定理**
$$x(0) = \frac{1}{N} \sum_{k=0}^{N-1} X(k)$$
**证：** 由 IDFT 定义式
$$x(n) = \frac{1}{N} \sum_{k=0}^{N-1} X(k)W_N^{-kn} \quad n=0, 1, \cdots, N-1$$
可知
$$x(0) = \frac{1}{N} \sum_{k=0}^{N-1} X(k)$$

**7. 证明：若 $x(n)$ 为实序列，$X(k)=\text{DFT}[x(n)]_N$，则 $X(k)$ 为共轭对称序列，即 $X(k)=X^*(N-k)$；若 $x(n)$ 实偶对称，即 $x(n)=x(N-n)$，则 $X(k)$ 也实偶对称；若 $x(n)$ 实奇对称，即 $x(n)=-x(N-n)$，则 $X(k)$ 为纯虚函数并奇对称。**
**证：** (1) 由教材(3.2.17)～(3.2.20)式知道，如果将 $x(n)$ 表示为
$$x(n) = x_r(n) + jx_i(n)$$
则

<!-- pages: 17-20 -->

$$X(k) = \text{DFT}[x(n)] = X_{\text{ep}}(k) + X_{\text{op}}(k)$$

其中， $X_{\text{ep}}(k)=\text{DFT}[x_{\text{r}}(n)]$，是 $X(k)$的共轭对称分量；$X_{\text{op}}(k)=\text{DFT}[jx_{\text{i}}(n)]$，是 $X(k)$的共轭反对称分量。所以，如果 $x(n)$为实序列，则 $X_{\text{op}}(k)=\text{DFT}[jx_{\text{i}}(n)]=0$，故 $X(k)=\text{DFT}[x(n)]=X_{\text{ep}}(k)$，即 $X(k)=X^*(N-k)$。

（2）由 DFT 的共轭对称性可知，如果

$$x(n) = x_{\text{ep}}(n) + x_{\text{op}}(n)$$

且

$$X(k) = \text{Re}[X(k)] + j\text{Im}[X(k)]$$

则

$$\text{Re}[X(k)] = \text{DFT}[x_{\text{ep}}(n)], \quad j\text{Im}[X(k)] = \text{DFT}[x_{\text{op}}(n)]$$

所以，当 $x(n)=x(N-n)$时，等价于上式中 $x_{\text{op}}(n)=0$，$x(n)$中只有 $x_{\text{ep}}(n)$成分，所以 $X(k)$只有实部，即 $X(k)$为实函数。又由（1）证明结果知道，实序列的 DFT 必然为共轭对称函数，即 $X(k)=X^*(N-k)=X(N-k)$，所以 $X(k)$实偶对称。

同理，当 $x(n)=-x(N-n)$时，等价于 $x(n)$只有 $x_{\text{op}}(n)$成分（即 $x_{\text{ep}}(n)=0$），故 $X(k)$只有纯虚部，且由于 $x(n)$为实序列，即 $X(k)$共轭对称，$X(k)=X^*(N-k)=-X(N-k)$，为纯虚奇函数。

8. 证明频域循环移位性质：设 $X(k)=\text{DFT}[x(n)]$，$Y(k)=\text{DFT}[y(n)]$，如果 $Y(k)=X((k+l))_NR_N(k)$，则

$$y(n) = \text{IDFT}[Y(k)] = W_N^{ln}x(n)$$

证：

$$y(n) = \text{IDFT}[Y(k)] = \frac{1}{N}\sum_{k=0}^{N-1}Y(k)W_N^{-kn}$$

$$= \frac{1}{N}\sum_{k=0}^{N-1}X((k+l))_NW_N^{-kn}$$

$$= W_N^{ln} \frac{1}{N}\sum_{k=0}^{N-1}X((k+l))_NW_N^{-(k+l)n}$$

令 $m=k+l$，则

$$y(n) = W_N^{ln} \frac{1}{N}\sum_{m=l}^{N-1+l}X((m))_NW_N^{-mn}$$

$$= W_N^{ln} \frac{1}{N}\sum_{m=0}^{N-1}X(m)W_N^{-mn} = W_N^{ln}x(n)$$

9. 已知 $x(n)$长度为 $N$，$X(k)=\text{DFT}[x(n)]$，

$$y(n) = \begin{cases} x(n) & 0 \leqslant n \leqslant N-1 \\ 0 & N \leqslant n \leqslant mN-1, m\text{为自然数} \end{cases}$$

$$Y(k) = \text{DFT}[y(n)]_{mN} \quad 0 \leqslant k \leqslant mN-1$$

求 $Y(k)$与 $X(k)$的关系式。

解：

$$Y(k) = \sum_{n=0}^{mN-1}y(n)W_{mN}^{kn} = \sum_{n=0}^{N-1}x(n)W_{mN}^{kn}$$

$$= \sum_{n=0}^{N-1}x(n)W_N^{\frac{k}{m}n} = X\left(\frac{k}{m}\right) \quad \frac{k}{m} = \text{整数}$$

10. 证明离散相关定理。若

$$X(k) = X_1^*(k)X_2(k)$$

$$x(n) = \text{IDFT}[X(k)] = \sum_{l=0}^{N-1}x_1^*(l)x_2((l+n))_NR_N(n)$$

证：根据 DFT 的唯一性，只要证明

$$\text{DFT}[x(n)]_N = \text{DFT}\left[\sum_{l=0}^{N-1}x_1^*(l)x_2((l+n))_NR_N(n)\right]_N = X_1^*(k)X_2(k)$$

即可。

$$X(k) = \text{DFT}[x(n)] = \sum_{n=0}^{N-1}x(n)W_N^{kn}$$

$$= \sum_{n=0}^{N-1}\left(\sum_{l=0}^{N-1}x_1^*(l)x_2((l+n))_N\right)W_N^{kn}$$

$$= \sum_{l=0}^{N-1}x_1^*(l)\sum_{n=0}^{N-1}x_2((l+n))_NW_N^{kn}$$

$$= \left(\sum_{l=0}^{N-1}x_1(l)W_N^{kl}\right)^*\sum_{n=0}^{N-1}x_2((l+n))_NW_N^{k(l+n)}$$

$$= X_1^*(k)\sum_{n=0}^{N-1}x_2((l+n))_NW_N^{k(l+n)}$$

令 $m=l+n$，则

$$\sum_{n=0}^{N-1}x_2((l-m))_NW_N^{k(l+n)} = \sum_{m=l}^{N-1+l}x_2((m))_NW_N^{km}$$

$$= \sum_{m=0}^{N-1}x_2((m))_NW_N^{km} = \sum_{m=0}^{N-1}x_2(m)W_N^{km} = X_2(k)$$

所以

$$X(k) = X_1^*(k)X_2(k) \quad 0 \leqslant k \leqslant N-1$$

当然也可以直接计算 $X(k)=X_1^*(k)X_2(k)$的 IDFT。

$$x(n) = \text{IDFT}[X(k)] = \text{IDFT}[X_1^*(k)X_2(k)]$$

$$= \frac{1}{N}\sum_{k=0}^{N-1}X_1^*(k)X_2(k)W_N^{-kn} = \frac{1}{N}\sum_{k=0}^{N-1}\left(\sum_{l=0}^{N-1}x_1(l)W_N^{kl}\right)^*X_2(k)W_N^{-kn}$$

$$= \sum_{l=0}^{N-1}x_1^*(l)\frac{1}{N}\sum_{k=0}^{N-1}X_2(k)W_N^{-k(l+n)} \quad 0 \leqslant n \leqslant N-1$$

由于

$$\frac{1}{N}\sum_{k=0}^{N-1}X_2(k)W_N^{-k(l+n)} = \frac{1}{N}\sum_{k=0}^{N-1}X_2(k)W^{-k((l+n))_N} = x_2((l+n))_N \quad 0 \leqslant n \leqslant N-1$$

$$x(n) = \sum_{l=0}^{N-1}x_1^*(l)x_2((l+n))_NR_N(n)$$

11. 证明离散帕塞瓦尔定理。若 $X(k)=\text{DFT}[x(n)]$，则

$$\sum_{n=0}^{N-1}|x(n)|^2 = \frac{1}{N}\sum_{k=0}^{N-1}|X(k)|^2$$

$$\frac{1}{N}\sum_{n=0}^{N-1}|X(k)|^2 = \frac{1}{N}\sum_{k=0}^{N-1}X(k)X^*(k) = \frac{1}{N}\sum_{k=0}^{N-1}X(k)\left(\sum_{n=0}^{N-1}x(n)W_N^{kn}\right)^*$$

$$= \sum_{n=0}^{N-1}x^*(n)\frac{1}{N}\sum_{k=0}^{N-1}X(k)W_N^{-kn}$$

$$= \sum_{n=0}^{N-1}x^*(n)x(n) = \sum_{n=0}^{N-1}|x(n)|^2$$

12. 已知 $f(n)=x(n)+jy(n)$，$x(n)$与 $y(n)$均为长度为 $N$ 的实序列。设

$$F(k) = \text{DFT}[f(n)]_N \quad 0 \leqslant k \leqslant N-1$$

(1) $$F(k) = \frac{1-a^N}{1-aW_N^k} + j\frac{1-b^N}{1-bW_N^k} \quad a, b\text{为实数}$$

(2) $$F(k) = 1 + jN$$

试求 $X(k)=\text{DFT}[x(n)]_N$，$Y(k)=\text{DFT}[y(n)]_N$ 以及 $x(n)$和 $y(n)$。

解：由 DFT 的共轭对称性可知

$$x(n) \leftrightarrow X(k) = F_{\text{ep}}(k)$$

$$jy(n) \leftrightarrow jY(k) = F_{\text{op}}(k)$$

方法一 (1)

$$X(k) = F_{\text{ep}}(k) = \frac{1}{2}[F(k) + F^*(N-k)] = \frac{1-a^N}{1-aW_N^k}$$

$$Y(k) = -jF_{\text{op}}(k) = \frac{1}{2j}[F(k) - F^*(N-k)] = \frac{1-b^N}{1-bW_N^k}$$

$$x(n) = \frac{1}{N}\sum_{k=0}^{N-1}X(k)W_N^{-kn} = \frac{1}{N}\sum_{k=0}^{N-1}\frac{1-a^N}{1-aW_N^k}W_N^{-kn}$$

$$= \frac{1}{N}\sum_{k=0}^{N-1}\left(\sum_{m=0}^{N-1}a^mW_N^{km}\right)W_N^{-kn} = \sum_{m=0}^{N-1}a^m\frac{1}{N}\sum_{k=0}^{N-1}W_N^{k(m-n)} \quad 0 \leqslant n \leqslant N-1$$

$$\frac{1}{N}\sum_{k=0}^{N-1}W_N^{k(m-n)} = \begin{cases} 1 & m=n \\ 0 & m \neq n \end{cases}, 0 \leqslant n, m \leqslant N-1$$

$$x(n) = a^n \quad 0 \leqslant n \leqslant N-1$$

同理

$$y(n) = b^n \quad 0 \leqslant n \leqslant N-1$$

$$X(k) = \frac{1}{2}[F(k) + F^*(N-k)] = \frac{1}{2}[1+jN+1-jN] = 1$$

$$Y(k) = \frac{1}{2j}[F(k) - F^*(N-k)] = N$$

$$x(n) = \frac{1}{N}\sum_{k=0}^{N-1}W_N^{-kn} = \delta(n)$$

$$y(n) = \frac{1}{N}\sum_{k=0}^{N-1}NW_N^{-kn} = N\delta(n)$$

方法二 令

$$A(k) = \frac{1-a^N}{1-aW_N^k}, \quad B(k) = j\frac{1-b^N}{1-bW_N^k}$$

只要证明 $A(k)$为共轭对称的，$B(k)$为共轭反对称，则就会有

$$A(k) = F_{\text{ep}}(k) = X(k), \quad B(k) = F_{\text{op}}(k) = jY(k)$$

因为

$$A^*(N-k) = \left(\frac{1-a^N}{1-aW_N^{N-k}}\right)^* = \frac{1-a^N}{1-aW_N^k} = A(k), \text{共轭对称}$$

$$B^*(N-k) = \left(j\frac{1-a^N}{1-bW_N^{N-k}}\right)^* = -j\frac{1-b^N}{1-bW_N^k} = -B(k), \text{共轭反对称}$$

$$Y(k) = \frac{1}{j}F_{\text{op}}(k) = \frac{1}{j}B(k) = \frac{1-b^N}{1-bW_N^k}$$

由方法一知

$$x(n) = \text{IDFT}[X(k)] = a^NR_N(n)$$

$$y(n) = \text{IDFT}[Y(k)] = b^NR_N(n)$$

13. 已知序列 $x(n)=a^nu(n)$，$0<a<1$，对 $x(n)$的 Z 变换 $X(z)$在单位圆上等间隔采样 $N$ 点，采样序列为

$$X(k) = X(z)\big|_{z=e^{j2\pi k/N}} \quad k = 0, 1, \cdots, N-1$$

求有限长序列 $\text{IDFT}[X(k)]_N$。

解：我们知道，$X(e^{j\omega})=X(z)\big|_{z=e^{j\omega}}$，是以 $2\pi$ 为周期的周期函数，所以

$$X((k))_N = X(z)\big|_{z=e^{j2\pi k/N}} = \tilde{X}(k) \tag{1}$$

$\tilde{X}(k)$以 $N$ 为周期，将 $\tilde{X}(k)$看作一周期序列 $\tilde{x}(n)$的 DFS 系数，则

$$\tilde{x}(n) = \frac{1}{N}\sum_{k=0}^{N-1}\tilde{X}(k)e^{j\frac{2\pi}{N}kn} = \frac{1}{N}\sum_{k=0}^{N-1}\tilde{X}(k)W_N^{-kn} \tag{2}$$

由式①知 $\tilde{X}(k)$为

$$\tilde{X}(k) = X(z)\big|_{z=e^{j\frac{2\pi}{N}k}} = W_N^{-k}\sum_{n=-\infty}^{\infty}x(n)z^{-n}\big|_{z=W_N^{-k}} = \sum_{n=-\infty}^{\infty}x(n)W_N^{kn} \tag{3}$$

将式③代入式②得到

$$\tilde{x}(n) = \frac{1}{N}\sum_{k=0}^{N-1}\left[\sum_{m=-\infty}^{\infty}x(m)W_N^{km}\right]W_N^{-kn} = \sum_{m=-\infty}^{\infty}x(m)\frac{1}{N}\sum_{k=0}^{N-1}W_N^{k(m-n)}$$

$$\frac{1}{N}\sum_{k=0}^{N-1}W_N^{k(m-n)} = \begin{cases} 1 & m = n+lN \\ 0 & \text{其它} m \end{cases}$$

<!-- pages: 21-24 -->
所以
$$ \tilde{x}(n) = \sum_{l=-\infty}^{\infty} x(n + lN) $$
由题意知
$$ X(k) = \tilde{X}(k) R_N(k) $$
所以根据有关 $X(k)$ 与 $x_N(n)$ 的周期延拓序列的 DFS 系数的关系有
$$ \begin{aligned} x_N(n) &= \text{IDFT}[X(k)] = \tilde{x}(n) R_N(n) = \sum_{l=-\infty}^{\infty} x(n + lN) R_N(n) \\ &= \sum_{l=-\infty}^{\infty} a^{n+lN} u(n + lN) R_N(n) \end{aligned} $$
由于 $0 \leq n \leq N-1$，所以
$$ u(n + lN) = \begin{cases} 1 & n + lN \geq 0 \text{ 即 } l \geq 0 \\ 0 & l < 0 \end{cases} $$
因此
$$ x_N(n) = a^n \sum_{l=0}^{\infty} a^{lN} R_N(n) = \frac{a^n}{1 - a^N} R_N(n) $$
**说明**：平时解题时，本题推导 $x_N(n) = \text{IDFT}[X(k)]_N = \sum_{l=-\infty}^{\infty} x(n + lN) R_N(n)$ 的过程可省去，直接引用频域采样理论给出的结论（教材中式(3.3.2)和(3.3.3)）即可。
14. 两个有限长序列 $x(n)$ 和 $y(n)$ 的零值区间为
$$ x(n) = 0 \quad n < 0, 8 \leq n $$
$$ y(n) = 0 \quad n < 0, 20 \leq n $$
对每个序列作 20 点 DFT，即
$$ X(k) = \text{DFT}[x(n)] \quad k = 0, 1, \cdots, 19 $$
$$ Y(k) = \text{DFT}[y(n)] \quad k = 0, 1, \cdots, 19 $$
如果
$$ F(k) = X(k)Y(k) \quad k = 0, 1, \cdots, 19 $$
$$ f(n) = \text{IDFT}[F(k)] \quad k = 0, 1, \cdots, 19 $$
试问在哪些点上 $f(n)$ 与 $x(n) * y(n)$ 值相等，为什么？
**解**：如前所述，记 $f_l(n) = x(n) * y(n)$，而 $f(n) = \text{IDFT}[F(k)] = x(n) \circledast_{20} y(n)$。$f_l(n)$ 长度为 27，$f(n)$ 长度为 20。由教材中式(3.4.3)知道 $f(n)$ 与 $f_l(n)$ 的关系为
$$ f(n) = \sum_{m=-\infty}^{\infty} f_l(n + 20m) R_{20}(n) $$
只有在如上周期延拓序列中无混叠的点上，才满足 $f(n) = f_l(n)$，所以
$$ f(n) = f_l(n) = x(n) * y(n) \quad 7 \leq n \leq 19 $$
15. 已知实序列 $x(n)$ 的 8 点 DFT 的前 5 个值为 $0.25$，$0.125 - \text{j}0.3018$，$0$，$0.125 - \text{j}0.0518$，$0$。
(1) 求 $X(k)$ 的其余 3 点的值；
(2) $x_1(n) = \sum_{m=-\infty}^{+\infty} x(n + 5 + 8m) R_8(n)$，求 $X_1(k) = \text{DFT}[x_1(n)]_8$；
(3) $x_2(n) = x(n) \text{e}^{\text{j}\pi n/4}$，求 $x_2(k) = \text{DFT}[x_2(n)]_8$。
**解**：(1) 因为 $x(n)$ 是实序列，由第 7 题证明结果有 $X(k) = X^*(N-k)$，即 $X(N-k) = X^*(k)$，所以，$X(k)$ 的其余 3 点值为
$$ \{X(5), X(6), X(7)\} = \{0.125 + \text{j}0.0518, 0, 0.125 + \text{j}0.3018\} $$
(2) 根据 DFT 的时域循环移位性质，
$$ X_1(k) = \text{DFT}[x_1(n)]_8 = W_8^{-5k} X(k) $$
(3)
$$ \begin{aligned} X_2(k) &= \text{DFT}[x_2(n)]_8 = \sum_{n=0}^{N-1} x_2(n) W_8^{kn} = \sum_{n=0}^{N-1} x(n) \text{e}^{\text{j}\pi n/4} \text{e}^{-\text{j}\pi nk/4} \\ &= \sum_{n=0}^{N-1} x(n) W_8^{(k-1)n} = \sum_{n=0}^{N-1} x(n) W_8^{((k-1))_8 n} = X(((k-1))_8) R_8(k) \end{aligned} $$
16. $x(n)$、$x_1(n)$ 和 $x_2(n)$ 分别如题 16 图(a)、(b)和(c)所示，已知 $X(k) = \text{DFT}[x(n)]_8$。求
$$ X_1(k) = \text{DFT}[x_1(n)]_8 \quad \text{和} \quad X_2(k) = \text{DFT}[x_2(n)]_8 $$
[注：用 $X(k)$ 表示 $X_1(k)$ 和 $X_2(k)$。]


**题 16 图**

<!-- pages: 80-83 -->
则

$$ Y_m(k) = \text{DFT}[y_m(n)]_L = \frac{1}{L} H(k) \circled{L} X(k) $$

$$ = \frac{1}{L} \sum_{j=0}^{L-1} H(j) X((j-k))_L R_L(k) $$

其中， $L \geq \max[N, M]$。
根据 DFT 的惟一性，只要证明 $y_m(n) = \text{IDFT}[Y_m(k)] = h(n) x(n)$，就证明了 DFT 的频域循环卷积定理。

$$ = \frac{1}{L} \sum_{k=0}^{N-1} \left[ \frac{1}{L} \sum_{j=0}^{L-1} H(j) X((k-j))_L \right] W_N^{-kn} $$

$$ = \frac{1}{L} \sum_{j=0}^{L-1} H(j) W_N^{-jn} \frac{1}{L} \sum_{k=0}^{N-1} X((k-j))_L W_N^{-(k-j)n} $$

$$ \xrightarrow{\text{令} m=k-j} = h(n) \frac{1}{L} \sum_{m=-j}^{N-1-j} X((m))_L W_N^{-mn} = h(n) \frac{1}{L} \sum_{m=0}^{N-1} X((m))_L W_N^{-mn} $$

$$ = h(n) \frac{1}{L} \sum_{m=0}^{N-1} X(m) W_N^{-mn} = h(n) x(n) $$

23*．已知序列 $x(n)=\{\underline{1}, 2, 3, 3, 2, 1\}$。
(1) 求出 $x(n)$ 的傅里叶变换 $X(e^{j\omega})$，画出幅频特性和相频特性曲线(提示：用 1024 点 FFT 近似 $X(e^{j\omega})$)；
(2) 计算 $x(n)$ 的 $N(N\geq6)$ 点离散傅里叶变换 $X(k)$，画出幅频特性和相频特性曲线；
(3) 将 $X(e^{j\omega})$ 和 $X(k)$ 的幅频特性和相频特性曲线分别画在同一幅图中，验证 $X(k)$ 是 $X(e^{j\omega})$ 的等间隔采样，采样间隔为 $2\pi/N$；
(4) 计算 $X(k)$ 的 $N$ 点 IDFT，验证 DFT 和 IDFT 的惟一性。
解：该题求解程序为 ex323.m，程序运行结果如题 23* 解图所示。第(1)小题用 1024 点 DFT 近似 $x(n)$ 的傅里叶变换；第(2)小题用 32 点 DFT。题 23* 解图(e)和(f)验证了 $X(k)$ 是 $X(e^{j\omega})$ 的等间隔采样，采样间隔为 $2\pi/N$。题 23* 解图(g)验证了 IDFT 的惟一性。

24*．给定两个序列： $x_1(n)=\{\underline{2}, 1, 1, 2\}$，$x_2(n)=\{\underline{1}, -1, -1, 1\}$。
(1) 直接在时域计算 $x_1(n)$ 与 $x_2(n)$ 的卷积；
(2) 用 DFT 计算 $x_1(n)$ 与 $x_2(n)$ 的卷积，总结出 DFT 的时域卷积定理。
解：设 $x_1(n)$ 和 $x_2(n)$ 的长度分别为 $M_1$ 和 $M_2$，

$$ X_1(k) = \text{DFT}[x_1(n)]_N, X_2(k) = \text{DFT}[x_2(n)]_N $$
$$ Y_c(k) = X_1(k) X_2(k), y_c(n) = \text{IDFT}[Y_c(k)]_N $$

所谓 DFT 的时域卷积定理，就是当 $N \geq M_1 + M_2 - 1$ 时，$y_c(n) = x_1(n) * x_2(n)$。本题中，$M_1=M_2=4$，所以，程序中取 $N=7$。本题的求解程序 ex324.m 如下：

```matlab
% 程序 ex324.m
x1n=[2 1 1 2]; x2n=[1 -1 -1 1];
%时域直接计算卷积 yn：
yn=conv(x1n, x2n)
```

![{{FIGURE:81}}](#)
**Figure 3.25:** 题 23* 解图

%用 DFT 计算卷积 ycn：
M1=length(x1n); M2=length(x2n); N=M1+M2-1;
X1k=fft(x1n, N);          %计算 x1n 的 N 点 DFT
X2k=fft(x2n, N);          %计算 x2n 的 N 点 DFT
Yck=X1k.*X2k; ycn=ifft(Yck, N)

程序运行结果：
直接在时域计算 $x_1(n)$ 与 $x_2(n)$ 的卷积 yn 和用 DFT 计算 $x_1(n)$ 与 $x_2(n)$ 的卷积 ycn 如下：
yn=[2    -1    -2     2    -2    -1     2]
ycn=[2.0000    -1.0000    -2.0000     2.0000    -2.0000    -1.0000     2.0000]

25*．已知序列 $h(n)=R_6(n)$，$x(n)=nR_8(n)$。
(1) 计算 $y_c(n)=h(n) \circled{8} x(n)$；
(2) 计算 $y_c(n)=h(n) \circled{16} x(n)$ 和 $y(n)=h(n) * x(n)$；
(3) 画出 $h(n)$、$x(n)$、$y_c(n)$ 和 $y(n)$ 的波形图，观察总结循环卷积与线性卷积的关系。
解：本题的求解程序为 ex325.m。程序运行结果如题 25* 解图所示。由图可见，循环卷积为线性卷积的周期延拓序列的主值序列；当循环卷积区间长度大于等于线性卷积序列长度时，二者相等，见图(b)和图(c)。

![{{FIGURE:82}}](#)
**Figure 3.26:** 题 25* 解图

程序 ex325.m 如下：
```matlab
%程序 ex325.m
hn=[1 1 1 1]; xn=[0 1 2 3];
%用 DFT 计算 4点循环卷积 yc4n：
H4k=fft(hn, 4);          %计算 h(n)的 4 点 DFT
X4k=fft(xn, 4);          %计算 x(n)的 4 点 DFT
Yc4k=H4k.*X4k; yc4n=ifft(Yc4k, 4);
%用 DFT 计算 8点循环卷积 yc8n：
H8k=fft(hn, 8);          %计算 h(n)的 8 点 DFT
X8k=fft(xn, 8);          %计算 x(n)的 8 点 DFT
Yc8k=H8k.*X8k; yc8n=ifft(Yc8k, 8);
yn=conv(hn, xn);         %时域计算线性卷积 yn：
```

26*．验证频域采样定理。设时域离散信号为

其中 $a=0.9$，$L=10$。

(1) 计算并绘制信号 $x(n)$ 的波形。
(2) 证明： $X(e^{j\omega}) = \text{FT}[x(n)] = x(0) + 2 \sum_{n=1}^{L} x(n) \cos(\omega n)$。
(3) 按照 $N=30$ 对 $X(e^{j\omega})$ 采样得到 $C_k = X(e^{j\omega})\big|_{\omega=\frac{2\pi}{N}k}$， $k=0,1,2,\cdots, N-1$。
(4) 计算并图示周期序列 $\tilde{x}(n) = \frac{1}{N} \sum_{k=0}^{N-1} C_k e^{j(2\pi/N)kn}$，试根据频域采样定理解释序列 $\tilde{x}(n)$ 与 $x(n)$ 的关系。
(5) 计算并图示周期序列 $\tilde{y}(n) = \sum_{m=-\infty}^{\infty} x(n+mN)$，比较 $\tilde{x}(n)$ 与 $\tilde{y}(n)$，验证(4)中的解释。
(6) 对 $N=15$，重复(3)～(5)。
解：求解本题(1)、(3)、(4)、(5)、(6)的程序为 ex326.m。下面证明(2)。

$$ X(e^{j\omega}) = \text{FT}[x(n)] = \sum_{n=-L}^{L} a^{|n|} e^{-j\omega n} = a^0 + \sum_{n=1}^{L} (a^n e^{-j\omega n} + a^n e^{j\omega n}) $$
$$ = x(0) + \sum_{n=1}^{L} a^n (e^{-j\omega n} + e^{j\omega n}) = x(0) + 2 \sum_{n=1}^{L} x(n) \cos(\omega n) $$

$N=30$ 和 $N=15$ 时，对频域采样 $C_k$ 进行离散傅里叶级数展开得到的序列分别如题 26* 解图(b)和(c)所示。由图显而易见，如果 $C_k$ 表示对 $X(e^{j\omega})$ 在 $[0, 2\pi]$ 上的 $N$ 点等间隔采样，则 $x_N(n)=\text{IDFT}[C_k]_N = \sum_{m=-\infty}^{\infty} x(n+mN) R_N(n) = \tilde{x}(n) R_N(n)$，简言述之：$x_N(n)$ 是 $x(n)$ 以 $N$ 为周期的周期延拓序列 $\tilde{x}(n)$ 的主值序列。
程序 ex326.m 如下：程序中直接对(2)中证明得到的结果采样得到 $C_k$。

```matlab
%程序 ex326.m
% 频域采样理论验证
clear all; close all;
a=0.9; L=10; n=-L:L;
%============ N=30 =============
N=30;
xn=a.^abs(n); %计算产生序列 x(n)
subplot(3,2,1); stem(n, xn, '.'); axis([-15, 15, 0, 1.2]); %(1)显示序列 x(n)
title('(a)x(n)的波形'); xlabel('n'); ylabel('x(n)'); box on
% 对 X(jw)采样 30 点：
for k=0: N-1,
    Ck(k+1)=1;
    for m=1: L,
        Ck(k+1)=Ck(k+1)+2*xn(m+L+1)*cos(2*pi*k*m/N); % (3)计算 30 点采样 Ck
    end
end
x30n=ifft(Ck, N); % (4)30 点 IDFT 得到所要求的周期序列的主值序列
%以下为绘图部分
n=0: N-1;

<!-- pages: 29-32 -->

```matlab
subplot(3, 2, 2); stem(n, x30n, '.'); axis([0, 30, 0, 1.2]); box on
title('(b)N=30 由 Ck 展开的的周期序列的主值序列'); xlabel('n'); ylabel('x30(n)')
%============= N=15 ========================
N=15;
% 对 X(jw)采样 15 点：
for k=0: N-1,
    Ck(k+1)=1;
    for m=1: L,
        Ck(k+1)=Ck(k+1)+2*xn(m+L+1)*cos(2*pi*k*m/N); % (3)计算 30 点采样 Ck
    end
end
x15n=ifft(Ck, N); % (4)15 点 IDFT 得到所要求的周期序列的主值序列
%以下为绘图部分
n=0: N-1;
subplot(3, 2, 3); stem(n, x15n, '.'); axis([0, 30, 0, 1.2]); box on
title('(c)N=15 由 Ck 展开的的周期序列的主值序列'); xlabel('n'); ylabel('x15(n)')
```
程序运行结果如题 26* 解图所示。


**题 26* 解图**
(a) x(n)的波形
(b) N=30由Ck展开的周期序列的主值序列
(c) N=15由Ck展开的周期序列的主值序列

27*．选择合适的变换区间长度 $N$，用 DFT 对下列信号进行谱分析，画出幅频特性和相频特性曲线。
(1) $x_1(n) = 2 \cos(0.2\pi n)$
(2) $x_2(n) = \sin(0.45\pi n)\sin(0.55\pi n)$
(3) $x_3(n) = 2^{-|n|} R_{21}(n+10)$
解：求解本题的程序为 ex327.m，程序运行结果如题 27* 解图所示。本题选择变换区间长度 $N$ 的方法如下：


**题 27* 解图**
(a) x1(n)的幅频特性图
(b) x1(n)的相频特性图
(c) x2(n)的幅频特性图
(d) x2(n)的相频特性图
(e) x3(n)的32点周期延拓序列
(f) DFT[x3(n)]$_{32}$ 的幅频特性图
(g) DFT[x3(n)]$_{32}$ 的相位
(h) x3(n)的64点周期延拓序列
(i) DFT[x3(n)]$_{64}$ 的幅频特性图
(j) DFT[x3(n)]$_{32}$ 的相位

对 $x_1(n)$，其周期为 10，所以取 $N_1=10$；因为 $x_2(n) = \sin(0.45\pi n)\sin(0.55\pi n) = 0.5[\cos(0.1\pi n) - \cos(\pi n)]$，其周期为 20，所以取 $N_2=20$；$x_3(n)$ 不是因果序列，所以先构造其周期延拓序列（延拓周期为 $N_3$），再对其主值序列进行 $N_3$ 点 DFT。
$x_1(n)$ 和 $x_2(n)$ 是周期序列，所以截取 1 个周期，用 DFT 进行谱分析，得出精确的离散谱。$x_3(n)$ 是非因果、非周期序列，通过试验选取合适的 DFT 变换区间长度 $N_3$ 进行谱分析。
$x_1(n)$ 的频谱如题 27* 解图 (a) 和 (b) 所示，$x_2(n)$ 的频谱如题 27* 解图 (c) 和 (d) 所示。用 32 点 DFT 对 $x_3(n)$ 的谱分析结果见题 27* 解图 (e)、(f) 和 (g)，用 64 点 DFT 对 $x_3(n)$ 的谱分析结果见题 27* 解图 (h)、(i) 和 (j)。比较可知，仅用 32 点分析结果就可以了。
请注意，$x_3(n)$ 的相频特性曲线的幅度很小，这是计算误差引起的。实质上，$x_3(n)$ 是一个实偶对称序列，所以其理论频谱应当是一个实偶函数，其相位应当是零。
程序 ex327.m 如下：

```matlab
%程序 ex327.m
% 用 DFT 对序列谱分析
n1=0:9; n2=0:50; n3=-10:10;
N1=10; N2=20; N3a=32; N3b=64;
x1n=2 * cos(0.2 * pi * n1);                    %计算序列 x1n
x2n=2 * sin(0.45 * pi * n2).* sin(0.55 * pi * n2); %计算序列 x2n
x3n=0.5. ^ abs(n3);                            %计算序列 x3n
x3anp=zeros(1, N3a);                           %构造 x3n 的周期延拓序列，周期为 N3a
for m=1:10,
    x3anp(m)=x3n(m+10); x3anp(N3a+1-m)=x3n(11-m);
end
x3bnp=zeros(1, N3b);                           %构造 x3n 的周期延拓序列，周期为 N3b
for m=1:10,
    x3bnp(m)=x3n(m+10); x3bnp(N3b+1-m)=x3n(11-m);
end
X1k=fft(x1n, N1);                              %计算序列 x1n 的 N1 点 DFT
X2k=fft(x2n, N2);                              %计算序列 x2n 的 N2 点 DFT
X3ak=fft(x3anp, N3a);                          %计算序列 x3n 的 N3a 点 DFT
X3bk=fft(x3bnp, N3b);                          %计算序列 x3n 的 N3b 点 DFT
%以下为绘图部分(省略)
```

## 3.6 教材第 4 章习题与上机题解答

快速傅里叶变换 (FFT) 是 DFT 的快速算法，没有新的物理概念。FFT 的基本思想和方法教材中都有详细的叙述，所以只给出教材第 4 章的习题与上机题解答。

1. 如果某通用单片计算机的速度为平均每次复数乘需要 4 $\mu\text{s}$，每次复数加需要 1 $\mu\text{s}$，用来计算 $N=1024$ 点 DFT，问直接计算需要多少时间。用 FFT 计算呢？照这样计算，用 FFT 进行快速卷积对信号进行处理时，估计可实现实时处理的信号最高频率。
解：当 $N=1024=2^{10}$ 时，直接计算 DFT 的复数乘法运算次数为
$$N^2 = 1024 \times 1024 = 1,048,576 \text{ 次}$$
复数加法运算次数为
$$N(N-1) = 1024 \times 1023 = 1,047,552 \text{ 次}$$
直接计算所用计算时间 $T_D$ 为
$$T_D = 4 \times 10^{-6} \times 1024^2 + 1,047,552 \times 10^{-6} = 5.241856 \text{ s}$$

用 FFT 计算 1024 点 DFT 所需计算时间 $T_F$ 为
$$T_F = 4 \times 10^{-6} \times \frac{N}{2} \text{lb} N + N \text{lb} N \times 10^{-6} = 4 \times 10^{-6} \times \frac{1024}{2} \times 10 + 1024 \times 10 \times 10^{-6} = 30.72 \text{ ms}$$
快速卷积时，需要计算一次 $N$ 点 FFT（考虑到 $H(k)=\text{DFT}[h(n)]$ 已计算好存入内存）、$N$ 次频域复数乘法和一次 $N$ 点 IFFT。所以，计算 1024 点快速卷积的计算时间 $T_c$ 约为
$$T_c = 2T_F + 1024 \text{ 次复数乘计算时间} = 71,680 \mu\text{s} + 4 \times 1024 \mu\text{s} = 65,536 \mu\text{s}$$
所以，每秒钟处理的采样点数（即采样速率）
$$F_s < \frac{1024}{65536 \times 10^{-6}} = 15,625 \text{ 次/秒}$$
由采样定理知，可实时处理的信号最高频率为
$$f_{\text{max}} < \frac{F_s}{2} = \frac{15,625}{2} = 7.8125 \text{ kHz}$$
应当说明，实际实现时，$f_{\text{max}}$ 还要小一些。这是由于实际中要求采样频率高于奈奎斯特速率，而且在采用重叠相加法时，重叠部分要计算两次。重叠部分长度与 $h(n)$ 长度有关，而且还有存取数据和指令周期等消耗的时间。

2. 如果将通用单片机换成数字信号处理专用单片机 TMS320 系列，计算复数乘和复数加各需要 10 ns。请重复做上题。
解：与第 1 题同理。
直接计算 1024 点 DFT 所需计算时间 $T_D$ 为
$$T_D = 10 \times 10^{-9} \times 1024^2 + 10 \times 10^{-9} \times 1,047,552 = 20.96128 \text{ ms}$$
用 FFT 计算 1024 点 DFT 所需计算时间 $T_F$ 为
$$T_F = 10 \times 10^{-9} \times \frac{N}{2} \text{lb} N + 10 \times 10^{-9} \times N \text{lb} N = 10^{-8} \times \frac{1024}{2} \times 10 + 10^{-8} \times 1024 \times 10 = 0.1536 \text{ ms}$$
快速卷积计算时间 $T_c$ 约为
$$T_c = 2T_F + 1024 \text{ 次复数乘计算时间} = 2 \times 0.1536 \times 10^{-3} + 10 \times 10^{-9} \times 1024 = 0.31744 \text{ ms}$$
可实时处理的信号最高频率 $f_{\text{max}}$ 为
$$f_{\text{max}} \leq \frac{1}{2} F_s = \frac{1}{2} \cdot \frac{1024}{T_c} = \frac{1}{2} \cdot 3.2258 \text{ MHz} = 1.6129 \text{ MHz}$$
由此可见，用 DSP 专用单片机可大大提高信号处理速度。所以，DSP 在数字信号处理领域得到广泛应用。机器周期小于 1 ns 的 DSP 产品已上市，其处理速度更高。

<!-- pages: 33-35 -->

3. 已知 $X(k)$ 和 $Y(k)$ 是两个 $N$ 点实序列 $x(n)$ 和 $y(n)$ 的 DFT，希望从 $X(k)$ 和 $Y(k)$ 求 $x(n)$ 和 $y(n)$，为提高运算效率，试设计用一次 $N$ 点 IFFT 来完成的算法。
**解：** 因为 $x(n)$ 和 $y(n)$ 均为实序列，所以，$X(k)$ 和 $Y(n)$ 为共轭对称序列，$jY(k)$ 为共轭反对称序列。可令 $X(k)$ 和 $mathrm{j}Y(k)$ 分别作为复序列 $F(k)$ 的共轭对称分量和共轭反对称分量，即
$$
F(k) = X(k) + \mathrm{j}Y(k) = F_{\mathrm{ep}}(k) + F_{\mathrm{op}}(k)
$$
计算一次 $N$ 点 IFFT 得到
$$
f(n) = \mathrm{IFFT}[F(k)] = \mathrm{Re}[f(n)] + \mathrm{j} \mathrm{Im}[f(n)]
$$
由 DFT 的共轭对称性可知
$$
$$
\begin{aligned}
$$
\mathrm{Re}[f(n)] &= \mathrm{IDFT}[F_{\mathrm{ep}}(k)] = \mathrm{IDFT}[X(k)] = x(n) \\
\mathrm{j} \mathrm{Im}[f(n)] &= \mathrm{IDFT}[F_{\mathrm{op}}(k)] = \mathrm{IDFT}[\mathrm{j}Y(k)] = \mathrm{j}y(n)
$$
\end{aligned}
$$
$$
故
$$
$$
\begin{aligned}
$$
x(n) &= \frac{1}{2}[f(n) + f^*(n)] \\
y(n) &= \frac{1}{2\mathrm{j}}[f(n) - f^*(n)]
$$
\end{aligned}
$$

$$
4. 设 $x(n)$ 是长度为 $2N$ 的有限长实序列，$X(k)$ 为 $x(n)$ 的 $2N$ 点 DFT。
(1) 试设计用一次 $N$ 点 FFT 完成计算 $X(k)$ 的高效算法。
(2) 若已知 $X(k)$，试设计用一次 $N$ 点 IFFT 实现求 $X(k)$ 的 $2N$ 点 IDFT 运算。
**解：** 本题的解题思路就是 DIT-FFT 思想。
(1) 在时域分别抽取偶数和奇数点 $x(n)$，得到两个 $N$ 点实序列 $x_1(n)$ 和 $x_2(n)$：
$$
$$
\begin{aligned}
$$
x_1(n) &= x(2n) \quad & n &= 0, 1, \cdots, N-1 \\
x_2(n) &= x(2n+1) \quad & n &= 0, 1, \cdots, N-1
$$
\end{aligned}
$$
$$
根据 DIT-FFT 的思想，只要求得 $x_1(n)$ 和 $x_2(n)$ 的 $N$ 点 DFT，再经过简单的一级蝶形运算就可得到 $x(n)$ 的 $2N$ 点 DFT。因为 $x_1(n)$ 和 $x_2(n)$ 均为实序列，所以根据 DFT 的共轭对称性，可用一次 $N$ 点 FFT 求得 $X_1(k)$ 和 $X_2(k)$。具体方法如下：
令
$$
$$
\begin{aligned}
$$
y(n) &= x_1(n) + \mathrm{j}x_2(n) \\
Y(k) &= \mathrm{DFT}[y(n)] \quad & k &= 0, 1, \cdots, N-1
$$
\end{aligned}
$$
$$
则
$$
$$
\begin{aligned}
$$
X_1(k) &= \mathrm{DFT}[x_1(n)] = Y_{\mathrm{ep}}(k) = \frac{1}{2}[Y(k) + Y^*(N-k)] \\
\mathrm{j}X_2(k) &= \mathrm{DFT}[\mathrm{j}x_2(n)] = Y_{\mathrm{op}}(k) = \frac{1}{2}[Y(k) - Y^*(N-k)]
$$
\end{aligned}
$$
$$
$2N$ 点 $\mathrm{DFT}[x(n)] = X(k)$ 可由 $X_1(k)$ 和 $X_2(k)$ 得到
$$
\left.
$$
\begin{aligned}
X(k) &= X_1(k) + W_{2N}^{k} X_2(k) \\
X(k+N) &= X_1(k) - W_{2N}^{k} X_2(k)
\end{aligned}
$$
\right\} \quad k = 0, 1, \cdots, N-1
$$
$$
这样，通过一次 $N$ 点 IFFT 计算就完成了计算 $2N$ 点 DFT。当然还要进行由 $Y(k)$ 求 $X_1(k)$、$X_2(k)$ 和 $X(k)$ 的运算(运算量相对很少)。
(2) 与(1)相同，设
$$
$$
\begin{aligned}
$$
x_1(n) &= x(2n) \quad & n &= 0, 1, \cdots, N-1 \\
x_2(n) &= x(2n+1) \quad & n &= 0, 1, \cdots, N-1 \\
X_1(k) &= \mathrm{DFT}[x_1(n)] \quad & k &= 0, 1, \cdots, N-1 \\
X_2(k) &= \mathrm{DFT}[x_2(n)] \quad & k &= 0, 1, \cdots, N-1
$$
\end{aligned}
$$
$$
则应满足关系式
$$
\left.
$$
\begin{aligned}
X(k) &= X_1(k) + W_{2N}^{k} X_2(k) \\
X(k+N) &= X_1(k) - W_{2N}^{k} X_2(k)
\end{aligned}
$$
\right\} \quad k = 0, 1, \cdots, N-1
$$
$$
由上式可解出
$$
\left.
$$
\begin{aligned}
$$
X_1(k) &= \frac{1}{2}[X(k) + X(k+N)] \\
X_2(k) &= \frac{1}{2}[X(k) - X(k+N)] W_{2N}^{-k}
$$
\end{aligned}
$$
\right\} \quad k = 0, 1, 2, \cdots, N-1
$$
$$
由以上分析可得出运算过程如下：
① 由 $X(k)$ 计算出 $X_1(k)$ 和 $X_2(k)$：
$$
$$
\begin{aligned}
$$
X_1(k) &= \frac{1}{2}[X(k) + X(k+N)] \\
X_2(k) &= \frac{1}{2}[X(k) + X(k+N)] W_{2N}^{-k}
$$
\end{aligned}
$$
$$
② 由 $X_1(k)$ 和 $X_2(k)$ 构成 $N$ 点频域序列 $Y(k)$：
$$
Y(k) = X_1(k) + \mathrm{j}X_2(k) = Y_{\mathrm{ep}}(k) + Y_{\mathrm{op}}(k)
$$
其中，$Y_{\mathrm{ep}}(k) = X_1(k)$，$Y_{\mathrm{op}}(k) = \mathrm{j}X_2(k)$，进行 $N$ 点 IFFT，得到
$$
y(n) = \mathrm{IFFT}[Y(k)] = \mathrm{Re}[y(n)] + \mathrm{j} \mathrm{Im}[y(n)] \quad n = 0, 1, \cdots, N-1
$$
由 DFT 的共轭对称性知
$$
$$
\begin{aligned}
$$
\mathrm{Re}[y(n)] &= \frac{1}{2}[y(n) + y^*(n)] = \mathrm{DFT}[Y_{\mathrm{ep}}(k)] = x_1(n) \\
\mathrm{j} \mathrm{Im}[y(n)] &= \frac{1}{2}[y(n) + y^*(n)] = \mathrm{DFT}[Y_{\mathrm{op}}(k)] = \mathrm{j}x_2(n)
$$
\end{aligned}
$$
$$
③ 由 $x_1(n)$ 和 $x_2(n)$ 合成 $x(n)$：
$$
$$
x(n) =
\begin{cases}
$$
x_1\left(\frac{n}{2}\right) & n = \text{偶数} \\
x_2\left(\frac{n-1}{2}\right) & n = \text{奇数}
$$
\end{cases}
$$
, \quad 0 \leqslant n \leqslant 2N-1
$$
$$
在编程序实现时，只要将存放 $x_1(n)$ 和 $x_2(n)$ 的两个数组的元素分别依次放入存放 $x(n)$ 的数组的偶数和奇数数组元素中即可。

5. 分别画出 16 点基 2DIT-FFT 和 DIF-FFT 运算流图，并计算其复数乘次数，如果考虑三类碟形的乘法计算，试计算复乘次数。
**解：** 本题比较简单，仿照教材中的 8 点基 2DIT-FFT 和 DIF-FFT 运算流图很容易画出 16 点基 2DIT-FFT 和 DIF-FFT 运算流图。但画图占篇幅较大，这里省略本题解答，请读者自己完成。

6*. 按照下面的 IDFT 算法编写 MATLAB 语言 IFFT 程序，其中的 FFT 部分不用写出清单，可调用 fft 函数。并分别对单位脉冲序列、矩形序列、三角序列和正弦序列进行 FFT 和 IFFT 变换，验证所编程序。
$$
x(n) = \mathrm{IDFT}[X(k)] = \frac{1}{N}[\mathrm{DFT}[X^*(k)]]^*
$$
**解：** 为了使用灵活方便，将本题所给算法公式作为函数编写 `ifft46.m` 如下：
```matlab
% 函数 ifft46.m
% 按照所给算法公式计算 IFET
function xn=ifft46(Xk, N)
Xk=conj(Xk);               % 对 Xk 取复共轭
xn=conj(fft(Xk, N))/N;     % 按照所给算法公式计算 IFFT
```
分别对单位脉冲序列、长度为 8 的矩形序列和三角序列进行 FFT，并调用函数 `ifft46` 计算 IFFT 变换，验证函数 `ifft46` 的程序 `ex406.m` 如下：
```matlab
% 程序 ex406.m
% 调用 fft 函数计算 IDFT
x1n=1;           % 输入单位脉冲序列 x1n
x2n=[1 1 1 1 1 1 1 1];   % 输入矩形序列向量 x2n
x3n=[1 2 3 4 4 3 2 1];   % 输入三角序列序列向量 x3n
N=8;
X1k=fft(x1n, N);         % 计算 x1n 的 N 点 DFT
X2k=fft(x2n, N);         % 计算 x2n 的 N 点 DFT
X3k=fft(x3n, N);         % 计算 x3n 的 N 点 DFT
x1n=ifft46(X1k, N)       % 调用 ifft46 函数计算 X1k 的 IDFT
x2n=ifft46(X2k, N)       % 调用 ifft46 函数计算 X2k 的 IDFT
x3n=ifft46(X3k, N)       % 调用 ifft46 函数计算 X3k 的 IDFT
```
运行程序输出时域序列如下所示，正是原序列 `x1n`、`x2n` 和 `x3n`。
```
x1n = 1    0    0    0    0    0    0    0
x2n = 1    1    1    1    1    1    1    1
x3n = 1    2    3    4    4    3    2    1