# 答疑：$\nabla(\nabla\cdot\mathbf{A})$、$\nabla^2\mathbf{A}$、$\nabla\times(\nabla\times\mathbf{A})$ 分别是什么意思？

> **问题来源**：1.7.4 节出现了矢量三重积恒等式
> $$\nabla \times (\nabla \times \mathbf{A}) = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}$$
> 然后反过来用这个式子**定义**了矢量拉普拉斯：
> $$\nabla^2 \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla \times (\nabla \times \mathbf{A})$$
> 两个 $\nabla$ 叠在一起的这几种写法，各自到底在执行什么计算？$\nabla^2\mathbf{A}$ 和标量拉普拉斯 $\nabla^2 u$ 是一回事吗？

---

## 一、先确认你已经会的：标量拉普拉斯 $\nabla^2 u$

对标量 $u$，定义非常干净：

$$\nabla^2 u = \nabla \cdot (\nabla u)$$

**操作顺序**：先求梯度（得矢量）→ 再求散度（得标量）。在直角坐标中展开就是三个二阶偏导之和：

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}$$

---

## 二、对矢量场，两个 nabla 有三种不同的组合

| 符号 | 读作 | 操作顺序 | 结果 |
|------|------|----------|:---:|
| $\nabla(\nabla \cdot \mathbf{A})$ | 散度的梯度 | ① $\mathbf{A}$ 求散度 → 标量 ② 对标量求梯度 → 矢量 | 矢量 |
| $\nabla \times (\nabla \times \mathbf{A})$ | 旋度的旋度 | ① $\mathbf{A}$ 求旋度 → 矢量 ② 对矢量求旋度 → 矢量 | 矢量 |
| $\nabla^2 \mathbf{A}$ | 矢量拉普拉斯 | 由式 (1.7.8) **定义** | 矢量 |

三种操作都从矢量场 $\mathbf{A}$ 出发，最终得到一个矢量场，但中间过程完全不同。

---

## 三、逐个拆开

### 3.1 $\nabla(\nabla \cdot \mathbf{A})$ —— 先散度，后梯度

**第一步**：对 $\mathbf{A}$ 求散度，得到一个标量函数：

$$f = \nabla \cdot \mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$

**第二步**：对这个标量函数求梯度：

$$\nabla f = \mathbf{e}_x\frac{\partial f}{\partial x} + \mathbf{e}_y\frac{\partial f}{\partial y} + \mathbf{e}_z\frac{\partial f}{\partial z}$$

合在一起，三个分量分别是：

$$\begin{aligned}
[\nabla(\nabla \cdot \mathbf{A})]_x &= \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_y}{\partial x\partial y} + \frac{\partial^2 A_z}{\partial x\partial z} \\[4pt]
[\nabla(\nabla \cdot \mathbf{A})]_y &= \frac{\partial^2 A_x}{\partial y\partial x} + \frac{\partial^2 A_y}{\partial y^2} + \frac{\partial^2 A_z}{\partial y\partial z} \\[4pt]
[\nabla(\nabla \cdot \mathbf{A})]_z &= \frac{\partial^2 A_x}{\partial z\partial x} + \frac{\partial^2 A_y}{\partial z\partial y} + \frac{\partial^2 A_z}{\partial z^2}
\end{aligned}$$

> **注意到没有？** 每个分量的结果里不但有自己分量的二阶导，还混进了其他两个分量的交叉导数。例如 $x$ 分量里出现了 $\partial^2 A_y/\partial x\partial y$ 和 $\partial^2 A_z/\partial x\partial z$。**三个分量被"搅在一起"了。**

---

### 3.2 $\nabla \times (\nabla \times \mathbf{A})$ —— 先旋度，后旋度

先算第一层旋度 $\mathbf{B} = \nabla \times \mathbf{A}$：

$$\mathbf{B} = \mathbf{e}_x\!\left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right) + \mathbf{e}_y\!\left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right) + \mathbf{e}_z\!\left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)$$

再算第二层旋度 $\nabla \times \mathbf{B}$，以 $x$ 分量为例：

$$\begin{aligned}
[\nabla \times (\nabla \times \mathbf{A})]_x &= \frac{\partial B_z}{\partial y} - \frac{\partial B_y}{\partial z} \\[4pt]
&= \frac{\partial}{\partial y}\!\left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right) - \frac{\partial}{\partial z}\!\left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right) \\[4pt]
&= \frac{\partial^2 A_y}{\partial y\partial x} - \frac{\partial^2 A_x}{\partial y^2} - \frac{\partial^2 A_x}{\partial z^2} + \frac{\partial^2 A_z}{\partial z\partial x}
\end{aligned}$$

> **同样**：每个分量里都有其他分量的交叉导数项。

---

### 3.3 $\nabla^2 \mathbf{A}$ —— 矢量拉普拉斯（关键！）

对标量，$\nabla^2 u = \nabla \cdot (\nabla u)$ 是自然定义。但对矢量，**不能**直接写成 $\nabla \cdot (\nabla\mathbf{A})$（因为矢量的梯度是并矢/张量，不是普通矢量）。

矢量拉普拉斯的**定义**来自矢量三重积恒等式：

回忆 1.1 节中普通矢量的三重矢积公式：

