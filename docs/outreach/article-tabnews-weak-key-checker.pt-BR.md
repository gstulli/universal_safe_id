# Rascunho de artigo: um verificador de chaves fracas em Python

> Rascunho de divulgação, pensado para comunidades técnicas em português (por exemplo, o TabNews). **Tradução para o inglês pendente.** Revise antes de publicar: confira os links, os números e se o repositório continua com os mesmos resultados.

---

# Chaves privadas minúsculas: escrevi um verificador de chaves fracas em Python (e o que ele não consegue provar)

*Código aberto, só biblioteca padrão, 32 testes. Protótipo de pesquisa, sem revisão de especialistas.*

## O caso que me fez escrever isto

Em outubro de 2026, duas reportagens ([TabNews](https://www.tabnews.com.br/augustresende/a-chave-privada-era-literalmente-4-o-firefox-confiava-nela-no-icp-brasil-nao-confia) e [Hardware.com.br](https://www.hardware.com.br/noticias/oito-certificados-tls-comprometidos-colocam-a-seguranca-da-internet-em-alerta/)) descreveram oito certificados de autoridades intermediárias cujas chaves privadas, segundo os relatos, eram números minúsculos: 4, 56, 66, 115, 155, 156, 230 e 237. As chaves usavam a curva NIST P-384, que deveria oferecer cerca de 192 bits de segurança. Um pesquisador provou possuir as chaves assinando uma mensagem. As reportagens divergem em alguns detalhes, e a causa da geração fraca não foi esclarecida nelas. Não tenho as chaves reais; o que fiz foi reproduzir o **tipo** de fraqueza.

A pergunta que me ocorreu: se a falha é tão grosseira, **quanto custa detectá-la?** Descobri que quase nada.

## A ideia

Uma chave pública em curva elíptica é `Q = d·G`, onde `d` é o escalar privado e `G` é o ponto gerador da curva. Se `d` é pequeno, basta calcular `1·G, 2·G, 3·G, ...` até algum limite `N` e comparar com `Q`. Como `d·G` e `(−d)·G` têm a mesma coordenada `x`, compara-se só o `x`. Isso pega também o caso do escalar negativo (`n − d`).

Com uma tabela de `N = 65.536` entradas (cerca de 2 a 4 segundos em Python puro), cada chave seguinte é uma consulta imediata:

```python
# simplificado: ver weakkeys/checks.py no repositório
def small_scalar_table(curve, limit=65536):
    table, point = {}, curve.generator
    for d in range(1, limit + 1):
        table.setdefault(point[0], d)          # +d e -d compartilham x
        point = curve.add(point, curve.generator)
    return table

def small_scalar(curve, public_point, table):
    return table.get(public_point[0])          # d, ou None
```

Qualquer chave cujo escalar privado esteja nesse intervalo é recuperada, e não só detectada: o verificador diz qual era o `d`.

## O que o programa verifica

Chaves públicas em P-256, P-384, secp256k1 e Ed25519, lidas de PEM, DER, certificados X.509 ou hexadecimal:

- ponto inválido ou fora da curva (risco de curva inválida) e coordenadas não reduzidas;
- **escalar privado minúsculo**, como acima;
- com `--deep`: escalares estruturados (`2^k`, `2^k±1`, bytes repetidos) e sementes triviais de Ed25519 (zeros, byte repetido, inteiros pequenos);
- Ed25519: ponto identidade, ponto de ordem pequena, codificação não canônica e componente de torção;
- a mesma chave repetida, chaves que são a negação uma da outra, e uma lista de bloqueio de *fingerprints*.

Não tem dependências além da biblioteca padrão (Python 3.9+). Exemplos:

```bash
python3 -m weakkeys demo                       # reproduz os oito valores relatados, em chaves sintéticas
python3 -m weakkeys check --pem cadeia.pem     # chaves públicas e certificados PEM
python3 -m weakkeys check --list chaves.txt --deep --json
```

## Como testei, e o que encontrei

- 32 testes (`python3 -m unittest discover -v`, cerca de 16 segundos).
- A aritmética de curvas confere com vetores conhecidos (o dobro do gerador em P-256 e secp256k1, o vetor de teste 1 do RFC 8032 para Ed25519) e com a biblioteca independente `cryptography`, que uso só nos testes.
- Os oito valores relatados, em chaves **sintéticas** de P-384, são rejeitados com o escalar recuperado. Um certificado X.509 de teste cuja chave privada é 4 é rejeitado de ponta a ponta. Uma chave comum passa.
- Custo medido em Python puro, um núcleo: a tabela de 65.536 múltiplos leva cerca de 2 s (P-256, secp256k1), 3 s (P-384) e 4 s (Ed25519). O modo `--deep` acrescenta de 3 a 8 s.

## O que ele **não** consegue provar

Isto é o mais importante:

1. **Não prova aleatoriedade.** Ele só acha padrões ruins conhecidos. Um gerador sutilmente previsível passa. Detectar isso é um problema em aberto.
2. **A profundidade é pequena por padrão.** Escalares acima do limite `N` não são encontrados, salvo os estruturados. Uma busca *baby-step giant-step* cobriria faixas muito maiores com pouca memória; não implementei.
3. **Python puro, sem tempo constante.** Serve para estudo e para chaves públicas. Um monitor que varra registros públicos de certificados precisaria de uma implementação otimizada.
4. **Sem RSA, sem P-521, sem validação de assinatura nem de cadeia,** e com um leitor DER propositalmente mínimo.
5. **Quem passa é só "não obviamente ruim".** Isso não prova que a chave seja boa.

Também não tenho visibilidade sobre o que realmente aconteceu no incidente. O que se pode dizer é que um teste desse tipo é barato, e que ele poderia ser executado antes de uma chave de autoridade ser ativada, por qualquer pessoa.

## O que isto ensina

A lição que tirei não é sobre este programa, e sim sobre processo: **o erro não deveria depender de alguém lembrar de verificar.** Se a criação de uma chave sensível só vale depois de ser publicada em estado pendente, verificada por monitores independentes e aprovada após um prazo, uma chave com `d = 4` não chega a ser usada. É assim que penso em outro projeto meu, uma proposta aberta de identidade sem dono (o Universal Safe ID), onde este verificador é o primeiro pedaço de um experimento maior. Não é o assunto deste artigo, mas é o motivo de eu ter escrito o código.

## Transparência e pedido de revisão

- O código e os documentos do projeto foram escritos com ajuda de um assistente de IA e **não foram revisados por especialistas em criptografia**. Se você é uma dessas pessoas, uma revisão sua seria muito valiosa: erros na aritmética, nas verificações ou no leitor DER são possíveis.
- Peço que **não use isto para proteger nada real**: ele só inspeciona chaves públicas.
- Aceito sugestões de verificações que faltam, de melhores formas de detectar geração fraca e de comparações com ferramentas existentes (por exemplo, *linters* de certificados). Se já existe uma ferramenta que faz melhor, prefiro contribuir com ela a manter a minha.

**Código e discussão:** https://github.com/gstulli/universal_safe_id (pasta `experiments/E17-weak-key-linter`, issue 17).

*Licença do código: Apache-2.0. Documentação: CC BY 4.0.*

---

## Notas para a publicação (não fazem parte do artigo)

- **Conferir antes de publicar:** os links das reportagens, o número de testes e os tempos (rode `python3 -m unittest discover` na pasta do experimento) e se a revisão externa já aconteceu.
- **Tom:** técnico e humilde. Evite afirmar o que causou o incidente.
- **Título alternativo:** "Reproduzindo uma falha de chaves com Python simples: o que um teste barato pega e o que não pega".
- **Onde postar:** TabNews (artigo), depois um resumo em LinkedIn e em comunidades de segurança, com o link para o artigo.
- **Chamada específica:** peça revisão de criptografia, e comparação com *linters* de certificado existentes.
