#periodictable
from colorama import Style,Fore
universal_peridic_table=[
    {"atomic_mass":"1.0078 u","melting_point": "-259.14°C (14.01 K)","boiling_point":"-252.87°C (20.28 K)","discovery_date": 1766,"discovered_by":"Henry Cavendish",
    },
    {"atomic_mass":"6.9410 u","melting_point": "180.54°C (453.69 K)","boiling_point":"1342°C (1615.15 K)","discovery_date": 1817,"discovered_by":"Johan August Arfwedson",
    },
    {"atomic_mass":"22.990 u","melting_point": "97.82°C (370.97 K) ","boiling_point":" 882.85°C (1156 K) ","discovery_date": 1807,"discovered_by":"   Humphry  Davy  ",
    }
]
def color_dis_red():
    print(Fore.CYAN+" ___________________________________________________________________________________________________________________________________")
    print("|========================================================="+Fore.YELLOW+"Peridic Table"+Fore.CYAN+"=============================================================|")
    print("|___________________________________________________________________________________________________________________________________|")
def hidrozen():
    title="""_    _ 
| |  | |
| |__| |ydrogen is a chemical element; it has symbol H and atomic number 1.
|  __  |It is the lightest and most abundant chemical element in the universe,
| |  | |constituting about 75% of all normal matter.
|_|  |_|  """
    print(Fore.LIGHTYELLOW_EX,f"{title}")
    print(Fore.LIGHTCYAN_EX+"=====================================================================================================================================")
    print(Fore.LIGHTRED_EX+"||        Atomic Mass      ||"+Fore.YELLOW+"       Melting point       ||"+Fore.GREEN+"      boiling_point      ||"+Fore.YELLOW+"        discovered_by       ||"+Fore.LIGHTWHITE_EX+" discovery_date  |" )
    print(Fore.LIGHTCYAN_EX+"=====================================================================================================================================")

    for atom_name in universal_peridic_table:
        print(Fore.LIGHTMAGENTA_EX+f"|{atom_name['atomic_mass']:^25}  | {atom_name['melting_point']:>25} | {atom_name['boiling_point']:>25} |  {atom_name['discovered_by']:>25}  | {atom_name['discovery_date']:^15} |")
        print(Fore.LIGHTCYAN_EX+"=====================================================================================================================================")

color_dis_red()
hidrozen()