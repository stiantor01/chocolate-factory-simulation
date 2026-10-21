# Transformation Matrices - chocolate_robot

Homogeneous transformation matrices between consecutive frames.
Convention: URDF RPY (XYZ extrinsic / ZYX intrinsic).

## Notation

### Frames

| Index | Link |
|-------|------|
| $L_{0}$ | base_link |
| $L_{1}$ | link_1 |
| $L_{2}$ | link_2 |
| $L_{3}$ | link_3 |
| $L_{4}$ | link_4 |
| $L_{5}$ | link_5_suctioncup |

### Joint Variables

| Variable | Joint | Type | From | To |
|----------|-------|------|------|----|
| $q_{1}$ | joint_1 | continuous (rad) | $L_{0}$ | $L_{1}$ |
| $q_{2}$ | joint_2 | continuous (rad) | $L_{1}$ | $L_{2}$ |
| $q_{3}$ | joint_3 | continuous (rad) | $L_{2}$ | $L_{3}$ |
| $q_{4}$ | joint_4 | continuous (rad) | $L_{3}$ | $L_{4}$ |
| $q_{5}$ | joint_5 | continuous (rad) | $L_{4}$ | $L_{5}$ |

Shorthand: $c_i = \cos(q_i)$, $s_i = \sin(q_i)$

### Kinematic Tree

```
L0: base_link
  +-- [continuous] joint_1 (q1)
      L1: link_1
        +-- [continuous] joint_2 (q2)
            L2: link_2
              +-- [continuous] joint_3 (q3)
                  L3: link_3
                    +-- [continuous] joint_4 (q4)
                        L4: link_4
                          +-- [continuous] joint_5 (q5)
                              L5: link_5_suctioncup
```

## Transforms

## joint_1

$L_{0}$ **base_link** -> $L_{1}$ **link_1** (continuous)
  Variable: $q_{1}$

- **origin xyz**: (0, 0, 0.06726) m
- **origin rpy**: (-3.141593, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{0}_{1}(q_{1}) = T_{fixed} \cdot R_{axis}(q_{1})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0.06726 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{1}) = \begin{bmatrix}
c_{1} & -s_{1} & 0 & 0 \\
s_{1} & c_{1} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## joint_2

$L_{1}$ **link_1** -> $L_{2}$ **link_2** (continuous)
  Variable: $q_{2}$

- **origin xyz**: (0, 0.101002, -0.204715) m
- **origin rpy**: (1.570796, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{1}_{2}(q_{2}) = T_{fixed} \cdot R_{axis}(q_{2})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & -1 & 0.101002 \\
0 & 1 & 0 & -0.204715 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{2}) = \begin{bmatrix}
c_{2} & -s_{2} & 0 & 0 \\
s_{2} & c_{2} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## joint_3

$L_{2}$ **link_2** -> $L_{3}$ **link_3** (continuous)
  Variable: $q_{3}$

- **origin xyz**: (0.515241, -0.432339, -0.000308) m
- **origin rpy**: (-3.141593, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{2}_{3}(q_{3}) = T_{fixed} \cdot R_{axis}(q_{3})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0.515241 \\
0 & -1 & 0 & -0.432339 \\
0 & 0 & -1 & -0.000308 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{3}) = \begin{bmatrix}
c_{3} & -s_{3} & 0 & 0 \\
s_{3} & c_{3} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## joint_4

$L_{3}$ **link_3** -> $L_{4}$ **link_4** (continuous)
  Variable: $q_{4}$

- **origin xyz**: (0.515241, 0.432339, 0.000012) m
- **origin rpy**: (-3.141593, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{3}_{4}(q_{4}) = T_{fixed} \cdot R_{axis}(q_{4})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0.515241 \\
0 & -1 & 0 & 0.432339 \\
0 & 0 & -1 & 0.000012 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{4}) = \begin{bmatrix}
c_{4} & -s_{4} & 0 & 0 \\
s_{4} & c_{4} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## joint_5

$L_{4}$ **link_4** -> $L_{5}$ **link_5_suctioncup** (continuous)
  Variable: $q_{5}$

- **origin xyz**: (0, 0.116157, -0.050557) m
- **origin rpy**: (-1.570796, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{4}_{5}(q_{5}) = T_{fixed} \cdot R_{axis}(q_{5})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0.116157 \\
0 & -1 & 0 & -0.050557 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{5}) = \begin{bmatrix}
c_{5} & -s_{5} & 0 & 0 \\
s_{5} & c_{5} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Global Transform Chains

Transform from root $L_0$ to any link, as product of local transforms along the kinematic chain.

$$T^{0}_{2} = T^{0}_{1}(q_{1}) \cdot T^{1}_{2}(q_{2})\quad (L_0 \to L_{2}: \text{link_2})$$

$$T^{0}_{3} = T^{0}_{1}(q_{1}) \cdot T^{1}_{2}(q_{2}) \cdot T^{2}_{3}(q_{3})\quad (L_0 \to L_{3}: \text{link_3})$$

$$T^{0}_{4} = T^{0}_{1}(q_{1}) \cdot T^{1}_{2}(q_{2}) \cdot T^{2}_{3}(q_{3}) \cdot T^{3}_{4}(q_{4})\quad (L_0 \to L_{4}: \text{link_4})$$

$$T^{0}_{5} = T^{0}_{1}(q_{1}) \cdot T^{1}_{2}(q_{2}) \cdot T^{2}_{3}(q_{3}) \cdot T^{3}_{4}(q_{4}) \cdot T^{4}_{5}(q_{5})\quad (L_0 \to L_{5}: \text{link_5_suctioncup})$$

