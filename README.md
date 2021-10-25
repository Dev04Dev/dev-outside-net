![logo](/resources/logo/logo_normal.png)

# dev-outside-net

> É uma aplicação desktop, criada para ajudar programadores iniciantes a estudar apesar da falta de internet, as vezes a falta de motivação faz com que iniciantes abandonem a programação por causa de algumas dificuldades, uma das maiores é a *Internet*! O objectivo deste projecto é justamente ajudar iniciantes a achar as respostas para perguntas mais básicas sobre programação, para que possam ter uma boa base e motivação para continuar a estudar por conta própria! 

## Features:

- Procura por palavras nos arquivos ".ml" na pasta "content" obtendo respostas rápidas para as palavras chaves pesquisadas!

- Contém os temas indexados no arquivo "main.json", na pasta content, para acessar rapidamente os temas desejados sem ter de pesquisar por palavras específicas!

- Tema, palette(Qt), fonte, e tema de ícones configuráveis via json (data/launch.json)
  
### Exemplo:

```json
{
"app-theme":"dark",
"icons-theme":"light",
"qt-palette":"dark"
}
```

*Mais por vir...*

---

## ScreenShots:

![screen1](/resources/assets/screen1.png)
![screen2](/resources/assets/screen2.png)
![screen3](/resources/assets/screen3.png)
![screen4](/resources/assets/screen4.png)

---

## Technical specifications:

> este projecto está a ser desenvolvido sob as seguintes especificações:

- Language: Python 3.8.10

- Operacional System: Ubuntu 20.04 LTS

- GUI: PyQt5==5.15.5(Qt5==5.15.2)
  
  ...
  
  *Veja outras dependências em*:
  
  - *./requirements.txt*
  
  - */frameworks*

## Contribute:

> Estou trabalhando em um guia para aqueles que quiserem contribuir! Mas enquanto isso, poderá:

1. Clonar este repositório, realizar testes e encontrar problemas!

` git clone https://github.com/Dev04Dev/dev-outside-net.git `

2. Caso encontre algum problema ou note algum comportamento estranho na aplicação por favor crie uma *issue* (caso ainda não exista), e relate o problema!

3. Deixar uma estrela neste *repo*, pois dá mais motivação ver que as pessoas se importam com o trabalho que está sendo realizado!

4. Partilhar essa ideia com outros!

5. Visitar as nossas redes sociais:
   
   [![Dev4Dev](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/projectdev4dev)
   [![Dev4Dev](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UChZcAI8vsPWPQeMs3sJZiNQ)

## State:

> Este Projecto está em estado de desenvolvimento, e ainda não tem nenhuma distribuição, o primeiro lançamento (*Alpha*) está previsto para Dezembro de 2021, apenas para testes!

## DONE:

- [x] Interface de usuário

- [x] Funcionalidades básicas (Pesquisar; Abrir os Resultados; Selecionar Tópicos)

- [x] Configurável

## TODO:

- [ ] Correção de alguns ***bugs***

- [ ] Adicionar funcionalidade para salvar o estado da janela ao sair

- [ ] Permitir o usuário configurar a aplicação pela Interface gráfica (GUI)

- [ ] Atualizar o estado(configurações, dados) da aplicação em tempo real!

## Contacts:

[projectdev4dev@gmail.com](mailto:projectdev4dev@gmail.com)

## Thankful:

- A funcionalidade de buscar por palavras em ficheiros foi baseada em:
  
  [ExCo/functions.py at master · matkuki/ExCo · GitHub](https://github.com/matkuki/ExCo/blob/master/functions.py)


*This Readme is under construction*
