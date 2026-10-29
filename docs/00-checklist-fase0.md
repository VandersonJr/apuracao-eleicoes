# Checklist da Fase 0: Fundação e pesquisa

## Ambiente
- [ ] Python 3.12 instalado (`python --version`)
- [ ] Git instalado (`git --version`)
- [ ] Repositório criado no GitHub e clonado/iniciado localmente
- [ ] Ambiente virtual criado e dependências instaladas
- [ ] `pytest` roda sem erros (teste de fumaça)
- [ ] Primeiro commit feito

## Pesquisa (fontes oficiais do TSE)
- [ ] Baixar o manual "QR Code no Boletim de Urna: manual para criação de aplicativos de leitura"
- [ ] Baixar os exemplos de boletins de urna (ZIP) e colocar em `data/amostras_tse/`
- [ ] Baixar a lista de hashes SHA-512 das chaves públicas e colocar em `data/chaves_publicas/`
- [ ] Confirmar qual versão da especificação vale para a eleição-alvo
- [ ] Anotar o contato técnico indicado no manual para dúvidas

## Documentação
- [ ] Ler o manual inteiro uma vez, sem anotar
- [ ] Reler preenchendo `docs/04-formato-qr.md`
- [ ] Conseguir explicar cada campo de um QR de exemplo com suas palavras
- [ ] Revisar `docs/01-escopo.md` e `docs/02-requisitos.md`

## Critério de aceite
Você explica, sem consultar, cada campo de um QR de exemplo, e o repositório roda `pytest` verde.
