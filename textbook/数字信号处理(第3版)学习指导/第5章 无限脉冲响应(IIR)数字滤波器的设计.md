---
title: "第5章 无限脉冲响应(IIR)数字滤波器的设计"
source: "第5章 无限脉冲响应(IIR)数字滤波器的设计.pdf"
pages: 32
doc_type: book
language: zh
structure_source: llm_scan
parsed_at: 2026-05-28T07:05:19Z
---

<!-- pages: 115-118 -->

# 第5章 无限脉冲响应(IIR)数字滤波器的设计

本章内容与教材第6章内容相对应。
目前，滤波器设计软件种类众多，功能齐全，且使用非常方便。只要滤波器设计的概念清楚，以正确的指标参数调用相应的滤波器设计程序或工具箱函数，便可得到正确的设计结果。因此，熟悉滤波器的基本概念及滤波器的基本设计方法显得尤为重要。本章内容主要围绕以下学习重点来安排。
（1）建立数字滤波器(DF)设计的正确概念，掌握滤波器的设计方法。
（2）结合例题和习题的求解过程介绍采用 MATLAB 信号处理工具箱函数设计数字滤波器的现代方法，使读者了解现在工程实际中设计滤波器是非常简单易行的，绝不像手算做习题那样困难。
（3）熟悉采样数字滤波系统的概念及其指标参数换算关系，这是用 DF 处理模拟信号的基本问题。

## 5.1 学习要点

### 5.1.1 IIR数字滤波器设计的基本概念及基本设计方法

**1. 滤波器设计指标参数定义及其描述**

滤波器设计指标参数定义及其描述在教材中有详细的介绍，下面仅给出低通滤波器幅频特性函数和损耗函数描述的滤波器指标参数的示意图，如图 5.1.1 所示，并给出二者的换算关系。


**图5.1.1** (a) 幅频特性；(b) 损耗函数

滤波器的指标常常在频域给出。数字滤波器的频响特性函数 $H(e^{j\omega})$ 一般为复函数，所以通常表示为
$$H(e^{j\omega}) = | H(e^{j\omega}) | e^{j\theta(\omega)}$$
其中，$|H(e^{j\omega})|$ 称为幅频特性函数，$\theta(\omega)$ 称为相频特性函数。常用的典型滤波器 $|H(e^{j\omega})|$ 是归一化的，即 $|H(e^{j\omega})|_{\text{max}}=1$，下面的讨论一般就是针对归一化情况的。对 IIR 数字滤波器，通常用幅频响应函数 $|H(e^{j\omega})|$ 来描述设计指标，而对线性相位特性的滤波器，一般用 FIR 数字滤波器设计实现。
应当注意，$H(e^{j\omega})$ 是以 $2\pi$ 为周期的，这是数字滤波器与模拟滤波器的最大区别。所以，在后面的叙述中，只给出主值区 $[-\pi, \pi]$ 区间上的设计指标描述。
图 5.1.1 中，$\delta_1$ 和 $\delta_2$ 分别称为通带波纹幅度和阻带波纹幅度，$\omega_{\text{p}}$ 为通带边界频率，$\alpha_{\text{p}}$ 为通带最大衰减(dB)，$\omega_{\text{s}}$ 为阻带边界频率，$\alpha_{\text{s}}$ 为阻带最小衰减(dB)。一般要求：
当 $0 \leqslant |\omega| \leqslant \omega_{\text{p}}$ 时，
$$ -20 \lg | H(e^{j\omega}) | \leqslant \alpha_{\text{p}} $$
当 $\omega_{\text{s}} \leqslant |\omega| \leqslant \pi$ 时，
$$ \alpha_{\text{s}} \leqslant -20 \lg | H(e^{j\omega}) | $$
$$ \alpha_{\text{p}} = -20 \lg \frac{1-\delta_1}{1} = 20 \lg \frac{1}{1-\delta_1} $$
$$ \alpha_{\text{s}} = -20 \lg \delta_2 $$
当 $\alpha_{\text{p}} = 3\text{ dB}$ 时，记 $\omega_{\text{p}}$ 为 $\omega_{\text{c}}$，称 $\omega_{\text{c}}$ 为 3 dB 截止频率。$\omega_{\text{c}}$ 是滤波器设计的重要参数之一。
因为 $|H(e^{j\omega_{\text{c}}})|^2 = 1/2$，所以 $\omega_{\text{c}}$ 又称为滤波器的半功率点。因此，设计数字滤波器时，应根据指标参数及对滤波特性的要求，选择合适的滤波器类型(巴特沃斯、切比雪夫、椭圆滤波器等)和设计方法(脉冲响应不变法、双线性变换法、直接法等)进行设计。IIR 数字滤波器的设计既可以从模拟滤波器的设计入手进行，也可以直接根据数字滤波器指标参数，直接调用滤波器设计子程序或函数进行。

**2. 采样数字滤波器的概念及其指标参数换算**

由于数字信号处理的诸多优点，在信号处理工程实际中，常常希望采用数字滤波器实现对模拟信号的滤波处理。所谓采样数字滤波器，就是实现这种处理的系统，其组成如图 5.1.2 所示。图中，设采样频率 $F_{\text{s}} \geqslant 2f_{\text{c}}(T=1/F_{\text{s}}$ 为采样间隔)，$f_{\text{c}}$ 为模拟信号 $x_{\text{a}}(t)$ 的最高频率。设 $G(j\Omega)$ 为理想低通滤波器，则截止频率为折叠频率即 $\pi/T$ (当 $G(j\Omega)$ 不是理想低通时，以下结论要进行修正)。
采样数字滤波系统的设计指标一般由采样数字滤波系统的等效模拟滤波器 $H_{\text{a}}(j\Omega)$ 的指标给出。所以设计这种滤波系统，其关键是由 $H_{\text{a}}(j\Omega)$ 指标确定其中的数字滤波器 $H(e^{j\omega})$ 的指标。可以证明，$H(e^{j\omega})$ 与 $H_{\text{a}}(j\Omega)$ 具有如下关系：
$$
H_{\text{a}}(j\Omega) = \begin{cases}
\left. H(e^{j\omega}) \right|_{\omega = \Omega T} = H(e^{j\Omega T}) & 0 \leqslant \Omega < \frac{\pi}{T} \\
0 & \frac{\pi}{T} \leqslant |\Omega|
$$
\end{cases}
\tag{5.1.1}
$$
$$
$$
H(e^{j\omega}) = \left. \sum_{k=-\infty}^{\infty} H_{\text{a}}\left( j\Omega - j \frac{2\pi}{T} k \right) \right|_{\Omega = \omega/T} = \sum_{k=-\infty}^{\infty} H_{\text{a}}\left( j \frac{\omega - 2\pi k}{T} \right)
$$
\tag{5.1.2}
$$
$$
且
$$
h(n) = \text{IFT}[H(e^{j\omega})] = T h_{\text{a}}(nT)
$$
\tag{5.1.3}
$$
$$
其中
$$
h_{\text{a}}(t) = \text{IFT}[H_{\text{a}}(j\Omega)]
$$
由此可见，$H_{\text{a}}(j\Omega)$ 与 $H(e^{j\omega})$ 之间仅是 $\omega = \Omega T$ 的频率尺度变换关系。


**图5.1.2** 采样数字滤波系统组成框图及等效模拟滤波系统

通过关系式(5.1.2)可由 $H_{\text{a}}(j\Omega)$ 指标确定数字滤波器 $H(e^{j\omega})$ 的指标(如 $\omega_{\text{p}}$，$\omega_{\text{s}}$，$\alpha_{\text{p}}$，$\alpha_{\text{s}}$ 等)；利用频率转换关系 $\omega = \Omega T$ 容易求出 $H(e^{j\omega})$ 的各边界频率；选用适当的设计方法可得到数字滤波器的系统函数 $H(z)$。
由(5.1.3)式知，也可以采用脉冲响应不变法将等效模拟滤波器 $H_{\text{a}}(s)$ 转换成采样数字系统中数字滤波器的系统函数 $H(z)$。但必须注意：① 对 $h_{\text{a}}(t)$ 的采样频率必须满足采样定理；② 对高通和带阻滤波处理，这种方法不能用，需要用双线性变换法，这时设计稍复杂一些，后面的[例 5.2.3]将详细说明双线性变换法的设计过程。

**3. IIR 数字滤波器的设计方法**

关于滤波器的设计原理与具体的设计方法，教材及其他《数字信号处理》书中都有详细叙述，本章不再赘述。下面仅对 IIR 数字滤波器的几种设计方法及设计步骤作简要归纳，并指出学习要点，并通过例题及习题与上机题解答说明各种设计方法的具体设计过程及相关设计公式，以便读者能有条理地解答滤波器设计题目，设计实际应用滤波器。
为了使初学者对 IIR 数字滤波器设计方法有一个整体概念，先抛开繁杂的设计过程和设计公式，用图 5.1.3 归纳 IIR 数字滤波器的一般设计方法。


**图5.1.3** IIR 数字滤波器的一般设计方法

下面对图 5.1.3 中给出的五种设计方法及其学习要点进行简要归纳。对频域直接逼近法和时域波形逼近法都必须借助计算机设计(即 CAD 设计)，且已有商业设计程序，所以只简要介绍其设计思想及逼近准则。

### 5.1.2 模拟滤波器的设计

为了叙述方便，用 AF 表示模拟滤波器，用 DF 表示数字滤波器。从教材中的详细介绍知道，从 AF 入手设计 DF 时，首先要设计一个“相应的 AF”，所以下面以流程图形式给出 AF 的设计步骤，如图 5.1.4 所示。


**图5.1.4** 模拟滤波器(AF)的设计步骤

由于 AF 设计手册中给出了各种典型 AF 归一化低通原型的设计公式和图表及系统函数 $G(p)$，因此设计 AF 很方便。所以，对需要设计的实际 AF (低通、高通、带通和带阻 AF)，首先将其指标参数转换成相应的归一化($\lambda_{\text{p}}=1$)低通指标参数，将设计各种实际 AF 转化为设计归一化低通 AF；最后将设计好的归一化低通 $G(p)$ 转换成实际滤波器 $H(s)$。为此，下面归纳四种实际 AF 系统函数 $H(s)$ 与其相应的归一化低通 AF 系统函数 $G(p)$ 的相互转换关系，如图 5.1.5 所示。图中总结出了图 5.1.4 中第(2)步和第(4)步所涉及的所有转换关系和转换公式。
图 5.1.5 中的系统函数及变量符号的含义如下：
$G(p)$——低通 AF 系统函数；
$p = \eta + j\lambda$ ——$G(p)$ 的拉氏复变量；
$G(j\lambda)$——低通 AF 频响函数；
$\lambda$——$G(\lambda)$ 的频率变量；
$H(s)$——需要设计的“实际 AF”系统函数；
$s = \sigma + j\Omega$ ——拉氏复变量；
$\Omega$——模拟角频率(rad/s)；
$H(j\Omega)$——实际 AF 的频响函数。
由图 5.1.5 很容易看出各种实际 AF 指标参数的符号和含义，以及向箭头方向转换的有关公式。由于四种实际 $H(j\Omega)$ 向 $G(j\lambda)$ 转换的公式较多，所以图中用①、②、③和④表示，它们分别代表以下四组频率变换公式。为了简化计算，一般取 $\lambda_{\text{p}}=1$，这时的 $G(p)$ 称为归一化低通滤波器，$\lambda$ 为归一化频率。当然，也可以根据需要，对于其他频率(如 $\lambda_{\text{s}}$ 或

<!-- pages: 119-122 -->
# 第5章 无限脉冲响应(IIR)数字滤波器的设计

λ<sub>c</sub>)进行归一化。根据教材中模拟滤波器的设计原理知道，设计巴特沃斯滤波器时，对于3 dB截止频率λ<sub>c</sub>进行归一化最方便。
图5.1.5中①、②、③、④对应的4组频率变换公式：


