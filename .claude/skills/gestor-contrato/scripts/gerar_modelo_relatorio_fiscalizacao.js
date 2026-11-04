// Gera modelos-oficiais/07-Relatorio-Fiscalizacao-template.docx
// Estrutura: modelo de Relatório de Fiscalização da SGD (Portaria SGD/MGI 750/2023, Anexo VIII,
// incluído pela Portaria 6.679/2024) + quadros do projeto (Anexos D e G de mapas/anexos-tr.md).
// Uso: node gerar_modelo_relatorio_fiscalizacao.js [saida.docx]
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, HeadingLevel, BorderStyle,
} = require('docx');

const FONT = 'Arial';
const W = 9026; // largura útil A4 com margens de 1440 DXA
const out = process.argv[2] ||
  path.join(__dirname, '..', '..', '..', '..', 'modelos-oficiais', '07-Relatorio-Fiscalizacao-template.docx');

const p = (text, opts = {}) => new Paragraph({
  spacing: { after: 120 }, alignment: opts.align,
  children: [new TextRun({ text, font: FONT, size: opts.size || 22, bold: opts.bold, italics: opts.italics, color: opts.color })],
});
const nota = (text) => p('Nota explicativa: ' + text + ' (apagar na versão final)', { italics: true, color: '808080', size: 18 });
const h = (text) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text, font: FONT })] });

function table(headers, rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const cell = (text, head, w) => new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: head ? { type: ShadingType.CLEAR, fill: 'D9E2F3', color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    children: [new Paragraph({ children: [new TextRun({ text, font: FONT, size: 18, bold: head })] })],
  });
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: headers.map((t, i) => cell(t, true, widths[i])) }),
      ...rows.map((r) => new TableRow({ children: r.map((t, i) => cell(t, false, widths[i])) })),
    ],
  });
}
const split = (n) => Array(n).fill(Math.floor(W / n)).map((v, i, a) => (i === n - 1 ? W - v * (n - 1) : v));
const blank = (n, k = 2) => Array.from({ length: k }, () => Array(n).fill(''));
const kv = (pairs) => table(['Campo', 'Conteúdo'], pairs.map(([a, b]) => [a, b]), [3200, W - 3200]);

