# Arquitetura Pipes and Filters
### Participantes:
- Aguinaldo Mendes
- Diego Henrique
- Gabriel Henrique
- Giovanni Menon

-----
### Descrição da arquitetura pipes and filters:

- A arquitetura Pipes and Filters é um estilo arquitetural utilizado para processar fluxos de dados, dividindo-os em várias etapas independentes (chamadas "filtros") conectadas por canais de comunicação (chamados "pipes"). Cada filtro executa uma transformação ou operação específica nos dados, e os resultados são passados para o próximo filtro através dos pipes, criando um fluxo contínuo de processamento. Esse padrão é amplamente usado em sistemas que lidam com grandes volumes de dados ou em pipelines de processamento de informações.

-----

### Características:
1. Composição de Filtros: O sistema é composto de uma sequência de filtros, onde cada um pode ser facilmente substituído ou reutilizado em outro contexto, promovendo modularidade.

2. Encadeamento Linear: Os dados fluem linearmente de um filtro para o próximo por meio dos pipes, criando uma série de etapas de processamento.

3. Paralelismo: Como cada filtro é independente, eles podem ser executados em paralelo, aumentando o desempenho em sistemas distribuídos ou de grande escala.

4. Transformação Incremental: Os dados são processados em etapas discretas, o que significa que cada filtro aplica uma transformação específica, facilitando a compreensão e manutenção do sistema.

-----

### Vantagens:
- Reusabilidade: Filtros podem ser reutilizados em diferentes contextos, o que facilita a expansão e modificação do sistema sem reescrever o código.

- Modularidade: Cada filtro é uma unidade de processamento isolada, o que facilita a compreensão, teste e manutenção.

- Facilidade de Extensão: Novos filtros podem ser adicionados ao pipeline de forma simples, sem grandes mudanças no sistema geral.

- Escalabilidade: A independência dos filtros permite que eles sejam executados paralelamente ou distribuídos entre várias máquinas.

### Desvantagens:
- Overhead de Comunicação: Se os pipes forem mal implementados ou a comunicação entre filtros for cara, pode haver perda de desempenho.

- Latência: Em pipelines longos com muitos filtros, a latência pode aumentar devido ao tempo necessário para os dados passarem por cada filtro.

### Exemplos de Uso:
- Processamento de dados em tempo real: Sistemas de análise de grandes volumes de dados, como log de servidores ou fluxos de sensores IoT, frequentemente utilizam esse padrão para processar, filtrar e transformar dados em várias etapas.

- Compiladores: A arquitetura Pipes and Filters é comumente usada em compiladores, onde o código-fonte passa por uma série de transformações (lexical, sintática, semântica) antes de ser convertido em código executável.

- Sistemas de streaming: Sistemas que lidam com processamento de áudio, vídeo, ou dados em tempo real muitas vezes adotam essa arquitetura para aplicar filtros sequenciais como compressão, equalização, ou formatação de dados.

- Processos de ETL (Extract, Transform, Load): Ferramentas de ETL que extraem, transformam e carregam dados de várias fontes frequentemente utilizam o padrão Pipes and Filters. Durante o processo, os dados passam por múltiplas transformações (filtros) e são transferidos entre diferentes sistemas ou bancos de dados (pipes). Essa abordagem modular permite flexibilidade e escalabilidade no processamento de grandes volumes de dados, sendo uma prática comum em ambientes de big data e data warehousing.

- Apache NiFi: O Apache NiFi exemplifica bem a arquitetura Pipes and Filters, permitindo que dados sejam roteados, transformados e processados em pipelines de dados configuráveis. No NiFi, processors atuam como os filtros, transformando os dados em diferentes etapas, enquanto os pipes transferem os dados entre essas etapas. É amplamente utilizado em fluxos de trabalho que envolvem grandes volumes de dados em tempo real, fornecendo uma interface visual para construir e gerenciar pipelines de dados complexos.

------
### Como rodar o projeto:
1. Instalar o loguru para os logs da aplicação: 
``` python
pip install loguru
```
2. Rodar o processamento dos dados:
```python
python pips_and_filters.py
````