**图5.1.5** 频率变换关系示意图

①
\begin{cases}
$$
频率变换公式：\lambda = \frac{\lambda_p \Omega}{\Omega_p} \\
归一化低通边界频率：\lambda_p = 1, \lambda_s = \frac{\Omega_s}{\Omega_p}
$$
\end{cases}

②
\begin{cases}
$$
频率变换公式：\lambda = \frac{-\lambda_p \Omega_p}{\Omega} \\
归一化低通边界频率：\lambda_p = 1, \lambda_s = \frac{\Omega_p}{\Omega_s}
$$
\end{cases}

③
\begin{cases}
$$
带宽 B_W = \Omega_{pu} - \Omega_{pl}，通带中心频率 \Omega_0 = \sqrt{\Omega_{pl}\Omega_{pu}} = \sqrt{\Omega_{sl}\Omega_{su}} \\
$$
[如果不满足，要进行指标调整(见教材第174页式(6.2.57))] \\
$$
频率变换公式：\lambda = -\lambda_p \frac{\Omega_0^2 - \Omega^2}{\Omega B_W} \\
归一化低通边界频率：\lambda_p = 1, \lambda_s = \frac{\Omega_0^2 - \Omega_{sl}^2}{\Omega_{sl} B_W}
$$
\end{cases}

④
\begin{cases}
$$
阻带带宽 B_W = \Omega_{su} - \Omega_{sl}，阻带中心频率 \Omega_0 = \sqrt{\Omega_{pl}\Omega_{pu}} = \sqrt{\Omega_{sl}\Omega_{su}} \\
$$
[如果不满足，按教材中式(6.2.57)调整] \\
$$
频率变换公式：\lambda = -\lambda_p \frac{\Omega B_W}{\Omega_0^2 - \Omega^2} \\
归一化低通边界频率：\lambda_p = 1, \lambda_s = \frac{\Omega B_W}{\Omega_0^2 - \Omega_{sl}^2}
$$
\end{cases}

归一化低通G(jλ)的通带最大衰减和阻带最小衰减仍为α<sub>p</sub>和α<sub>s</sub>。图5.1.4中第(3)、(4)个方框涉及的设计与转换方法直接套用教材6.2.6节的相关公式或例题的解法。

## 5.1.3 从AF入手设计DF

由于AF设计理论很成熟，而且有很多特性优良的典型AF可供选用，所以常常从AF入手来设计DF。其设计流程图如图5.1.6所示。
图5.1.6中的(3)(设计相应AF)前面已介绍过。所以只要掌握了将H<sub>a</sub>(s)转换成H(z)的方法与公式，以及相应的数字频率ω与模拟频率Ω之间的关系式，就可以进行图5.1.6中的(2)和(4)，从而完成从AF入手设计DF。用脉冲响应不变法和双线性变换法将AF的系统函数H<sub>a</sub>(s)转换成DF的系统函数H(z)的步骤、公式及ω与Ω的关系式，教材中都有详细的叙述，所以不再重复。


**图5.1.6** 从AF入手设计DF流程图

## 5.1.4 IIR – DF的直接设计法

所谓直接设计法，就是直接在数字域设计IIR – DF的方法。相对而言，因为从AF入手设计DF是先设计相应的AF，然后再通过s – z平面映射，将H<sub>a</sub>(s)转换成H(z)，所以这属于间接设计法。该设计法只能设计与几种典型AF相对应的幅频特性的DF。而需要设计任意形状幅频特性的DF时，只能用直接设计法。直接设计法一般都要借助于计算机进行设计，即计算机辅助设计(CAD)。现在已有多种DF优化设计程序。优化准则不同，所设计的滤波器特点亦不同。所以最主要的是建立优化设计的概念，了解各种优化准则的特点，并根据设计要求，选择合适的优化程序设计DF。
例如，设希望逼近的频响特性为H<sub>d</sub>(e<sup>jω</sup>)，所设计的实际滤波器频响函数为H(e<sup>jω</sup>)。二者的频响误差为
$$ E(e^{j\omega}) = H_d(e^{j\omega}) - H(e^{j\omega}) $$
均方误差定义为
$$ \varepsilon^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} | E(e^{j\omega}) |^2 d\omega $$
使均方误差ε<sup>2</sup>最小的优化设计准则称之为“最小均方误差准则”。这里的“最小”指|E(e<sup>jω</sup>)|在整个频带[−π, π]上的积分(总和)最小，而既非通带波纹最小，又非阻带波动最小。所以，用这种优化程序设计的滤波器的阻带最小衰减和通带波纹可能不满足要求。特别是以理想滤波器特性作为H<sub>d</sub>(e<sup>jω</sup>)时，为了使ε<sup>2</sup>最小，优化过程尽可能逼近H<sub>d</sub>(e<sup>jω</sup>)的间断特性(即使过渡带最窄)，而使通带出现较大过冲、阻带最小衰减过小，不能满足工程要求。
建立如上概念后，调用频域最小均方误差准则优化设计程序时，可正确构造H<sub>d</sub>(e<sup>jω</sup>)。设置合适的过渡带特性，可使通带和阻带逼近精度大大提高，即以加宽过渡带为代价，换取通带平坦性和更大的阻带最小衰减。这一原则在各种设计法中都成立。或者根据需要，选用其它优化设计方法。IIR – DF的优化技术设计法有[22]频域最小均方误差法，最小P误差法、最小平方逆设计法和线性规划法等。利用线性规划法可实现等波纹逼近，即最大误差最小化逼近。

## 5.2 例 题

[例5.2.1] 设计低通DF，要求幅频特性单调下降。3 dB截止频率ω<sub>p</sub> = ω<sub>c</sub> = π/3 rad，阻带截止频率ω<sub>s</sub> = 4π/5 rad，阻带最小衰减α<sub>s</sub> = 15 dB，采样频率f<sub>s</sub> = 30 kHz，分别用脉冲响应不变法和双线性变换法设计。
解：(1) 用脉冲响应不变法设计。按图5.1.6流程设计。
① 确定DF指标参数。
$$ \omega_p = \omega_c = \frac{\pi}{3} \text{ rad}, \alpha_p = 3 \text{ dB} $$
$$ \omega_s = \frac{4\pi}{5} \text{ rad}, \alpha_s = 15 \text{ dB} $$
② 将DF指标参数转换成相应的AF指标参数。因为在脉冲响应不变法中，ω = ΩT，所以
$$ \Omega_p = \frac{\omega_p}{T} = \frac{\pi}{3} \times 30 \times 10^3 = 10\,000\pi \text{ rad/s}, \alpha_p = 3 \text{ dB} $$
$$ \Omega_s = \frac{\omega_s}{T} = \frac{4\pi}{5} \times 30 \times 10^3 = 24\,000\pi \text{ rad/s}, \alpha_s = 3 \text{ dB} $$
③ 求相应的AF系统函数H<sub>a</sub>(s)。
a. 计算阶数N，根据要求，应选择巴特沃斯AF。由教材(6.2.18)式有
$$ \lambda_{sp} = \frac{\Omega_s}{\Omega_p} = \frac{24\,000\pi}{10\,000\pi} = 2.4 $$
$$ k_{sp} = \sqrt{\frac{10^{0.1\alpha_s} - 1}{10^{0.1\alpha_p} - 1}} = \sqrt{\frac{10^{1.5} - 1}{10^{0.3} - 1}} = 5.5463 $$
$$ N = \frac{\lg k_{sp}}{\lg \lambda_{sp}} = \frac{\lg 5.5463}{\lg 2.4} = 1.9569 $$
取N = 2。
b. 查教材第157页表6.2.1，得到二阶巴特沃斯归一化低通原型：
$$ G(p) = \frac{1}{p^2 + \sqrt{2}p + 1} $$
c. 频率变换，由图5.1.5中LP→LP变换公式求出相应的AF系统函数H<sub>a</sub>(s)：
$$ H_a(s) = G(p) \big|_{p=\frac{s}{\Omega_p}} = \frac{\Omega_p^2}{s^2 + \sqrt{2}\Omega_p s + \Omega_p^2} = \frac{10^8\pi^2}{s^2 + 10^4\pi\sqrt{2}s + 10^8\pi^2} $$
④ 将H<sub>a</sub>(s)转换成H<sub>1</sub>(z)：
$$ H_1(z) = \frac{0.4265z^{-1}}{1 - 0.7040z^{-1} + 0.2274z^{-2}} $$
以上结果是调用MATLAB impinvar函数直接求出的，这样就不用求极点s<sub>1</sub>和s<sub>2</sub>以及部分分式展开。请读者按教材(6.3.1)式和(6.3.4)式或(6.3.11)式计算，验证以上结果。
(2) 用双线性变换法设计。
① 确定DF指标参数；与脉冲响应不变法中的①相同。
② 将DF指标参数转换成相应AF指标参数。因为在双线性变换法中，ω和Ω为非线性关系，Ω = (2/T) tan(ω/2)，所以，需要预畸变校正(学习重点)。只有采用非线性预畸变校正，由DF边界频率求得相应AF边界频率，才能在经过双线性变换，将H<sub>a</sub>(s)转换成H(z)过程中的非线性畸变后，保持DF原来边界频率不变。按教材(6.4.7)式得到
$$ \Omega_p = \frac{2}{T} \tan \frac{\omega_p}{2} = 6 \times 10^4 \tan \frac{\pi}{6} = 3.4641 \times 10^4 \text{ rad/s}, \quad \alpha_p = 3 \text{ dB} $$
$$ \Omega_s = \frac{2}{T} \tan \frac{\omega_s}{2} = 6 \times 10^4 \tan \frac{2\pi}{5} = 18.466 \times 10^4 \text{ rad/s}, \quad \alpha_s = 15 \text{ dB} $$
③ 设计相应的H<sub>a</sub>(s)。
a. 计算阶数N：由教材中(6.2.18)式，有
$$ k_{sp} = 5.5463 \text{ (与脉冲响应不变法中的 ③ 相同)} $$
$$ \lambda_{sp} = \frac{\Omega_s}{\Omega_p} = \frac{18.4661}{3.4661} = 5.3276 $$
$$ N = \frac{\lg k_{sp}}{\lg \lambda_{sp}} = \frac{\lg 5.5463}{\lg 5.3276} = 1.0242 $$
工程上为了简化系统，可取N = 1(工程上允许时，可如此处理)。
b. 查教材表6.2.1得归一化低通原型G(p)为
$$ G(p) = \frac{1}{s+1} $$
c. 经频率变换，得
$$ H_a(s) = G(p) \big|_{p=\frac{s}{\Omega_p}} = \frac{\Omega_p}{s+\Omega_p} = \frac{3.4641 \times 10^4}{s+3.4641 \times 10^4} $$
④ 用双线性变换法将H<sub>a</sub>(s)转换成H<sub>2</sub>(z)，由教材中(6.4.3)式，有
$$ H_2(z) = H_a(s) \big|_{s=\frac{2}{T} \frac{1-z^{-1}}{1+z^{-1}}} = \frac{3.4641 \times 10^4}{6 \times 10^4 \frac{1-z^{-1}}{1+z^{-1}} + 3.4641 \times 10^4} = \frac{0.366(1+z^{-1})}{1-0.26795z^{-1}} $$
(3) 设计性能比较。用脉冲响应不变法设计的H<sub>1</sub>(z)和用双线性变换法设计的H<sub>2</sub>(z)的损耗函数曲线分别如图5.2.1(a)和(b)所示。由图可见，在通带内，二者均能满足要求，但|H<sub>1</sub>(e<sup>jω</sup>)|在ω = π附近存在频率混叠失真，从而使ω<sub>s</sub> = 0.8π处衰减不到–12 dB，不满足指标要求。|H<sub>2</sub>(e<sup>jω</sup>)|无频率混叠失真，满足要求。但|H<sub>2</sub>(e<sup>jω</sup>)|存在非线性频率失真，且

<!-- pages: 9-9 -->

频率越高，失真越明显。



