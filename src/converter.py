def mxn_to_usd(mxn):
    """Convierte Pesos Mexicanos a Dólares.

    Args:
        mxn (float): Cantidad en Pesos Mexicanos

    Returns:
        float: Cantidad en Dólares Estadounidenses
    """
    tipo_cambio = 17.3  # 1 USD = 17.3 MXN (ejemplo)
    return round(mxn / tipo_cambio, 2)


def usd_to_mxn(usd):
    """Convierte Dólares a Pesos Mexicanos.

    Args:
        usd (float): Cantidad en Dólares

    Returns:
        float: Cantidad en Pesos Mexicanos
    """
    tipo_cambio = 17.3
    return round(usd * tipo_cambio, 2)


def mxn_to_eur(mxn):
    """Convierte Pesos Mexicanos a Euros.

    Args:
        mxn (float): Cantidad en Pesos Mexicanos

    Returns:
        float: Cantidad en Euros
    """
    tipo_cambio = 18.9  # 1 EUR = 18.9 MXN (ejemplo)
    return round(mxn / tipo_cambio, 2)


def eur_to_mxn(eur):
    """Convierte Euros a Pesos Mexicanos.

    Args:
        eur (float): Cantidad en Euros

    Returns:
        float: Cantidad en Pesos Mexicanos
    """
    tipo_cambio = 18.9
    return round(eur * tipo_cambio, 2)
