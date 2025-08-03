# SQLite

**Cursor** - É um objeto que permite executar comandos SQL (como SELECT, INSERT, DELETE, UPDATE) dentro da conexão com o banco de dados.

**Execute** - Envia uma string contendo comandos SQL para o banco de dados, e executa esse comando.

**Commit** - Serve para confirmar (gravar) todas essas alterações permanentemente no banco. Quando fazemos mudanças no banco de dados, essas alterações ficam temporariamente guardadas na transação atual.

**Close** - Fecha a conexão com o banco de dados SQLite. 

**Lastrowid** - Retorna o ID que acabou de ser criado, sem a necessidade de consultas.

**Fetchall** - Pertence ao objeto Cursor. Quando vocÊ executa uma consulta SQL, que retorna várias linhas (como um SELECT), o método curosr.fetchall() pega todas essas linhas de uma vez e retorna uma lista com elas. Cada linha representa uma tupla com os valores das colunas selecionadas.



# Pydantic

É uma biblioteca que o FastAPI usa para validar e transformar dados automaticamente.
Quando a API recebe uma requisição (por exemplo, para cadastrar um usuario), o FastAPI usa esses modelos para garantir que os dados enviados estão corretos antes de entrar na sua lógica.

**BaseModel** - É uma classe base fornecida pela biblioteca Pydantic, que o FAstAPI usa para validação de dados.