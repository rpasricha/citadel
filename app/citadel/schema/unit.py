from enum import Enum
Unit = Enum("Unit", [
    'Atto',
    'LM-PER-W',
    'S-PER-M',
    'MM',
    'GigaC',
    'W-M2',
    'DEG_C-PER-HR',
    'OE-CM',
    'GRAD',
    'A-PER-M',
    'FT-PER-SEC2',
    'AT-PER-M',
    'PicoF',
    'PicoA',
    'MHO',
    'J-PER-KG',
    'M-K',
    'CD-PER-M2',
    'BTU-PER-LB-DEG_F',
    'Phot',
    'Yocto',
    'C-M',
    'SAMPLE-PER-SEC',
    'MilliH',
    'KiloA',
    'FT-PER-HR',
    'J-PER-MOL-K',
    'W-M2-PER-SR',
    'EV-PER-K',
    'KM',
    'ArcMIN',
    'GRAIN-PER-GAL',
    'C-PER-M3',
    'AbC-PER-CM2',
    'US_DRY_QT',
    'V-A',
    'ExaC',
    'C_MIL',
    'RAD-PER-SEC2',
    'StatC-PER-MOL',
    'C-M2',
    'A-PER-RAD',
    'DEG_R-HR-PER-BTU',
    'DeciM',
    'StatH',
    'KiloCAL',
    'FBM',
    'AbV-PER-CM',
    'StatV',
    'J-PER-KG-K-M3',
    'VoltMeter',
    'THM',
    'ZeptoC',
    'MIL',
    'GigaEV',
    'Day',
    'A-PER-J',
    'DEG_R-PER-HR',
    'MIN-Angle',
    'M2-K-PER-W',
    'Exbi',
    'MicroA',
    'FT2-DEG_R',
    'CM-SEC-DEG_C',
    'GAL_US-PER-DAY',
    'Debye',
    'MilliRAD',
    'YottaC',
    'PARSEC',
    'KHZ',
    'MC',
    'DAY_Sidereal',
    'BBL',
    'HZ-PER-K',
    'FT2',
    'DEG_F-PER-MIN',
    'FT2-HR-DEG_F',
    'Femto',
    'M3-PER-HR',
    'M3',
    'ST',
    'AT',
    'MicroIN',
    'MicroC',
    'Hecto',
    'KW',
    'FemtoC',
    'MinuteTime',
    'M2',
    'CLO',
    'BTU_TH',
    'Mebi',
    'PER-T-M',
    'ElementaryCharge',
    'SEC2',
    'GAL_US-PER-MIN',
    'AbT',
    'M3-PER-K',
    'KN',
    'StatC-PER-CM2',
    'PER-H',
    'AbOHM',
    'C3-M-PER-J2',
    'MI2',
    'H-PER-M',
    'DecaC',
    'ThermEEC',
    'MicroG',
    'HZ-PER-V',
    'LB-DEG_R',
    'BUI',
    'Micro',
    'K-PER-SEC',
    'LM',
    'REV-PER-MIN',
    'MilliA',
    'CM2-MIN',
    'K-PER-T',
    'StatV-PER-CM',
    'C-PER-M',
    'K-PER-MIN',
    'DEG_F-PER-SEC',
    'C-M2-PER-V',
    'DEG-PER-HR',
    'Exa',
    'RAD',
    'PER-M3',
    'J-PER-KG-K-PA',
    'DEG_F',
    'ANGSTROM',
    'CentiC',
    'StatMHO',
    'M3-PER-KG-SEC2',
    'PT',
    'SiderealDay',
    'M-PER-F',
    'DEG_F-HR-PER-BTU',
    'FemtoM',
    'MilliM',
    'CORD',
    'PINT',
    'TSP',
    'PER-HR',
    'PCA',
    'BTU-PER-LB-DEG_R',
    'MegaEV-FemtoM',
    'Tera',
    'SquareFootHourDegreeFahrenheitPerBtu',
    'LM-SEC',
    'PERCENT',
    'DECADE',
    'W-PER-M2-K',
    'J-PER-M4',
    'K-PER-HR',
    'FT3',
    'KiloHZ',
    'StatH-PER-CM',
    'RD',
    'Yobi',
    'YD2',
    'K-PER-W',
    'Centi',
    'MegaHZ',
    'IN',
    'AbV',
    'MHz',
    'MeV-PER-c',
    'AbF-PER-CM',
    'Yotta',
    'FT',
    'AC-FT',
    'MeV',
    'MI-PER-HR',
    'LongFUR',
    'Wb-M',
    'LB-MOL-DEG_R',
    'L',
    'HourSidereal',
    'IN-PER-SEC',
    'A-PER-DEGC',
    'FR',
    'DEG_R-HR',
    'Kibi',
    'AbF',
    'LUX',
    'W-PER-M2-SR',
    'FT2-DEG_F',
    'BIOT',
    'AbH',
    'AbA-CM2',
    'PK',
    'REV-PER-HR',
    'Tebi',
    'TeslaMeter',
    'MicroF',
    'HZ-PER-M',
    'Gamma',
    'M2-K',
    'DEG2',
    'IN2',
    'FA',
    'Giga',
    'Milli',
    'DEG_R-PER-SEC',
    'YR_Sidereal',
    'C',
    'HR',
    'CUP',
    'J-PER-T',
    'C4-M4-PER-J3',
    'FARAD',
    'WEBER',
    'GallonUS',
    'MilliG',
    'V-PER-M2',
    'Gs',
    'M3-PER-KG',
    'M2-SR',
    'PER-MIN',
    'HR_Sidereal',
    'BTU-PER-DEG_R',
    'MicroRAD',
    'US_DRY_PINT',
    'MeV-PER-CM',
    'AU',
    'KN-PER-SEC',
    'M3-PER-SEC2',
    'OERSTED',
    'FT2-PER-HR',
    'S-M2-PER-MOL',
    'US_DRY_GAL',
    'MicroH',
    'Deka',
    'CD-PER-IN2',
    'FUR_Long',
    'AbV-SEC',
    'CM2-SEC',
    'MI3',
    'AC',
    'MegaHZ-PER-T',
    'Mega',
    'REL-PERMEABILITY',
    'Zetta',
    'AttoC',
    'FM',
    'GAL_IMP',
    'YR_365Day',
    'C-PER-MOL',
    'CAL',
    'YearTropical',
    'StatV-CM',
    'GallonUSPerDay',
    'DEG_C-PER-MIN',
    'MIN_Sidereal',
    'SquareFootPerBtuInch',
    'LB-MOL-DEG_F',
    'KiloCAL-PER-MIN',
    'M-PER-SEC2',
    'DEG',
    'PicoFarad',
    'NMI-PER-HR',
    'GigaHZ',
    'Kilo',
    'FT2-HR-DEG_R',
    'HZ',
    'FC',
    'SH',
    'KiloEV-PER-MicroM',
    'CM-PER-SEC2',
    'G-DEG_C',
    'MilLength',
    'HA',
    'AH',
    'AbA-PER-CM2',
    'RAD-PER-HR',
    'A',
    'NUM-PER-YR',
    'GAL_US',
    'KM-PER-HR',
    'K',
    'M-PER-K',
    'DeciC',
    'Deca',
    'UnitPole',
    'REL-PERMITTIVITY',
    'OZ_US',
    'IN3-PER-MIN',
    'DEG-PER-SEC',
    'DEG_R-PER-MIN',
    'PINT_US_Dry',
    'YD',
    'NMI-PER-MIN',
    'Gibi',
    'YD3-PER-MIN',
    'V-PER-SEC',
    'KiloCAL-PER-SEC',
    'DEG_R',
    'EV-PER-T',
    'M-PER-MIN',
    'KiloCAL-PER-MOL-DEG_C',
    'Year365Day',
    'OHM',
    'NanoA',
    'KiloEV',
    'YD3',
    'ZettaC',
    'FT-PER-MIN',
    'CP',
    'CM2',
    'J-PER-T2',
    'RT',
    'ARCMIN',
    'FT-LBF-SEC',
    'SiderealYear',
    'KM-PER-SEC',
    'QT_US_Dry',
    'C2-M-PER-J',
    'MI_US',
    'MegaHZ-PER-K',
    'FT3-PER-SEC',
    'GON',
    'UNITLESS',
    'M-PER-HR',
    'StatOHM',
    'KiloC',
    'IN-PER-SEC2',
    'H',
    'StatS',
    'C-PER-M2',
    'Pebi',
    'StatF',
    'N-PER-C',
    'PER-SEC',
    'HR-FT2',
    'GR',
    'ArcSEC',
    'M-K-PER-W',
    'STILB',
    'TBSP',
    'QT',
    'NP',
    'Zepto',
    'ARE',
    'M3-PER-SEC',
    'A-PER-M2',
    'NanoF',
    'At-PER-IN',
    'W-PER-SR',
    'GAL',
    'TeslaSecond',
    'NUM',
    'Deci',
    'S',
    'REV-PER-SEC',
    'MACH',
    'C-PER-KG',
    'DEG-PER-SEC2',
    'SiderealMinute',
    'NMI',
    'MinuteSidereal',
    'BUA',
    'KG-K',
    'LY',
    'DWT',
    'LB-DEG_F',
    'CM-PER-SEC',
    'MI-PER-MIN',
    'V-PER-M',
    'AbC',
    'M-KG',
    'J-PER-K',
    'PT_US',
    'F-PER-M',
    'YoctoC',
    'Peta',
    'SEC',
    'AbS',
    'QT_US',
    'GI',
    'M2-PER-K',
    'HZ-PER-T',
    'ARCSEC',
    'FT2-SEC-DEG_F',
    'StatA',
    'PER-M',
    'StatC',
    'G',
    'FT-PER-SEC',
    'LA',
    'FT3-PER-MIN',
    'RAD-PER-SEC',
    'DAY',
    'PetaC',
    'DEG_F-PER-HR',
    'AbA',
    'DEG_F-HR',
    'IN3',
    'DEG-PER-MIN',
    'M',
    'FARADAY',
    'KM3-PER-SEC2',
    'VOLT',
    'KiloCAL-PER-GM-DEG_C',
    'MX',
    'NanoC',
    'RAD-PER-MIN',
    'PER-T-SEC',
    'MilliC',
    'SR',
    'DIOPTER',
    'FATH',
    'TeraC',
    'HectoC',
    'StatA-PER-CM2',
    'MI-US',
    'REV',
    'CH',
    'M-PER-SEC',
    'T',
    'CM',
    'S2-FT',
    'FT2-SEC-DEG_R',
    'FT_US',
    'PicoC',
    'FT-L',
    'ROD',
    'Pico',
    'Zebi',
    'DEG_C-PER-SEC',
    'Nano',
    'MicroM',
    'MBTU-PER-MIN',
    'Gallons-PER-HOUR',
    'MBTU',
    'KiloW-HR',
    'KW-reactive',
    'PowerFactor',
    'PercentReletiveHumidity',
    'Pounds-force-per-square-inch',
    'Inches-of-water',
    'MIN',
    'GAL-PER-MIN',
    'No-units',
    'Parts-per-million',
    'Percent',
    'Revolutions-per-minute-BACNet',
    'MegaW-HR',
    ])
