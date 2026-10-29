# Formato do QR Code do BU

> Resumo em palavras próprias da especificação oficial do TSE, conferido com os exemplos reais.
> As páginas citadas são as numeradas no rodapé do manual. **O PDF do manual não deve ser
> versionado no Git** (a obra tem aviso de reprodução restrita); guarde-o localmente em
> `docs/referencias/` e mantenha essa pasta no `.gitignore`.

## Fonte
- Documento: *QR Code no Boletim de Urna: manual para criação de aplicativos de leitura*
- Edição: Brasília, setembro de 2018 (Eleições 2018). Responsável: Seção de Voto Informatizado (Sevin/Csele/STI) do TSE
- Contato técnico do TSE para dúvidas: qrcodenobu@tse.jus.br (p. 7)
- Versão do formato nos exemplos reais: `VRQR:1.5`
- Data em que consultei: 28/10/2026
- **Vigente para a eleição-alvo? NÃO CONFIRMADO.** Este é o manual de 2018. Ao consultar a documentação das Eleições 2022, o TSE informava que o manual de 2020 continuava válido. Falta baixar a versão mais recente e comparar o campo `VRQR` e a lista de campos.

## Estrutura geral (p. 19)
- O conteúdo usa só caracteres do modo alfanumérico do QR Code (sem acentos, por isso **não há nomes**)
- Formato chave/valor: `CHAVE:valor`, tudo em uma linha, registros separados por **um espaço**
- Cada QR Code tem até 1.100 caracteres e três partes: cabeçalho do QR, conteúdo do BU e segurança
- O manual diz que um BU pode ter até 4 QR Codes (p. 18), mas **um exemplo oficial tem 7** (`QRBU:1:7`). Portanto o parser não pode assumir um máximo
- Quando o conteúdo é dividido entre QR Codes, o corte ocorre no último espaço antes do limite: **um registro pode ficar partido entre dois QR Codes**, e o espaço do corte é removido. Para remontar (e para calcular hash), o espaço precisa ser recolocado
- O **índice do QR Code não vem em ordem de leitura**: é preciso ordenar por `n` antes de juntar

## Cabeçalho de cada QR Code (p. 19)

| Campo | Significado | Exemplo real |
|---|---|---|
| `QRBU:n:x` | Marca de início. `n` = posição deste QR, `x` = total de QR Codes do BU | `QRBU:1:1`, `QRBU:2:7` |
| `VRQR:n.y` | Versão do formato de representação | `VRQR:1.5` |
| `VRCH:nnnn` | Versão da chave usada na assinatura (define qual chave pública buscar) | `VRCH:20180830` |

## Cabeçalho do BU (p. 20-21)

| Campo | Significado | Exemplo real | Observação |
|---|---|---|---|
| `ORIG` | Origem do BU: `VOTA` (urna), `RED` ou `SA` (contingência) | `VOTA` | Mesma seção pode ter BU de origens diferentes |
| `ORLC` | Tipo de eleição: `LEG` (oficial) ou `COM` (comunitária) | `LEG` | Só `LEG` interessa ao projeto |
| `PROC` | Número do processo eleitoral | `3081` | |
| `DTPL` | Data do pleito (aaaammdd) | `20181007` | |
| `PLEI` | Número do pleito | `3113` | |
| `TURN` | Turno (1 ou 2) | `1` | |
| `FASE` | `O` oficial, `S` simulado, `T` treinamento | `S` | **Só `O` pode ser somada** em uso real |
| `UNFE` | Sigla da UF (`ZZ` = exterior) | `AC` | |
| `MUNI` | Número do município (código TSE, não IBGE) | `1392` | |
| `ZONA` | Zona eleitoral | `1` | |
| `SECA` | Seção eleitoral | `806` | |
| `AGRE` | Seções agregadas, separadas por ponto | `17.18.19.100` | **Opcional**: um BU pode cobrir várias seções |
| `IDUE` | Número de série da urna | `1521040` | |
| `IDCA` | Código de identificação da carga (24 dígitos) | `782589169776784142348224` | |
| `VERS` | Versão do software da urna | `6.32.0.4` | |
| `LOCA` | Local de votação | `3794` | Só Vota e RED |
| `APTO` | Eleitores aptos | `1` | Só Vota e RED |
| `COMP` | Comparecimento | `1` | Só Vota e RED |
| `FALT` | Faltosos | `0` | Só Vota e RED |
| `HBMA` | Habilitados por ano de nascimento | `1` | Só seções biométricas |
| `DTAB`, `HRAB` | Data e hora de abertura da urna | `20181007`, `172642` | |
| `DTFC`, `HRFC` | Data e hora de fechamento | `20181007`, `192556` | |
| `JUNT`, `TURM` | Junta e turma apuradora | | Só SA |
| `DTEM`, `HREM` | Data e hora de emissão | | Só SA e RED |