**图5.2.1**

其它类型的 DF 设计过程见教材第 6 章习题与上机题解答。

[例 5.2.2] 采样数字系统的组成框图如图 5.2.2 所示。理想情况下，A/D 变换器对模拟信号采样，得到序列 $x(n)=x_a(nT)$，而 D/A 变换器是将序列 $y(n)$ 变成模拟带限信号 $y_a(t)$。

$$ y_a(t) = \sum_{n=-\infty}^{\infty} y(n) \frac{\sin\left[\frac{\pi(t-nT)}{T}\right]}{\frac{\pi(t-nT)}{T}} $$

整个系统的作用可等效为一个线性时不变模拟滤波器。

(1) 如果 $h(n)$ 表示一截止频率为 $\pi/8$ 的低通数字滤波器，采样频率 $F_s = \frac{1}{T} = 10\ \text{kHz}$。试求等效模拟滤波器的截止频率。


**图5.2.2**

(2) 如果 $F_s = 20\ \text{kHz}$，重复(1)。

解：对采样数字系统，数字频率 $\omega$ 与模拟频率 $f$ 满足线性关系 $\omega = 2\pi f T$。已知数字滤波器截止频率 $\omega_c = \frac{\pi}{8}\ \text{rad}$，所以，必须满足

$$ \omega_c = \frac{\pi}{8} = 2\pi f_c T $$

$f_c$ 为等效模拟滤波器截止频率。由上式可求得

$$ f_c = \frac{\omega_c}{2\pi T} = \frac{\frac{\pi}{8}}{2\pi} F_s = \frac{1}{16} F_s $$

<!-- pages: 124-127 -->

故
(1) $f_c = \frac{1}{16} \times 10000 = 625 \text{ Hz}$
(2) $f_c = \frac{1}{16} \times 20000 = 1250 \text{ Hz}$

由以上结果可见，对相同的数字滤波特性 $H(\mathrm{e}^{\mathrm{j}\omega})$，当采样数字系统中的采样频率不同时，等效的模拟滤波器频响函数 $H_{\mathrm{a}}(\mathrm{j}\Omega)$ 的边界频率也不同，反之亦然。

**[例 5.2.3]** 采样数字滤波器组成如图 5.1.2 所示，分别用双线性变换法和脉冲响应不变法设计其中的数字滤波器。总体等效模拟滤波器指标参数如下：
(1) 输入模拟信号 $x_{\mathrm{a}}(t)$ 的最高频率 $f_{\mathrm{c}} = 100 \text{ Hz}$；
(2) 选用巴特沃斯滤波器，3 dB 截止频率 $f_{\mathrm{c}} = 100 \text{ Hz}$，阻带截止频率 $f_{\mathrm{s}} = 150 \text{ Hz}$，阻带最小衰减 $\alpha_{\mathrm{s}} = 20 \text{ dB}$。

**解：** 为了满足采样定理，减少脉冲响应不变法引入的频率混叠失真，并降低对恢复滤波器的要求，取采样频率 $F_{\mathrm{s}} = 400 \text{ Hz}$。
**(1) 用双线性变换法。**
① 由(5.1.2)式确定数字滤波器 $H(\mathrm{e}^{\mathrm{j}\omega})$ 的指标参数。因为采用双线性变换法设计，数字频率 $\omega$ 与相应的模拟频率 $\Omega$ 之间为非线性关系 $\left( \Omega = \frac{2}{T} \tan \frac{\omega}{2} \right)$。但根据(5.1.1)式和(5.1.2)式，采样数字系统要求其中的数字滤波器 $H(\mathrm{e}^{\mathrm{j}\omega})$ 与总等效模拟滤波器 $H_{\mathrm{a}}(\mathrm{j}\Omega)$ 之间的频率映射关系为线性关系 $\omega = \Omega T$。所以，不能直接按等效模拟滤波器技术指标设计相应模拟滤波器 $H_{\mathrm{a}}(s)$，再将其用双线性变换法映射成数字滤波器 $H(z)$。因此，我们必须先按(5.1.2)式将等效模拟滤波器指标参数转换成采样数字滤波系统中的数字滤波器指标参数，再用双线性变换法的一般设计步骤设计该数字滤波器。
采样数字滤波系统中数字滤波器的指标参数：
通带边界频率：
$$ \omega_{\mathrm{p}} = \omega_{\mathrm{c}} = 2\pi f_{\mathrm{c}} T = \frac{2\pi \times 100}{400} = \frac{\pi}{2} \text{ rad} $$
通带最大衰减：
$$ \alpha_{\mathrm{p}} = 3 \text{ dB} $$
阻带截止频率：
$$ \omega_{\mathrm{s}} = 2\pi f_{\mathrm{s}} T = \frac{2\pi \times 150}{400} = \frac{3\pi}{4} \text{ rad} $$
阻带最小衰减：
$$ \alpha_{\mathrm{s}} = 20 \text{ dB} $$
② 用双线性变换法设计数字滤波器的一般过程如下：
a. 预畸变校正，确定相应的模拟滤波器的指标参数：
$$ \Omega_{\mathrm{p}} = \frac{2}{T} \tan \frac{\omega_{\mathrm{p}}}{2} = 800 \tan \frac{\pi}{4} = 800 \text{ rad/s}, \alpha_{\mathrm{p}} = 3 \text{ dB} $$
$$ \Omega_{\mathrm{s}} = \frac{2}{T} \tan \frac{\omega_{\mathrm{s}}}{2} = 800 \tan \frac{3\pi}{8} = 1931.37 \text{ rad/s}, \alpha_{\mathrm{s}} = 20 \text{ dB} $$

b. 设计相应的模拟滤波器，确定其系统函数 $H_{\mathrm{a}}(s)$。
(a) 求 $H_{\mathrm{a}}(s)$ 阶数 $N$：
$$ k_{\mathrm{sp}} = \sqrt{\frac{10^{0.1\alpha_{\mathrm{s}}} - 1}{10^{0.1\alpha_{\mathrm{p}}} - 1}} = \sqrt{\frac{10^{2} - 1}{10^{0.3} - 1}} = 9.9700 $$
$$ \lambda_{\mathrm{sp}} = \frac{\Omega_{\mathrm{s}}}{\Omega_{\mathrm{p}}} = \frac{1931.37}{800} = 2.414 $$
$$ N = \frac{\lg k_{\mathrm{sp}}}{\lg \lambda_{\mathrm{sp}}} = \frac{\lg 9.9700}{\lg 2.141} = 2.609 $$
取 $N=3$。

在实际工作中，调用 IIR 滤波器阶数来计算程序函数，很容易求出满足要求的最小阶数 $N$ 值。如前述，`buttord` 函数用于计算 butterworth 滤波器阶数。本例中，求阶数的 MATLAB 程序如下：
```matlab
Wp=800; Rp=3;
Ws=1931.37; Rs=20;
[N, Wc]=buttord(Wp, Ws, Rp, Rs, 's');
```
运行结果：
`N=3, Wc=897.9654`

(b) 求相应的模拟滤波器系统函数 $H_{\mathrm{a}}(s)$。查表得到三阶 Butterworth 归一化低通原型系统函数：
$$ G_{\mathrm{a}}(p) = \frac{1}{1 + 2p + 2p^2 + p^3} $$
去归一化(即低通原型到低通的频率变换)，得
$$ H_{\mathrm{a}}(s) = G_{\mathrm{a}}(p) \left|_{p=\frac{s}{\Omega_{\mathrm{c}}}=\frac{s}{800}} \right. = \frac{5.12 \times 10^8}{s^3 + 1.6 \times 10^3 s^2 + 1.28 \times 10^6 s + 5.12 \times 10^8} $$

c. 用双线性变换法将 $H_{\mathrm{a}}(s)$ 映射成数字滤波器系统函数 $H(z)$：
$$ \begin{aligned} H(z) &= H_{\mathrm{a}}(s) \left|_{s=\frac{2}{T} \frac{1-z^{-1}}{1+z^{-1}}} \right. \\ &= \frac{0.1667 + 0.5z^{-1} + 0.5z^{-2} + 0.1667z^{-3}}{1 - 1.3278 \times 10^{-15}z^{-1} + 0.333z^{-2} + 3.362 \times 10^{-16}z^{-3}} \end{aligned} $$
损耗函数曲线如图 5.2.3(a)所示。

实际工程设计时，可直接调用 MATLAB 函数来完成数字滤波器的双线性变换法设计。程序如下：
```matlab
Wp=pi/2; rp=3; Ws=3*pi/4; rs=20;      %数字滤波器指标参数
[N, Wc]=buttord(Wp, Ws, rp, rs);      %计算阶数 N 和 3dB 截止频率 Wc
[B, A]=butter(N, wc);                 %求数字滤波器系统函数 H(z)
```
运行结果如下：
`B=[ 0.1970   0.5910   0.5910   0.1970]`
`A=[ 1.0000   0.2114   0.3452   0.0194]`
由此可写出系统函数：
$$ \hat{H}(z) = \frac{0.1970 + 0.5910z^{-1} + 0.5910z^{-2} + 0.1970z^{-3}}{1 + 0.2114z^{-1} + 0.3452z^{-2} + 0.0194z^{-3}} $$
损耗函数曲线如图 5.2.3(b)所示。比较发现，$\hat{H}(z)$ 和 $H(z)$ 的幅频特性都满足设计指标要求，但二者的系数有较大差别。这是函数 `butter` 在计算过程中进行合理的数据归一化的结果。$\hat{H}(z)$ 的优点是其系数差别小，便于量化实现，所以，在实际设计中一般直接调用 MATLAB 函数来完成数字滤波器的双线性变换法设计。

![{{FIGURE:125}}](image_placeholder)
**图 5.2.3:** (a) 手工计算结果幅频特性；(b) `butter` 函数计算结果幅频特性。

**(2) 用脉冲响应不变法。** 由于总的等效模拟滤波器为低通滤波器，所以根据(5.1.3)式，直接用脉冲不变法将等效模拟滤波器转换成数字滤波器即可满足要求。因此首先按所给的等效模拟滤波器指标参数设计其系统函数 $H_{\mathrm{a}}(s)$，然后将 $H_{\mathrm{a}}(s)$ 转换成 $H(z)$ 即可。
① 设计等效模拟滤波器 $H_{\mathrm{a}}(s)$。
a. 计算阶数 $N$：
$$ k_{\mathrm{sp}} = 9.970 $$
$$ \lambda_{\mathrm{sp}} = \frac{f_{\mathrm{s}}}{f_{\mathrm{p}}} = \frac{150}{100} = 1.5 $$
$$ N = \frac{\lg k_{\mathrm{sp}}}{\lg \lambda_{\mathrm{sp}}} = \frac{\lg 9.970}{\lg 1.5} = 5.67 $$
取 $N=6$。

b. 查表得到六阶 Butterworth 归一化低通原型 $G(p)$，并以 3 dB 截止频率 $\Omega_{\mathrm{c}} = 2\pi \times 100$ 去归一化得模拟滤波器系统函数 $H_{\mathrm{a}}(s)$：
$$ G(p) = \frac{1}{s^6 + 3.8637s^5 + 7.4641s^4 + 9.1416s^3 + 7.4641s^2 + 3.8637s + 1} $$
$$ \begin{aligned} H_{\mathrm{a}}(s) &= G(p) \left|_{p=\frac{s}{\Omega_{\mathrm{c}}}} \right. \\ &= \frac{6.1529 \times 10^{16}}{s^6 + 2.42765s^5 + 2.9467s^4 + 2.2676 \times 10^9 s^3 + 1.1633 \times 10^{12}s^2 + 3.7836 \times 10^{14}s + 6.1529 \times 10^{16}} \end{aligned} $$
② 调用 MATLAB 函数 `impvar`，将 $H_{\mathrm{a}}(s)$ 转换成 $H(z)$：
$$ \begin{aligned} H(z) &= [9.6634 \times 10^{-15} + 0.024z^{-1} + 0.3347z^{-2} + 0.2985z^{-3} + 0.0463z^{-4} \\ &\quad + 7.4472 \times 10^{-4}z^{-5}][1 - 0.7666z^{-1} + 0.7674z^{-2} - 0.3857z^{-3} \\ &\quad + 0.1310z^{-4} - 0.0260z^{-5} + 0.0023z^{-6}]^{-1} \end{aligned} $$

