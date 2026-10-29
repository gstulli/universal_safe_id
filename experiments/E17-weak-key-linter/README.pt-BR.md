# E17: verificador de chaves fracas (primeiro protótipo)

🌐 [English](README.md) · **Português (Brasil)**

> ⚠️ **Protótipo de pesquisa.** Inspeciona apenas chaves **públicas**. **Nunca** cole chaves privadas, e nunca use chaves ou dados pessoais reais aqui. Uma chave que passa é só "não obviamente ruim": **isso não prova qualidade** (seção 23.10 do whitepaper).

- **Whitepaper:** seções 23.4 a 23.6 (rejeição de segredos fracos, publicar antes de usar, monitoramento contínuo) · seção 16, experimento E17
- **Issue:** [#17](https://github.com/gstulli/universal_safe_id/issues/17)
- **Estado:** **em andamento.** Só a primeira parte (o verificador) foi prototipada. "Publicar antes de usar" e a prova de comprometimento ainda não foram implementados.

## Hipótese

Rejeição por construção, monitores e "publicar antes de usar" detectam chaves fracas e impedem a sua ativação (seção 16 do whitepaper, E17).

## O que este protótipo faz

Verifica chaves públicas nas curvas NIST P-256, NIST P-384, secp256k1 e Ed25519, lidas de chaves públicas PEM, certificados PEM, arquivos DER ou pontos em hexadecimal.

| Verificação | Gravidade | Observações |
|---|---|---|
| Codificação inválida, ponto fora da curva, coordenada não reduzida | FAIL | Risco de curva inválida |
| **Escalar privado minúsculo** (o tipo relatado no incidente de outubro de 2026 com autoridades intermediárias) | FAIL | Testa escalares privados de ±1 a ±N por consulta em tabela (N = 65.536 por padrão) |
| Escalar estruturado (`2^k`, `2^k±1`, bytes repetidos) | FAIL | `--deep` |
| Semente trivial de Ed25519 (zeros, byte repetido, inteiros pequenos) | FAIL | `--deep` |
| Ed25519: ponto identidade ou de ordem pequena; codificação não canônica | FAIL | |
| Ed25519: ponto com componente de torção | WARN | Fora do subgrupo de ordem prima |
| Mesma chave mais de uma vez em um lote | FAIL | |
| Chaves que são negações uma da outra (escalares d e −d) | WARN | |
| *Fingerprint* em uma lista de bloqueio | FAIL | SHA-256 da codificação canônica |

**Não tem dependências** além da biblioteca padrão do Python (3.9 ou superior). Os testes usam o pacote opcional `cryptography` como conferência independente.

## Como usar

A partir desta pasta:

```bash
python3 -m weakkeys demo                                   # reproduz os valores relatados em chaves sintéticas
python3 -m weakkeys check --pem cadeia.pem                 # chaves públicas e/ou certificados PEM
python3 -m weakkeys check --point p384:04<hex...>          # uma chave pública em hexadecimal
python3 -m weakkeys check --list chaves.txt --deep --json  # um CURVA:HEX por linha; busca mais profunda; saída JSON
python3 -m weakkeys fingerprint --pem cadeia.pem           # fingerprints SHA-256
```

Código de saída: `0` nenhuma chave rejeitada, `1` ao menos uma rejeitada, `2` erro de uso ou de leitura.

## Método e critério de sucesso

Definidos no whitepaper (seção 16, E17). Para este primeiro protótipo, fixamos um critério mais estreito **antes de executar**: *toda chave construída com os valores de escalar relatados no incidente é rejeitada, com o escalar recuperado; chaves comuns passam; os resultados concordam com uma implementação independente na aritmética de curvas.*

## Resultado (primeira execução, 29 de outubro de 2026)

- **Testes:** 32 passam (`python3 -m unittest discover -v`, cerca de 16 s). Incluem vetores conhecidos (o dobro do gerador em NIST P-256 e secp256k1, vetor de teste 1 do RFC 8032 para Ed25519), a conferência da derivação de chaves públicas contra a biblioteca independente `cryptography` e a leitura de certificados X.509 reais.
- **Reprodução do incidente (sintética):** os oito valores de escalar relatados na imprensa (4, 56, 66, 115, 155, 156, 230, 237) em P-384 são rejeitados, com o escalar recuperado. Um certificado X.509 cuja chave tem escalar privado 4 é rejeitado de ponta a ponta. Uma chave P-384 comum passa. As chaves reais dos certificados **não** foram usadas (não as temos): as chaves são sintéticas, construídas a partir dos valores relatados.
- **Custo (Python puro, um núcleo, máquina de desenvolvimento):** construir a tabela de 65.536 múltiplos leva cerca de 2 s (P-256, secp256k1), 3 s (P-384) e 4 s (Ed25519), uma vez por execução. Depois disso, cada chave é uma consulta O(1). O `--deep` acrescenta cerca de 3 a 7 s por curva para escalares estruturados e cerca de 8 s para sementes triviais de Ed25519.
- **Frente ao critério de sucesso:** atendido para o critério mais estreito acima. O critério mais amplo do E17 ("todas as chaves fracas conhecidas rejeitadas; detecção em minutos; nenhuma ativação sem verificação independente") **ainda não** foi atendido: só existe o verificador, sem fluxo de ativação nem protocolo de prova de comprometimento.

## Limitações (o que isto não mostra)

- **Detecta padrões conhecidos, não aleatoriedade.** Um gerador sutilmente fraco passa. Esta é uma questão em aberto (questão 36 do whitepaper).
- **A profundidade da busca é pequena por padrão.** Escalares acima de N (padrão 65.536) não são encontrados, a menos que sejam estruturados. Uma busca *baby-step giant-step* cobriria faixas bem maiores com pouca memória; não foi implementada.
- Python puro e sem tempo constante. Um monitor real, que varresse registros públicos de certificados, exigiria uma implementação otimizada.
- Sem RSA (o USI não permitiria RSA; verificações de máximo divisor comum em lote são trabalho futuro), sem P-521, sem validação de assinatura ou de cadeia de certificados, e com um leitor DER deliberadamente mínimo.
- O `demo` e os testes usam chaves sintéticas derivadas de valores de escalar relatados na imprensa. As reportagens divergem em detalhes e a causa da geração fraca não foi esclarecida (seção 23.1 do whitepaper).

## Próximos passos

1. Revisão criptográfica independente deste código e das verificações.
2. Ampliar a busca com *baby-step giant-step*; acrescentar P-521 e máximo divisor comum em lote para RSA.
3. Prototipar "publicar antes de usar" (estado pendente, monitores independentes, atraso de ativação) e o protocolo de prova de comprometimento.
4. Medir de ponta a ponta o tempo de detecção e de bloqueio, como exige o E17 do whitepaper.