## Blocos repetidos (p. 21-22)

**Por eleição:** `IDEL` (código da eleição). No SA também aparecem `MAJO` e `PROP`.

**Por cargo apurado:**

| Campo | Significado |
|---|---|
| `CARG` | Código do cargo (tabela abaixo) |
| `TIPO` | 0 majoritário, 1 proporcional, 2 consulta |
| `VERC` | Versão do pacote de candidatos |

**Por partido (somente cargos proporcionais):** `PART` (número do partido), `LEGP` (votos de legenda do partido), `TOTP` (total do partido).

**Votos por candidato:** `número:quantidade`, por exemplo `10:1`. Só aparecem candidatos que receberam votos. Nos majoritários ficam logo após o cabeçalho do cargo; nos proporcionais, agrupados pelo partido.

**Resumo do cargo (fecha o bloco):**

| Campo | Significado |
|---|---|
| `APTA` | Eleitores aptos a votar no cargo |
| `NOMI` | Votos nominais |
| `LEGC` | Votos de legenda (só proporcionais) |
| `BRAN` | Brancos |
| `NULO` | Nulos |
| `TOTC` | Total apurado do cargo |

## Códigos de cargo (p. 23)

| Código | Cargo |
|---|---|
| 1 | Presidente |
| 3 | Governador |
| 5 | Senador |
| 6 | Deputado federal |
| 7 | Deputado estadual |
| 8 | Deputado distrital |
| 9 | Conselheiro distrital |
| **11** | **Prefeito** (alvo do MVP) |
| **13** | **Vereador** (fase 8) |

## Segurança (p. 23 e 26-28)

| Campo | Significado |
|---|---|
| `HASH` | SHA-512 em hexadecimal (128 caracteres). Fica no fim de **cada** QR Code e é **cumulativo** |
| `ASSI` | Assinatura **Ed25519** (EdDSA) em hexadecimal (128 caracteres = 64 bytes). Só no **último** QR Code. É a mesma impressa no papel como "ASSINATURA QR CODE" |

**Como o hash é formado (p. 27):** o hash do QR `n` é o SHA-512 do conteúdo acumulado dos QR anteriores (cada um seguido de ` HASH:valor`) somado aos dados do QR `n`. A assinatura é feita sobre o **último hash**, não sobre o texto inteiro.

**Chave pública (p. 27-28):**
- Uma chave por UF, gerada para cada versão (`VRCH`)
- Formato do endereço: `http://qrcodenobu.tse.jus.br/tse.qrcodebu/[VRCH]/[legal|comunitaria]/[o|s][uf]qrcode.pub`
- `o` = oficial, `s` = simulado; `uf` em minúsculas (`zz` para exterior). Exemplo: `sacqrcode.pub` = simulado, Acre
- O arquivo é binário e contém **somente os 32 bytes da chave**
- Para conferir se a chave baixada é a legítima, compare o SHA-512 do arquivo com a lista oficial (`chavesqrcodeoficial.sha512` e `chavesqrcodesimulado.sha512`, um hash por arquivo `.pub`, no formato do `sha512sum`)

