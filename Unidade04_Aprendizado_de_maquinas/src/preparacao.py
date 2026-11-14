"""Regras de preparação dos dados (Fase 3 do CRISP-DM).

As regras ficam neste módulo para que o mesmo código seja usado na
preparação (notebook 03) e na pontuação de novos clientes (notebook 06).
"""
import numpy as np
import pandas as pd

SERVICOS_ADICIONAIS = [
    "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies",
]


def preparar_dados(df_bruto: pd.DataFrame) -> pd.DataFrame:
    """Recebe a tabela bruta de clientes e devolve a tabela pronta para o modelo."""
    df = df_bruto.copy()

    # --- LIMPAR -----------------------------------------------------------
    # TotalCharges chega como texto; clientes recém-chegados (tenure = 0)
    # trazem um espaço em branco porque ainda não receberam fatura.
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["tenure"] * df["MonthlyCharges"])

    # "No internet service" / "No phone service" repetem a informação de
    # InternetService / PhoneService; viram simplesmente "No".
    df[SERVICOS_ADICIONAIS] = df[SERVICOS_ADICIONAIS].replace("No internet service", "No")
    df["MultipleLines"] = df["MultipleLines"].replace("No phone service", "No")

    # SeniorCitizen é a única coluna binária codificada como 0/1.
    df["SeniorCitizen"] = df["SeniorCitizen"].replace({0: "No", 1: "Yes"})

    # --- CONSTRUIR --------------------------------------------------------
    df["NumServicosAdicionais"] = (df[SERVICOS_ADICIONAIS] == "Yes").sum(axis=1)
    df["FaixaTenure"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, np.inf],
        labels=["00-12m", "13-24m", "25-48m", "49m+"],
    ).astype(str)

    # --- FORMATAR ---------------------------------------------------------
    # A variável-alvo só existe nos dados históricos.
    if "Churn" in df.columns:
        df["Churn"] = (df["Churn"] == "Yes").astype(int)

    return df
