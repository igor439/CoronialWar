# Estrutura de games com Pygame


Este projeto exemplifica como passar de nível do game para outro de maneira encapsular cada nível. Isto é, pode-se fazer alterações em cada fase do game independentemente, pois a estrutura os integrará ao game de maneira natural.


Como toda aplicação que necessita de movimento, por freme, a aplicação faz da sua maneira três principais ações. Captar as ações e os eventos do game, atualizar o frame atual, e por fim renderizá-lo na tela para em seguida recomeçar o loop. Utilizando-se de dois Elementos principais,Poliformismo e Stack/pilha (estrutura de dados). Esta estrutura pode ser construída de maneira a manter as boas práticas, limpa e modularizada.




 Todo o controle e a passagem de fases será feito pela classe abstrata **State**. Todas as fases serão colocadas em uma stack a primeira fase será a primeira, a segunda fase a segunda e assim sucessivamente. A classe state terá como métodos abstratos Update e Render e será responsável pela retirada ou colocada das fases no stack. Toda classe que será referente a uma fase deve herdar State para que o Stack via polimorfismo comporte todas elas sem problemas.
 
 
 Chamando o método Render sempre do objeto no topo do Stack o controle de fases independerá do objeto das fases em si.
