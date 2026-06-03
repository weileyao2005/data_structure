# 答疑：拉普拉斯 $\nabla^2 u$ 在直角坐标系中是怎么算出来的？

> **问题**：1.6.4 节给出了 $\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}$，这个结果怎么一步步推导的？

---

## 总思路

$\nabla^2 u = \nabla \cdot (\nabla u)$，就是**两步走**：

```
第1步：对标量 u 求梯度 → 得到一个矢量场 ∇u
第2步：对这个矢量场求散度 → 得到一个标量 ∇²u
```

---

## 第1步：写出 $\nabla u$

由 1.3 节公式 (1.3.9)，直角坐标系中梯度为：

$$\nabla u = \mathbf{e}_x\frac{\partial u}{\partial x} + \mathbf{e}_y\frac{\partial u}{\partial y} + \mathbf{e}_z\frac{\partial u}{\partial z}$$

这是一个**矢量场**，我们把它记作 $\mathbf{G}$：

$$\mathbf{G} = \nabla u = \mathbf{e}_x G_x + \mathbf{e}_y G_y + \mathbf{e}_z G_z$$

其中三个分量分别是：

$$G_x = \frac{\partial u}{\partial x}, \qquad G_y = \frac{\partial u}{\partial y}, \qquad G_z = \frac{\partial u}{\partial z}$$

---

## 第2步：对 $\mathbf{G}$ 求散度

由 1.4 节公式 (1.4.12)，直角坐标系中散度为：

$$\nabla \cdot \mathbf{G} = \frac{\partial G_x}{\partial x} + \frac{\partial G_y}{\partial y} + \frac{\partial G_z}{\partial z}$$

把第1步的 $G_x, G_y, G_z$ 代入：

$$\begin{aligned}
\nabla \cdot (\nabla u) &= \frac{\partial}{\partial x}\!\left(\frac{\partial u}{\partial x}\right) + \frac{\partial}{\partial y}\!\left(\frac{\partial u}{\partial y}\right) + \frac{\partial}{\partial z}\!\left(\frac{\partial u}{\partial z}\right) \\[6pt]
&= \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}
\end{aligned}$$

**写在一起就得到了**：

$$\boxed{\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}}$$

---

## 换个写法：直接用 $\nabla$ 算符"点乘"自己

把 $\nabla = \mathbf{e}_x\frac{\partial}{\partial x} + \mathbf{e}_y\frac{\partial}{\partial y} + \mathbf{e}_z\frac{\partial}{\partial z}$ 和自己做**形式的点乘**：

$$\begin{aligned}
\nabla \cdot \nabla &= \left(\mathbf{e}_x\frac{\partial}{\partial x} + \mathbf{e}_y\frac{\partial}{\partial y} + \mathbf{e}_z\frac{\partial}{\partial z}\right) \cdot \left(\mathbf{e}_x\frac{\partial}{\partial x} + \mathbf{e}_y\frac{\partial}{\partial y} + \mathbf{e}_z\frac{\partial}{\partial z}\right)
\end{aligned}$$

展开这个"点乘"（注意：$\mathbf{e}_x \cdot \mathbf{e}_x = 1$，$\mathbf{e}_x \cdot \mathbf{e}_y = 0$，交叉项全为零）：

$$= \frac{\partial}{\partial x}\frac{\partial}{\partial x} + \frac{\partial}{\partial y}\frac{\partial}{\partial y} + \frac{\partial}{\partial z}\frac{\partial}{\partial z} = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

这就是为什么 $\nabla^2$ 也叫"拉普拉斯算符"——它就是 $\nabla \cdot \nabla$。

---

## 注意：$\nabla^2 u$ 是一个标量，没有"x分量"

容易混淆的一点：$\nabla^2 u$ 作用在标量 $u$ 上，结果是**一个标量**，不是矢量。所以不存在"$\nabla^2 u$ 的 x 分量"这种说法——它本身就是一个数。

你说"x分量"可能想到的是后面 1.7 节中**矢量拉普拉斯**的情况：

$$(\nabla^2 \mathbf{A})_x = \nabla^2 A_x$$

这时候才是对一个矢量的每个直角分量分别做标量拉普拉斯运算。但那是 1.7 节的内容——而且**只在直角坐标系中成立**！
