class PrisonNames(object):
    ASP = 'ASP (AVENAL SP)'
    CAL = 'CAL (CALIPATRIA SP)'
    CCC = 'CCC (CA CORRECTIONAL CENTER)'
    CCI = 'CCI (CA CORRECTIONAL INSTITUTION)'
    CCWF = "CCWF (CENTRAL CA WOMEN'S FAC)"
    CEN = 'CEN (CENTINELA SP)'
    CHCF = 'CHCF (CA HEALTH CARE FAC - STOCKTON)'
    CIM = 'CIM (CA INSTITUTION FOR MEN)'
    CIW = 'CIW (CA INSTITUTION FOR WOMEN)'
    CMC = "CMC (CA MEN'S COLONY)"
    CMF = 'CMF (CA MEDICAL FAC)'
    COR = 'COR (CA SP, CORCORAN)'
    CRC_MEN = 'CRC (CAL REHAB CTR, MEN)'
    CRC_WOMEN = 'CRC (CAL REHAB CTR, WOMEN)'
    CTF = 'CTF (CORRECTIONAL TRAINING FAC)'
    CVSP = 'CVSP (CHUCKAWALLA VALLEY SP)'
    DVI = 'DVI (DEUEL VOCATIONAL INSTITUTION)'
    FOL_FEMALE = 'FOL (FOLSOM SP) (FEMALE)'
    FOL_MALE = 'FOL (FOLSOM SP) (MALE)'
    FRCC = 'FRCC (FRCCC BAKERSFIELD)'
    HDSP = 'HDSP (HIGH DESERT SP)'
    ISP = 'ISP (IRONWOOD SP)'
    KVSP = 'KVSP (KERN VALLEY SP)'
    LAC = 'LAC (CA SP, LOS ANGELES COUNTY)'
    MCSP = 'MCSP (MULE CREEK SP)'
    NCWF = "NCWF (NO CAL WOMEN'S FACIL)"
    NKSP = 'NKSP (NORTH KERN SP)'
    PBSP = 'PBSP (PELICAN BAY SP)'
    PVSP = 'PVSP (PLEASANT VALLEY SP)'
    RJD = 'RJD (RJ DONOVAN CORRECTIONAL FAC)'
    SAC = 'SAC (CA SP, SACRAMENTO)'
    SATF = 'SATF (CA SUBSTANCE ABUSE TREAT FAC)'
    SBRN = 'SBRN (SAN BRUNO CO. JAIL)'
    SCC = 'SCC (SIERRA CONSERVATION CENTER)'
    SOL = 'SOL (CA SP, SOLANO)'
    SRTA = 'SRTA (SANTA RITA CO. JAIL-RC)'
    SQ = 'SQ (SAN QUENTIN SP)'
    SVSP = 'SVSP (SALINAS VALLEY SP)'
    VSP = 'VSP (VALLEY SP)'
    WSP = 'WSP (WASCO SP)'


