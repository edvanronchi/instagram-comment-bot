# Bot de Comentários Automáticos para Instagram

Este é um projeto de bot de comentários automáticos para Instagram. O bot é capaz de publicar comentários automaticamente em publicações específicas com base na url, usuários e outras opções configuráveis.

### Parâmetros do Bot

```sh
self.username = username  # Login
self.password = password  # Senha
self.link_sorteio = 'https://www.instagram.com/p/{}/'.format(link_sorteio)  # URL do sorteio : 'CDR1vidnewh'
self.list_time = list_time  # Intervalo de tempo em segundos para cada comentario: [1, 2, 3, 4]
self.qtd_users = qtd_users  # Número de pessoas marcadas: 1, 2, 3...
self.contador_global = contador_global  # Número que fica ao lado dos usuarios marcados
self.list_users = list_users  # Lista de usuarios que serão marcados
self.test = test  # Modo teste: True/False
```