### 5.3 教材第 6 章习题与上机题解答

1. 设计一个巴特沃斯低通滤波器，要求通带截止频率 $f_{\mathrm{p}}=6 \text{ kHz}$，通带最大衰减 $\alpha_{\mathrm{p}} = 3 \text{ dB}$，阻带截止频率 $f_{\mathrm{s}}=12 \text{ kHz}$，阻带最小衰减 $\alpha_{\mathrm{s}} = 25 \text{ dB}$。求出滤波器归一化系统函数 $G(p)$ 以及实际滤波器的 $H_{\mathrm{a}}(s)$。

**解：(1) 求阶数 $N$。**
$$ N = \frac{\lg k_{\mathrm{sp}}}{\lg \lambda_{\mathrm{sp}}} $$
$$ k_{\mathrm{sp}} = \sqrt{\frac{10^{0.1\alpha_{\mathrm{s}}} - 1}{10^{0.1\alpha_{\mathrm{p}}} - 1}} = \sqrt{\frac{10^{2.5} - 1}{10^{0.3} - 1}} \approx 17.794 $$
$$ \lambda_{\mathrm{sp}} = \frac{\Omega_{\mathrm{s}}}{\Omega_{\mathrm{p}}} = \frac{2\pi \times 12 \times 10^3}{2\pi \times 6 \times 10^3} = 2 $$
将 $k_{\mathrm{sp}}$ 和 $\lambda_{\mathrm{sp}}$ 值代入 $N$ 的计算公式，得
$$ N = \frac{\lg 17.794}{\lg 2} = 4.15 $$
所以取 $N=5$ (实际应用中，根据具体要求，也可能取 $N=4$，指标稍微差一点，但阶数低一阶，使系统实现电路得到简化)。

(2) 求归一化系统函数 $G(p)$。由阶数 $N=5$ 直接查教材第 157 页表 6.2.1，得到五阶巴特沃斯归一化低通滤波器系统函数 $G(p)$ 为
$$ G(p) = \frac{1}{p^5 + 3.2361p^4 + 5.2361p^3 + 5.2361p^2 + 3.2361p + 1} $$
或
$$ G(p) = \frac{1}{(p^2 + 0.618p + 1)(p^2 + 1.618p + 1)(p + 1)} $$
当然，也可以先按教材(6.2.13)式计算出极点：
$$ p_k = \mathrm{e}^{\mathrm{j}\pi\left(\frac{1}{2} + \frac{2k+1}{2N}\right)}, \quad k=0,1,2,3,4 $$
再由教材(6.2.12)式写出 $G(p)$ 表达式为

<!-- pages: 14-17 -->

# 第5章 无限脉冲响应(IIR)数字滤波器的设计 - 例题与习题解答

$$
G(p) = \frac{1}{\prod_{k=0}^{4}(p-p_k)}
$$

最后代入 $p_k$ 值并进行分母展开，便可得到与查表相同的结果。

(3) 去归一化（即 LP–LP 频率变换），由归一化系统函数 $G(p)$ 得到实际滤波器系统函数 $H_a(s)$。

由于本题中 $\alpha_p = 3\text{ dB}$，即 $\Omega_c = \Omega_p = 2\pi \times 6 \times 10^3 \text{ rad/s}$，因此

$$
$$
\begin{aligned}
$$
H_a(s) &= H_a(p) \big|_{p=\frac{s}{\Omega_c}} \\
&= \frac{\Omega_c^5}{s^5 + 3.2361\Omega_c s^4 + 5.2361\Omega_c^2 s^3 + 5.2361\Omega_c^3 s^2 + 3.2361\Omega_c^4 s + \Omega_c^5}
$$
\end{aligned}
$$

$$
对分母因式形式，则有

$$
$$
\begin{aligned}
$$
H_a(s) &= H_a(p) \big|_{p=\frac{s}{\Omega_c}} \\
&= \frac{\Omega_c^5}{(s^2 + 0.6180\Omega_c s + \Omega_c^2)(s^2 + 1.6180\Omega_c s + \Omega_c^2)(s + \Omega_c)}
$$
\end{aligned}
$$

$$
如上结果中，$\Omega_c$ 的值未代入相乘，这样使读者能清楚地看到去归一化后，3 dB 截止频率对归一化系统函数的改变作用。

2. 设计一个切比雪夫低通滤波器，要求通带截止频率 $f_p = 3 \text{ kHz}$，通带最大衰减 $\alpha_p = 0.2 \text{ dB}$，阻带截止频率 $f_s = 12 \text{ kHz}$，阻带最小衰减 $\alpha_s = 50 \text{ dB}$。求出滤波器归一化系统函数 $G(p)$ 和实际的 $H_a(s)$。

**解：**(1) 确定滤波器技术指标。
$$
\alpha_p = 0.2 \text{ dB}, \qquad \Omega_p = 2\pi f_p = 6\pi \times 10^3 \text{ rad/s}
$$
$$
\alpha_s = 50 \text{ dB}, \qquad \Omega_s = 2\pi f_s = 24\pi \times 10^3 \text{ rad/s}
$$
$$
\lambda_p = 1, \qquad \lambda_s = \frac{\Omega_s}{\Omega_p} = 4
$$

(4) 求阶数 $N$ 和 $\varepsilon$。
$$
N = \frac{\text{arch}k^{-1}}{\text{arch}\lambda_s}
$$
$$
k^{-1} = \sqrt{\frac{10^{0.1\alpha_s}-1}{10^{0.1\alpha_p}-1}} \approx 1456.65
$$
$$
N = \frac{\text{arch}1456.65}{\text{arch}4} = 3.8659
$$

为了满足指标要求，取 $N=4$。
$$
\varepsilon = \sqrt{10^{0.1\alpha_p}-1} = 0.2171
$$

(3) 求归一化系统函数 $G(p)$。
$$
G(p) = \frac{1}{\varepsilon \cdot 2^{N-1} \prod_{k=1}^{N}(p-p_k)} = \frac{1}{1.7368 \prod_{k=1}^{4}(p-p_k)}
$$

其中，极点 $p_k$ 由教材(6.2.46)式求出如下：
$$
p_k = -\text{ch}\xi \sin\frac{(2k-1)\pi}{2N} + j\text{ch}\xi \cos\frac{(2k-1)\pi}{2N} \qquad k = 1, 2, 3, 4
$$

$$
\xi = \frac{1}{N}\text{arsh}\frac{1}{\varepsilon} = \frac{1}{4}\text{arsh}\frac{1}{0.2171} \approx 0.5580
$$

$$
p_1 = -\text{ch}0.5580 \sin\frac{\pi}{8} + j\text{ch}0.5580 \cos\frac{\pi}{8} = -0.4438 + j1.0715
$$
$$
p_2 = -\text{ch}0.5580 \sin\frac{3\pi}{8} + j\text{ch}0.5580 \cos\frac{3\pi}{8} = -1.0715 + j0.4438
$$
$$
p_3 = -\text{ch}0.5580 \sin\frac{5\pi}{8} + j\text{ch}0.5580 \cos\frac{5\pi}{8} = -1.0715 - j0.4438
$$
$$
p_4 = -\text{ch}0.5580 \sin\frac{7\pi}{8} + j\text{ch}0.5580 \cos\frac{7\pi}{8} = -0.4438 - j1.0715
$$

(4) 将 $G(p)$ 去归一化，求得实际滤波器系统函数 $H_a(s)$：
$$
$$
\begin{aligned}
$$
H_a(s) &= G(p) \big|_{p=\frac{s}{\Omega_p}} \\
&= \frac{\Omega_p^4}{1.7368 \prod_{k=1}^{4}(s-\Omega_p p_k)} = \frac{\Omega_p^4}{1.7368 \prod_{k=1}^{4}(s-s_k)}
$$
\end{aligned}
$$

$$
其中，$s_k = \Omega_p p_k = 6\pi \times 10^3 p_k$, $k=1, 2, 3, 4$。因为 $p_4 = p_1^*$, $p_3 = p_2^*$，所以，$s_4 = s_1^*$, $s_3 = s_2^*$。将两对共轭极点对应的因子相乘，得到分母为二阶因子的形式，其系数全为实数。

$$
$$
\begin{aligned}
$$
H_a(s) &= \frac{7.2687 \times 10^{16}}{(s^2 - 2\text{Re}[s_1]s + |s_1|^2)(s^2 - 2\text{Re}[s_2]s + |s_2|^2)} \\
&= \frac{7.2687 \times 10^{16}}{(s^2 + 1.6731 \times 10^4 s + 4.7791 \times 10^8)(s^2 + 4.0394 \times 10^4 s + 4.7790 \times 10^8)}
$$
\end{aligned}
$$

$$
也可得到分母多项式形式，请读者自己计算。

3. 设计一个巴特沃斯高通滤波器，要求其通带截止频率 $f_p = 20 \text{ kHz}$，阻带截止频率 $f_s = 10 \text{ kHz}$，$f_p$ 处最大衰减为 $3 \text{ dB}$，阻带最小衰减 $\alpha_s = 15 \text{ dB}$。求出该高通滤波器的系统函数 $H_a(s)$。

**解：**(1) 确定高通滤波器技术指标要求：
$$
f_p = 20 \text{ kHz}, \qquad \alpha_p = 3 \text{ dB}
$$
$$
f_s = 10 \text{ kHz}, \qquad \alpha_s = 15 \text{ dB}
$$

(2) 求相应的归一化低通滤波器技术指标要求：套用图 5.1.5 中高通到低通频率转换公式②，$\lambda_p = 1$, $\lambda_s = \Omega_p / \Omega_s$，得到
$$
\lambda_p = 1, \quad \alpha_p = 3 \text{ dB}
$$
$$
\lambda_s = \frac{\Omega_p}{\Omega_s} = 2, \quad \alpha_s = 15 \text{ dB}
$$

(3) 设计相应的归一化低通 $G(p)$。题目要求采用巴特沃斯类型，故
$$
k_{sp} = \sqrt{\frac{10^{0.1\alpha_p}-1}{10^{0.1\alpha_s}-1}} = 0.18
$$
$$
\lambda_{sp} = \frac{\lambda_s}{\lambda_p} = 2
$$
$$
N = -\frac{\lg k_{sp}}{\lg \lambda_{sp}} = -\frac{\lg 0.18}{\lg 2} = 2.47
$$

所以，取 $N=3$，查教材中表 6.2.1，得到三阶巴特沃斯归一化低通 $G(p)$ 为
$$
G(p) = \frac{1}{p^3 + 2p^2 + 2p + 1}
$$

(4) 频率变换。将 $G(p)$ 变换成实际高通滤波器系统函数 $H(s)$：
$$
H(s) = G(p) \big|_{p=\frac{\Omega_c}{s}} = \frac{s^3}{s^3 + 2\Omega_c s^2 + 2\Omega_c^2 s + \Omega_c^3}
$$

式中
$$
\Omega_c = 2\pi f_c = 2\pi \times 20 \times 10^3 = 4\pi \times 10^4 \text{ rad/s}
$$

4. 已知模拟滤波器的系统函数 $H_a(s)$ 如下：
(1) $H_a(s) = \frac{s+a}{(s+a)^2 + b^2}$
(2) $H_a(s) = \frac{b}{(s+a)^2 + b^2}$

式中 $a$、$b$ 为常数，设 $H_a(s)$ 因果稳定，试采用脉冲响应不变法将其转换成数字滤波器 $H(z)$。

