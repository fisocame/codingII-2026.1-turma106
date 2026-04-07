from services.estoque import executar_rota

print(executar_rota("/produtos", "POST", {"nome": "PI do 5 período", "quantidade": 1}))
print(executar_rota("/produtos", "POST", {"nome": "PI do 2 período", "quantidade": 3}))

print(executar_rota("/produtos", "GET"))

print(executar_rota("/produtos/buscar", "GET", {"nome": "PI do 5 período"}))

print(executar_rota("/produtos/atualizar", "PUT", {"nome": "PI do 5 período", "quantidade": 2}))

print(executar_rota("/produtos", "GET"))

print(executar_rota("/produtos/deletar", "DELETE", {"nome": "PI do 5 período"}))

print(executar_rota("/produtos", "GET"))