## Dado complementar: nomes (p. 31)
O QR Code **não traz nomes** de candidatos, partidos, cargos ou município; só códigos. Os nomes vêm de um arquivo JSON publicado pelo TSE às vésperas da eleição:

`http://qrcodenobu.tse.jus.br/json-bu/[fase]/[idProcesso]/[f][ppppp][uf][mmmmm]-qbu.js`

- `fase` por extenso (`oficial`, `simulado`, `treinamento`) e `f` a inicial (`o`, `s`, `t`)
- `ppppp` = número do pleito e `mmmmm` = município, ambos com zeros à esquerda
- O JSON tem assinatura própria (EdDSA, **outra chave**, em `json-bu/s99999br-av.js`; hash na lista `s99999br-av.sha512`)
- Atenção: o JSON é da eleição como um todo naquele município. **Sem ele o sistema só enxerga números de candidatos**

## Regras de consistência conferidas nos exemplos reais
- `TOTC = NOMI + LEGC + BRAN + NULO` (por cargo; `LEGC` só existe em proporcionais). Vale em todos os cargos dos exemplos do manual
- Para cargo com uma vaga, `TOTC` ≤ comparecimento. **Para senador com duas vagas, `TOTC` pode chegar a 2 × comparecimento** (exemplo: comparecimento 30, `TOTC:60`)
- Consequência: **a verificação "votos + brancos + nulos = comparecimento" que sugeri antes está errada em geral**. A correta é a soma por cargo acima
- A soma dos votos por candidato deve ser igual a `NOMI`

## Resultado dos testes com os exemplos do TSE (28/10/2026)
- Os exemplos vêm em PDF (BU impresso) e em `.imgbu` (formato interno da urna, ASN.1; **não é necessário ao projeto**). Os QR Codes foram extraídos dos PDFs rasterizados a 300 dpi
- Foram decodificados QR Codes de 5 BUs. Em 4 deles todos os QR Codes foram lidos
- **Cadeia de hash verificada com sucesso** nos 4 BUs completos (inclusive o de 2 QR Codes), usando o método descrito acima
- Um BU de 7 QR Codes teve só 4 lidos pelo OpenCV: leitura de múltiplos QR por página exige mais robustez (tema da Fase 1)
- **A assinatura Ed25519 ainda não foi verificada** porque exige baixar a chave `.pub` do site do TSE (Fase 3)

## Implicações para o projeto
1. **Chave de deduplicação** deve considerar `(PLEI, TURN, CARG, MUNI, ZONA, SECA)` e também `AGRE`. Não basta a seção
2. **`ORIG` diferente para a mesma seção** (ex.: um BU do Vota e outro do RED) precisa de regra explícita: não somar os dois
3. **Rejeitar `FASE` diferente de `O`** e `ORLC` diferente de `LEG`
4. **BU incompleto** (faltam QR Codes da sequência) fica em estado "incompleto" e não entra na soma
5. Ordenar os QR Codes por `n` e conferir que `n` vai de 1 até `x` sem repetição
6. Candidato é identificado por **número + cargo**; o nome vem do JSON complementar

## Dúvidas em aberto
- [ ] Baixar o manual mais recente (2020 ou posterior) e comparar com este: `VRQR`, campos novos, regras de corte
- [ ] Confirmar a pasta e o nome corretos da chave `.pub` para a versão `VRCH` real (nos exemplos é `20180830`; o manual cita `20180618` no exemplo da p. 28)
- [ ] O código C++ da p. 30 parece usar, como "assinatura", o mesmo hexadecimal apresentado como chave pública na p. 27. Não copiar o exemplo às cegas: validar a implementação com os BUs reais
- [ ] Como o TSE trata o 2º turno: `PLEI` e `IDEL` diferentes? Conferir com BU de 2º turno
- [ ] Onde obter o JSON complementar de uma eleição municipal real (processo, pleito e município)