# Visão e escopo

## Objetivo
Ler o QR Code do BU impresso, validar sua autenticidade, contabilizar votos e indicar o candidato mais votado.

## Aviso obrigatório
Ferramenta independente de conferência. **Não é sistema oficial** e não substitui a totalização do TSE.
Todo resultado exibido deve mostrar a cobertura ("X de Y seções apuradas").

## Dentro do escopo (MVP)
- Município único
- Cargo de prefeito
- Entrada: foto do QR Code do BU impresso
- Validação de assinatura digital
- Apuração, ranking e relatório CSV

## Fora do escopo (por enquanto)
- Vereador (proporcional)
- Cargos estaduais e federais
- OCR do BU impresso
- Qualquer divulgação como resultado oficial

## Premissas
- Desenvolvimento solo, nível básico em Python
- Especificação do TSE vigente confirmada na Fase 0

## Riscos principais
Formato do QR mudar, assinatura difícil de implementar, cobertura parcial gerar conclusão errada, BUs falsos.