const children = [
  p('<ÓRGÃO OU ENTIDADE>', { bold: true, align: AlignmentType.CENTER }),
  p('RELATÓRIO DE FISCALIZAÇÃO Nº <nº>/<aaaa>', { bold: true, size: 28, align: AlignmentType.CENTER }),
  p('Nível de serviço e recebimento — mês de referência <mm/aaaa> | OS ou entrega nº <nº>', { align: AlignmentType.CENTER }),
  nota('em serviço com pagamento mensal, um relatório por mês de referência (mês da prestação, não da nota ou do pagamento); em pagamento único ou por parcela, um relatório por entrega. Quando o objeto seguir modelo de contratação da SGD, mantenha também a estrutura do modelo dele'),

  h('1. Identificação'),
  kv([['Contrato nº / processo', '<xx/aaaa> / <nº do processo>'], ['Contratada / CNPJ', '<razão social> / <CNPJ>'],
    ['Objeto', '<descrição do objeto>'], ['Mês de referência ou OS/entrega', '<mm/aaaa> ou <nº>'],
    ['Nota de empenho', '<nº, data, valor>'], ['Valor previsto do período', 'R$ <valor>'],
    ['Fiscal Técnico', '<nome, portaria>'], ['Fiscal Requisitante', '<nome, portaria>'],
    ['Fiscal Administrativo', '<nome, portaria>'], ['Gestor do Contrato', '<nome, portaria>']]),

  h('2. Dados de entrada e fontes'),
  p('Dados entregues pela contratada ou extraídos das ferramentas de medição, conforme o TR. Dado sem fonte identificada não entra no cálculo.'),
  table(['Dado', 'Fonte (arquivo, ferramenta)', 'Recebido em', 'Período coberto', 'Observação'], blank(5, 3), split(5)),

  h('3. Registro de ocorrências'),
  p('Conforme o art. 117, § 1º, da Lei nº 14.133, de 2021, o fiscal anota em registro próprio as ocorrências da execução e determina o necessário para regularizar faltas e defeitos.'),
  table(['Data', 'Tipo', 'Descrição', 'Item ou sistema afetado', 'Providência'], blank(5), split(5)),

  h('4. Recebimento do que foi entregue'),
  table(['Item', 'Qtd. contratada', 'Entregue no período', 'Confere com proposta e TR?', 'Garantia do fabricante registrada? (série, consulta)', 'Amostragem'], blank(6), split(6)),
  nota('a garantia registrada em nome do órgão é condição do recebimento definitivo quando o TR a exigir; a amostragem segue o Anexo E do TR, quando houver'),

  h('5. Aferição dos níveis de serviço'),
  table(['Indicador', 'Fórmula (item do TR)', 'Meta', 'Valor aferido', 'Faixa', '% glosa', 'Base de cálculo (R$)', 'Glosa (R$)'], blank(8), split(8)),
  nota('recalcule cada indicador a partir dos dados brutos da seção 2, aplicando as exclusões previstas no TR, com prova'),

  h('6. Avaliação do Fiscal Requisitante'),
  p('<A entrega atendeu à necessidade descrita no ETP e no TR? Ocorrências relatadas pelos usuários. Critério escrito no TR que fundamenta eventual não aceitação.>'),

  h('7. Avaliação do Fiscal Administrativo'),
  table(['Verificação', 'Situação', 'Evidência'], [
    ['Nota fiscal confere com proposta, contrato e empenho (valor, itens, período, CNPJ)', '', ''],
    ['Regularidade fiscal, trabalhista e previdenciária', '', ''],
    ['Comprovação trabalhista mensal (Anexo F), quando houver', '', ''],
    ['Garantia contratual vigente, quando exigida', '', ''],
    ['Saldo de empenho suficiente para este pagamento', '', ''],
  ], [4600, 1800, W - 6400]),

  h('8. Cálculo do pagamento'),
  kv([['Valor previsto do período', 'R$ <valor>'], ['(−) Glosas por indicador', 'R$ <soma da seção 5>'],
    ['Teto de glosa do período (TR, Anexo G)', '<percentual> = R$ <valor>'], ['Glosa aplicada (limitada ao teto)', 'R$ <valor>'],
    ['Valor a pagar', 'R$ <valor>']]),
  nota('glosa acima do teto não aumenta o desconto: a diferença vai para processo sancionatório (Lei nº 14.133, de 2021, arts. 155 a 163)'),

  h('9. Controle financeiro e de quantidades'),
  table(['Empenho (R$)', 'Pago antes (R$)', 'Este pagamento (R$)', 'Saldo do empenho (R$)', 'Valor anual previsto (R$)', 'Acumulado no exercício (R$)'], blank(6, 1), split(6)),
  table(['Item', 'Qtd. contratada', 'Usada no período', 'Acumulada', 'Saldo', '% usado'], blank(6), split(6)),
  p('Alertas: <saldo do empenho insuficiente para os próximos 2 meses | valor anual previsto em risco | quantidade acumulada acima ou próxima da contratada | nenhum>'),

  h('10. Conclusão'),
  p('☐ Apto para pagamento: R$ <valor>'),
  p('☐ Apto com glosa: R$ <valor>, glosa total de R$ <valor> (seção 5)'),
  p('☐ Não apto: <pendências e responsáveis>'),
  p('Providências e recomendações (notificação, glosa, abertura de processo sancionatório): <...>'),
  p('Dessa forma, encaminhamos este Relatório de Fiscalização para análise do(a) Gestor(a) do Contrato e providências cabíveis.'),

  h('11. Assinaturas'),
  table(['Papel', 'Nome', 'Assinatura e data'], [['Fiscal Técnico', '', ''], ['Fiscal Requisitante', '', ''], ['Fiscal Administrativo', '', ''], ['Ciência do Gestor do Contrato', '', '']], [3000, 3000, W - 6000]),
];

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [{ id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
      run: { font: FONT, size: 24, bold: true }, paragraph: { spacing: { before: 240, after: 120 }, keepNext: true } }],
  },
  sections: [{ properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } }, children }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(out, b); console.log(out); });
