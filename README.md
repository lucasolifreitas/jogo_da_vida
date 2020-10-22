Desafio
Você precisa implementar sua própria versão do Jogo da Vida, criado pelo matemático John Horton Conway em 1970.
Este é um jogo do tipo zero-player, o que significa que sua evolução é determinada por seu estado inicial,
não necessitando de interação subsequente. O universo do Jogo da Vida, é um tabuleiro bidimensional de células quadradas,
onde cada uma delas tem um de dois estados possíveis: viva ou morta.
Cada célula interage com suas oito vizinhas adjacentes horizontais, verticais ou diagonais.

Regras
As regras que controlam o comportamento do jogo são simples e elegantes:
1.	Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
2.	Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
3.	Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
4.	Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.


Execução do Script

O código foi todo desenvolvido com a linguagem Python.
Para executá-lo basta escolher uma matriz de entrada e rodar o script.
No início do código existem algumas matrizes de entrada como exemplo
mas fica a critério do usuário usar algumas dessas matrizes ou inserir uma nova.






