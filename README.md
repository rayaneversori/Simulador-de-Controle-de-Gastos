# Simulador de Controle de Gastos

## Descrição do Projeto
O **Simulador de Controle de Gastos** é uma aplicação interativa desenvolvida em Python, cujo objetivo é ajudar usuários a gerenciar suas despesas de forma prática e eficiente. O projeto também inclui mensagens motivacionais para incentivar hábitos financeiros saudáveis.

---

## Funcionalidades

1. **Adicionar despesas**: 
   - Permite registrar uma despesa, incluindo categoria e valor.
2. **Visualizar despesas**: 
   - Exibe todas as despesas cadastradas e calcula o total gasto.
3. **Mensagens motivacionais**: 
   - Apresenta frases inspiradoras relacionadas à economia e finanças pessoais.
4. **Menu interativo**: 
   - Interface simples para navegação das funcionalidades.

---

## Cronograma de Desenvolvimento

| **Etapa**             | **Descrição**                                | **Prazo**        |
|-----------------------|----------------------------------------------|------------------|
| Planejamento          | Estruturar o projeto, definir objetivos      | Dia 1            |
| Inicialização         | Criar o repositório e o arquivo base         | Dia 1            |
| Desenvolvimento Base  | Implementar funcionalidades principais       | Dias 2 e 3       |
| Interface do Usuário  | Adicionar menu interativo                    | Dia 4            |
| Funcionalidades Extras| Inserir mensagens motivacionais              | Dia 5            |
| Integração Final      | Realizar merges e testes                     | Dia 6            |
| Documentação Final    | Escrever README.md e desafios enfrentados    | Dia 7            |

---

## Processo de Desenvolvimento

### 1. Organização do Código em Merges
- Dividimos o projeto em **branches** distintas:
  - `backend`: Implementação da lógica de despesas.
  - `interface`: Criação do menu interativo.
  - `inspiracao`: Adição de mensagens motivacionais.
- Cada branch foi desenvolvida e testada separadamente antes de ser integrada à branch principal (`main`).

### 2. Frequência de Commits
- Realizamos commits frequentes para documentar cada avanço no projeto, o que facilitou o rastreamento de alterações e a resolução de conflitos.

### 3. Desafios Enfrentados
- **Conflitos durante o merge**: Um conflito ocorreu ao integrar a funcionalidade de mensagens motivacionais com o menu interativo. Para resolver, usamos ferramentas do Git e ajustamos o código manualmente.
- **Erros de lógica**: Durante a implementação da visualização de despesas, esquecemos de calcular o total. Isso foi corrigido com novos commits na branch `backend`.
- **Erros de entrada do usuário**: Foi necessário adicionar validações para garantir que os valores inseridos fossem numéricos.

### 4. Benefícios do Uso do Git
- O **controle de versões** garantiu que pudéssemos voltar a estados anteriores do projeto em caso de erro.
- As **branches** possibilitaram o desenvolvimento simultâneo de funcionalidades sem interferência.
- Os **commits frequentes** permitiram um histórico detalhado, facilitando o aprendizado e a correção de erros.