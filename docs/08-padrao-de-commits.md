# Padrão de commits

## Formato

```
<emoji> <palavra-chave>: <descrição curta no imperativo>
```

Exemplo: `:sparkles: feat: adiciona leitura de QR Code por imagem`

Regras:
- Use o **shortcode do emoji** (ex.: `:sparkles:`), que evita problemas de codificação no terminal e é renderizado pelo GitHub.
- A palavra-chave vem da tabela abaixo. Tipos sem palavra-chave usam só o emoji.
- Descrição em português, curta (até ~70 caracteres), sem ponto final.
- Um commit por mudança lógica.
- Detalhes adicionais vão no corpo da mensagem (segundo `-m`).

## Tabela de tipos

| Tipo do commit | Emoji | Palavra-chave |
|---|---|---|
| Acessibilidade | ♿ `:wheelchair:` | |
| Adicionando um teste | ✅ `:white_check_mark:` | test |
| Atualizando a versão de um submódulo | ⬆️ `:arrow_up:` | |
| Retrocedendo a versão de um submódulo | ⬇️ `:arrow_down:` | |
| Adicionando uma dependência | ➕ `:heavy_plus_sign:` | build |
| Alterações de revisão de código | 👌 `:ok_hand:` | style |
| Animações e transições | 💫 `:dizzy:` | |
| Arquivo .gitignore | 🙈 `:see_no_evil:` | chore |
| Bugfix | 🐛 `:bug:` | fix |
| Comentários | 💡 `:bulb:` | docs |
| Commit inicial | 🎉 `:tada:` | init |
| Configuração | 🔧 `:wrench:` | chore |
| Deploy | 🚀 `:rocket:` | |
| Documentação | 📚 `:books:` | docs |
| Em progresso | 🚧 `:construction:` | |
| Estilização de interface | 💄 `:lipstick:` | feat |
| Infraestrutura | 🧱 `:bricks:` | ci |
| Lista de ideias (tasks) | 🔜 `:soon:` | |
| Mocks | 🤡 `:clown_face:` | test |
| Mover/Renomear | 🚚 `:truck:` | chore |
| Novo recurso | ✨ `:sparkles:` | feat |
| Package.json em JS | 📦 `:package:` | build |
| Performance | ⚡ `:zap:` | perf |
| Refatoração | ♻️ `:recycle:` | refactor |
| Limpeza de Código | 🧹 `:broom:` | cleanup |
| Removendo um arquivo | 🗑️ `:wastebasket:` | remove |
| Removendo uma dependência | ➖ `:heavy_minus_sign:` | build |
| Responsividade | 📱 `:iphone:` | |
| Revertendo mudanças | 💥 `:boom:` | fix |
| Segurança | 🔒️ `:lock:` | security |
| SEO | 🔍️ `:mag:` | |
| Tag de versão | 🔖 `:bookmark:` | |
| Teste de aprovação | ✔️ `:heavy_check_mark:` | test |
| Testes | 🧪 `:test_tube:` | test |
| Texto | 📝 `:pencil:` | |
| Tipagem | 🏷️ `:label:` | |
| Tratamento de erros | 🥅 `:goal_net:` | |
| Dados | 🗃️ `:card_file_box:` | raw |

## Exemplos para este projeto

```
:tada: init: estrutura inicial do repositório (Fase 0)
:books: docs: preenche formato do QR Code do BU
:sparkles: feat: adiciona leitura de QR Code por imagem
:white_check_mark: test: adiciona testes do parser do BU
:lock: security: valida assinatura digital do BU
:bug: fix: corrige contagem de BU duplicado
:heavy_plus_sign: build: adiciona opencv-python às dependências
:card_file_box: raw: adiciona amostras de BU do TSE
```
