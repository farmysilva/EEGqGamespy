# EEGqGamespy
###### Um sistema de EEG quantitativo para pesquisa em jogos
*************************************************************

Pensado em uma estrutura de três camadas interligadas, o sistema possui uma camada denominada drive que é responsável por determinar qual o hardware de aquisição e suas especificações de comunicação. Por exemplo: Numero de Canais de aquisição disponíveis, taxa de amostragem, fabricante e modelo.
A segunda camada foi pensada para realizar o armazenamento dos dados provenientes da interface do drive, demonstrar seus gráficos de plotagem, realizar os filtros e transformações necessárias para que a informação seja o mais fidedígna possível. Essa camada de aquisição é responsável também por integrar dados provenientes da terceira camada, juntos aos dados de eeg coletados.
A terceira camada, task, é responsável por configurar, apresentar e fornecer dados de um conjunto de tarefas que podem ser adicionadas ao sistema. Estas tarefas, fornecem informações (marcadores) para ser integrado aos dados do eeg coletados.

## Como um estudo em desenvolvimento, estas informações podem sofrer alterações com o tempo.
## Meu contato:
###### farmygsf@cos.urfj.br

