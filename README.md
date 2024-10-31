# Controle de estoque com telegram

## Trabalho de Engenharia de Requisitos

Professor: Marcelo Campinhos

Alunos: 

## 1. Identificação do Problema (Engenharia de Requisitos e Gestão)

### **Identificação do Problema:**

No desenvolvimento deste sistema, identificamos que muitas empresas enfrentam dificuldades para manter o controle eficiente de seu estoque. Em empresas pequenas e médias, geralmente o estoque é gerido manualmente, o que leva a problemas como desatualização da quantidade de produtos, atrasos na reposição e falta de visibilidade sobre os itens disponíveis. Isso impacta diretamente a operação e o atendimento ao cliente, podendo resultar em rupturas de estoque e perda de vendas.

### **Técnicas de Elicitação:**

- **Brainstorming**: Com a equipe, discutimos as principais dificuldades enfrentadas no gerenciamento de estoque, considerando problemas como a falta de atualização em tempo real e a necessidade de notificações automáticas para reposição de itens.
- **Entrevistas fictícias com stakeholders**: Criamos perfis fictícios de stakeholders, como o gerente de estoque e o responsável pelo atendimento ao cliente, para entender melhor suas necessidades. O gerente de estoque, por exemplo, deseja uma solução que o notifique automaticamente sobre baixos níveis de estoque, enquanto o atendimento ao cliente precisa de informações precisas para evitar promessas de vendas sem estoque.
- **Análise de documentos**: Examinamos relatórios de vendas e planilhas de inventário para identificar os dados essenciais para um sistema de automação. A análise nos mostrou a importância de ter uma visão centralizada e acessível das quantidades em estoque e do histórico de transações.

### **Requisitos Funcionais e Não Funcionais:**

- **Requisitos Funcionais**:
    - O sistema deve permitir que o estoque seja atualizado automaticamente após cada venda registrada.
    - Notificações devem ser enviadas pelo Telegram para o gerente de estoque sempre que um item atingir um nível crítico.
    - O usuário deve poder consultar a quantidade em estoque diretamente pelo Telegram.
- **Requisitos Não Funcionais**:
    - A comunicação entre o backend e o Telegram deve ser segura, utilizando autenticação e criptografia.
    - O sistema deve ter uma resposta rápida para consultas, garantindo uma experiência ágil para os usuários.
    - A solução precisa ser escalável, pois espera-se que o volume de transações e consultas aumente ao longo do tempo.

## 2. Modelagem de Processos (Modelagem de Processos e Gestão)

### **Modelagem do Processo Atual:**

No processo atual, o controle de estoque é feito de forma manual. Após cada venda, um funcionário precisa atualizar uma planilha de estoque e verificar manualmente quando cada item está próximo de acabar. Esse processo é suscetível a erros, como falta de atualização imediata, o que pode gerar discrepâncias entre o estoque físico e o registrado.

### **Modelagem do Processo Automatizado:**

Com o novo sistema automatizado, o processo mudará significativamente. O fluxo de trabalho inclui:

- O backend registra automaticamente uma transação de venda e atualiza o estoque no banco de dados.
- Quando um item atinge um nível crítico, o sistema envia uma notificação via bot do Telegram para o gerente de estoque.
- Usuários autorizados podem consultar a quantidade disponível em tempo real pelo Telegram, sem precisar acessar sistemas complexos.

### **Pontos de Melhoria e Impacto nos Indicadores de Desempenho:**

Esse processo automatizado elimina a necessidade de atualizações manuais, reduzindo erros humanos. Como resultado, espera-se que a precisão do estoque melhore e o tempo para reposição de itens críticos diminua. Além disso, o acesso em tempo real ao inventário aumenta a eficiência e reduz o risco de ruptura de estoque.

## 3. Proposta de Solução (Arquitetura de Computadores e Engenharia de Software)

### **Arquitetura de Hardware e Software:**

- **Backend**: Desenvolvido em python utilizando FastAPI, o backend será responsável pelo processamento de vendas e consultas ao estoque. Ele se comunicará com o banco de dados para registrar e recuperar informações, oferecendo uma API RESTful para integração com o bot do Telegram.
- **Frontend (Telegram)**: A interface será baseada em um bot do Telegram, permitindo que os usuários façam consultas e recebam notificações em tempo real. O Telegram foi escolhido pela sua acessibilidade e simplicidade, pois os usuários podem interagir com o sistema diretamente de seus dispositivos móveis.
- **Banco de Dados**: O banco de dados será SQL, ideal para a estrutura de inventário e histórico de vendas, pois permite consultas rápidas e armazenamento de dados estruturados.
- **Servidor**: O sistema será hospedado em uma máquina virtual na nuvem da AWS, configurada para rodar o backend e o banco de dados. Isso permite escalabilidade e flexibilidade, garantindo que a solução cresça conforme a demanda.