**解：**该题所给 $H_a(s)$ 正是模拟滤波器二阶基本节的两种典型形式。所以，求解该题具有代表性，解该题的过程，就是导出这两种典型形式的 $H_a(s)$ 的脉冲响应不变法转换公式。设采样周期为 $T$。

$H_a(s)$ 的极点为
$$
s_1 = -a + jb, \qquad s_2 = -a - jb
$$

将 $H_a(s)$ 部分分式展开（用待定系数法）：
$$
$$
\begin{aligned}
$$
H_a(s) &= \frac{s+a}{(s+a)^2 + b^2} = \frac{A_1}{s-s_1} + \frac{A_2}{s-s_2} \\
&= \frac{A_1(s-s_2) + A_2(s-s_1)}{(s+a)^2 + b^2} \\
&= \frac{(A_1 + A_2)s - A_1 s_2 - A_2 s_1}{(s+a)^2 + b^2}
$$
\end{aligned}
$$

$$
比较分子各项系数可知，$A_1$、$A_2$ 应满足方程：
$$
$$
\begin{cases}
A_1 + A_2 = 1 \\
-A_1 s_2 - A_2 s_1 = a
\end{cases}
$$

$$
解之得，$A_1 = 1/2$，$A_2 = 1/2$，所以
$$
H_a(s) = \frac{1/2}{s - (-a + jb)} + \frac{1/2}{s - (-a - jb)}
$$

套用教材(6.3.4)式，得到
$$
H(z) = \sum_{k=1}^{2} \frac{A_k}{1 - e^{s_k T} z^{-1}} = \frac{\frac{1}{2}}{1 - e^{(-a+jb)T} z^{-1}} + \frac{\frac{1}{2}}{1 - e^{(-a-jb)T} z^{-1}}
$$

按照题目要求，上面的 $H(z)$ 表达式就可作为该题的答案。但在工程实际中，一般用无复数乘法器的二阶基本节结构来实现。由于两个极点共轭对称，所以将 $H(z)$ 的两项通分并化简整理，可得
$$
H(z) = \frac{1 - z^{-1} e^{-aT} \cos(bT)}{1 - 2 e^{-aT} \cos(bT) z^{-1} + e^{-2aT} z^{-2}}
$$

用脉冲响应不变法转换成数字滤波器时，直接套用上面的公式即可，且对应结构图中无复数乘法器，便于工程实际中实现。

将 $H_a(s)$ 部分分式展开：
$$
H_a(s) = \frac{\frac{j}{2}}{s - (-a - jb)} + \frac{-\frac{j}{2}}{s - (-a + jb)}
$$

套用教材(6.3.4)式，得到
$$
H(z) = \frac{\frac{j}{2}}{1 - e^{(-a-jb)T} z^{-1}} + \frac{-\frac{j}{2}}{1 - e^{(-a+jb)T} z^{-1}}
$$

通分并化简整理，得到
$$
H(z) = \frac{z^{-1} e^{-aT} \sin(bT)}{1 - 2 e^{-aT} \cos(bT) z^{-1} + e^{-2aT} z^{-2}}
$$

5. 已知模拟滤波器的系统函数如下：
(1) $H_a(s) = \frac{1}{s^2 + s + 1}$
(2) $H_a(s) = \frac{b}{2s^2 + 3s + 1}$

试采用脉冲响应不变法和双线性变换法将其转换为数字滤波器。设 $T=2 \text{ s}$。

**解：**Ⅰ. 用脉冲响应不变法

**方法一**　直接按脉冲响应不变法设计公式，$H_a(s)$ 的极点为
$$
s_1 = -\frac{1}{2} + j\frac{\sqrt{3}}{2}, \qquad s_2 = -\frac{1}{2} - j\frac{\sqrt{3}}{2}
$$

$$
H_a(s) = \frac{-j\frac{\sqrt{3}}{3}}{s - \left(-\frac{1}{2} + j\frac{\sqrt{3}}{2}\right)} + \frac{j\frac{\sqrt{3}}{3}}{s - \left(-\frac{1}{2} - j\frac{\sqrt{3}}{2}\right)}
$$

$$
H(z) = \frac{-j\frac{\sqrt{3}}{3}}{1 - e^{\left(-\frac{1}{2}+j\frac{\sqrt{3}}{2}\right)T} z^{-1}} + \frac{j\frac{\sqrt{3}}{3}}{1 - e^{\left(-\frac{1}{2}-j\frac{\sqrt{3}}{2}\right)T} z^{-1}}
$$

将 $T=2$ 代入上式，得

<!-- pages: 18-21 -->

$$
H(z) = \frac{-\mathrm{j} \frac{\sqrt{3}}{3}}{1 - \mathrm{e}^{-1 + \mathrm{j} \sqrt{3}} z^{-1}} + \frac{\mathrm{j} \frac{\sqrt{3}}{3}}{1 - \mathrm{e}^{-1 - \mathrm{j} \sqrt{3}} z^{-1}} = \frac{2\sqrt{3}}{3} \cdot \frac{z^{-1} \mathrm{e}^{-1} \sin \sqrt{3}}{1 - 2 z^{-1} \mathrm{e}^{-1} \cos \sqrt{3} + \mathrm{e}^{-2} z^{-2}}
$$

**方法二** 直接套用 4 题(2)所得公式。为了套用公式，先对 $H_{\mathrm{a}}(s)$ 的分母配方，将 $H_{\mathrm{a}}(s)$ 化成 4 题中的标准形式：

$$
H_{\mathrm{a}}(s) = \frac{b}{(s + a)^2 + b^2} \cdot c \qquad c \text{为一常数}
$$

由于

$$
s^2 + s + 1 = \left( s + \frac{1}{2} \right)^2 + \frac{3}{4} = \left( s + \frac{1}{2} \right)^2 + \left( \frac{\sqrt{3}}{2} \right)^2
$$

所以

$$
H_{\mathrm{a}}(s) = \frac{1}{s^2 + s + 1} = \frac{\frac{\sqrt{3}}{2}}{\left( s + \frac{1}{2} \right)^2 + \left( \frac{\sqrt{3}}{2} \right)^2} \cdot \frac{2\sqrt{3}}{3}
$$

对比可知，$a = \frac{1}{2}$，$b = \frac{\sqrt{3}}{2}$，套用公式，得

$$
H(z) = \frac{2\sqrt{3}}{3} \cdot \frac{z^{-1} \mathrm{e}^{-aT} \sin(bT)}{1 - 2 z^{-1} \mathrm{e}^{-aT} \cos(bT) + z^{-2} \mathrm{e}^{-2aT}} \bigg|_{T=2} = \frac{2\sqrt{3}}{3} \cdot \frac{z^{-1} \mathrm{e}^{-1} \sin \sqrt{3}}{1 - 2 z^{-1} \mathrm{e}^{-1} \cos \sqrt{3} + z^{-2} \mathrm{e}^{-2}}
$$

(2)

$$
H_{\mathrm{a}}(s) = \frac{1}{2s^2 + 3s + 1} = \frac{1}{s + \frac{1}{2}} + \frac{-1}{s + 1}
$$

$$
H(z) = \frac{1}{1 - \mathrm{e}^{-\frac{1}{2}T} z^{-1}} + \frac{-1}{1 - \mathrm{e}^{-T} z^{-1}} \bigg|_{T=2} = \frac{1}{1 - \mathrm{e}^{-1} z^{-1}} - \frac{1}{1 - \mathrm{e}^{-2} z^{-1}}
$$

或通分合并两项得

$$
H(z) = \frac{(\mathrm{e}^{-1} - \mathrm{e}^{-2}) z^{-1}}{1 - (\mathrm{e}^{-1} + \mathrm{e}^{-2}) z^{-1} + \mathrm{e}^{-3} z^{-2}}
$$

**Ⅱ．用双线性变换法**

(1)

$$
H(z) = H_{\mathrm{a}}(s) \bigg|_{s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}, \, T=2} = \frac{1}{\left( \frac{1 - z^{-1}}{1 + z^{-1}} \right)^2 + \frac{1 - z^{-1}}{1 + z^{-1}} + 1} = \frac{(1 + z^{-1})^2}{(1 - z^{-1})^2 + (1 - z^{-1})(1 + z^{-1}) + (1 + z^{-1})^2} = \frac{1 + 2z^{-1} + z^{-2}}{3 + z^{-2}}
$$

$$
H(z) = H_{\mathrm{a}}(s) \bigg|_{s = \frac{1 - z^{-1}}{1 + z^{-1}}} = \frac{1}{2 \left( \frac{1 - z^{-1}}{1 + z^{-1}} \right)^2 + 3 \frac{1 - z^{-1}}{1 + z^{-1}} + 1} = \frac{(1 + z^{-1})^2}{2(1 - z^{-1})^2 + 3(1 - z^{-2}) + (1 + z^{-1})^2} = \frac{1 + 2z^{-1} + z^{-2}}{6 - 2z^{-1}}
$$

6．设 $h_{\mathrm{a}}(t)$ 表示一模拟滤波器的单位冲激响应，即

$$
h_{\mathrm{a}}(t) = \begin{cases}
\mathrm{e}^{-0.9t} & t \geqslant 0 \\
$$
0 & t < 0
\end{cases}
$$

$$
用脉冲响应不变法，将此模拟滤波器转换成数字滤波器(用 $h(n)$ 表示单位脉冲响应，即 $h(n)=h_{\mathrm{a}}(nT)$)。确定系统函数 $H(z)$，并把 $T$ 作为参数，证明：$T$ 为任何值时，数字滤波器是稳定的，并说明数字滤波器近似为低通滤波器还是高通滤波器。

**解：** 模拟滤波器系统函数为

$$
H_{\mathrm{a}}(s) = \int_{0}^{\infty} \mathrm{e}^{-0.9t} \mathrm{e}^{-st} \mathrm{d}t = \frac{1}{s + 0.9}
$$

$H_{\mathrm{a}}(s)$ 的极点 $s_1 = -0.9$，故数字滤波器的系统函数应为

$$
H(z) = \frac{1}{1 - \mathrm{e}^{s_1 T} z^{-1}} = \frac{1}{1 - \mathrm{e}^{-0.9T} z^{-1}}
$$

$H(z)$ 的极点为

$$
z_1 = \mathrm{e}^{-0.9T}, \qquad | z_1 | = \mathrm{e}^{-0.9T}
$$

所以，$T>0$ 时，$| z_1 | < 1$，$H(z)$ 满足因果稳定条件。对 $T=1$ 和 $T=0.5$，画出 $H(\mathrm{e}^{\mathrm{j}\omega})$ 曲线如题 6 解图实线和虚线所示。


**题6解图**：显示了 $T=1$ 和 $T=0.5$ 时，数字滤波器幅度响应 $|H(\mathrm{e}^{\mathrm{j}\omega})|$ 随数字频率 $\omega/\pi$ 变化的曲线。两条曲线都随频率升高而下降，表现为低通特性。实线($T=1$)衰减较慢，虚线($T=0.5$)衰减较快。

由图可见，该数字滤波器近似为低通滤波器。且 $T$ 越小，滤波器频率混叠越小，滤波特性越好(即选择性越好)。反之，$T$ 越大，极点 $z_1 = \mathrm{e}^{s_1 T} = \mathrm{e}^{-0.9T}$ 离单位圆越远，选择性越差，而且频率混叠越严重，$\omega=\pi$ 附近衰减越小，使数字滤波器频响特性不能模拟原模拟滤波器的频响特性。

7．假设某模拟滤波器 $H_{\mathrm{a}}(s)$ 是一个低通滤波器，又知 $H(z)=H_{\mathrm{a}}(s) \big|_{s=\frac{z+1}{z-1}}$，数字滤波器 $H(z)$ 的通带中心位于下面哪种情况？并说明原因。

(1) $\omega=0$(低通)。

(2) $\omega=\pi$(高通)。

(3) 除 $0$ 或 $\pi$ 以外的某一频率(带通)。

**解：方法一** 按题意可写出

故

