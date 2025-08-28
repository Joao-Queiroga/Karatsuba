# 🚀 Algoritmo de Karatsuba em Python

## 📖 Descrição do projeto
Este projeto implementa o **algoritmo de Karatsuba**, uma técnica de multiplicação eficiente para números inteiros grandes, criada por Anatolii Karatsuba em 1960.
O algoritmo reduz o número de multiplicações necessárias ao utilizar a estratégia de **divisão e conquista**, alcançando uma complexidade de tempo `O(n^log₂3) ≈ O(n^1.585)`, melhor que a multiplicação tradicional `O(n²)`.

---

## 🔎 Lógica do algoritmo
1. **Caso base:** se algum número tiver apenas 1 dígito, multiplica diretamente.
2. **Divisão:** os números são separados ao meio:
   - `x = a * 10^m + b`
   - `y = c * 10^m + d`
3. **Três multiplicações recursivas:**
   - `p1 = a * c`
   - `p2 = b * d`
   - `p3 = (a + b) * (c + d)`
4. **Combinação dos resultados:**
resultado = p1 * 10^(2*m) + (p3 - p1 - p2) * 10^m + p2

---

## 🧩 Implementação (linha a linha)
Arquivo: `main.py`

- `def dividir_numero(n, m)`:
Divide o número em duas partes de acordo com `m`. Se o número tiver menos dígitos, a parte alta vira `0`.

- `def karatsuba(x, y)`:
- Caso base: retorna `x * y` se `abs(x) < 10 or abs(y) < 10`.
- Calcula `m`, o tamanho da metade, a partir do maior número.
- Divide os números em `a, b` e `c, d`.
- Calcula recursivamente:
 - `p1 = karatsuba(a, c)`
 - `p2 = karatsuba(b, d)`
 - `p3 = karatsuba(a+b, c+d)`
- Combina os resultados com deslocamento por potências de 10.

---

## ▶️ Como executar o projeto
1. Clone o repositório:
```sh
git clone https://github.com/SEU_USUARIO/trabalho_karatsuba.git
cd trabalho_karatsuba
```