$$\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = \mathbf{b}(\mathbf{a} \cdot \mathbf{c}) - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$$

把 $\mathbf{a}$ 和 $\mathbf{b}$ 替换为 $\nabla$，$\mathbf{c}$ 替换为 $\mathbf{A}$，形式上得到：

$$\nabla \times (\nabla \times \mathbf{A}) = \nabla(\nabla \cdot \mathbf{A}) - (\nabla \cdot \nabla)\mathbf{A}$$

其中 $\nabla \cdot \nabla = \nabla^2$（标量拉普拉斯算符）。移项就得到**矢量拉普拉斯的定义**：

$$\boxed{\nabla^2 \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla \times (\nabla \times \mathbf{A})} \tag{1.7.8}$$

**用语言说就是**：矢量拉普拉斯 = 散度的梯度 减去 旋度的旋度。

---

## 四、直角坐标系中验证：交叉项为何恰好消掉

用上面 3.1 和 3.2 的结果代入定义 (1.7.8)，只验证 $x$ 分量：

**由 3.1 —— 散度的梯度的 $x$ 分量**：

$$[\nabla(\nabla \cdot \mathbf{A})]_x = \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_y}{\partial x\partial y} + \frac{\partial^2 A_z}{\partial x\partial z}$$

**由 3.2 —— 旋度的旋度的 $x$ 分量**：

$$[\nabla \times (\nabla \times \mathbf{A})]_x = \frac{\partial^2 A_y}{\partial y\partial x} - \frac{\partial^2 A_x}{\partial y^2} - \frac{\partial^2 A_x}{\partial z^2} + \frac{\partial^2 A_z}{\partial z\partial x}$$

**两式相减**（假定混合偏导可交换次序，即 $\frac{\partial^2 A_y}{\partial x\partial y} = \frac{\partial^2 A_y}{\partial y\partial x}$，$\frac{\partial^2 A_z}{\partial x\partial z} = \frac{\partial^2 A_z}{\partial z\partial x}$）：

$$\begin{aligned}
(\nabla^2 \mathbf{A})_x &= [\nabla(\nabla \cdot \mathbf{A})]_x - [\nabla \times (\nabla \times \mathbf{A})]_x \\[4pt]
&= \left[\frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_y}{\partial x\partial y} + \frac{\partial^2 A_z}{\partial x\partial z}\right]
   - \left[\frac{\partial^2 A_y}{\partial y\partial x} - \frac{\partial^2 A_x}{\partial y^2} - \frac{\partial^2 A_x}{\partial z^2} + \frac{\partial^2 A_z}{\partial z\partial x}\right] \\[6pt]
&= \frac{\partial^2 A_x}{\partial x^2} + \cancel{\frac{\partial^2 A_y}{\partial x\partial y}} + \cancel{\frac{\partial^2 A_z}{\partial x\partial z}}
   - \cancel{\frac{\partial^2 A_y}{\partial x\partial y}} + \frac{\partial^2 A_x}{\partial y^2} + \frac{\partial^2 A_x}{\partial z^2} - \cancel{\frac{\partial^2 A_z}{\partial x\partial z}} \\[6pt]
&= \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_x}{\partial y^2} + \frac{\partial^2 A_x}{\partial z^2} \\[6pt]
&= \nabla^2 A_x
\end{aligned}$$

**所有四个交叉导数项（来自 $A_y$ 和 $A_z$ 的）恰好全部消掉！** 最终只剩下 $A_x$ 自己的三个二阶偏导之和。$y$ 分量和 $z$ 分量的过程完全对称，结论一致。于是在直角坐标系中：

$$\nabla^2 \mathbf{A} = \mathbf{e}_x \nabla^2 A_x + \mathbf{e}_y \nabla^2 A_y + \mathbf{e}_z \nabla^2 A_z \quad \text{（仅直角坐标成立！）}$$

> **关键认识**：直角坐标中 $\nabla^2 \mathbf{A}$ 可以简单地"对每个分量分别做标量拉普拉斯"——这不是定义如此，而是 $\nabla(\nabla\cdot\mathbf{A})$ 和 $\nabla\times(\nabla\times\mathbf{A})$ 中的交叉导数项恰好互相抵消的结果。在圆柱坐标和球坐标中，因为单位矢量随位置变化，交叉项无法消掉，所以 $(\nabla^2\mathbf{A})_\rho \neq \nabla^2 A_\rho$ 等等。

---

## 五、一句话总结

| 运算 | 含义 |
|------|------|
| $\nabla(\nabla\cdot\mathbf{A})$ | 先求散度得标量，再求梯度得矢量。每个分量里包含其他分量的交叉导数。 |
| $\nabla\times(\nabla\times\mathbf{A})$ | 先求旋度，再求旋度。同样包含交叉导数。 |
| $\nabla^2\mathbf{A}$ | 定义为上面两者之差。**交叉导数项恰好全部消掉**，只剩每个分量自己的三个二阶偏导之和。 |

**记住这个图像**：

```
散度的梯度 ∇(∇·A)  ─┐
                      ├── 两者相减 = ∇²A（交叉项全部消掉）
旋度的旋度 ∇×(∇×A) ─┘
```