$$
s = \mathrm{j}\Omega = \frac{z+1}{z-1} \bigg|_{z=\mathrm{e}^{\mathrm{j}\omega}} = \frac{\mathrm{e}^{\mathrm{j}\omega}+1}{\mathrm{e}^{\mathrm{j}\omega}-1} = \mathrm{j} \frac{\cos \frac{\omega}{2}}{\sin \frac{\omega}{2}} = \mathrm{j} \cot \frac{\omega}{2}
$$

即

$$
| \Omega | = \left| \cot \frac{\omega}{2} \right|
$$

原模拟低通滤波器以 $\Omega=0$ 为通带中心，由上式可知，$\Omega=0$ 时，对应于 $\omega=\pi$，故答案为(2)。

**方法二** 找出对应于 $\Omega=0$ 的数字频率 $\omega$ 的对应值即可。

令 $z=1$，对应于 $\mathrm{e}^{\mathrm{j}\omega}=1$，应有 $\omega=0$，则 $H(1)=H_{\mathrm{a}}(s) \big|_{s=\frac{1+1}{1-1}}=H_{\mathrm{a}}(\infty)$ 对应的不是模拟低通中心频率，所以，答案(1)即 $\omega=0$(低通)不对。

令 $z=-1$，对应于 $\mathrm{e}^{\mathrm{j}\omega}=-1$，应有 $\omega=\pi$，则 $H(-1)=H_{\mathrm{a}}(s) \big|_{s=\frac{-1+1}{-1-1}}=H_{\mathrm{a}}(0)$，即将 $\Omega=0$ 映射到 $\omega=\pi$ 处，所以答案为(2)。

**方法三** 直接根据双线性变换法设计公式及模拟滤波器由低通到高通频率变换公式求解。

双线性变换设计公式为

$$
H(z) = H_{\mathrm{a}}(s) \bigg|_{s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}} = \frac{1}{T} \frac{z-1}{z+1}}
$$

当 $T=2$ 时，$H(z)=H_{\mathrm{a}}\left( \frac{z-1}{z+1} \right)$，这时，如果 $H_{\mathrm{a}}(s)$ 为低通，则 $H(z)$ 亦为低通。

如果将 $H_{\mathrm{a}}(s)$ 变换为高通滤波器：

$$
H_{\mathrm{ah}}(s) = H_{\mathrm{a}}\left( \frac{1}{s} \right)
$$

则可将 $H_{\mathrm{ah}}(s)$ 用双线性变换法变成数字高通；

这正是题中所给变换关系，所以数字滤波器 $H_{\mathrm{a}}\left( \frac{z+1}{z-1} \right)$ 通带中心位于 $\omega=\pi$，故答案(2)正确。

8．题 8 图是由 $RC$ 组成的模拟滤波器，写出其系统函数 $H_{\mathrm{a}}(s)$，并选用一种合适的转换方法，将 $H_{\mathrm{a}}(s)$ 转换成数字滤波器 $H(z)$，最后画出网络结构图。


**题8图**：一个由电容 $C$ 和电阻 $R$ 串联构成的模拟高通滤波器电路图，输入为 $x_{\mathrm{a}}(t)$，输出为 $y_{\mathrm{a}}(t)$，电容 $C$ 串联在信号路径上，电阻 $R$ 并联到地。

**解：** 模拟 $RC$ 滤波网络的频率响应函数为

$$
H_{\mathrm{a}}(\mathrm{j}\Omega) = \frac{R}{R + \frac{1}{\mathrm{j}\Omega C}} = \frac{\mathrm{j}\Omega}{\mathrm{j}\Omega + \frac{1}{RC}}
$$

显然，$H_{\mathrm{a}}(\mathrm{j}\Omega)$ 具有高通特性，用脉冲响应不变法必然会产生严重的频率混叠失真。所以应选用双线性变换法。将 $H_{\mathrm{a}}(\mathrm{j}\Omega)$ 中的 $\mathrm{j}\Omega$ 用 $s$ 代替，可得到 $RC$ 滤波网络的系统函数：

$$
H_{\mathrm{a}}(s) = \frac{s}{s + \frac{1}{RC}}
$$

用双线性变换法设计公式，可得

$$
$$
\begin{aligned}
$$
H(z) = H_{\mathrm{a}}(s) \bigg|_{s = \frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}} &= \frac{\frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}}}{\frac{2}{T} \frac{1 - z^{-1}}{1 + z^{-1}} + \frac{1}{RC}} \\
&= \frac{1}{a + 1} \cdot \frac{1 - z^{-1}}{z + \frac{a - 1}{a + 1} z^{-1}} \qquad a = \frac{T}{2RC}
$$
\end{aligned}
$$

$$
$H(z)$ 的结构图如题 8 解图所示。


**题8解图**：实现 $H(z) = \frac{1}{a+1} \cdot \frac{1 - z^{-1}}{1 + \frac{a-1}{a+1} z^{-1}}$ 的直接Ⅱ型网络结构图。输入为 $x(n)$，输出为 $y(n)$。图中包含两个系数为 $\frac{1}{a+1}$ 和 $\frac{1-a}{a+1}$ 的乘法器，一个单位延迟单元 $z^{-1}$，以及加法器。

由图可见，在模拟域由一个 $R$ 和一个 $C$ 组成的 $RC$ 滤波网络，用双线性变换法转换成数字滤波器后，用两个乘法器、两个加法器和一个单位延迟器实现其数字滤波功能。也可用软件实现该数字滤波功能。由滤波器差分方程编写程序较容易。为此，由 $H(z)$ 求出差分方程。

$$
$$
\begin{aligned}
$$
Y(z) = H(z)X(z) &= \frac{1}{a + 1} \cdot \frac{1 - z^{-1}}{1 + \frac{a - 1}{a + 1} z^{-1}} X(z) \\
Y(z)\left(1 + \frac{a - 1}{a + 1} z^{-1}\right) &= \frac{1}{a + 1}(1 - z^{-1})X(z) \\
y(n) + \frac{a - 1}{a + 1} y(n - 1) &= \frac{1}{a + 1}[x(n) - x(n - 1)] \\
y(n) &= \frac{1}{a + 1}[x(n) - x(n - 1) - (a - 1)y(n - 1)]
$$
\end{aligned}
$$

$$
编程序实现差分方程中的计算，即可实现对输入信号序列 $x(n)$ 的高通滤波。

9．设计低通数字滤波器，要求通带内频率低于 $0.2\pi$ rad 时，容许幅度误差在 1 dB 之内；频率在 $0.3\pi$ 到 $\pi$ 之间的阻带衰减大于 10 dB。试采用巴特沃斯型模拟滤波器进行设计，用脉冲响应不变法进行转换，采样间隔 $T=1$ ms。

**解：** 本题要求用巴特沃斯型模拟滤波器设计，所以，由巴特沃斯滤波器的单调下降特性，数字滤波器指标描述如下：

$$
$$
\begin{aligned}
$$
\omega_{\mathrm{p}} &= 0.2\pi \ \mathrm{rad}, \quad \alpha_{\mathrm{p}} = 1 \ \mathrm{dB} \\
\omega_{\mathrm{s}} &= 0.3\pi \ \mathrm{rad}, \quad \alpha_{\mathrm{s}} = 10 \ \mathrm{dB}
$$
\end{aligned}
$$

$$
采用脉冲响应不变法转换，所以，相应的模拟低通巴特沃斯滤波器指标为

$$
\Omega_{\mathrm{p}} = \frac{\omega_{\mathrm{p}}}{T} = 0.2\pi \times 1000 = 200\pi \ \mathrm{rad/s}, \quad \alpha_{\mathrm{p}} = 1 \ \mathrm{dB}
$$

<!-- pages: 22-25 -->

# 第5章 无限脉冲响应(IIR)数字滤波器的设计 - 例题与习题解答

## 9. (续)

$\Omega_s = \frac{\omega_s}{T} = 0.3\pi \times 1000 = 300\pi \text{ rad/s}, \alpha_s = 10 \text{ dB}$

$$
N = -\frac{\lg k_{\text{sp}}}{\lg \lambda_{\text{sp}}}
$$

$$
k_{\text{sp}} = \sqrt{\frac{10^{0.1\alpha_p} - 1}{10^{0.1\alpha_s} - 1}} = \sqrt{\frac{10^{0.1} - 1}{10 - 1}} = 0.1696
$$

$$
\lambda_{\text{sp}} = \frac{\Omega_s}{\Omega_p} = \frac{300\pi}{200\pi} = 1.5
$$

$$
N = -\frac{\lg 0.1696}{\lg 1.5} = 4.376
$$

取 $N=5$。查教材 6.1 节的表 6.2.1（第 157 页），可知模拟滤波器系统函数的归一化低通原型为

$$
G(p) = \frac{1}{\prod_{k=0}^{4} (p - p_k)}
$$

$$
p_0 = -0.3090 + \text{j}0.9511 = p_4^*
$$

$$
p_1 = -0.8090 + \text{j}0.5818 = p_3^*
$$

$$
$$
p_2 = -1
$$

$$
将 $G(p)$ 部分分式展开：

$$
H_a(p) = \sum_{k=0}^{4} \frac{A_k}{p - p_k}
$$

其中，系数为

$$
A_0 = -0.1382 + \text{j}0.4253, \ A_1 = -0.8091 - \text{j}1.1135, \ A_2 = 1.8947
$$

$$
A_3 = -0.8091 + \text{j}1.1135, \ A_4 = -0.1382 - \text{j}0.4253
$$

$$
\Omega_c = \Omega_s(10^{0.1\alpha_s} - 1)^{-\frac{1}{2N}} = 300\pi(10 - 1)^{-\frac{1}{10}} = 756.566 \text{ rad/s}
$$

$$
H_a(s) = G(p) \Big|_{p=\frac{s}{\Omega_c}} = \sum_{k=0}^{4} \frac{\Omega_c A_k}{s - \Omega_c p_k} = \sum_{k=0}^{4} \frac{B_k}{s - s_k}
$$

其中，$B_k = \Omega_c A_k, \ s_k = \Omega_c p_k$。

(3) 用脉冲响应不变法将 $H_a(s)$ 转换成数字滤波器的系统函数 $H(z)$：

$$
H(z) = \sum_{k=0}^{4} \frac{B_k}{1 - e^{s_k T} z^{-1}}, \quad T = 1 \text{ ms} = 10^{-3} \text{ s}
$$

$$
= \sum_{k=0}^{4} \frac{B_k}{1 - e^{10^{-3} s_k} z^{-1}}
$$

我们知道，脉冲响应不变法的主要缺点是存在的频率混叠失真，使设计的滤波器阻带指标变差。另外，由该题的设计过程可见，当 $N$ 较大时，部分分式展开求解系数 $A_k$ 或 $B_k$ 相当困难，所以实际工作中用得很少，主要采用双线性变换法设计，见第 10 题。

---

## 10. 要求同题 9，试采用双线性变换法设计数字低通滤波器。

解：已知条件如下：
数字滤波器指标：
$$
\omega_p = 0.2\pi \text{ rad}, \quad \alpha_p = 1 \text{ dB}
$$
$$
\omega_s = 0.3\pi \text{ rad}, \quad \alpha_s = 10 \text{ dB}
$$

采用双线性变换法，所以要进行预畸变校正，确定相应的模拟滤波器指标（为了计算方便，取 $T=1 \text{ s}$）：

$$
\Omega_p = \frac{2}{T} \tan \frac{\omega_p}{2} = 2 \tan 0.1\pi = 0.649\ 839\ 4 \text{ rad/s}, \quad \alpha_p = 1 \text{ dB}
$$

$$
\Omega_s = \frac{2}{T} \tan \frac{\omega_s}{2} = 2 \tan 0.15\pi = 1.019\ 050\ 9 \text{ rad/s}, \quad \alpha_s = 10 \text{ dB}
$$

(1) 求相应模拟滤波器阶数 $N$：

其中，$k_{\text{sp}}$ 与题 9 相同（因为 $\alpha_p$、$\alpha_s$ 相同），即

