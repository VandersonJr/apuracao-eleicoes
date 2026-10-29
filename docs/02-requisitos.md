# Requisitos

## Funcionais
- RF01: ler QR Code a partir de imagem
- RF02: interpretar o conteúdo e extrair seção, zona, município, cargo, votos, brancos e nulos
- RF03: validar a assinatura digital; só BUs válidos entram na soma
- RF04: detectar o mesmo BU lido mais de uma vez
- RF05: apurar votos por candidato e indicar o mais votado (ou empate)
- RF06: exibir cobertura (seções apuradas / total)
- RF07: exportar relatório CSV
- RF08: registrar log de auditoria

## Não funcionais
- RNF01: reprodutibilidade (mesma entrada, mesmo resultado)
- RNF02: rastreabilidade (cada voto aponta para o BU de origem)
- RNF03: nunca exibir dado parcial como definitivo
- RNF04: parser isolado e versionado por especificação