### **Justificativa das Escolhas Tecnológicas:**

- **Python e FastAPI para o Backend**:
    - **Desempenho e Eficiência**: FastAPI é um framework de alta performance baseado em Python, que usa assincronismo nativo, ideal para lidar com múltiplas requisições simultâneas, como ocorre em um sistema de automação de estoque.
    - **Simplicidade e Flexibilidade**: A API é RESTful e permite integração rápida com outros sistemas, facilitando a criação de endpoints e a manipulação de dados do estoque.
    - **Documentação Automática**: O FastAPI gera uma documentação interativa e automática (via Swagger e OpenAPI), o que facilita a manutenção e a compreensão do sistema.
- **Telegram como Interface de Usuário (Frontend)**:
    - **Acessibilidade**: O Telegram é amplamente utilizado e acessível em dispositivos móveis e desktops, facilitando a interação do usuário com o sistema a qualquer momento e lugar.
    - **Simplicidade de Uso**: Com comandos simples, o usuário pode consultar o estoque ou receber notificações sem precisar acessar uma interface complexa, o que melhora a experiência do usuário e reduz o tempo de treinamento.
    - **Notificações em Tempo Real**: O bot pode enviar notificações automáticas para alertar sobre níveis baixos de estoque, o que é essencial para a eficiência da operação.
- **Banco de Dados SQL**:
    - **Consistência e Integridade dos Dados**: A estrutura relacional do SQL permite que o sistema mantenha a integridade e consistência dos dados do inventário, evitando registros duplicados ou inconsistentes.
    - **Consultas Rápidas e Estruturadas**: O SQL facilita a criação de consultas para relatórios e análises de inventário, permitindo acesso rápido às informações necessárias.
    - **Escalabilidade**: Um banco de dados SQL pode ser facilmente expandido para incluir mais produtos ou categorias à medida que a empresa cresce, mantendo a organização dos dados de forma eficiente.
- **Servidor na Nuvem (AWS):**
    - **Escalabilidade**: Ajuste automático de capacidade conforme a demanda.
    - **Alta Disponibilidade**: Redundância para minimizar interrupções.
    - **Segurança**: Controle de acesso e proteção contra acessos não autorizados.
    - **Custo-Efetivo**: Pagamento conforme o uso, otimizado para expansão.

### **Integração dos Componentes:**

O bot do Telegram será integrado ao backend através de webhook. As transações de vendas serão imediatamente refletidas no banco de dados, e notificações serão enviadas quando determinados critérios forem atingidos (por exemplo, quando um produto está prestes a esgotar).

**Segurança, Escalabilidade e Custos Operacionais:**

- **Segurança**: Será implementada autenticação para garantir que apenas usuários autorizados possam acessar as informações de estoque pelo Telegram.
- **Escalabilidade**: A estrutura de backend em FastAPI, combinada com a hospedagem na nuvem, permitirá expansão conforme necessário. Em cenários de alta demanda, será possível adicionar mais instâncias de backend ou utilizar cache para acelerar as respostas.
- **Custos Operacionais**: Optar por uma solução em nuvem permite uma gestão mais eficiente dos custos, uma vez que a infraestrutura pode ser ajustada conforme a demanda, garantindo que a empresa pague apenas pelo uso necessário.

## 4. Desenvolvimento de Protótipo (Engenharia de Software)

### **Desenvolvimento do Protótipo:**

A partir do design da arquitetura, iniciamos o desenvolvimento de um protótipo funcional, com foco na criação de um MVP (Produto Mínimo Viável) que demonstra as principais funcionalidades do sistema de controle de estoque automatizado.

### **Funcionalidades do Protótipo:**

- **Consulta de Estoque**: O protótipo permite que o usuário consulte a quantidade disponível de itens diretamente pelo Telegram, enviando um comando ao bot que retorna as informações em tempo real.
- **Atualização Automática de Estoque**: A cada venda simulada, o estoque é atualizado no banco de dados através do backend em FastAPI.
- **Notificação de Baixo Estoque**: Ao atingir um nível crítico de estoque para determinado produto, o sistema envia uma notificação automática pelo Telegram para alertar o gerente.

### **Boas Práticas de Engenharia de Software:**

- **Modularidade**: O protótipo foi desenvolvido com uma arquitetura modular. Dividimos o código em módulos distintos para o backend (FastAPI), banco de dados e integração com o Telegram. Isso facilita a manutenção e futuras expansões do sistema.
- **Versionamento**: Utilizamos controle de versão com Git para gerenciar o código do protótipo, garantindo rastreabilidade das mudanças e possibilitando o trabalho colaborativo com a equipe.
- **Testes Iniciais**: Implementamos testes unitários básicos para validar as funções principais, como a atualização de estoque e a consulta de informações. Esses testes ajudam a garantir que o protótipo funcione conforme esperado, mesmo que esteja em estágio inicial.