$$
k_{\text{sp}} = 0.1696
$$

$$
\lambda_{\text{sp}} = \frac{\Omega_s}{\Omega_p} = \frac{1.019\ 050\ 9}{0.649\ 839\ 4} = 1.5682
$$

$$
N = -\frac{\lg 0.1692}{\lg 1.5682} = 3.9435, \quad \text{取} N = 4
$$

(2) 查教材表 6.2.1，得

$$
G(p) = \frac{1}{s^4 + 2.6131s^3 + 3.4142s^2 + 2.6131s + 1}
$$

(3) 去归一化，求出 $H_a(s)$：

$$
\Omega_c = \Omega_p(10^{0.1\alpha_p} - 1)^{-\frac{1}{2N}} = 0.649\ 839\ 4(10^{0.1} - 1)^{-\frac{1}{8}} = 0.7743 \text{ rad/s}
$$

$$
H_a(s) = G(p) \Big|_{p=\frac{s}{\Omega_c}} = \frac{\Omega_c^4}{s^4 + 2.6131\Omega_c s^3 + 3.4142\Omega_c^2 s^2 + 2.6131\Omega_c^3 s + \Omega_c^4}
$$

$$
= \frac{0.3595}{s^4 + 2.0234s^3 + 2.0470s^2 + 1.2131s + 0.3995}
$$

(4) 用双线性变换法将 $H_a(s)$ 转换成 $H(z)$：

$$
H(z) = H_a(s) \Big|_{s=\frac{2}{T} \frac{1-z^{-1}}{1+z^{-1}}}, \quad T=1
$$

$$
$$
= \Omega_c^4 (1+z^{-1})^4 \Big[ 16(1-z^{-1})^4 + 2.6131\Omega_c (1+z^{-1})(1-z^{-1})^3 \cdot 8 + 3.4142\Omega_c^2 \times 2^2 (1+z^{-1})^2 (1-z^{-1})^4 + 2.6131\Omega_c^3 \times 2 \cdot (1+z^{-1})^3 (1-z^{-1}) + (1+z^{-1})^4 \Omega_c^4 \Big]^{-1}
$$

$$
请读者按 $T=1 \text{ ms}$ 进行设计，比较设计结果。

---

## 11. 设计一个数字高通滤波器，要求通带截止频率 $\omega_p = 0.8\pi \text{ rad}$，通带衰减不大于 $3 \text{ dB}$，阻带截止频率 $\omega_s = 0.5\pi \text{ rad}$，阻带衰减不小于 $18 \text{ dB}$。希望采用巴特沃斯型滤波器。

解：(1) 确定数字高通滤波器技术指标：
$$
\omega_p = 0.8\pi \text{ rad}, \ \alpha_p = 3 \text{ dB}
$$
$$
\omega_s = 0.5\pi \text{ rad}, \ \alpha_s = 18 \text{ dB}
$$

(3) 将高通滤波器指标转换成归一化模拟低通指标。套用图 5.1.5 中高通到低通频率转换公式②，$\lambda_p=1, \ \lambda_s=\Omega_p/\Omega_s$，得到低通归一化边界频率为（本题 $\Omega_p=\Omega_c$）
$$
\lambda_p = 1, \ \alpha_p = 3 \text{ dB}
$$
$$
\lambda_s = \frac{\Omega_p}{\Omega_s} = 3.0777, \ \alpha_s = 18 \text{ dB}
$$

(4) 设计归一化低通 $G(p)$：

$$
k_{\text{sp}} = \sqrt{\frac{10^{0.1\alpha_p} - 1}{10^{0.1\alpha_s} - 1}} = \sqrt{\frac{10^{0.3} - 1}{10^{1.8} - 1}} = 0.1266
$$

$$
\lambda_{\text{sp}} = \frac{\lambda_s}{\lambda_p} = 3.0777
$$

查教材表 6.2.1，得归一化低通 $G(p)$ 为

$$
G(p) = \frac{1}{s^2 + \sqrt{2}s + 1}
$$

(5) 频率变换，求模拟高通 $H_a(s)$：
$$
H_a(s) = G(p) \Big|_{p=\frac{\Omega_c}{s}} = \frac{s^2}{s^2 + \sqrt{2}\Omega_c s + \Omega_c^2} = \frac{s^2}{s^2 + 4.3515s + 9.4679}
$$

(6) 用双线性变换法将 $H_a(s)$ 转换成 $H(z)$：
$$
H(z) = H_a(s) \Big|_{s=\frac{1-z^{-1}}{1+z^{-1}}} = \frac{1 - 2z^{-1} + z^{-2}}{14.8194 + 16.9358z^{-1} + 14.8194z^{-2}}
$$

---

## 12. 设计一个数字带通滤波器，通带范围为 $0.25\pi \text{ rad}$ 到 $0.45\pi \text{ rad}$，通带内最大衰减为 $3 \text{ dB}$，$0.15\pi \text{ rad}$ 以下和 $0.55\pi \text{ rad}$ 以上为阻带，阻带内最小衰减为 $15 \text{ dB}$。要求采用巴特沃斯型模拟低通滤波器。

解：(1) 确定数字带通滤波器技术指标：
$$
\omega_{\text{pl}} = 0.25\pi \text{ rad}, \ \omega_{\text{pu}} = 0.45\pi \text{ rad}
$$
$$
\omega_{\text{sl}} = 0.15\pi \text{ rad}, \ \omega_{\text{su}} = 0.55\pi \text{ rad}
$$
通带内最大衰减 $\alpha_p = 3 \text{ dB}$，阻带内最小衰减 $\alpha_s = 15 \text{ dB}$。

$$
\Omega_{\text{pu}} = \frac{2}{T} \tan \frac{\omega_{\text{pu}}}{2} = \tan 0.225\pi = 0.8541 \text{ rad/s}
$$

$$
\Omega_{\text{pl}} = \frac{2}{T} \tan \frac{\omega_{\text{pl}}}{2} = \tan 0.125\pi = 0.4142 \text{ rad/s}
$$

$$
\Omega_{\text{su}} = \frac{2}{T} \tan \frac{\omega_{\text{su}}}{2} = \tan 0.275\pi = 1.1708 \text{ rad/s}
$$

$$
\Omega_{\text{sl}} = \frac{2}{T} \tan \frac{\omega_{\text{sl}}}{2} = \tan 0.075\pi = 0.2401 \text{ rad/s}
$$

通带中心频率

$$
\Omega_0 = \sqrt{\Omega_{\text{pu}}\Omega_{\text{pl}}} = 0.5948 \text{ rad/s}
$$

通带宽度

$$
B_W = \Omega_{\text{pu}} - \Omega_{\text{pl}} = 0.4399 \text{ rad/s}
$$

$$
\Omega_{\text{pl}}\Omega_{\text{pu}} = 0.8541 \times 0.4142 = 0.3538, \quad \Omega_{\text{sl}}\Omega_{\text{su}} = 0.2401 \times 1.1708 = 0.2811
$$

因为 $\Omega_{\text{pl}}\Omega_{\text{pu}} > \Omega_{\text{sl}}\Omega_{\text{su}}$，所以不满足教材(6.2.56)式。按照教材(6.2.57)式，增大 $\Omega_{\text{sl}}$，则

$$
\hat{\Omega}_{\text{sl}} = \frac{\Omega_{\text{pl}}\Omega_{\text{pu}}}{\Omega_{\text{su}}} = \frac{0.3538}{1.1708} = 0.3022
$$

采用修正后的 $\hat{\Omega}_{\text{sl}}$ 设计巴特沃斯模拟带通滤波器。

(3) 将带通指标转换成归一化低通指标。套用图 5.1.5 中带通到低通频率转换公式③，
$$
\lambda_p = 1, \ \lambda_s = \frac{\Omega_0^2 - \Omega_{\text{sl}}^2}{\Omega_{\text{sl}} B_W}
$$

求归一化低通边界频率：

$$
= \frac{0.3538 - 0.3022^2}{0.3022 \times 0.4399}
$$

$$
$$
= 1.9744
$$

$$
$\alpha_p = 3 \text{ dB}, \quad \alpha_s = 15 \text{ dB}$

(4) 设计模拟归一化低通 $G(p)$：

$$
k_{\text{sp}} = \sqrt{\frac{10^{0.1\alpha_p} - 1}{10^{0.1\alpha_s} - 1}} = \sqrt{\frac{10^{0.3} - 1}{10^{1.5} - 1}} = 0.1803
$$

取 $N=3$。

查教材表 6.2.1，得到归一化低通系统函数 $G(p)$：

$$
G(p) = \frac{1}{p^3 + 2p^2 + 2p + 1}
$$

(5) 频率变换，将 $G(p)$ 转换成模拟带通 $H_a(s)$：

$$
H_a(s) = G(p) \Big|_{p=\frac{s^2+\Omega_0^2}{s B_W}}
$$

$$
= \frac{B_W^3 s^3}{(s^2 + \Omega_0^2)^3 + 2(s^2 + \Omega_0^2)^2 s B_W + 2(s^2 + \Omega_0^2) s^2 B_W^2 + s^3 B_W^3}
$$

<!-- pages: 26-29 -->

$$
= \frac{0.085s^3}{s^6 + 0.8798s^5 + 1.4484s^4 + 0.7076s^3 + 0.5124s^2 + 0.1101s + 0.0443}
$$

（6）用双线性变换公式将 $H_a(s)$ 转换成 $H(z)$：
$$
H(z) = H_a(s) \Big|_{s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}}
$$
$$
= \frac{(0.0181 + 1.7764 \times 10^{-15} z^{-1} - 0.0543 z^{-2} - 4.4409 z^{-3} + 0.0543 z^{-4} - 2.7756 \times 10^{-15} z^{-5} - 0.0181 z^{-6})(1 - 2.272 z^{-1} + 3.5151 z^{-2} - 3.2685 z^{-3} + 2.3129 z^{-4} - 0.9628 z^{-5} + 0.278 z^{-6})^{-1}}
$$

以上繁杂的设计过程和计算，可以用下面几行程序 ex612.m 实现。程序运行结果如题 12 解图所示。得到的系统函数系数为
B = [ 0.0234    0   -0.0703    0    0.0703    0   -0.0234]
A = [1.0000   -2.2100    3.2972   -2.9932    2.0758   -0.8495    0.2406]

与手算结果有差别，这一般是由手算过程中可能产生的计算误差造成的。

```matlab
%程序 ex612.m
wp=[0.25, 0.45]; ws=[0.15, 0.55]; Rp=3; As=15;      %设置带通数字滤波器指标参数
[N, wc]=buttord(wp, ws, Rp, As);                    %计算带通滤波器阶数 N 和 3 dB 截止频率 Wc
[B, A]=butter(N, wc);                                %计算带通滤波器系统函数分子分母多项式系数向量 A 和 B
myplot(B, A);                                        %调用自编绘图函数 myplot 绘制带通滤波器的损耗函数曲线
```


**题12解图**

13*. 设计巴特沃斯数字带通滤波器，要求通带范围为 $0.25\pi \text{ rad} \leqslant \omega \leqslant 0.45\pi \text{ rad}$，通带最大衰减为 3 dB，阻带范围为 $0 \leqslant \omega \leqslant 0.15\pi \text{ rad}$ 和 $0.55\pi \text{ rad} \leqslant \omega \leqslant \pi \text{ rad}$，阻带最小衰减为 40 dB。调用 MATLAB 工具箱函数 buttord 和 butter 设计，并显示数字滤波器系统函数 $H(z)$ 的系数，绘制数字滤波器的损耗函数和相频特性曲线。这种设计对应于脉冲响应不变法还是双线性变换法？

**解：** 调用函数 buttord 和 butter 设计巴特沃斯数字带通滤波器程序 ex613.m 如下：