STANDARDIZED_PRISON_NAMES = {
    PrisonNames.ASP: PrisonNames.ASP,
    PrisonNames.CAL: PrisonNames.CAL,
    'CAL (CAL SP, CALIPATRIA)': PrisonNames.CAL,

    PrisonNames.CCC: PrisonNames.CCC,
    'CCC (CAL CORRECTL CTR)': PrisonNames.CCC,

    PrisonNames.CCI: PrisonNames.CCI,
    'CCI (CAL CORRECTL INSTITN)': PrisonNames.CCI,

    PrisonNames.CCWF: PrisonNames.CCWF,
    "CCWF (CENT CAL WOMEN'S FACIL)": PrisonNames.CCWF,

    PrisonNames.CEN: PrisonNames.CEN,
    'CEN (CAL SP, CENTINELA)': PrisonNames.CEN,

    PrisonNames.CHCF: PrisonNames.CHCF,
    'CHCF (CAL HEALTH CARE FACIL)': PrisonNames.CHCF,

    PrisonNames.CIM: PrisonNames.CIM,
    'CIM (CAL INSTITN FOR MEN)': PrisonNames.CIM,

    PrisonNames.CIW: PrisonNames.CIW,
    'CIW (CAL INST FOR WOMEN)': PrisonNames.CIW,

    PrisonNames.CMC: PrisonNames.CMC,
    "CMC (CAL MEN'S COLONY)": PrisonNames.CMC,

    PrisonNames.CMF: PrisonNames.CMF,
    'CMF (CAL MEDICAL FACIL)': PrisonNames.CMF,

    PrisonNames.COR: PrisonNames.COR,
    'COR (CAL SP, CORCORAN)': PrisonNames.COR,

    # In later years, the name doesn't include "men", but it is referring to the men's prison
    PrisonNames.CRC_MEN: PrisonNames.CRC_MEN,
    'CRC (CA REHABILITATION CENTER)': PrisonNames.CRC_MEN,

    PrisonNames.CRC_WOMEN: PrisonNames.CRC_WOMEN,

    PrisonNames.CTF: PrisonNames.CTF,
    'CTF (CORRECTL TRAINING FACIL)': PrisonNames.CTF,
    'CTF (CORRL TRAING FAC)': PrisonNames.CTF,

    PrisonNames.CVSP: PrisonNames.CVSP,

    PrisonNames.DVI: PrisonNames.DVI,
    'DVI (DEUEL VOCATL INSTITN)': PrisonNames.DVI,

    PrisonNames.FOL_FEMALE: PrisonNames.FOL_FEMALE,
    'FWF (FOLSOM WF) (FEMALE)': PrisonNames.FOL_FEMALE,

    PrisonNames.FOL_MALE: PrisonNames.FOL_MALE,
    PrisonNames.FRCC: PrisonNames.FRCC,

    PrisonNames.HDSP: PrisonNames.HDSP,
    'HDP (HIGH DESERT SP)': PrisonNames.HDSP,

    PrisonNames.ISP: PrisonNames.ISP,
    'IRON (IRONWOOD SP)': PrisonNames.ISP,

    PrisonNames.KVSP: PrisonNames.KVSP,

    PrisonNames.LAC: PrisonNames.LAC,
    'LAC (CAL SP, LOS ANGELES CO)': PrisonNames.LAC,
    'LARC (CAL SP RC, LOS ANGELES)': PrisonNames.LAC,

    PrisonNames.MCSP: PrisonNames.MCSP,
    PrisonNames.NCWF: PrisonNames.NCWF,
    PrisonNames.NKSP: PrisonNames.NKSP,
    PrisonNames.PBSP: PrisonNames.PBSP,
    PrisonNames.PVSP: PrisonNames.PVSP,

    PrisonNames.RJD: PrisonNames.RJD,
    'RJD (RJ DONOVAN CORR FACIL)': PrisonNames.RJD,

    PrisonNames.SAC: PrisonNames.SAC,
    'SAC (CAL SP, SACRAMENTO)': PrisonNames.SAC,

    PrisonNames.SATF: PrisonNames.SATF,
    'SATF (CAL SATF AND SP - COR)': PrisonNames.SATF,

    PrisonNames.SBRN: PrisonNames.SBRN,

    PrisonNames.SCC: PrisonNames.SCC,
    'SCC (SIERRA CONSERV CTR)': PrisonNames.SCC,

    PrisonNames.SOL: PrisonNames.SOL,
    'SOL (CAL SP, SOLANO)': PrisonNames.SOL,

    PrisonNames.SQ: PrisonNames.SQ,
    'SQ (CAL SP, SAN QUENTIN)': PrisonNames.SQ,

    PrisonNames.SRTA: PrisonNames.SRTA,

    PrisonNames.SVSP: PrisonNames.SVSP,
    'SVSP (SALINAS VAL SP)': PrisonNames.SVSP,

    PrisonNames.VSP: PrisonNames.VSP,
    'VSPM (VALLEY SP MEN)': PrisonNames.VSP,

    PrisonNames.WSP: PrisonNames.WSP,
}