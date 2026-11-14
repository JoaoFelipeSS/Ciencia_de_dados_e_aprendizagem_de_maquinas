"""Simulação do retorno financeiro da campanha de retenção.

Os valores abaixo são PREMISSAS definidas na Fase 1 (Entendimento do
Negócio). Não vêm do dataset e devem ser substituídos por números reais
da operadora quando existirem.
"""
import numpy as np

PREMISSAS = {
    "custo_contato": 50.0,   # custo da oferta de retenção por cliente contatado ($)
    "taxa_sucesso": 0.30,    # fração dos clientes em risco que aceitam a oferta e ficam
    "meses_horizonte": 12,   # meses de receita preservada por cliente retido
}


def retorno_campanha(y_real, contatar, cobranca_mensal, **premissas):
    """Calcula o resultado simulado de contatar os clientes marcados.

    y_real          : 1 se o cliente cancelou, 0 caso contrário
    contatar        : True/False para cada cliente (entra ou não na campanha)
    cobranca_mensal : valor mensal pago por cada cliente
    """
    p = {**PREMISSAS, **premissas}
    y_real = np.asarray(y_real).astype(bool)
    contatar = np.asarray(contatar).astype(bool)
    cobranca_mensal = np.asarray(cobranca_mensal, dtype=float)

    alcancados = contatar & y_real
    receita = (alcancados * cobranca_mensal).sum() * p["taxa_sucesso"] * p["meses_horizonte"]
    custo = contatar.sum() * p["custo_contato"]
    return {
        "clientes_contatados": int(contatar.sum()),
        "churners_alcancados": int(alcancados.sum()),
        "receita_preservada": round(float(receita), 2),
        "custo_campanha": round(float(custo), 2),
        "retorno_liquido": round(float(receita - custo), 2),
    }