```matlab
%程序 ex613.m
wp=[0.25, 0.45]; ws=[0.15, 0.55]; rp=3; rs=40;
[N, wc]=buttord(wp, ws, rp, rs);
[B, A]=butter(N, wc)
clf; mpplot(B, A, rs)
```

程序运行结果：
数字滤波器系统函数 H(z) 的系数：
B=[ 0.0001       0   -0.0007       0    0.0022       0   -0.0036       0    0.0035       0   -0.0022
       0    0.0007       0   -0.0001]
A =[ 1.0000   -5.3093   16.2913   -34.7297   56.9399   -74.5122   80.0136   -71.1170   52.6408   -32.2270   16.1696    -6.4618     1.9831    -0.4218    0.0524]

函数 buttord 和 butter 是采用双线性变换法来设计巴特沃斯数字滤波器的。
数字滤波器的损耗函数和相频特性曲线如题 13* 解图所示。


**题13*解图**

14*. 设计一个工作于采样频率 80 kHz 的巴特沃斯低通数字滤波器，要求通带边界频率为 4 kHz，通带最大衰减为 0.5 dB，阻带边界频率为 20 kHz，阻带最小衰减为 45 dB。调用 MATLAB 工具箱函数 buttord 和 butter 设计，并显示数字滤波器系统函数 $H(z)$ 的系数，绘制损耗函数和相频特性曲线。


**题14*解图**

**解：** 本题以模拟频率给定滤波器指标，所以，程序中先要计算出对应的数字边界频率，然后调用 MATLAB 工具箱函数 buttord 和 butter 来设计数字滤波器。设计程序为 ex614.m。

```matlab
%程序 ex614.m
Fs=80000; T=1/Fs;
wp=2*pi*4000/Fs; ws=2*pi*20000/Fs; rp=0.5; rs=45;
[N, wc]=buttord(wp/pi, ws/pi, rp, rs);
[B, A]=butter(N, wc);
clf; mpplot(B, A, rs);    %调用本书绘图函数 mpplot 绘图
```

程序运行结果：
阶数 N=4，数字滤波器系统函数 H(z) 的系数：
B=[ 0.0028   0.0111   0.0166   0.0111   0.0028]
A=[ 1.0000  -2.6103   2.7188  -1.3066   0.2425]

数字滤波器的损耗函数和相频特性曲线如题 14* 解图所示。由图可见，滤波器通带截止频率大于 $0.1\pi$（对应的模拟频率分别为 4 kHz），阻带截止频率为 $0.5\pi$（对应的模拟频率分别为 20 kHz），完全满足设计要求。

15*. 设计一个工作于采样频率 80 kHz 的切比雪夫Ⅰ型低通数字滤波器，滤波器指标要求与题 14* 相同。调用 MATLAB 工具箱函数 cheblord 和 cheby1 设计，并显示数字滤波器系统函数 $H(z)$ 的系数，绘制损耗函数和相频特性曲线。与题 14* 的设计结果比较，简述巴特沃斯滤波器和切比雪夫Ⅰ型滤波器的特点。

**解：** 本题除了调用的 MATLAB 工具箱函数 cheblord 和 cheby1 与题 14* 不同以外，程序与 14* 题完全相同。本题求解程序 ex615.m 如下：

```matlab
% 程序 ex615.m
Fs=80000; T=1/Fs;
wp=2*pi*4000/Fs; ws=2*pi*20000/Fs; rp=0.5; rs=45; %数字滤波器指标
[N, wp]=cheblord(wp/pi, ws/pi, rp, rs);
[B, A]=cheby1(N, rp, wp);
clf; mpplot(B, A, rs); %调用本书绘图函数 mpplot 绘图
```

程序运行结果：
阶数 N=3，比题 14* 设计的巴特沃斯滤波器低 1 阶。
数字滤波器系统函数 H(z) 的系数：
B=[0.0023   0.0069   0.0069   0.0023]
A=[1.0000  -2.5419   2.2355  -0.6753]

数字滤波器的损耗函数和相频特性曲线如题 15* 解图所示。由图可见，完全满足设计要求。巴特沃斯滤波器和切比雪夫Ⅰ型滤波器的特点见教材第 179 页。


**题15*解图**

16*. 设计一个工作于采样频率 2500 kHz 的椭圆高通数字滤波器，要求通带边界频率为 325 kHz，通带最大衰减为 1 dB，阻带边界频率为 225 kHz，阻带最小衰减为 40 dB。调用 MATLAB 工具箱函数 ellipord 和 ellip 设计，并显示数字滤波器系统函数 $H(z)$ 的系数，绘制损耗函数和相频特性曲线。

**解：** 本题求解程序 ex616.m 如下：

```matlab
% 程序 ex616.m
Fs=2500000; fp=325000; rp=1; fs=225000; rs=40;          %滤波器指标
wp=2*fp/Fs; ws=2*fs/Fs;                                   %将边界频率转换为数字频率
[N, wpo]=ellipord(wp, ws, rp, rs);
[B, A]=ellip(N, rp, rs, wpo, 'high');
clf; mpplot(B, A, rs); %调用本书绘图函数 mpplot 绘图
```

程序运行结果：
阶数 N=5，数字滤波器系统函数 H(z) 的系数：
B=[0.2784   -1.2102    2.2656   -2.2656    1.2102   -0.2784]
A=[1.0000   -2.1041    2.5264   -1.4351    0.4757    0.0329]

数字滤波器的损耗函数和相频特性曲线如题 16* 解图所示。由图可见，完全满足设计要求。


**题16*解图**

17*. 设计一个工作于采样频率 5 MHz 的椭圆带通数字滤波器，要求通带边界频率为 560 kHz 和 780 kHz，通带最大衰减为 0.5 dB，阻带边界频率为 375 kHz 和 1 MHz，阻带最小衰减为 50 dB。调用 MATLAB 工具箱函数 ellipord 和 ellip 设计，并显示数字滤波器系统函数 $H(z)$ 的系数，绘制损耗函数和相频特性曲线。

**解：** 本题求解程序 ex617.m 如下：

```matlab
% 程序 ex617.m
fpl=560000; fpu=780000; fsl=375000; fsu=1000000; Fs=5000000; %滤波器指标
wp=[2*fpl/Fs, 2*fpu/Fs]; ws=[2*fsl/Fs, 2*fsu/Fs];
rp=0.5; rs=50;                                               %将边界频率转换为数字频率
[N, wpo]=ellipord(wp, ws, rp, rs);
[B, A]=ellip(N, rp, rs, wpo);
clf; mpplot(B, A, rs); %调用本书绘图函数 mpplot 绘图

<!-- pages: 30-32 -->

**第5章 无限脉冲响应(IIR)数字滤波器的设计 - 例题与习题解答**

程序运行结果：
阶数 N=4，2N阶数字带通滤波器系统函数 H(z) 的系数：
B = [0.0043   -0.0184   0.0415   -0.0638   0.0734   -0.0638   0.0415   -0.0184   0.0043]
A = [1.0000   -5.1091   13.4242   -22.3290   25.6190   -20.5716   11.3936   -3.9943   0.7205]
数字滤波器的损耗函数和相频特性曲线如题 17* 解图所示。由图可见，完全满足设计要求。


**题 17* 解图**
(a) 损耗函数曲线
(b) 相频特性曲线

18*. 设计一个工作于采样频率 5 kHz 的椭圆带阻数字滤波器，要求通带边界频率为 500 Hz 和 2125 Hz，通带最大衰减为 1 dB，阻带边界频率为 1050 kHz 和 1400 Hz，阻带最小衰减为 40 dB。调用 MATLAB 工具箱函数 ellipord 和 ellip 设计，并显示数字滤波器系统函数 $H(z)$ 的系数，绘制损耗函数和相频特性曲线。


**题 18* 解图**
(a) 损耗函数曲线
(b) 相频特性曲线

解：本题求解程序 ex618.m 如下：
```matlab
% 程序 ex618.m
fpl=500; fpu=2125; fsl=1050; fsu=1400; Fs=5000; rp=1; rs=40; %滤波器指标
wp=[2*fpl/Fs, 2*fpu/Fs]; ws=[2*fsl/Fs, 2*fsu/Fs]; %将边界频率转换为数字频率
[N, wpo]=ellipord(wp, ws, rp, rs)
[B, A]=ellip(N, rp, rs, wpo, 'stop')
clf; mpplot(B, A, rs); %调用本书绘图函数 mpplot 绘图
```

程序运行结果：
阶数 N=3，2N阶数字带阻滤波器系统函数 H(z) 的系数：
B = [0.0748   0.0557   0.1618   0.0897   0.1618   0.0557   0.0748]
A = [1.0000   0.2604   -1.2316   -0.0633   1.0458   0.0040   -0.3412]
数字滤波器的损耗函数和相频特性曲线如题 18* 解图所示。

19*. 用脉冲响应不变法设计一个巴特沃斯低通数字滤波器，指标要求与题 14* 的相同。编写程序先调用 MATLAB 工具箱函数 buttord 和 butter 设计过渡模拟低通滤波器，再调用脉冲响应不变法设计函数 impinvar，将过渡模拟低通滤波器转换成低通数字滤波器 $H(z)$，并显示过渡模拟低通滤波器和数字滤波器系统函数的系数，绘制损耗函数和相频特性曲线。请归纳本题的设计步骤和所用的计算公式，并比较本题与题 14* 的设计结果，观察双线性变换法的频率非线性失真和脉冲响应不变法的频谱混叠失真。

解：本题求解程序 ex619.m 如下：
```matlab
% 程序 ex619.m
Fs=80000; T=1/Fs;
fp=4000; fs=20000; rp=0.5; rs=45; %相应的模拟滤波器指标
wp=2*pi*fp; ws=2*pi*fs; %将边界频率转换为角频率
[N, wc]=buttord(wp, ws, rp, rs, 's');
[B, A]=butter(N, wc, 's');
[Bz, Az]=impinvar(B, A, Fs) %调用转换函数 impinvar 将 AF 转换成 DF
%以下计算 AF 和 DF 的频响特性
fk=0:10:Fs/2; omega=2*pi*fk; %对 AF 频响函数在[0, Fs/2]上以间隔 10 Hz 采样
Hs=freqs(B, A, omega);
ms=abs(Hs); ps=angle(Hs);
[H, W]=freqz(Bz, Az, 1000); %对 DF 频响函数在[0, Fs/2]采样 1000 点
m=abs(H); p=angle(H);
msmin=20*log10(ms(end)/max(ms)) %AF 在 f=Fs/2 点的衰减
mmin=20*log10(m(end)/max(m)) %DF 在 ω=π 点的衰减
%以下绘制 AF 和 DF 的损耗函数和相频特性曲线(省略)
```
程序运行结果：
阶数 N=4，N阶数字低通滤波器系统函数 H(z) 的系数：
Bz = [-0.0000   0.0043   0.0128   0.0024   0]
Az = [1.0000   -2.8902   3.2452   -1.6605   0.3250]
模拟滤波器的损耗函数和相频特性曲线如题 19* 解图(a)和(b)所示，数字滤波器的损耗函数和相频特性曲线如题 19* 解图(c)和(d)所示。由图可见，脉冲响应不变法设计的数字滤波器的频响特性基本模拟了模拟滤波器的频响形状，但存在频谱混叠失真。模拟滤波器的损耗函数在 f=Fs/2 点的衰减为 msmin = -69.0823 dB，而数字滤波器的损耗函数在 $\omega = \pi$ 点的衰减为 mmin = -63.4990 dB，这就是频谱混叠失真引起了 -5.5832 dB 的衰减误差。题 14* 是用双线性变换法设计的，不存在频谱混叠失真，但存在频率非线性失真，所以数字滤波器的频响曲线形状与模拟滤波器的频响形状差别较大，而且，频率越高，频率非线性失真越严重。
本题的设计步骤和所用的计算公式请读者在教材 6.3 节查找。


**题 19* 解图**
(a) AF损耗函数曲线
(b) AF相频特性曲线
(c) DF损耗函数曲线
(d) DF相频特性曲线