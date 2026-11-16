# DevOps com Inteligência Artificial Generativa

Projeto desenvolvido como atividade prática da **Unidade 5 — Projeto Integrador de DevOps com Inteligência Artificial Generativa**.

O objetivo é demonstrar como um pipeline de integração contínua (CI/CD) pode executar testes automatizados, identificar falhas e utilizar Inteligência Artificial Generativa para auxiliar no diagnóstico de erros a partir da análise dos logs.

## Tecnologias utilizadas

- **Python 3.12:** desenvolvimento da aplicação e scripts.
- **Pytest:** execução dos testes automatizados.
- **GitLab:** gerenciamento do repositório e das alterações.
- **GitLab CI/CD:** automação dos testes e execução do pipeline.
- **OpenAI API:** análise dos logs e geração de sugestões para correção.

## Estrutura do projeto

```text
DevOps-genai-lab/
├── app.py
├── test_app.py
├── genai_analyst.py
├── .gitlab-ci.yml
├── requirements.txt
└── README.md
```

**Descrição dos arquivos:**

- `app.py`: aplicação Python contendo um erro intencional.
- `test_app.py`: testes automatizados para validar o funcionamento da aplicação.
- `genai_analyst.py`: agente responsável por analisar logs com IA generativa.
- `.gitlab-ci.yml`: configuração do pipeline de integração contínua.
- `requirements.txt`: dependências necessárias para executar o projeto.
- `README.md`: documentação do projeto.

## Funcionamento do projeto

O processo foi organizado nas seguintes etapas:

1. Criação do repositório e envio dos arquivos para o GitLab.
2. Configuração do pipeline no arquivo `.gitlab-ci.yml`.
3. Criação de uma branch e abertura de um Merge Request.
4. Execução automática dos testes com Pytest.
5. Identificação de uma falha intencional no código.
6. Acionamento do agente de IA para analisar os logs.
7. Geração de um diagnóstico para auxiliar na identificação e correção do problema.

## Erro identificado

A aplicação possui uma função de cálculo de frete que realiza a soma de dois valores.

O erro ocorre quando o código tenta somar um número decimal (`float`) com um valor de texto (`str`).

**Código com erro:**

```python
return base_price + tax_rate
```

**Mensagem apresentada nos testes:**

```text
TypeError: unsupported operand type(s)
for +: 'float' and 'str'
```

A solução é converter o valor recebido como texto para um número antes de realizar a operação.

**Exemplo de correção:**

```python
return base_price + float(tax_rate)
```

## Análise com Inteligência Artificial Generativa

Após a execução dos testes, o agente de IA foi utilizado para analisar os logs e auxiliar no diagnóstico da falha.

A integração permitiu compreender como a IA pode interpretar mensagens de erro, identificar possíveis causas e fornecer orientações técnicas para a correção do código.

O projeto não aplica alterações automaticamente. As recomendações precisam ser avaliadas antes de qualquer modificação.

## Como executar

**1. Instalar as dependências:**

```bash
python -m pip install -r requirements.txt
```

**2. Executar os testes:**

```bash
python -m pytest -q test_app.py
```

**3. Configurar o GitLab CI/CD:**

- Enviar os arquivos para o repositório.
- Configurar a variável `OPENAI_API_KEY` em Settings → CI/CD → Variables.
- Criar uma branch e abrir um Merge Request.
- Acompanhar a execução do pipeline.

**4. Consultar a análise da IA:**

Após a falha dos testes, o job `ai_debugger` é acionado e gera um relatório chamado `ai_report.md`, disponível nos artefatos do pipeline.

Para publicar o relatório automaticamente nos comentários do Merge Request, também é necessário configurar um token do GitLab com as permissões adequadas.

## Resultados obtidos

Durante a execução do laboratório, o pipeline identificou a falha intencional nos testes automatizados e o agente de IA realizou a análise dos logs.

A atividade demonstrou como a integração entre DevOps e Inteligência Artificial Generativa pode auxiliar na identificação de problemas e no processo de manutenção de software.
