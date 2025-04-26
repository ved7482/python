# Understanding `divmod()` in Python

The `divmod(dividend, divisor)` function returns a **tuple** containing the **quotient** and the **remainder** when the first argument (dividend) is divided by the second (divisor).

---

## Syntax

```python
 divmod(x, y)
```

- **x**: a non-complex number (*numerator* or *dividend*)
- **y**: a non-complex number (*denominator* or *divisor*)

**Returns:** A tuple *(q, r)* consisting of:
- **q**: Quotient
- **r**: Remainder

> **Note:**
> - If **x** and **y** are integers, the return is the same as `(x // y, x % y)`.
> - If either **x** or **y** is a float, the result is `(q, x % y)` where **q** is the whole part of the quotient.

---

## ✨ Examples

| Statement | Result |
|:---|:---|
| `print(divmod(8, 3))` | **(2, 2)** |
| `print(divmod(3, 8))` | **(0, 3)** |
| `print(divmod(5, 5))` | **(1, 0)** |
| `print(divmod(0, 9))` | **(0, 0)** |
| `print(divmod(3, 0))` | **ZeroDivisionError: integer division or modulo by zero** |
| `print(divmod(8.0, 3))` | **(2.0, 2.0)** |
| `print(divmod(3, 8.0))` | **(0.0, 3.0)** |
| `print(divmod(7.5, 2.5))` | **(3.0, 0.0)** |
| `print(divmod(2.6, 0.5))` | **(5.0, 0.10000000000000009)** |
| `print(divmod(2.6, 0))` | **ZeroDivisionError: float divmod()** |
| `print(divmod(0.0, 8.0))` | **(0.0, 0.0)** |

---

## ☑️ Important Points

> 📌 **Zero Division**
> - If the second argument is `0`, a **ZeroDivisionError** is raised.

> 📌 **Zero Dividend**
> - If the first argument is `0`, the result is always **(0, 0)**.

> 📌 **Integer and Float Behavior**
> - For integers: `divmod(x, y)` = `(x // y, x % y)`
> - For floats: `divmod(x, y)` returns a float quotient and modulus.

---

## 📅 Summary Box

> **`divmod()` Function**
> - **Inputs:** Two non-complex numbers.
> - **Output:** Tuple (**quotient, remainder**).
> - **Errors:** Raises **ZeroDivisionError** if divisor is zero.
> - **Handles both:** Integer and Float division gracefully.

---