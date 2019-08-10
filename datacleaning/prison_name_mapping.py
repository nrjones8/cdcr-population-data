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
    SQ_FEMALE = 'SQ (SAN QUENTIN SP) (FEMALE)'
    SVSP = 'SVSP (SALINAS VALLEY SP)'
    VSP = 'VSP (VALLEY SP)'
    WSP = 'WSP (WASCO SP)'

STANDARDIZED_PRISON_NAMES = {
    PrisonNames.ASP: PrisonNames.ASP,
    'Avenal State Prison (ASP)': PrisonNames.ASP,


    PrisonNames.CAL: PrisonNames.CAL,
    'CAL (CAL SP, CALIPATRIA)': PrisonNames.CAL,
    'Calipatria State Prison (CAL)': PrisonNames.CAL,

    PrisonNames.CCC: PrisonNames.CCC,
    'CCC (CAL CORRECTL CTR)': PrisonNames.CCC,
    'California Correctional Center (CCC)': PrisonNames.CCC,

    PrisonNames.CCI: PrisonNames.CCI,
    'CCI (CAL CORRECTL INSTITN)': PrisonNames.CCI,
    'California Correctional Institution (CCI)': PrisonNames.CCI,

    PrisonNames.CCWF: PrisonNames.CCWF,
    "CCWF (CENT CAL WOMEN'S FACIL)": PrisonNames.CCWF,
    "Central California Women's Facility (CCWF)": PrisonNames.CCWF,

    PrisonNames.CEN: PrisonNames.CEN,
    'CEN (CAL SP, CENTINELA)': PrisonNames.CEN,
    'Centinela State Prison (CEN)': PrisonNames.CEN,

    PrisonNames.CHCF: PrisonNames.CHCF,
    'CHCF (CAL HEALTH CARE FACIL)': PrisonNames.CHCF,
    'California Health Care Facility - Stockton (CHCF)': PrisonNames.CHCF,

    PrisonNames.CIM: PrisonNames.CIM,
    'CIM (CAL INSTITN FOR MEN)': PrisonNames.CIM,
    'California Institution for Men (CIM)': PrisonNames.CIM,

    PrisonNames.CIW: PrisonNames.CIW,
    'CIW (CAL INST FOR WOMEN)': PrisonNames.CIW,
    'California Institution for Women (CIW)': PrisonNames.CIW,

    PrisonNames.CMC: PrisonNames.CMC,
    "CMC (CAL MEN'S COLONY)": PrisonNames.CMC,
    "California Men's Colony (CMC)": PrisonNames.CMC,

    PrisonNames.CMF: PrisonNames.CMF,
    'CMF (CAL MEDICAL FACIL)': PrisonNames.CMF,
    'California Medical Facility (CMF)': PrisonNames.CMF,

    PrisonNames.COR: PrisonNames.COR,
    'COR (CAL SP, CORCORAN)': PrisonNames.COR,
    'California State Prison, Corcoran (COR)': PrisonNames.COR,

    # In later years, the name doesn't include "men", but it is referring to the men's prison
    PrisonNames.CRC_MEN: PrisonNames.CRC_MEN,
    'CRC (CA REHABILITATION CENTER)': PrisonNames.CRC_MEN,
    'California Rehabilitation Center (CRC)': PrisonNames.CRC_MEN,

    PrisonNames.CRC_WOMEN: PrisonNames.CRC_WOMEN,

    PrisonNames.CTF: PrisonNames.CTF,
    'CTF (CORRECTL TRAINING FACIL)': PrisonNames.CTF,
    'CTF (CORRL TRAING FAC)': PrisonNames.CTF,
    'Correctional Training Facility (CTF)': PrisonNames.CTF,

    PrisonNames.CVSP: PrisonNames.CVSP,
    'Chuckawalla Valley State Prison (CVSP)': PrisonNames.CVSP,

    PrisonNames.DVI: PrisonNames.DVI,
    'DVI (DEUEL VOCATL INSTITN)': PrisonNames.DVI,
    'Deuel Vocational Institution (DVI)': PrisonNames.DVI,

    PrisonNames.FOL_FEMALE: PrisonNames.FOL_FEMALE,
    'FWF (FOLSOM WF) (FEMALE)': PrisonNames.FOL_FEMALE,
    'Folsom State Prison (FOL) (FEMALE)': PrisonNames.FOL_FEMALE,

    PrisonNames.FOL_MALE: PrisonNames.FOL_MALE,
    'Folsom State Prison (FOL) (MALE)': PrisonNames.FOL_MALE,

    PrisonNames.FRCC: PrisonNames.FRCC,

    PrisonNames.HDSP: PrisonNames.HDSP,
    'HDP (HIGH DESERT SP)': PrisonNames.HDSP,
    'High Desert State Prison (HDSP)': PrisonNames.HDSP,

    PrisonNames.ISP: PrisonNames.ISP,
    'IRON (IRONWOOD SP)': PrisonNames.ISP,
    'Ironwood State Prison (ISP)': PrisonNames.ISP,

    PrisonNames.KVSP: PrisonNames.KVSP,
    'Kern Valley State Prison (KVSP)': PrisonNames.KVSP,

    PrisonNames.LAC: PrisonNames.LAC,
    'LAC (CAL SP, LOS ANGELES CO)': PrisonNames.LAC,
    'LARC (CAL SP RC, LOS ANGELES)': PrisonNames.LAC,
    'California State Prison, Los Angeles County (LAC)': PrisonNames.LAC,

    PrisonNames.MCSP: PrisonNames.MCSP,
    'Mule Creek State Prison (MCSP)': PrisonNames.MCSP,

    PrisonNames.NCWF: PrisonNames.NCWF,

    PrisonNames.NKSP: PrisonNames.NKSP,
    'North Kern State Prison (NKSP)': PrisonNames.NKSP,

    PrisonNames.PBSP: PrisonNames.PBSP,
    'Pelican Bay State Prison (PBSP)': PrisonNames.PBSP,

    PrisonNames.PVSP: PrisonNames.PVSP,
    'Pleasant Valley State Prison (PVSP)': PrisonNames.PVSP,

    PrisonNames.RJD: PrisonNames.RJD,
    'RJD (RJ DONOVAN CORR FACIL)': PrisonNames.RJD,
    'RJ Donovan Correctional Facility (RJD)': PrisonNames.RJD,

    PrisonNames.SAC: PrisonNames.SAC,
    'SAC (CAL SP, SACRAMENTO)': PrisonNames.SAC,
    'California State Prison, Sacramento (SAC)': PrisonNames.SAC,

    PrisonNames.SATF: PrisonNames.SATF,
    'SATF (CAL SATF AND SP - COR)': PrisonNames.SATF,
    'California Substance Abuse Treatment Facility (SATF)': PrisonNames.SATF,

    PrisonNames.SBRN: PrisonNames.SBRN,

    PrisonNames.SCC: PrisonNames.SCC,
    'SCC (SIERRA CONSERV CTR)': PrisonNames.SCC,
    'Sierra Conservation Center (SCC)': PrisonNames.SCC,

    PrisonNames.SOL: PrisonNames.SOL,
    'SOL (CAL SP, SOLANO)': PrisonNames.SOL,
    'California State Prison, Solano (SOL)': PrisonNames.SOL,

    PrisonNames.SQ: PrisonNames.SQ,
    'SQ (CAL SP, SAN QUENTIN)': PrisonNames.SQ,
    'San Quentin State Prison (SQ)': PrisonNames.SQ,

    # Reports from pre-2019 didn't have any women at San Quentin; so the previous PDFs assume
    # that SQ is men, but we specify explicitly here for 2019 and on.
    PrisonNames.SQ_FEMALE: PrisonNames.SQ_FEMALE,

    PrisonNames.SRTA: PrisonNames.SRTA,

    PrisonNames.SVSP: PrisonNames.SVSP,
    'SVSP (SALINAS VAL SP)': PrisonNames.SVSP,
    'Salinas Valley State Prison (SVSP)': PrisonNames.SVSP,

    PrisonNames.VSP: PrisonNames.VSP,
    'VSPM (VALLEY SP MEN)': PrisonNames.VSP,
    'Valley State Prison (VSP)': PrisonNames.VSP,

    PrisonNames.WSP: PrisonNames.WSP,
    'Wasco State Prison (WSP)': PrisonNames.WSP
}