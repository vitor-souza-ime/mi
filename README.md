# Teorema do Macaco Infinito em Python: Uma Abordagem Experimental por Simulação de Monte Carlo

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Este repositório contém um experimento simples em Python que simula a geração aleatória de strings de três letras até encontrar a string `"FOA"` três vezes, contabilizando o número de tentativas necessárias em cada ocorrência.

📁 Repositório: [github.com/vitor-souza-ime/mi](https://github.com/vitor-souza-ime/mi)  
📄 Arquivo principal: `main.py`

---

## 📌 Descrição

O script `main.py` executa a seguinte lógica:

- Gera strings aleatórias compostas por 3 letras maiúsculas do alfabeto (`A-Z`);
- Verifica se a string gerada é exatamente `"FOA"`;
- Conta quantas tentativas foram necessárias até que `"FOA"` seja encontrada 3 vezes;
- Exibe o número de tentativas individuais para cada ocorrência e o total geral.

---

## ▶️ Como executar

1. **Clone o repositório**:

```bash
git clone https://github.com/vitor-souza-ime/mi.git
cd mi
````

2. **(Opcional) Crie um ambiente virtual e ative-o**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Execute o script principal**:

```bash
python main.py
```

---

## 📋 Exemplo de saída

```
Iniciando busca pela string 'FOA'...
Ocorrência 1: 'FOA' encontrada após 12743 tentativas.
Ocorrência 2: 'FOA' encontrada após 10230 tentativas.
Ocorrência 3: 'FOA' encontrada após 13798 tentativas.

Total de tentativas para encontrar 'FOA' 3 vezes: 36771
```

---

## 🎯 Objetivos educacionais

Este projeto pode ser utilizado para:

* Demonstrar probabilidade empírica e simulações com strings aleatórias;
* Ilustrar conceitos de busca, repetição e contadores em Python;
* Utilização da biblioteca `random` e manipulação de strings.

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença [MIT](LICENSE).

---




