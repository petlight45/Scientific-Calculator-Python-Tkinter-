from tkinter import *
from math import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import pyperclip
import threading
import time


def highest_val_in_lst_id(list):
    highest_val = -1000000000.0
    list_id = 0
    for data in list:
        if data > highest_val:
            highest_val = data
            highest_id = list_id
        list_id += 1
    return highest_id


def arg_dist_conv(list):
    new_list = []
    for data in list:
        arg_dist = abso(data - 180)
        new_list.append(arg_dist)
    return new_list


def abso(x):
    return float(str(x).replace("-", ""))


def degrees_to_radians(x):
    answer = round((pi / 180) * x, 4)
    return answer


def radians_to_degrees(x):
    answer = round((180 / pi) * x, 4)
    return answer


def rpn(num):
    if "-" in str(num):
        return "negative"
    else:
        return "positive"


def vector_product_calc(a, b, c, d, e, f):
    determinant_i = t_by_2_md(b, c, e, f)
    determinant_j = - 1 * (t_by_2_md(a, c, d, f))
    determinant_k = t_by_2_md(a, b, d, e)
    if determinant_j < 0:
        determinant = str(determinant_i) + "i " + " - " + str(determinant_j * (-1)) + "j"
    else:
        determinant = str(determinant_i) + "i " + " + " + str(determinant_j) + "j"
    if determinant_k < 0:
        determinant = str(determinant) + " - " + str(determinant_k * (-1)) + "k"
    else:
        determinant = str(determinant) + " + " + str(determinant_k) + "k"
    return determinant


def get_mode(list):
    mode = 0
    occurences = 0
    for data in list:
        count = 0
        for data_2 in list:
            if data_2 == data:
                count += 1
        if count > occurences:
            occurences = count
            mode = data
    return mode


def sort_list(list):
    list_2 = []
    val = pow(10, 10)
    start = 0
    while start < len(list):
        smallest_id = 0
        line_no = 0
        smallest_val = 10000000000000000.0
        if list == []:
            break
        for data in list:
            if data < smallest_val:
                smallest_id = line_no
                smallest_val = data
            line_no += 1
        list_2.append(smallest_val)
        temp_list_1 = list[0:smallest_id]
        if smallest_id == len(list) - 1:
            temp_list_2 = []
        else:
            temp_list_2 = list[smallest_id + 1:]
        list.clear()
        for data in temp_list_1:
            list.append(data)
        for data in temp_list_2:
            list.append(data)
    return list_2


def absolute(x):
    value = str(x)
    value = value.replace("-", "")
    if "." in value:
        answer = float(value)
        return answer
    else:
        answer = int(value)
        return answer


constants_label = [
    "Speed of light (c) ms" + chr(0x207B) + chr(0x00B9) + ")",
    "Charge of an electron (e) C",
    "Universal gravitational constant (G)' Nm" + chr(0x00B2) + "/kg" + chr(0x00B2),
    "Planck's constant (h) Js",
    "Dirac's constant (h) Js",
    "Boltzmann's constant (k) JK" + chr(0x207B) + chr(0x00B9) + ")",
    "Avogadro's constant (NA) mol" + chr(0x207B) + chr(0x00B9) + ")",
    "Faraday's constant (F) Cmol" + chr(0x207B) + chr(0x00B9) + ")",
    "Ideal gas constant (R) JK" + chr(0x207B) + chr(0x00B9) + "mol" + chr(0x207B) + chr(0x00B9) + ")",
    "Mass of an electron (me) kg",
    "Mass of a proton (mp) kg",
    "Mass of a neutron (mn) kg",
    "Atomic mass unit (u, amu or Da) kg",
    "Permittivity of free space (e0)",
    "Coulomb's constant (K) Nm" + chr(0x00B2) + "C" + chr(0x207B) + chr(0x00B2),
    "Permeability of free space (μ0) NA" + chr(0x207B) + chr(0x00B2),
    "Rydberg constant (R8) m" + chr(0x207B) + chr(0x00B9) + ")",
    "Bohr radius (a0) m"
]
constants = [
    "299792458",
    "1.602176565 *(10**(-19))",
    "6.67384*(10**(-11))",
    "6.626070040*(10**(-34))",
    "1.054571800*(10**(-34))",
    "1.3806488*(10**(-23))",
    "6.022140857*(10**(23))",
    "96485.3365",
    "8.3144621",
    "9.10938291*(10**(-31))",
    "1.672621777*(10**(-27))",
    "1.674927351*(10**(-27))",
    "1.660538921*(10**(-27))",
    "8.854187817*(10**(-12))",
    "8.9875517973681764*(10**(9))",
    "4*3.142*(10**(-7))",
    "1.0973731568539*(10**(-7))",
    "5.2917721092*(10**(-11))",
]

charges_data = [
    '1  hydrogen  1+',
    '2  helium  0',
    '3  lithium  1+',
    '4  beryllium  2+',
    '5  boron  3-, 3+',
    '6  carbon  4+',
    '7  nitrogen  3-',
    '8  oxygen  2-',
    '9  fluorine  1-',
    '10  neon  0',
    '11  sodium  1+',
    '12  magnesium  2+',
    '13  aluminum  3+',
    '14  silicon  4+, 4-',
    '15  phosphorus  5+, 3+, 3-',
    '16  sulfur  2-, 2+, 4+, 6+',
    '17  chlorine  1-',
    '18  argon  0',
    '19  potassium  1+',
    '20  calcium  2+',
    '21  scandium  3+',
    '22  titanium  4+, 3+',
    '23  vanadium  2+, 3+, 4+, 5+',
    '24  chromium  2+, 3+, 6+',
    '25  manganese  2+, 4+, 7+',
    '26  iron  2+, 3+',
    '27  cobalt  2+, 3+',
    '28  nickel  2+',
    '29  copper  1+, 2+',
    '30  zinc  2+',
    '31  gallium  3+',
    '32  germanium  4-, 2+, 4+',
    '33  arsenic  3-, 3+, 5+',
    '34  selenium  2-, 4+, 6+',
    '35  bromine  1-, 1+, 5+',
    '36  krypton  0',
    '37  rubidium  1+',
    '38  strontium  2+',
    '39  yttrium  3+',
    '40  zirconium  4+',
    '41  niobium  3+, 5+',
    '42  molybdenum  3+, 6+',
    '43  technetium  6+',
    '44  ruthenium  3+, 4+, 8+',
    '45  rhodium  4+',
    '46  palladium  2+, 4+',
    '47  silver  1+',
    '48  cadmium  2+',
    '49  indium  3+',
    '50  tin  2+, 4+',
    '51  antimony  3-, 3+, 5+',
    '52  tellurium  2-, 4+, 6+',
    '53  iodine  1-',
    '54  xenon  0',
    '55  cesium  1+',
    '56  barium  2+',
    '57  lanthanum  3+',
    '58  cerium  3+, 4+',
    '59  praseodymium  3+',
    '60  neodymium  3+, 4+',
    '61  promethium  3+',
    '62  samarium  3+',
    '63  europium  3+',
    '64  gadolinium  3+',
    '65  terbium  3+, 4+',
    '66  dysprosium  3+',
    '67  holmium  3+',
    '68  erbium  3+',
    '69  thulium  3+',
    '70  ytterbium  3+',
    '71  lutetium  3+',
    '72  hafnium  4+',
    '73  tantalum  5+',
    '74  tungsten  6+',
    '75  rhenium  2+, 4+, 6+, 7+',
    '76  osmium  3+, 4+, 6+, 8+',
    '77  iridium  3+, 4+, 6+',
    '78  platinum  2+, 4+, 6+',
    '79  gold  1+, 2+, 3+',
    '80  mercury  1+, 2+',
    '81  thallium  1+, 3+',
    '82  lead  2+, 4+',
    '83  bismuth  3+',
    '84  polonium  2+, 4+',
    '85  astatine  ?',
    '86  radon  0',
    '87  francium  ?',
    '88  radium  2+',
    '89  actinium  3+',
    '90  thorium  4+',
    '91  protactinium  5+',
    '92  uranium  3+, 4+, 6+',
]

electronegativity_data = [
    "Hydrogen  2.20",
    "Helium  no data",
    "Lithium  0.98",
    "Beryllium  1.57",
    "Boron  2.04",
    "Carbon  2.55",
    "Nitrogen  3.04",
    "Oxygen  3.44",
    "Fluorine  3.98",
    "Neon  no data",
    "Sodium  0.93",
    "Magnesium  1.31",
    "Aluminum  1.61",
    "Silicon  1.90",
    "Phosphorus  2.19",
    "Sulfur  2.58",
    "Chlorine  3.16",
    "Argon  no data",
    "Potassium  0.82",
    "Calcium  1.00",
    "Scandium  1.36",
    "Titanium  1.54",
    "Vanadium  1.63",
    "Chromium  1.66",
    "Manganese  1.55",
    "Iron  1.83",
    "Cobalt  1.88",
    "Nickel  1.91",
    "Copper  1.90",
    "Zinc  1.65",
    "Gallium  1.81",
    "Germanium  2.01",
    "Arsenic  2.18",
    "Selenium  2.55",
    "Bromine  2.96",
    "Krypton  3.00",
    "Rubidium  0.82",
    "Strontium  0.95",
    "Yttrium  1.22",
    "Zirconium  1.33",
    "Niobium  1.6",
    "Molybdenum  2.16",
    "Technetium  1.9",
    "Ruthenium  2.2",
    "Rhodium  2.28",
    "Palladium  2.20",
    "Silver  1.93",
    "Cadmium  1.69",
    "Indium  1.78",
    "Tin  1.96",
    "51  Sb  Antimony  2.05",
    "52  Te  Tellurium  2.1",
    "53  I  Iodine  2.66",
    "54  Xe  Xenon  2.6",
    "55  Cs  Cesium  0.79",
    "56  Ba  Barium  0.89",
    "57  La  Lanthanum  1.10",
    "58  Ce  Cerium  1.12",
    "59  Pr  Praseodymium  1.13",
    "60  Nd  Neodymium  1.14",
    "61  Pm  Promethium  1.13",
    "62  Sm  Samarium  1.17",
    "63  Eu  Europium  1.2",
    "64  Gd  Gadolinium  1.2",
    "65  Tb  Terbium  1.22",
    "66  Dy  Dysprosium  1.23",
    "67  Ho  Holmium  1.24",
    "68  Er  Erbium  1.24",
    "69  Tm  Thulium  1.25",
    "70  Yb  Ytterbium  1.1",
    "71  Lu  Lutetium  1.27",
    "72  Hf  Hafnium  1.3",
    "73  Ta  Tantalum  1.5",
    "74  W  Tungsten  2.36",
    "75  Re  Rhenium  1.9",
    "76  Os  Osmium  2.2",
    "77  Ir  Iridium  2.2",
    "78  Pt  Platinum  2.28",
    "79  Au  Gold  2.54",
    "80  Hg  Mercury  2.00",
    "81  Tl  Thallium  1.62",
    "82  Pb  Lead  2.33",
    "83  Bi  Bismuth  2.02",
    "84  Po  Polonium  2.0",
    "85  At  Astatine  2.2",
    "86  Rn  Radon  no data",
    "87  Fr  Francium  0.7",
    "88  Ra  Radium  0.89",
    "89  Ac  Actinium  1.1",
    "90  Th  Thorium  1.3",
    "91  Pa  Protactinium  1.5",
    "92  U  Uranium  1.38",
    "93  Np  Neptunium  1.36",
    "94  Pu  Plutonium  1.28",
    "95  Am  Americium  1.3",
    "96  Cm  Curium  1.3",
    "97  Bk  Berkelium  1.3",
    "98  Cf  Californium  1.3",
    "99  Es  Einsteinium  1.3",
    "100  Fm  Fermium  1.3",
    "101  Md  Mendelevium  1.3",
    "102  No  Nobelium  1.3",
    "103  Lr  Lawrencium  no data",
    "104  Rf  Rutherfordium  no data",
    "105  Db  Dubnium  no data",
    "106  Sg  Seaborgium  no data",
    "107  Bh  Bohrium  no data",
    "108  Hs  Hassium  no data",
    "109  Mt  Meitnerium  no data",
    "110  Ds  Darmstadtium  no data",
    "111  Rg  Roentgenium  no data",
    "112  Cn  Copernicium  no data",
    "113  Nh  Nihonium  no data",
    "114  Fl  Flerovium  no data",
    "115  Mc  Moscovium  no data",
    "116  Lv  Livermorium  no data",
    "117  Ts  Tennessine  no data",
    "118  Og  Oganesson  no data",
]
list_element = [
    "Actinium  symbol:Ac  atomic_no:89  molecular_mass:227.028  melting_point:1050  boiling_point:3200±300",
    "Aluminum  symbol:Al  atomic_no:13  molecular_mass:26.981539(5)  melting_point:660.37  boiling_point:2467",
    "Americium  symbol:Am  atomic_no:95  molecular_mass:243  melting_point:994±4  boiling_point:2607",
    "Antimony  symbol:Sb  atomic_no:51  molecular_mass:121.757  melting_point:630.74  boiling_point:1750",
    "Argon    symbol:Ar  atomic_no:18  molecular_mass:39.948(1)  melting_point:-189.2  boiling_point:-185.7",
    "Arsenic  symbol:As  atomic_no:33  molecular_mass:74.92159(2)  melting_point:817 (28 atm)  boiling_point:613(sublimes)",
    "Astatine  symbol:At  atomic_no:85  molecular_mass:210  melting_point:302  boiling_point:337",
    "Barium    symbol:Ba  atomic_no:56  molecular_mass:137.327(7)  melting_point:725  boiling_point:1640",
    "Berkelium  symbol:Bk  atomic_no:97  molecular_mass:247  melting_point:Unknown  boiling_point:Unknown",
    "Beryllium  symbol:Be  atomic_no:4     molecular_mass:9.012182(3)  melting_point:1278±5  boiling_point:2970(5 torr)",
    "Bismuth  symbol:Bi  atomic_no:83  molecular_mass:208.98037(3)  melting_point:271.3  boiling_point:1560±5",
    "Bohrium  symbol:Bh  atomic_no:107  molecular_mass:262  melting_point:2079  boiling_point:2550(sublimes)",
    "Boron    symbol:B  atomic_no:5      molecular_mass:10.811(5)  melting_point:-7.2  boiling_point:58.78",
    "Bromine  symbol:Br  atomic_no:35  molecular_mass:79.904  melting_point:320.9  boiling_point:765",
    "Cadmium  symbol:Cd  atomic_no:48  molecular_mass:112.411(8)  melting_point:28.40±0.01  boiling_point:669.3",
    "Calcium  symbol:Ca  atomic_no:20  molecular_mass:40.078(9)  melting_point:839±2  boiling_point:1484",
    "Californium    symbol:Cf  atomic_no:98  molecular_mass:251  melting_point:Unknown  boiling_point:Unknown",
    "Carbon    symbol:C  atomic_no:6      molecular_mass:12.011(1)  melting_point:3652(sublimes)",
    "Cerium    symbol:Ce  atomic_no:58  molecular_mass:140.115(4)  melting_point:798  boiling_point:3443",
    "Cesium    symbol:Cs  atomic_no:55  molecular_mass:132.90543(5)  melting_point:28.40±0.01  boiling_point:669.3",
    "Chlorine  symbol:Cl  atomic_no:17  molecular_mass:35.4527(9)  melting_point:-100.98  boiling_point:-34.6",
    "Chromium  symbol:Cr  atomic_no:24  molecular_mass:51.9961(6)  melting_point:1857±20  boiling_point:2672",
    "Cobalt    symbol:Co  atomic_no:27  molecular_mass:58.93320(1)  melting_point:1495  boiling_point:2870",
    "Copper    symbol:Cu  atomic_no:29  molecular_mass:63.546(3)  melting_point:1083.4±0.2  boiling_point:2567",
    "Curium    symbol:Cm  atomic_no:96  molecular_mass:247  melting_point:1340±40",
    "Dubnium    symbol:Db  atomic_no:105  2molecular_mass:62  melting_point:Unknown  boiling_point:Unknown",
    "Dysprosium  symbol:Dy  atomic_no:66  molecular_mass:162.50(3)  melting_point:1412  boiling_point:2567",
    "Einsteinium  symbol:Es  atomic_no:99  molecular_mass:252  melting_point:Unknown  boiling_point:Unknown",
    "Erbium    symbol:Er  atomic_no:68  molecular_mass:167.26(3)  melting_point:1529  boiling_point:2868",
    "Europium  symbol:Eu  atomic_no:63  molecular_mass:151.965(9)  melting_point:822  boiling_point:1527",
    "Fermium    symbol:Fm  atomic_no:100  molecular_mass:257  melting_point:Unknown  boiling_point:Unknown",
    "Fluorine  symbol:F  atomic_no:9      molecular_mass:18.9984032(9)  melting_point:-219.62  boiling_point:-188.4",
    "Francium  symbol:Fr  atomic_no:87  molecular_mass:223  melting_point:27  boiling_point:677",
    "Gadolinium  symbol:Gd  atomic_no:64  molecular_mass:157.25(3)  melting_point:1313  boiling_point:3273",
    "Gallium    symbol:Ga  atomic_no:31  molecular_mass:69.723(1)  melting_point:29.78  boiling_point:2403",
    "Germanium  symbol:Ge  atomic_no:32  molecular_mass:72.61(2)  melting_point:937.4  boiling_point:2830",
    "Gold    symbol:Au  atomic_no:79  molecular_mass:196.96654(3)  melting_point:1064.434  boiling_point:2808±2",
    "Hafnium    symbol:Hf  atomic_no:72  molecular_mass:178.49(2)  melting_point:2227±20  boiling_point:4602",
    "Hassium    symbol:Hs  atomic_no:108  molecular_mass:265  melting_point:Unknown  boiling_point:Unknown",
    "Helium    symbol:He  atomic_no:2      molecular_mass:4.002602(2)  melting_point:-272.226 amt  boiling_point:-268.934",
    "Holmium    symbol:Ho  atomic_no:67  molecular_mass:164.93032(3)  melting_point:1474  boiling_point:2700",
    "Hydrogen  symbol:H  atomic_no:1  molecular_mass:1.00794(7)  melting_point:-259.34  boiling_point:-252.87",
    "Indium    symbol:In  atomic_no:49  molecular_mass:114.82(1)  melting_point:156.61  boiling_point:2080",
    "Iodine    symbol:I  atomic_no:53  molecular_mass:126.90447(3)  melting_point:113.5  boiling_point:184.35",
    "Iridium    symbol:Ir  atomic_no:77  molecular_mass:192.22(3)  melting_point:2410  boiling_point:4130",
    "Iron    symbol:Fe  atomic_no:26  molecular_mass:55.847(3)  melting_point:1535  boiling_point:2750",
    "Krypton    symbol:Kr  atomic_no:36  molecular_mass:83.80(1)  melting_point:-156.6  boiling_point:-152.30±0.10",
    "Lanthanum  symbol:La  atomic_no:57  molecular_mass:138.9055(2)  melting_point:918  boiling_point:3464",
    "Lawrencium  symbol:Lr  atomic_no:103  molecular_mass:262  melting_point:Unknown  boiling_point:Unknown",
    "Lead    symbol:Pb  atomic_no:82  molecular_mass:207.2(1)  melting_point:327.502  boiling_point:1740",
    "Lithium    symbol:Li  atomic_no:3  molecular_mass:6.941(2)  melting_point:180.54  boiling_point:1342",
    "Lutetium  symbol:Lu  atomic_no:71  molecular_mass:174.967(1)  melting_point:1663  boiling_point:3402",
    "Magnesium  symbol:Mg  atomic_no:12  molecular_mass:24.3050(6)  melting_point:648.8±0.5  boiling_point:1090",
    "Manganese  symbol:Mn  atomic_no:25  molecular_mass:54.93805(1)  melting_point:1244±3  boiling_point:1962",
    "Meitnerium  symbol:Mt  atomic_no:109  molecular_mass:266  melting_point:Unknown  boiling_point:Unknown",
    "Mendelevium  symbol:Md  atomic_no:101  molecular_mass:258  melting_point:Unknown  boiling_point:Unknown",
    "Mercury    symbol:Hg  atomic_no:80  molecular_mass:200.59(3)  melting_point:-38.87  boiling_point:356.58",
    "Molybdenum  symbol:Mo  atomic_no:42  molecular_mass:95.94(1)  melting_point:2617  boiling_point:4612",
    "Neodymium  symbol:Nd  atomic_no:60  molecular_mass:144.24(3)  melting_point:1021  boiling_point:3074",
    "Neon    symbol:Ne  atomic_no:10  molecular_mass:20.1797(6)  melting_point:-248.67  boiling_point:-246.048",
    "Neptunium  symbol:Np  atomic_no:93  molecular_mass:237.048  melting_point:640±1  boiling_point:3902",
    "Nickel    symbol:Ni  atomic_no:28  molecular_mass:58.6934  melting_point:1453  boiling_point:2732",
    "Niobium    symbol:Nb  atomic_no:41  molecular_mass:92.90638(2)  melting_point:2468±10  boiling_point:4742",
    "Nitrogen  symbol:N  atomic_no:7  molecular_mass:14.00674(7)  melting_point:-209.86  boiling_point:-195.8",
    "Nobelium  symbol:Os  atomic_no:76  molecular_mass:190.2(1)  melting_point:3045±30  boiling_point:5027±100",
    "Oxygen    symbol:O  atomic_no:8  molecular_mass:15.9994(3)  melting_point:-218.4  boiling_point:-182.962",
    "Palladium  symbol:Pd  atomic_no:46  molecular_mass:106.42(1)  melting_point:1554  boiling_point:3140",
    "Phosphorus  symbol:P  atomic_no:15  molecular_mass:30.973762(4)  melting_point:44.1(white)  boiling_point:280(white)",
    "Platinum  symbol:Pt  atomic_no:78  molecular_mass:195.08(3)  melting_point:1772  boiling_point:3827±100",
    "Plutonium  symbol:Pu  atomic_no:94  molecular_mass:244  melting_point:641  boiling_point:3232",
    "Polonium  symbol:Po  atomic_no:84  molecular_mass:209  melting_point:254  boiling_point:962",
    "Potassium  symbol:K  atomic_no:19  molecular_mass:39.0983(1)  melting_point:63.25  boiling_point:759.9",
    "Praseodymium  symbol:Pr  atomic_no:59  molecular_mass:140.90765(3)  melting_point:931  boiling_point:3520",
    "Promethium  symbol:Pm  atomic_no:61  molecular_mass:145  melting_point:1042  boiling_point:3000(estimate)",
    "Protactinium  symbol:Pa  atomic_no:91  molecular_mass:231.0359  melting_point:1600  boiling_pont:Unknown",
    "Radium    symbol:Ra  atomic_no:88  molecular_mass:226.025  melting_point:700  boiling_point:1140",
    "Radon    symbol:Rn  atomic_no:86  molecular_mass:222  melting_point:-71  boiling_point:-61.8",
    "Rhenium    symbol:Re  atomic_no:75  molecular_mass:186.207(1)  melting_point:3180  boiling_point:5627(estimate)",
    "Rhodium    symbol:Rh  atomic_no:45  molecular_mass:102.90550(3)  melting_point:1965±3  boiling_point:3727±100",
    "Rubidium  symbol:Rb  atomic_no:37  molecular_mass:85.4678(3)  melting_point:38.89  boiling_point:686",
    "Ruthenium  symbol:Ru  atomic_no:44  molecular_mass:101.07(2)  melting_point:2310  boiling_point:3900",
    "Rutherfordium  symbol:Rf  atomic_no:104  molecular_mass:261  melting_point:Unknown  boiling_point:Unknown",
    "Samarium  symbol:Sm  atomic_no:62  molecular_mass:150.36(3)  melting_point:1074  boiling_point:1794",
    "Scandium  symbol:Sc  atomic_no:21  molecular_mass:44.955910(9)  melting_point:1541  boiling_point:2836",
    "Seaborgium  symbol:Sg  atomic_no:106  molecular_mass:263  melting_point:Unknown  boiling_point:Unknown",
    "Selenium  symbol:Se  atomic_no:34  molecular_mass:78.96(3)  melting_point:217  boiling_point:684.9±1.0",
    "Silicon    symbol:Si  atomic_no:14  molecular_mass:28.0855(3)  melting_point:1410  boiling_point:2355",
    "Silver    symbol:Ag  atomic_no:47  molecular_mass:107.8682(2)  melting_point:961.93  boiling_point:2212",
    "Sodium    symbol:Na  atomic_no:11  molecular_mass:22.989768(6)  melting_point:97.81±0.03  boiling_point:882.9",
    "Strontium  symbol:Sr  atomic_no:38  molecular_mass:87.62(1)  melting_point:769  boiling_point:1384",
    "Sulfur    symbol:S  atomic_no:16  molecular_mass:32.066(6)  melting_point:112.8  boiling_point:444.674",
    "Tantalum  symbol:Ta  atomic_no:73  molecular_mass:180.9479(1)  melting_point:2996  boiling_point:5425±100",
    "Technetium  symbol:Tc  atomic_no:43  molecular_mass:98  melting_point:2172  boiling_point:4877",
    "Tellurium  symbol:Te  atomic_no:52  molecular_mass:127.60(3)  melting_point:449.5±0.3  boiling_point:989.8±3.8",
    "Terbium    symbol:Tb  atomic_no:65  molecular_mass:158.92534(3)  melting_point:1356  boiling_point:3230",
    "Thallium  symbol:Tl  atomic_no:81  molecular_mass:204.3833(2)  melting_point:303.5  boiling_point:1457±10",
    "Thorium    symbol:Th  atomic_no:90  molecular_mass:232.0381(1)  melting_point:1750  boiling_point:3800(app.)",
    "Thulium    symbol:Tm  atomic_no:69  molecular_mass:168.93421(3)  melting_point:1545  boiling_point:1950",
    "Tin      symbol:Sn  atomic_no:50  molecular_mass:118.710(7)  melting_point:231.9681  boiling_point:2270",
    "Titanium  symbol:Ti  atomic_no:22  molecular_mass:47.88(3)  melting_point:1660±10  boiling_point:32878",
    "Tungsten  symbol:W  atomic_no:74  molecular_mass:183.85(3)  melting_point:3410±20  boiling_point:5660",
    "Uranium    symbol:U  atomic_no:92  molecular_mass:238.0289(1)  melting_point:1132±0.8  boiling_point:3818",
    "Vanadium  symbol:V  atomic_no:23  molecular_mass:50.9415(1)  melting_point:1890±10  boiling_point:3380",
    "Xenon    symbol:Xe  atomic_no:54  molecular_mass:131.29(2)  melting_point:-111.9  boiling_point:-107.1±0.3",
    "Ytterbium  symbol:Yb  atomic_no:70  molecular_mass:173.04(3)  melting_point:819  boiling_point:1196",
    "Yttrium    symbol:Y  atomic_no:39  molecular_mass:88.90585(2)  melting_point:1552  boiling_point:5338",
    "Zinc    symbol:Zn  atomic_no:30  molecular_mass:65.39(2)  melting_point:419.58  boiling_point:907",
    "Zirconium  symbol:Zr  atomic_no:40  molecular_mass:91.224(2)  melting_point:1852±2  boiling_point:4377", ]


def find_combination(n, r):
    try:
        answer = (factorial(n)) / (factorial(r) * factorial(n - r))
        return answer
    except:
        answer = "Invalid"
        return answer


def find_permutation(n, r):
    try:
        answer = factorial(n) / factorial(n - r)
        return answer
    except:
        answer = "Invalid"
        return answer


def quadratic_formula(a, b, c):
    root = []
    discriminant = pow(b, 2) - (4 * a * c)
    if discriminant < 0.0:
        return root
    else:
        try:
            answer_1 = (((-1 * b) + pow(discriminant, 0.5)) / (2 * a))
            answer_2 = (((-1 * b) - pow(discriminant, 0.5)) / (2 * a))
            root.append(answer_1)
            root.append(answer_2)
            return root
        except:
            root.clear()
            return root


def find_roots(a, b, c, d, e, f, g, h, i, j, k, l):
    power = [b, d, f, h, j, l]
    highest = -1000
    for data in power:
        if data > highest:
            highest = data
    root = []
    probable_root = []
    n = -100.0
    while n <= 100.0:
        m = round(n, 2)
        try:
            solved = a * (pow(m, b)) + c * (pow(m, d)) + e * (pow(m, f)) + g * (pow(m, h)) + i * (pow(m, j)) + k * (
                pow(m, l))
        except:
            solved = 100
        if solved == 0.0 and solved == -0.0:
            probable_root.append(m)
        n += 1.0
    print(probable_root)
    if highest == 2 and len(probable_root) == 2:
        root = probable_root.copy()
        return root
    else:
        root = probable_root.copy()
    probable_root.clear()
    n = -100.0
    while n <= 100.0:
        m = round(n, 4)
        try:
            solved = a * (pow(m, b)) + c * (pow(m, d)) + e * (pow(m, f)) + g * (pow(m, h)) + i * (pow(m, j)) + k * (
                pow(m, l))
        except:
            solved = 100
        if solved >= -1.0 and solved <= 1.0:
            probable_root.append(m)
        n += 0.01
    print(probable_root)
    if probable_root == []:
        root.clear()
        return root
    num_id = 0
    average_count = 0
    init_num = 0
    new_root = []
    total_num = 0
    for num in probable_root:
        if num_id == len(probable_root) - 1:
            average_count += 1
            total_num += num
            new_root.append(round((total_num / average_count), 4))
            break
        elif num_id == 0:
            init_num = num
            average_count += 1
            total_num += num
        else:
            if num - init_num >= 0.5:
                new_root.append(round((total_num / average_count), 4))
                total_num = 0
                average_count = 0
                total_num += num
                average_count += 1
                init_num = num
            else:
                total_num += num
                average_count += 1
                init_num = num
        num_id += 1
    print(new_root)
    if root == []:
        root = new_root.copy()
        return root
    for num in new_root:
        num_exists = False
        for num_2 in root:
            if float(str(num - num_2).replace("-", "")) <= 0.5:
                num_exists = True
                break
        if num_exists:
            pass
        else:
            root.append(num)
    print(root)
    return root


def t_by_4_md(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    determinatant = a * (t_by_3_md(f, g, h, j, k, l, n, o, p)) - b * (t_by_3_md(e, g, h, i, k, l, m, o, p)) + c * (
        t_by_3_md(e, f, h, i, j, l, m, n, p)) - d * (t_by_3_md(e, f, g, i, j, k, m, n, o))
    return determinatant


def t_by_3_md(a, b, c, d, e, f, g, h, i):
    determinant = a * (t_by_2_md(e, f, h, i)) - b * (t_by_2_md(d, f, g, i)) + c * (t_by_2_md(d, e, g, h))
    return determinant


def t_by_2_md(a, b, c, d):
    determinant = (a * d) - (b * c)
    return determinant


def update_root():
    root.update_idletasks()
    root.update()


root = Tk()
root_width = 300
root_height = 420

if os.path.exists(os.path.join(os.getcwd(), "data")) and os.path.exists(os.path.join(os.getcwd(), "data", "bg.jpg")) and os.path.exists(os.path.join(os.getcwd(), "data", "calc.jpg")) and os.path.exists(os.path.join(os.getcwd(), "data", "icon.ico")):
    pass
else:
    messagebox.showerror("Error", "File Missing")
    root.destroy()
    exit()
if len(os.listdir(os.path.join(os.getcwd(), "data"))) < 41:
    root.withdraw()
    first_run = Toplevel()
    screen_height = first_run.winfo_screenheight()
    screen_width = first_run.winfo_screenwidth()
    first_run.geometry("{}x{}+{}+{}".format(220, 80, int((screen_width - 220) / 2), int((screen_height - 80) / 2)))
    first_run.resizable(0, 0)
    first_run.wm_attributes("-topmost", 1)
    first_run.overrideredirect(1)
    canvas_first_run = Canvas(first_run, height=80, width=220)
    canvas_first_run.pack()
    loading_var = StringVar()
    loading_var.set("load")
    image_n = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "load.jpg")), "r")
    image_m = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "calc.jpg")), "r")
    canvas_first_run.create_image(110, 40, image=image_n)


    def update_main():
        canvas_first_run.update()
        canvas_first_run.update_idletasks()
        first_run.update_idletasks()
        first_run.update()
        return


    def loading_text():
        dot = 4
        text = "Loading App For First Use" + "." * dot
        load_text = canvas_first_run.create_text(90, 30, text=text, fill="#772801",font=("lucide caligraphy", 7, "bold"))
        update_main()



    canvas_first_run.create_text(100, 10, text="Scientific Calculator v1.0", fill="#000537",
                                 font=("Lucida Handwriting", 8, "bold"))
    canvas_first_run.create_text(100, 70, text="Credit: Peterlight", fill="#451D52", font=("Segoe", 7, "bold"))
    canvas_first_run.create_image(180, 40, image=image_m)

    b = canvas_first_run.create_rectangle(10, 60, 121, 50, fill="white")
    a = canvas_first_run.create_rectangle(10, 60, 10, 50, fill="#46768C")


    def update():
        x_2 = 10
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "main.jpg")):
        image_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_main = image_main.resize((root_width, root_height), Image.ANTIALIAS)
        image_main.save(os.path.join(os.getcwd(), "data", "main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "modulo.jpg")):
        image_modulo = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_modulo = image_modulo.resize((200, 120), Image.ANTIALIAS)
        image_modulo.save(os.path.join(os.getcwd(), "data", "modulo.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "factorial.jpg")):
        image_factorial = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_factorial = image_factorial.resize((200, 60), Image.ANTIALIAS)
        image_factorial.save(os.path.join(os.getcwd(), "data", "factorial.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "hyp.jpg")):
        image_hyp = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_hyp = image_hyp.resize((140, 120), Image.ANTIALIAS)
        image_hyp.save(os.path.join(os.getcwd(), "data", "hyp.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "simul_m.jpg")):
        image_simul_m = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_simul_m = image_simul_m.resize((300, 150), Image.ANTIALIAS)
        image_simul_m.save(os.path.join(os.getcwd(), "data", "simul_m.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "simul_2nd.jpg")):
        image_simul_2nd = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_simul_2nd = image_simul_2nd.resize((600, 180), Image.ANTIALIAS)
        image_simul_2nd.save(os.path.join(os.getcwd(), "data", "simul_2nd.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "simul_3rd.jpg")):
        image_simul_3rd = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_simul_3rd = image_simul_3rd.resize((700, 250), Image.ANTIALIAS)
        image_simul_3rd.save(os.path.join(os.getcwd(), "data", "simul_3rd.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "simul_4th.jpg")):
        image_simul_4th = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_simul_4th = image_simul_4th.resize((800, 320), Image.ANTIALIAS)
        image_simul_4th.save(os.path.join(os.getcwd(), "data", "simul_4th.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "quad_main.jpg")):
        image_quad_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_quad_main = image_quad_main.resize((300, 100), Image.ANTIALIAS)
        image_quad_main.save(os.path.join(os.getcwd(), "data", "quad_main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "quad_2nd.jpg")):
        image_quad_2nd = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_quad_2nd = image_quad_2nd.resize((500, 200), Image.ANTIALIAS)
        image_quad_2nd.save(os.path.join(os.getcwd(), "data", "quad_2nd.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "quad_other.jpg")):
        image_quad_other = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_quad_other = image_quad_other.resize((500, 400), Image.ANTIALIAS)
        image_quad_other.save(os.path.join(os.getcwd(), "data", "quad_other.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "nbase_convert.jpg")):
        image_nbase_convert = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_nbase_convert = image_nbase_convert.resize((200, 180), Image.ANTIALIAS)
        image_nbase_convert.save(os.path.join(os.getcwd(), "data", "nbase_convert.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "nbase_calculate.jpg")):
        image_nbase_calculate = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_nbase_calculate = image_nbase_calculate.resize((400, 240), Image.ANTIALIAS)
        image_nbase_calculate.save(os.path.join(os.getcwd(), "data", "nbase_calculate.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "complex_main.jpg")):
        image_complex_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_complex_main = image_complex_main.resize((300, 240), Image.ANTIALIAS)
        image_complex_main.save(os.path.join(os.getcwd(), "data", "complex_main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "complex_2.jpg")):
        image_complex_2 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_complex_2 = image_complex_2.resize((400, 300), Image.ANTIALIAS)
        image_complex_2.save(os.path.join(os.getcwd(), "data", "complex_2.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "complex_root.jpg")):
        image_complex_root = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_complex_root = image_complex_root.resize((300, 70), Image.ANTIALIAS)
        image_complex_root.save(os.path.join(os.getcwd(), "data", "complex_root.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "complex_form.jpg")):
        image_complex_form = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_complex_form = image_complex_form.resize((300, 160), Image.ANTIALIAS)
        image_complex_form.save(os.path.join(os.getcwd(), "data", "complex_form.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "complex_arith.jpg")):
        image_complex_arith = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_complex_arith = image_complex_arith.resize((300, 240), Image.ANTIALIAS)
        image_complex_arith.save(os.path.join(os.getcwd(), "data", "complex_arith.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "stat_main.jpg")):
        image_stat_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_stat_main = image_stat_main.resize((300, 100), Image.ANTIALIAS)
        image_stat_main.save(os.path.join(os.getcwd(), "data", "stat_main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "stat_2.jpg")):
        image_stat_2 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_stat_2 = image_stat_2.resize((300, 220), Image.ANTIALIAS)
        image_stat_2.save(os.path.join(os.getcwd(), "data", "stat_2.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "stat_op_1.jpg")):
        image_stat_op_1 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_stat_op_1 = image_stat_op_1.resize((300, 280), Image.ANTIALIAS)
        image_stat_op_1.save(os.path.join(os.getcwd(), "data", "stat_op_1.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "stat_op_2.jpg")):
        image_stat_op_2 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_stat_op_2 = image_stat_op_2.resize((300, 320), Image.ANTIALIAS)
        image_stat_op_2.save(os.path.join(os.getcwd(), "data", "stat_op_2.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "constants_main.jpg")):
        image_constants_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_constants_main = image_constants_main.resize((600, 400), Image.ANTIALIAS)
        image_constants_main.save(os.path.join(os.getcwd(), "data", "constants_main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "constants_periodic.jpg")):
        image_constants_periodic = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_constants_periodic = image_constants_periodic.resize((1000, 550), Image.ANTIALIAS)
        image_constants_periodic.save(os.path.join(os.getcwd(), "data", "constants_periodic.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "constants_element.jpg")):
        image_constants_element = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_constants_element = image_constants_element.resize((300, 280), Image.ANTIALIAS)
        image_constants_element.save(os.path.join(os.getcwd(), "data", "constants_element.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "vec_main.jpg")):
        image_vec_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_vec_main = image_vec_main.resize((300, 280), Image.ANTIALIAS)
        image_vec_main.save(os.path.join(os.getcwd(), "data", "vec_main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "vec_2.jpg")):
        image_vec_2 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_vec_2 = image_vec_2.resize((300, 300), Image.ANTIALIAS)
        image_vec_2.save(os.path.join(os.getcwd(), "data", "vec_2.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "vec_arith.jpg")):
        image_vec_arith = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_vec_arith = image_vec_arith.resize((300, 400), Image.ANTIALIAS)
        image_vec_arith.save(os.path.join(os.getcwd(), "data", "vec_arith.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "mat_main.jpg")):
        image_mat_main = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_mat_main = image_mat_main.resize((300, 320), Image.ANTIALIAS)
        image_mat_main.save(os.path.join(os.getcwd(), "data", "mat_main.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "mat_2.jpg")):
        image_mat_2 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_mat_2 = image_mat_2.resize((300, 400), Image.ANTIALIAS)
        image_mat_2.save(os.path.join(os.getcwd(), "data", "mat_2.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "mat_arith.jpg")):
        image_mat_arith = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_mat_arith = image_mat_arith.resize((300, 160), Image.ANTIALIAS)
        image_mat_arith.save(os.path.join(os.getcwd(), "data", "mat_arith.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "chav.jpg")):
        image_chav = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_chav = image_chav.resize((400, 80), Image.ANTIALIAS)
        image_chav.save(os.path.join(os.getcwd(), "data", "chav.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "hcf.jpg")):
        image_hcf = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_hcf = image_hcf.resize((400, 120), Image.ANTIALIAS)
        image_hcf.save(os.path.join(os.getcwd(), "data", "hcf.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "deg_rad.jpg")):
        image_deg_rad = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_deg_rad = image_deg_rad.resize((300, 100), Image.ANTIALIAS)
        image_deg_rad.save(os.path.join(os.getcwd(), "data", "deg_rad.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        # if not os.path.exists(os.path.join(os.getcwd(), "data", "deg_rad_2.jpg")):
        image_deg_rad_2 = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_deg_rad_2 = image_deg_rad_2.resize((200, 80), Image.ANTIALIAS)
        image_deg_rad_2.save(os.path.join(os.getcwd(), "data", "deg_rad_2.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        image_rad_deg = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_rad_deg = image_rad_deg.resize((200, 120), Image.ANTIALIAS)
        image_rad_deg.save(os.path.join(os.getcwd(), "data", "rad_deg.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        image_about = Image.open(os.path.join(os.getcwd(), "data", "bg.jpg"), "r")
        image_about = image_about.resize((300, 300), Image.ANTIALIAS)
        image_about.save(os.path.join(os.getcwd(), "data", "about.jpg"), "jpeg")
        x_2 += 3
        canvas_first_run.coords(a, 10, 60, x_2, 50)
        update_main()
        time.sleep(0.2)
        loading_var.set("done")
        first_run.destroy()



    loading_text()
    update()
root.deiconify()
image_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "main.jpg"), "r"))
image_modulo = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "modulo.jpg"), "r"))
image_factorial = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "factorial.jpg"), "r"))
image_hyp = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "hyp.jpg"), "r"))
image_simul_m = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "simul_m.jpg"), "r"))
image_simul_2nd = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "simul_2nd.jpg"), "r"))
image_simul_3rd = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "simul_3rd.jpg"), "r"))
image_simul_4th = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "simul_4th.jpg"), "r"))
image_quad_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "quad_main.jpg"), "r"))
image_quad_2nd = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "quad_2nd.jpg"), "r"))
image_quad_other = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "quad_other.jpg"), "r"))
image_nbase_convert = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "nbase_convert.jpg"), "r"))
image_nbase_calculate = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "nbase_calculate.jpg"), "r"))
image_complex_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "complex_main.jpg"), "r"))
image_complex_2 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "complex_2.jpg"), "r"))
image_complex_root = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "complex_root.jpg"), "r"))
image_complex_form = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "complex_form.jpg"), "r"))
image_complex_arith = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "complex_arith.jpg"), "r"))
image_stat_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "stat_main.jpg"), "r"))
image_stat_2 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "stat_2.jpg"), "r"))
image_stat_op_1 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "stat_op_1.jpg"), "r"))
image_stat_op_2 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "stat_op_2.jpg"), "r"))
image_constants_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "constants_main.jpg"), "r"))
image_constants_periodic = ImageTk.PhotoImage(
    Image.open(os.path.join(os.getcwd(), "data", "constants_periodic.jpg"), "r"))
image_constants_element = ImageTk.PhotoImage(
    Image.open(os.path.join(os.getcwd(), "data", "constants_element.jpg"), "r"))
image_vec_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "vec_main.jpg"), "r"))
image_vec_2 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "vec_2.jpg"), "r"))
image_vec_arith = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "vec_arith.jpg"), "r"))
image_mat_main = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "mat_main.jpg"), "r"))
image_mat_2 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "mat_2.jpg"), "r"))
image_mat_arith = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "mat_arith.jpg"), "r"))
image_chav = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "chav.jpg"), "r"))
image_hcf = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "hcf.jpg"), "r"))
image_deg_rad = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "deg_rad.jpg"), "r"))
image_deg_rad_2 = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "deg_rad_2.jpg"), "r"))
image_rad_deg = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "rad_deg.jpg"), "r"))
image_about = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "data", "about.jpg"), "r"))
root.geometry("{}x{}+{}+{}".format(root_width, root_height, int((root.winfo_screenwidth() - root_width) / 2),
                                   int((root.winfo_screenheight() - root_height) / 2)))
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
root.focus_force()
root.wm_attributes("-topmost", 0)
root.title("Calculator")
root.iconbitmap(os.path.join("data", "icon.ico"))
update_root()
menu_root = Menu(root)
root.configure(menu=menu_root)
menu_file = Menu(menu_root, tearoff=0)
menu_root.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="About", command=lambda: about())
menu_settings = Menu(menu_root, tearoff=0)
menu_root.add_cascade(label="Settings", menu=menu_settings)
menu_settings.add_command(label="Change Approximation Value", command=lambda: chav())
approximate_val = IntVar()
approximate_val.set(4)
cwk_am = StringVar()

def about():
    about_height = 300
    about_width = 300
    about_window = Toplevel()
    about_window.wm_attributes("-topmost", 1)
    about_window.geometry("{}x{}+{}+{}".format(about_width, about_height, int((root.winfo_screenwidth()-about_width)/2), int((root.winfo_screenheight()-about_height)/2)))
    about_window.title("About")
    about_window.resizable(0,0)
    about_window.iconbitmap(os.path.join("data", "icon.ico"))
    canvas_about = Canvas(about_window, height=about_height, width=about_width)
    canvas_about.pack()
    global image_about
    canvas_about.create_image(150,150, image=image_about)
    text_about = Text(canvas_about)
    canvas_about.create_window(150,150, window=text_about, height=280, width=280)
    text_about.tag_configure("headings", font=("Times", 12, "bold"), justify=CENTER)
    text_about.tag_configure("info", font=("Segoe", 9, "bold"), justify=LEFT)
    author_info = "Author Name: Faboyede Peterlight\nAuthor Details: 200Level, Department of Civil and Environmental Engineering, FUTA, Akure\nPhone No: 09060990102\nEmail Address:Petlight45@yahoo.com"
    text_about.insert(END, "Author Info\n", "headings")
    text_about.insert(END, author_info + "\n\n\n", "info")
    app_info = "App Name: Scientific Calculator v1.0\nProgramming Language: Python\nDate: March 16, 2019"
    text_about.insert(END, "App Info\n", "headings")
    text_about.insert(END, app_info, "info")
    text_about.config(state=DISABLED)

def instruct():
    instruct_height = 300
    instruct_width = 300
    instruct_window = Toplevel()
    instruct_window.resizable(0,0)
    instruct_window.wm_attributes("-topmost", 1)
    instruct_window.geometry("{}x{}+{}+{}".format(instruct_width, instruct_height, int((root.winfo_screenwidth()-instruct_width)/2), int((root.winfo_screenheight()-instruct_height)/2)))
    instruct_window.title("Instructions")
    instruct_window.iconbitmap(os.path.join("data", "icon.ico"))
    canvas_instruct = Canvas(instruct_window, height=instruct_height, width=instruct_width)
    canvas_instruct.pack()
    global image_about
    canvas_instruct.create_image(150,150, image=image_about)
    text_instruct = Text(canvas_instruct)
    canvas_instruct.create_window(150,150, window=text_instruct, height=280, width=280)
    text_instruct.tag_configure("headings", font=("Times", 12, "bold"), justify=CENTER)
    text_instruct.tag_configure("info", font=("Segoe", 9, "bold"), justify=LEFT)
    author_info = "Author Name: Faboyede Peterlight\nAuthor Details: 200Level, Department of Civil and Environmental Engineering, FUTA, Akure\nPhone No: 09060990102\nEmail Address:Petlight45@yahoo.com"
    text_instruct.insert(END, "Author Info\n", "headings")
    text_instruct.insert(END, author_info + "\n\n\n", "info")
    app_info = "App Name: Scientific Calculator v1.0\nProgramming Language: Python\nDate: March 16, 2019"
    text_instruct.insert(END, "App Info\n", "headings")
    text_instruct.insert(END, app_info, "info")
    text_instruct.config(state=DISABLED)

def chav():
    global approximate_val
    chav_width = 400
    chav_height = 80
    chav_window = Toplevel()
    chav_window.geometry("{}x{}+{}+{}".format(chav_width, chav_height,
                                              int((chav_window.winfo_screenwidth() - chav_width) / 2),
                                              int((chav_window.winfo_screenheight() - chav_height) / 2)))
    chav_window.configure(bg="#ECF3FB")
    chav_window.resizable(0, 0)
    chav_window.wm_attributes("-topmost", 1)
    chav_window.focus_force()
    chav_window.wm_attributes("-topmost", 0)
    chav_window.title("Change Approximation Value")
    chav_window.iconbitmap(os.path.join("data", "icon.ico"))
    canvas_chav = Canvas(chav_window, width=chav_width, height=chav_height)
    canvas_chav.pack()
    global image_chav
    canvas_chav.create_image(200, 40, image=image_chav)
    entry_value = Entry(canvas_chav, justify=CENTER, font=("Cambria", 9, "bold"))
    entry_value.insert(END, str(approximate_val.get()))
    entry_value.focus_force()
    canvas_chav.create_text(200, 20, justify=CENTER,
                            text="Enter the d.p figure you want your decimal numbers to be approximated to.\n Min=0, Press enter to continue",
                            font=("Segoe", 7, "bold"))
    canvas_chav.create_window(200, 60, window=entry_value, width=40)

    def con_chav(event):
        continue_chav()

    entry_value.bind("<Return>", con_chav)

    def continue_chav():
        try:
            value = int(entry_value.get())
            if value >= 0:
                approximate_val.set(value)
                chav_window.destroy()
                return
            else:
                messagebox.showerror("Error", "Invalid Value")
                chav_window.wm_attributes("-topmost", 1)
                chav_window.focus_force()
                entry_value.focus_force()
                chav_window.wm_attributes("-topmost", 0)
        except:
            messagebox.showerror("Error", "Invalid Value")
            chav_window.wm_attributes("-topmost", 1)
            chav_window.focus_force()
            entry_value.focus_force()
            chav_window.wm_attributes("-topmost", 0)


class Main:

    def __init__(self):
        global approximate_val
        self.back_col = "#ECF3FB"
        global root_height
        global root_width
        self.canvas = Canvas(root, height=root.winfo_height(), width=root.winfo_width(), bg=self.back_col)
        self.canvas.pack()
        hint_but  = Menubutton(self.canvas, text="!", fg="black", bg="#ECF3FB", font=("Segoe", 9, "bold"), activebackground="black", activeforeground="white")
        menu_hint = Menu(hint_but, tearoff=0)
        hint_but.configure(menu=menu_hint)
        menu_hint.add_cascade(label="You can copy items from the upper box by pressing key 'Z'")
        menu_hint.add_separator()
        menu_hint.add_cascade(label="You can copy items from the lower box by pressing key 'C'")
        update_root()
        self.canvas.update()
        global image_main
        global image_factorial
        global image_modulo
        global image_hyp
        global image_simul_m
        global image_simul_2nd
        global image_simul_3rd
        global image_simul_4th
        self.canvas.create_window(root_width/2, 390, window=hint_but)
        self.canvas.create_image(root_width / 2, root_height / 2, image=image_main)
        demacate_x_1 = self.canvas.create_rectangle(3, 8, 5, 112, fill="#DEE6FF")
        demacate_x_2 = self.canvas.create_rectangle(root_width - 2, 8, root_width - 4, 112, fill="#DEE6FF")
        demacate_y_1 = self.canvas.create_rectangle(3, 8, root_width - 4, 10, fill="#DEE6FF")
        demacate_y_2 = self.canvas.create_rectangle(3, 109, root_width - 4, 112, fill="#DEE6FF")
        label_display_1_var = StringVar()
        label_display_1_var.set("")
        old_label_display_1_var = StringVar()
        old_label_display_1_var.set("")
        label_display_1 = Text(root, bg="#FCFDFE")
        label_display_1.tag_configure("label_1", font=("Segoe", 9, "bold"), justify=LEFT, foreground="black")
        label_display_1.config(state=DISABLED)

        self.canvas.create_window(root_width / 2, 40, window=label_display_1, width=root_width - 10, height=60)
        label_display_2_var = StringVar()
        label_display_2_var.set("")
        label_display_2 = Text(root, bg="#FCFDFE")
        label_display_2.tag_configure("label_2", font=("Segoe", 12, "bold"), justify=RIGHT, foreground="black")
        label_display_2.config(state=DISABLED)
        self.canvas.create_window(root_width / 2, 90, window=label_display_2, width=root_width - 10, height=40)

        def update_label_1():
            label_display_1.config(state=NORMAL)
            label_display_1.delete(1.0, END)
            label_display_1.insert(END, label_display_1_var.get(), "label_1")
            label_display_1.config(state=DISABLED)
            label_display_2.config(state=NORMAL)
            label_display_2.delete(1.0, END)
            label_display_2.insert(END, label_display_2_var.get(), "label_2")
            label_display_2.config(state=DISABLED)

        update_label_1()

        def create_button():
            button_x_coord = -10
            button_y_coord = 150
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="x^y",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("power")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord, window=Button(self.canvas, bg="Black", fg="White",
                                                                                    text=chr(0x207F) + chr(
                                                                                        0x221A) + "x",
                                                                                    font=("Segoe", 9, "bold"),
                                                                                    command=lambda: button_press(
                                                                                        "root")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="x!",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("!")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="log x",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("log_b_10")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="log" + chr(0x207F) + "x",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("log_a_base_b")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="ln x",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("nlog")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="e" + chr(0x207F),
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("expo")), width=35, height=20)
            button_x_coord = -10
            button_y_coord = 170
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, text="(" + chr(0x00AD) + ")", bg="Black", fg="White",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("-")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="hyp",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("hyp")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="trig",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("trig")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="(",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("(")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text=")",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(")")), width=35, height=20)
            button_x_coord += 60
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="simult",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(
                                                        "simultaneous")), width=74, height=20)
            button_x_coord = -10
            button_y_coord = 190
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="nb",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("nbase")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="qte",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("quadratic")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="nCx",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("combination")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="nPx",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("permutation")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="cplx",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("complex")), width=35, height=20)
            button_x_coord += 60
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="statistics",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(
                                                        "statistics")), width=74,
                                      height=20)
            button_x_coord = -10
            button_y_coord = 210
            button_x_coord += 60
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="constants",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("constant")), width=74, height=20)
            button_x_coord += 60
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="vec",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("vector")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="matr",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("matrix")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="e",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(
                                                        "(" + str(round(e, approximate_val.get())) + ")")), width=35,
                                      height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text=chr(0x03A0),
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(
                                                        "(" + str(round(pi, approximate_val.get())) + ")")), width=35,
                                      height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="Rnd",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(
                                                        "round")), width=35,
                                      height=20)
            button_x_coord = -10
            button_y_coord = 230
            button_x_coord += 60
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="x(modulo)y",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("mod")), width=75, height=20)
            button_x_coord += 60
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="hcf",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("hcf")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="d<=>r",
                                                    font=("Segoe", 7, "bold"),
                                                    command=lambda: button_press("deg_to_rad")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="C<=>F",
                                                    font=("Segoe", 7, "bold"),
                                                    command=lambda: button_press("cel_to_far")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="C<=>K",
                                                    font=("Segoe", 7, "bold"),
                                                    command=lambda: button_press("cel_to_kel")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Black", fg="White", text="lcm",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("lcm")), width=35, height=20)
            button_x_coord = -10
            button_y_coord = 270
            button_x_coord += 45
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="0",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("0")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="1",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("1")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="2",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("2")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="3",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("3")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="4",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("4")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="5",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("5")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="6",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press(
                                                        "6")), width=20,
                                      height=20)

            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="7",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("7")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="8",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("8")), width=20, height=20)
            button_x_coord += 25
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Blue", fg="White", text="9",
                                                    font=("Cambria", 9, "bold"),
                                                    command=lambda: button_press("9")), width=20, height=20)

            button_x_coord = -10
            button_y_coord = 310
            button_x_coord += 55
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Brown", fg="Black", text="+",
                                                    font=("Lucida Handwriting", 9, "bold"),
                                                    command=lambda: button_press("+")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Brown", fg="Black", text="-",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("-")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Brown", fg="Black", text="X",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("*")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Brown", fg="Black", text="/",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("/")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Brown", fg="Black", text=".",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press(".")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Brown", fg="Black", text="=",
                                                    font=("Segoe", 9, "bold"),
                                                    command=lambda: button_press("solve")), width=35, height=20)

            button_x_coord = -10
            button_y_coord = 350
            button_x_coord += 120
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Pink", text="Del",
                                                    font=("Lucida Handwriting", 9, "bold"),
                                                    command=lambda: button_press("delete")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Orange", text="Clr",
                                                    font=("Lucida Handwriting", 9, "bold"),
                                                    command=lambda: button_press("clear")), width=35, height=20)
            button_x_coord += 40
            self.canvas.create_window(button_x_coord, button_y_coord,
                                      window=Button(self.canvas, bg="Indigo", fg="White", text="Rep",
                                                    font=("Lucida Handwriting", 9, "bold"),
                                                    command=lambda: button_press("replay")), width=35, height=20)
            

        create_button()

        def bind_key(event):
            if int(event.keycode) >= 48 and int(event.keycode) <= 57:
                button_press(event.char)
            elif int(event.keycode) == 190:
                button_press(".")
            elif int(event.keycode) == 187:
                button_press("+")
            elif int(event.keycode) == 189:
                button_press("-")
            elif int(event.keycode) == 191:
                button_press("/")
            elif int(event.keycode) == 88:
                button_press("*")
            elif int(event.keycode) == 8:
                button_press("delete")
            elif int(event.keycode) == 46:
                button_press("clear")
            elif int(event.keycode) == 13:
                button_press("solve")
            elif int(event.keycode) == 90:
                button_press("copy1")
            elif int(event.keycode) == 67:
                button_press("copy2")
            print(event.keycode)

        root.bind("<Key>", bind_key)

        def button_press(input):
            if input == "@" or input == "#" or input == "$" or input == "&":
                return
            elif input == "hcf":
                hcf_width = 400
                hcf_height = 120
                hcf_window = Toplevel()
                hcf_window.geometry("{}x{}+{}+{}".format(hcf_width, hcf_height,
                                                         int((hcf_window.winfo_screenwidth() - hcf_width) / 2),
                                                         int((hcf_window.winfo_screenheight() - hcf_height) / 2)))
                hcf_window.configure(bg="#ECF3FB")
                hcf_window.resizable(0, 0)
                hcf_window.wm_attributes("-topmost", 1)
                hcf_window.focus_force()
                hcf_window.wm_attributes("-topmost", 0)
                hcf_window.title("Highest Common Factor")
                hcf_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_hcf = Canvas(hcf_window, width=hcf_width, height=hcf_height, bg="#ECF3FB")
                canvas_hcf.pack()
                global image_hcf
                canvas_hcf.create_image(200, 60, image=image_hcf)
                entry_value_x = Entry(canvas_hcf, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_hcf, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_hcf.create_text(200, 10, text="Press enter to continue", font=("Segoe", 9, "bold"))
                canvas_hcf.create_text(100 - 20, 40, text="First Number", font=("Segoe", 9, "bold"))
                canvas_hcf.create_text(100 - 20, 80, text="Second Number", font=("Segoe", 9, "bold"))
                canvas_hcf.create_window(200 + 20, 40, window=entry_value_x, width=140)
                canvas_hcf.create_window(200 + 20, 80, window=entry_value_y, width=140)

                def hcf_cont_bind(event):
                    continue_hcf()

                entry_value_x.bind("<Return>", hcf_cont_bind)
                entry_value_y.bind("<Return>", hcf_cont_bind)

                def continue_hcf():
                    if "." in entry_value_x.get():
                        messagebox.showerror("Error", "Invalid x value")
                        hcf_window.wm_attributes("-topmost", 1)
                        hcf_window.focus_force()
                        hcf_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if "." in entry_value_y.get():
                        messagebox.showerror("Error", "Invalid y value")
                        hcf_window.wm_attributes("-topmost", 1)
                        hcf_window.focus_force()
                        hcf_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    try:
                        value_x = int(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        hcf_window.wm_attributes("-topmost", 1)
                        hcf_window.focus_force()
                        hcf_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = int(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid y value")
                        hcf_window.wm_attributes("-topmost", 1)
                        hcf_window.focus_force()
                        hcf_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    try:
                        pow_solve = str(gcd(value_x, value_y))
                    except:
                        messagebox.showerror("Error", "Invalid Value")
                        hcf_window.wm_attributes("-topmost", 1)
                        hcf_window.focus_force()
                        hcf_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    hcf_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)





            elif input == "lcm":

                lcm_width = 400

                lcm_height = 120

                lcm_window = Toplevel()

                lcm_window.geometry("{}x{}+{}+{}".format(lcm_width, lcm_height,

                                                         int((lcm_window.winfo_screenwidth() - lcm_width) / 2),

                                                         int((lcm_window.winfo_screenheight() - lcm_height) / 2)))

                lcm_window.configure(bg="#ECF3FB")

                lcm_window.resizable(0, 0)

                lcm_window.wm_attributes("-topmost", 1)

                lcm_window.focus_force()

                lcm_window.wm_attributes("-topmost", 0)

                lcm_window.title("Lowest Common Multiple")
                lcm_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_lcm = Canvas(lcm_window, width=lcm_width, height=lcm_height, bg="#ECF3FB")

                canvas_lcm.pack()

                canvas_lcm.create_image(200, 60, image=image_hcf)
                entry_value_x = Entry(canvas_lcm, justify=CENTER, font=("Cambria", 9, "bold"))

                entry_value_x.focus_force()

                entry_value_y = Entry(canvas_lcm, justify=CENTER, font=("Cambria", 9, "bold"))

                canvas_lcm.create_text(200, 10, text="Press enter to continue", font=("Segoe", 9, "bold"))

                canvas_lcm.create_text(100 - 20, 40, text="First Number", font=("Segoe", 9, "bold"))

                canvas_lcm.create_text(100 - 20, 80, text="Second Number", font=("Segoe", 9, "bold"))

                canvas_lcm.create_window(200 + 20, 40, window=entry_value_x, width=140)

                canvas_lcm.create_window(200 + 20, 80, window=entry_value_y, width=140)

                def lcm_cont_bind(event):

                    continue_lcm()

                entry_value_x.bind("<Return>", lcm_cont_bind)

                entry_value_y.bind("<Return>", lcm_cont_bind)

                def continue_lcm():

                    if "." in entry_value_x.get():
                        messagebox.showerror("Error", "Invalid x value")

                        lcm_window.wm_attributes("-topmost", 1)

                        lcm_window.focus_force()

                        lcm_window.wm_attributes("-topmost", 0)

                        entry_value_x.focus_force()

                        return

                    if "." in entry_value_y.get():
                        messagebox.showerror("Error", "Invalid y value")

                        lcm_window.wm_attributes("-topmost", 1)

                        lcm_window.focus_force()

                        lcm_window.wm_attributes("-topmost", 0)

                        entry_value_y.focus_force()

                        return

                    try:

                        value_x = int(entry_value_x.get())

                    except:

                        messagebox.showerror("Error", "Invalid x value")

                        lcm_window.wm_attributes("-topmost", 1)

                        lcm_window.focus_force()

                        lcm_window.wm_attributes("-topmost", 0)

                        entry_value_x.focus_force()

                        return

                    try:

                        value_y = int(entry_value_y.get())

                    except:

                        messagebox.showerror("Error", "Invalid y value")

                        lcm_window.wm_attributes("-topmost", 1)

                        lcm_window.focus_force()

                        lcm_window.wm_attributes("-topmost", 0)

                        entry_value_y.focus_force()

                        return

                    if value_x > value_y:
                        highest_num = value_x
                        lowest_num = value_y
                    elif value_y > value_x:
                        highest_num = value_y
                        lowest_num = value_x
                    elif value_y == value_x:
                        highest_num = value_x
                        lowest_num = value_y
                    answer = value_x * value_y
                    for num in range(highest_num, (highest_num * lowest_num) + 1):
                        if num % value_x == 0 and num % value_y == 0:
                            answer = num
                            break
                    pow_solve = str(answer)
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                        label_display_1_var.set("(" + str(pow_solve) + ")")

                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")

                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                        label_display_1_var.set("(" + str(pow_solve) + ")")

                        label_display_2_var.set("")

                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                        label_display_1_var.set("(" + str(pow_solve) + ")")

                        label_display_2_var.set("")
                    update_label_1()

                    old_label_display_1_var.set(label_display_1_var.get())

                    lcm_window.destroy()

                    root.wm_attributes("-topmost", 1)

                    root.focus_force()

                    root.wm_attributes("-topmost", 0)

            elif input == "complex":
                complex_width = 300

                complex_height = 240

                complex_window = Toplevel()

                complex_window.geometry("{}x{}+{}+{}".format(complex_width, complex_height,

                                                             int((
                                                                         complex_window.winfo_screenwidth() - complex_width) / 2),

                                                             int((
                                                                         complex_window.winfo_screenheight() - complex_height) / 2)))

                complex_window.configure(bg="#ECF3FB")

                complex_window.resizable(0, 0)

                complex_window.wm_attributes("-topmost", 1)

                complex_window.focus_force()

                complex_window.wm_attributes("-topmost", 0)

                complex_window.title("Complex Numbers")
                complex_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_complex = Canvas(complex_window, width=complex_width, bg="#ECF3FB", height=complex_height)

                canvas_complex.pack()

                global image_complex_main
                canvas_complex.create_image(150, 120, image=image_complex_main)
                canvas_complex.create_text(150, 10, fill="black", text="Select Operation", justify=CENTER,
                                           font=("Times", 9, "bold"))

                canvas_complex.create_window(150, 40, window=Button(canvas_complex, text="Roots of a Complex No",
                                                                    command=lambda: continue_complex_1("roots"),
                                                                    bg="Black",
                                                                    fg="White", font=("Segoe", 9, "bold")),
                                             width=250)

                canvas_complex.create_window(150, 80, window=Button(canvas_complex, text="Argument of a Complex Number",

                                                                    command=lambda: continue_complex_1("arg"),
                                                                    bg="Black",

                                                                    fg="White", font=("Segoe", 9, "bold")),
                                             width=250)
                canvas_complex.create_window(150, 120, window=Button(canvas_complex, text="Modulus of a Complex Number",

                                                                     command=lambda: continue_complex_1("modulus"),
                                                                     bg="Black",

                                                                     fg="White", font=("Segoe", 9, "bold")),
                                             width=250)

                canvas_complex.create_window(150, 160,
                                             window=Button(canvas_complex, text="Conversion of Complex Numbers",

                                                           command=lambda: continue_complex_1("conv"),
                                                           bg="Black",

                                                           fg="White", font=("Segoe", 9, "bold")),
                                             width=250)

                canvas_complex.create_window(150, 200,
                                             window=Button(canvas_complex, text="Arithmetic Operations",

                                                           command=lambda: continue_complex_1_arith(),
                                                           bg="Black",

                                                           fg="White", font=("Segoe", 9, "bold")),
                                             width=250)

                def continue_complex_1_arith():
                    complex_arith_type_width = 300

                    complex_arith_type_height = 240
                    complex_arith_type_window = Toplevel()

                    complex_arith_type_window.geometry(
                        "{}x{}+{}+{}".format(complex_arith_type_width, complex_arith_type_height,

                                             int((
                                                         complex_arith_type_window.winfo_screenwidth() - complex_arith_type_width) / 2),

                                             int((
                                                         complex_arith_type_window.winfo_screenheight() - complex_arith_type_height) / 2)))

                    complex_arith_type_window.configure(bg="#ECF3FB")

                    complex_arith_type_window.resizable(0, 0)

                    complex_arith_type_window.wm_attributes("-topmost", 1)

                    complex_arith_type_window.focus_force()

                    complex_arith_type_window.wm_attributes("-topmost", 0)

                    complex_arith_type_window.title("Arithmetic Operations of Complex No")
                    complex_arith_type_window.iconbitmap(os.path.join("data", "icon.ico"))

                    canvas_complex_arith_type = Canvas(complex_arith_type_window, width=complex_arith_type_width,
                                                       bg="#ECF3FB",
                                                       height=complex_arith_type_height)

                    canvas_complex_arith_type.pack()

                    global image_complex_arith
                    canvas_complex_arith_type.create_image(150, 120, image=image_complex_arith)
                    canvas_complex_arith_type.create_text(150, 10, fill="black",
                                                          text="Select the type of arithmetic operation",
                                                          justify=CENTER, font=("Times", 9, "bold"))

                    canvas_complex_arith_type.create_window(150, 40, window=Button(canvas_complex_arith_type,
                                                                                   text="Addition",
                                                                                   command=lambda: continue_complex_arith_type_1(
                                                                                       "add"),
                                                                                   bg="Black",
                                                                                   fg="White",
                                                                                   font=("Segoe", 9, "bold")),
                                                            width=250)

                    canvas_complex_arith_type.create_window(150, 80, window=Button(canvas_complex_arith_type,
                                                                                   text="Subtraction",

                                                                                   command=lambda: continue_complex_arith_type_1(
                                                                                       "subtract"),
                                                                                   bg="Black",

                                                                                   fg="White",
                                                                                   font=("Segoe", 9, "bold")),
                                                            width=250)
                    canvas_complex_arith_type.create_window(150, 120, window=Button(canvas_complex_arith_type,
                                                                                    text="Division",

                                                                                    command=lambda: continue_complex_arith_type_1(
                                                                                        "divide"),
                                                                                    bg="Black",

                                                                                    fg="White",
                                                                                    font=("Segoe", 9, "bold")),
                                                            width=250)
                    canvas_complex_arith_type.create_window(150, 160, window=Button(canvas_complex_arith_type,
                                                                                    text="Multiplication",

                                                                                    command=lambda: continue_complex_arith_type_1(
                                                                                        "multiply"),
                                                                                    bg="Black",

                                                                                    fg="White",
                                                                                    font=("Segoe", 9, "bold")),
                                                            width=250)
                    canvas_complex_arith_type.create_window(150, 200, window=Button(canvas_complex_arith_type,
                                                                                    text="Power",

                                                                                    command=lambda: continue_complex_arith_type_1(
                                                                                        "power"),
                                                                                    bg="Black",

                                                                                    fg="White",
                                                                                    font=("Segoe", 9, "bold")),
                                                            width=250)

                    def continue_complex_arith_type_1(type):
                        complex_arith_type_window.destroy()
                        continue_complex_1(type)

                def continue_complex_1(input):
                    if input == "conv":
                        title = "Conversion of Complex Numbers"
                    elif input == "modulus":
                        title = "Modulus of a complex No"
                    elif input == "arg":
                        title = "Argument of a Complex No"
                    elif input == "roots":
                        title = "Roots of Complex Numbers"
                    elif input == "add" or input == "multiply" or input == "subtract" or input == "divide":
                        title = "Arithmetic Op Involving Complex No: " + input[0].upper() + input[1:].lower() + " 1st"
                    elif input == "power":
                        title = "Arithmetic Op Involving Complex No: " + input[0].upper() + input[1:].lower()
                    complex_1_width = 400
                    complex_1_height = 300
                    complex_1_window = Toplevel()
                    complex_window.destroy()
                    complex_1_window.geometry("{}x{}+{}+{}".format(complex_1_width, complex_1_height,

                                                                   int((
                                                                               complex_1_window.winfo_screenwidth() - complex_1_width) / 2),

                                                                   int((
                                                                               complex_1_window.winfo_screenheight() - complex_1_height) / 2)))

                    complex_1_window.configure(bg="#ECF3FB")

                    complex_1_window.resizable(0, 0)

                    complex_1_window.wm_attributes("-topmost", 1)

                    complex_1_window.focus_force()

                    complex_1_window.wm_attributes("-topmost", 0)

                    complex_1_window.title(title)
                    complex_1_window.iconbitmap(os.path.join("data", "icon.ico"))

                    canvas_complex_1 = Canvas(complex_1_window, width=complex_1_width, bg="#ECF3FB",
                                              height=complex_1_height)

                    canvas_complex_1.pack()
                    global image_complex_2
                    canvas_complex_1.create_image(200, 150, image=image_complex_2)
                    canvas_complex_1.create_text(200, 20, fill="black", text=title, justify=CENTER,
                                                 font=("Segoe", 12, "bold"))
                    entry_a_cart = StringVar()
                    entry_op_cart = StringVar()
                    entry_b_cart = StringVar()
                    radio_but_var = StringVar()
                    radio_but_var.set("cartesian")

                    def continue_complex_2_bind(event):
                        continue_complex_2()

                    canvas_complex_1.create_window(150, 60, window=Radiobutton(canvas_complex_1,
                                                                               text="Cartesian Form(a + jb or a - jb)",
                                                                               bg="#7198A7", activebackground="#7198A7",
                                                                               activeforeground="black",
                                                                               font=("Segoe", 9, "bold"),
                                                                               fg="black", value="cartesian",
                                                                               variable=radio_but_var,
                                                                               command=lambda: change_state_type(
                                                                                   radio_but_var.get())))
                    entry_a_cartesian = Entry(canvas_complex_1, textvariable=entry_a_cart, justify=CENTER,
                                              font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(40, 80, window=entry_a_cartesian, width=60)
                    entry_op_cartesian = Entry(canvas_complex_1, textvariable=entry_op_cart, justify=CENTER,
                                               font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(120, 80, window=entry_op_cartesian, width=30)
                    canvas_complex_1.create_window(180, 80,
                                                   window=Label(canvas_complex_1, text="j", justify=CENTER, bg="black",
                                                                fg="white",
                                                                font=("Segoe", 9, "bold")), width=20, height=20)
                    entry_b_cartesian = Entry(canvas_complex_1, textvariable=entry_b_cart, justify=CENTER,
                                              font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(220, 80, window=entry_b_cartesian, width=60)
                    canvas_complex_1.create_window(200, 110, window=Radiobutton(canvas_complex_1,
                                                                                text="Polar Form(r[cosa + jsinb]) Note:Must be true polar form",
                                                                                bg="#7198A7",
                                                                                activebackground="#7198A7",
                                                                                activeforeground="black",
                                                                                font=("Segoe", 9, "bold"),
                                                                                fg="black", value="polar",
                                                                                variable=radio_but_var,
                                                                                command=lambda: change_state_type(
                                                                                    radio_but_var.get())))
                    entry_r_polar = StringVar()
                    entry_tita_cos_polar = StringVar()
                    entry_op_polar = StringVar()
                    entry_tita_sin_polar = StringVar()
                    entry_r_pol = Entry(canvas_complex_1, textvariable=entry_r_polar, justify=CENTER,
                                        font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(40, 140, window=entry_r_pol, width=60)
                    canvas_complex_1.create_window(80, 140,
                                                   window=Label(canvas_complex_1, bg="black", fg="white", text="[",
                                                                justify=CENTER,
                                                                font=("Segoe", 15, "bold")), width=20)
                    canvas_complex_1.create_window(105, 140,
                                                   window=Label(canvas_complex_1, bg="black", fg="white", text="Cos",
                                                                justify=CENTER,
                                                                font=("Segoe", 9, "bold")), width=30)
                    entry_tita_cos_pol = Entry(canvas_complex_1, textvariable=entry_tita_cos_polar, justify=CENTER,
                                               font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(150, 140, window=entry_tita_cos_pol, width=60)
                    entry_op_pol = Label(canvas_complex_1, text="+", bg="black", fg="white", justify=CENTER,
                                         font=("Segoe", 12, "bold"))
                    canvas_complex_1.create_window(210, 140, window=entry_op_pol, width=20)
                    canvas_complex_1.create_window(270, 140,
                                                   window=Label(canvas_complex_1, bg="black", fg="white", text="jsin",
                                                                justify=CENTER,
                                                                font=("Segoe", 9, "bold")), width=40)

                    entry_tita_sin_pol = Entry(canvas_complex_1, textvariable=entry_tita_sin_polar, justify=CENTER,
                                               font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(320, 140, window=entry_tita_sin_pol, width=60)
                    canvas_complex_1.create_window(360, 140,
                                                   window=Label(canvas_complex_1, bg="black", fg="white", text="]",
                                                                justify=CENTER,
                                                                font=("Segoe", 15, "bold")), width=20)
                    canvas_complex_1.create_window(200, 200, window=Radiobutton(canvas_complex_1,
                                                                                text="Exponential Form(re^(j" + chr(
                                                                                    0x03B8) + ") Note: angle is in radians",
                                                                                bg="#7198A7",
                                                                                activebackground="#7198A7",
                                                                                activeforeground="black",
                                                                                font=("Segoe", 9, "bold"),
                                                                                fg="black", value="exponential",
                                                                                variable=radio_but_var,
                                                                                command=lambda: change_state_type(
                                                                                    radio_but_var.get())))
                    entry_r_exponential = StringVar()
                    entry_tita_exponential = StringVar()
                    entry_r_exp = Entry(canvas_complex_1, textvariable=entry_r_exponential, justify=CENTER,
                                        font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(160, 260, window=entry_r_exp, width=60)
                    canvas_complex_1.create_window(200, 260,
                                                   window=Label(canvas_complex_1, bg="black", fg="white", text="e",
                                                                justify=CENTER,
                                                                font=("Segoe", 15, "bold")), width=20)
                    canvas_complex_1.create_window(220, 230,
                                                   window=Label(canvas_complex_1, bg="black", fg="white", text="j",
                                                                justify=CENTER,
                                                                font=("Segoe", 9, "bold")), width=20)
                    entry_tita_exp = Entry(canvas_complex_1, textvariable=entry_tita_exponential, justify=CENTER,
                                           font=("Cambria", 9, "bold"))
                    canvas_complex_1.create_window(260, 230, window=entry_tita_exp, width=60)

                    def disable_cartesian():
                        entry_a_cartesian.configure(state=DISABLED)
                        entry_op_cartesian.configure(state=DISABLED)
                        entry_b_cartesian.configure(state=DISABLED)

                    def disable_polar():
                        entry_r_pol.configure(state=DISABLED)
                        entry_tita_cos_pol.configure(state=DISABLED)
                        entry_tita_sin_pol.configure(state=DISABLED)

                    def disable_exponential():
                        entry_r_exp.configure(state=DISABLED)
                        entry_tita_exp.configure(state=DISABLED)

                    def enable_cartesian():
                        entry_a_cartesian.configure(state=NORMAL)
                        entry_op_cartesian.configure(state=NORMAL)
                        entry_b_cartesian.configure(state=NORMAL)

                    def enable_polar():
                        entry_r_pol.configure(state=NORMAL)
                        entry_tita_cos_pol.configure(state=NORMAL)
                        entry_tita_sin_pol.configure(state=NORMAL)

                    def enable_exponential():
                        entry_r_exp.configure(state=NORMAL)
                        entry_tita_exp.configure(state=NORMAL)

                    disable_polar()
                    disable_exponential()
                    enable_cartesian()

                    def continue_complex_2_bind(event):
                        continue_complex_2(radio_but_var.get())

                    def change_state_type(selected):
                        if selected == "cartesian":
                            disable_polar()
                            disable_exponential()
                            enable_cartesian()
                        elif selected == "polar":
                            disable_cartesian()
                            disable_exponential()
                            enable_polar()
                        elif selected == "exponential":
                            disable_cartesian()
                            disable_polar()
                            enable_exponential()

                    entry_a_cartesian.bind("<Return>", continue_complex_2_bind)
                    entry_op_cartesian.bind("<Return>", continue_complex_2_bind)
                    entry_b_cartesian.bind("<Return>", continue_complex_2_bind)
                    entry_r_pol.bind("<Return>", continue_complex_2_bind)
                    entry_tita_cos_pol.bind("<Return>", continue_complex_2_bind)
                    entry_tita_sin_pol.bind("<Return>", continue_complex_2_bind)
                    entry_r_exp.bind("<Return>", continue_complex_2_bind)
                    entry_tita_exp.bind("<Return>", continue_complex_2_bind)

                    def continue_complex_2(selected):
                        if input != "None":
                            if selected == "cartesian":
                                try:
                                    a = float(eval(entry_a_cartesian.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_a_cartesian.focus_force()
                                    return
                                try:
                                    b = float(eval(entry_b_cartesian.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_b_cartesian.focus_force()
                                    return
                                if entry_op_cartesian.get() in ["+", "-"]:
                                    if entry_op_cartesian.get() == "+":
                                        b = 1 * b
                                    else:
                                        b = -1 * b
                                else:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_op_cartesian.focus_force()
                                    return
                                if rpn(a) == "positive" and rpn(b) == "positive":
                                    argument = radians_to_degrees(atan(abso(b) / abso(a)))
                                elif rpn(a) == "negative" and rpn(b) == "positive":
                                    argument = radians_to_degrees(atan(abso(b) / abso(a)))
                                    argument = 180 - argument
                                elif rpn(a) == "negative" and rpn(b) == "negative":
                                    argument = radians_to_degrees(atan(abso(b) / abso(a)))
                                    argument = 180 + argument
                                elif rpn(a) == "positive" and rpn(b) == "negative":
                                    argument = radians_to_degrees(atan(abso(b) / abso(a)))
                                    argument = 360 - argument
                                modulus = round(pow((pow(abso(a), 2) + pow(abso(b), 2)), 0.5), 4)
                            elif selected == "polar":
                                try:
                                    modulus = float(eval(entry_r_pol.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_r_pol.focus_force()
                                    return
                                try:
                                    argument = float(eval(entry_tita_cos_pol.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_tita_cos_pol.focus_force()
                                    return
                                try:
                                    argument_1 = float(eval(entry_tita_sin_pol.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_tita_sin_pol.focus_force()
                                    return
                                if argument_1 != argument:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_tita_cos_pol.focus_force()
                                    return
                                a = round(modulus * cos(degrees_to_radians(argument)), 3)
                                b = round(modulus * sin(degrees_to_radians(argument)), 3)
                            elif selected == "exponential":
                                try:
                                    modulus = float(eval(entry_r_exp.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_r_exp.focus_force()
                                    return
                                try:
                                    argument = radians_to_degrees(float(eval(entry_tita_exp.get())))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    complex_1_window.wm_attributes("-topmost", 1)
                                    complex_1_window.focus_force()
                                    complex_1_window.wm_attributes("-topmost", 0)
                                    entry_tita_exp.focus_force()
                                    return
                                a = round(modulus * cos(degrees_to_radians(argument)), 3)
                                b = round(modulus * sin(degrees_to_radians(argument)), 3)
                            if input == "power":
                                complex_1_window.destroy()
                                complex_power_width = 300

                                complex_power_height = 70

                                complex_power_window = Toplevel()

                                complex_power_window.geometry(
                                    "{}x{}+{}+{}".format(complex_power_width, complex_power_height,

                                                         int((
                                                                     complex_power_window.winfo_screenwidth() - complex_power_width) / 2),

                                                         int((
                                                                     complex_power_window.winfo_screenheight() - complex_power_height) / 2)))

                                complex_power_window.configure(bg="#ECF3FB")

                                complex_power_window.resizable(0, 0)

                                complex_power_window.wm_attributes("-topmost", 1)

                                complex_power_window.focus_force()

                                complex_power_window.wm_attributes("-topmost", 0)

                                complex_power_window.title("Power")
                                complex_power_window.iconbitmap(os.path.join("data", "icon.ico"))

                                canvas_complex_power = Canvas(complex_power_window, width=complex_power_width,
                                                              bg="#ECF3FB",
                                                              height=complex_power_height)

                                canvas_complex_power.pack()
                                global image_complex_root
                                canvas_complex_power.create_image(150, 35, image=image_complex_root)
                                canvas_complex_power.create_text(150, 10, fill="black", text="Enter the power below",
                                                                 justify=CENTER,
                                                                 font=("Segoe", 9, "bold"))
                                canvas_complex_power.create_window(120, 40,
                                                                   window=Label(canvas_complex_power, justify=RIGHT,
                                                                                bg="#7198A7", fg="white",
                                                                                font=("Segoe", 9, "bold"),
                                                                                text="Power:"), width=60)
                                entry_root_complex = Entry(canvas_complex_power, justify=CENTER,
                                                           font=("Cambria", 9, "bold"))
                                entry_root_complex.focus_force()
                                canvas_complex_power.create_window(180, 40, window=entry_root_complex, width=60)

                                def continue_complex_power_bind(event):
                                    continue_complex_power()

                                entry_root_complex.bind("<Return>", continue_complex_power_bind)

                                def continue_complex_power():
                                    try:
                                        power = float(entry_root_complex.get())
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        complex_power_window.wm_attributes("-topmost", 1)
                                        complex_power_window.focus_force()
                                        complex_power_window.wm_attributes("-topmost", 0)
                                        entry_root_complex.focus_force()
                                        return
                                    argument_final = round(argument * power, 3)
                                    modulus_final = round(pow(modulus, power), 3)
                                    a_final = round(modulus_final * cos(degrees_to_radians(argument_final)), 3)
                                    b_final = round(modulus_final * sin(degrees_to_radians(argument_final)), 3)
                                    complex_power_window.destroy()
                                    finish_arth(modulus_final, argument_final, a_final, b_final)
                            elif input == "add" or input == "subtract" or input == "multiply" or input == "divide":
                                complex_1_window.destroy()
                                complex_1_1_width = 400
                                complex_1_1_height = 300
                                complex_1_1_window = Toplevel()
                                complex_1_1_window.geometry("{}x{}+{}+{}".format(complex_1_1_width, complex_1_1_height,

                                                                                 int((
                                                                                             complex_1_1_window.winfo_screenwidth() - complex_1_1_width) / 2),

                                                                                 int((
                                                                                             complex_1_1_window.winfo_screenheight() - complex_1_1_height) / 2)))

                                complex_1_1_window.configure(bg="#ECF3FB")

                                complex_1_1_window.resizable(0, 0)

                                complex_1_1_window.wm_attributes("-topmost", 1)

                                complex_1_1_window.focus_force()

                                complex_1_1_window.wm_attributes("-topmost", 0)

                                complex_1_1_window.title(title.replace("1st", "2nd"))

                                canvas_complex_1_1 = Canvas(complex_1_1_window, width=complex_1_1_width, bg="#ECF3FB",
                                                            height=complex_1_1_height)

                                canvas_complex_1_1.pack()
                                global image_complex_2
                                canvas_complex_1_1.create_image(200, 150, image=image_complex_2)
                                canvas_complex_1_1.create_text(200, 20, fill="black", text=title.replace("1st", "2nd"),
                                                               justify=CENTER,
                                                               font=("Segoe", 12, "bold"))
                                entry_1_a_cart = StringVar()
                                entry_1_op_cart = StringVar()
                                entry_1_b_cart = StringVar()
                                radio_but_var = StringVar()
                                radio_but_var.set("cartesian")

                                def continue_complex_2_bind(event):
                                    continue_complex_2()

                                canvas_complex_1_1.create_window(150, 60,
                                                                 window=Radiobutton(canvas_complex_1_1,
                                                                                    text="Cartesian Form(a + jb or a - jb)",
                                                                                    bg="#7198A7",
                                                                                    activebackground="#7198A7",
                                                                                    activeforeground="white",
                                                                                    font=("Segoe", 9, "bold"),
                                                                                    fg="white", value="cartesian",
                                                                                    variable=radio_but_var,
                                                                                    command=lambda: change_state_type(
                                                                                        radio_but_var.get())))
                                entry_1_a_cartesian = Entry(canvas_complex_1_1, textvariable=entry_1_a_cart,
                                                            justify=CENTER,
                                                            font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(40, 80, window=entry_1_a_cartesian, width=60)
                                entry_1_op_cartesian = Entry(canvas_complex_1_1, textvariable=entry_1_op_cart,
                                                             justify=CENTER,
                                                             font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(120, 80, window=entry_1_op_cartesian, width=30)
                                canvas_complex_1_1.create_window(180, 80,
                                                                 window=Label(canvas_complex_1_1, text="j",
                                                                              justify=CENTER, bg="black", fg="white",
                                                                              font=("Segoe", 9, "bold")),
                                                                 width=20, height=20)
                                entry_1_b_cartesian = Entry(canvas_complex_1_1, textvariable=entry_1_b_cart,
                                                            justify=CENTER,
                                                            font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(220, 80, window=entry_1_b_cartesian, width=60)
                                canvas_complex_1_1.create_window(200, 110, window=Radiobutton(canvas_complex_1_1,
                                                                                              text="Polar Form(r[cosa + jsinb]) Note:Must be true polar form",
                                                                                              bg="#7198A7",
                                                                                              activebackground="#7198A7",
                                                                                              activeforeground="white",
                                                                                              font=("Segoe", 9,
                                                                                                    "bold"), fg="white",
                                                                                              value="polar",
                                                                                              variable=radio_but_var,
                                                                                              command=lambda: change_state_type(
                                                                                                  radio_but_var.get())))
                                entry_1_r_polar = StringVar()
                                entry_1_tita_cos_polar = StringVar()
                                entry_1_op_polar = StringVar()
                                entry_1_tita_sin_polar = StringVar()
                                entry_1_r_pol = Entry(canvas_complex_1_1, textvariable=entry_1_r_polar, justify=CENTER,
                                                      font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(40, 140, window=entry_1_r_pol, width=60)
                                canvas_complex_1_1.create_window(80, 140,
                                                                 window=Label(canvas_complex_1_1, bg="black",
                                                                              fg="white", text="[", justify=CENTER,
                                                                              font=("Segoe", 15, "bold")),
                                                                 width=20)
                                canvas_complex_1_1.create_window(105, 140,
                                                                 window=Label(canvas_complex_1_1, bg="black",
                                                                              fg="white", text="Cos", justify=CENTER,
                                                                              font=("Segoe", 9, "bold")),
                                                                 width=30)
                                entry_1_tita_cos_pol = Entry(canvas_complex_1_1, textvariable=entry_1_tita_cos_polar,
                                                             justify=CENTER,
                                                             font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(150, 140, window=entry_1_tita_cos_pol, width=60)
                                entry_1_op_pol = Label(canvas_complex_1_1, text="+", bg="black", fg="white",
                                                       justify=CENTER,
                                                       font=("Segoe", 12, "bold"))
                                canvas_complex_1_1.create_window(210, 140, window=entry_1_op_pol, width=20)
                                canvas_complex_1_1.create_window(270, 140,
                                                                 window=Label(canvas_complex_1_1, bg="black",
                                                                              fg="white", text="jsin", justify=CENTER,
                                                                              font=("Segoe", 9, "bold")),
                                                                 width=40)

                                entry_1_tita_sin_pol = Entry(canvas_complex_1_1, textvariable=entry_1_tita_sin_polar,
                                                             justify=CENTER,
                                                             font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(320, 140, window=entry_1_tita_sin_pol, width=60)
                                canvas_complex_1_1.create_window(360, 140,
                                                                 window=Label(canvas_complex_1_1, bg="black",
                                                                              fg="white", text="]", justify=CENTER,
                                                                              font=("Segoe", 15, "bold")),
                                                                 width=20)
                                canvas_complex_1_1.create_window(200, 200, window=Radiobutton(canvas_complex_1_1,
                                                                                              text="Exponential Form(re^(j" + chr(
                                                                                                  0x03B8) + ") Note: angle is in radians",
                                                                                              bg="#7198A7",
                                                                                              activebackground="#7198A7",
                                                                                              activeforeground="white",
                                                                                              font=("Segoe", 9,
                                                                                                    "bold"), fg="white",
                                                                                              value="exponential",
                                                                                              variable=radio_but_var,
                                                                                              command=lambda: change_state_type(
                                                                                                  radio_but_var.get())))
                                entry_1_r_exponential = StringVar()
                                entry_1_tita_exponential = StringVar()
                                entry_1_r_exp = Entry(canvas_complex_1_1, textvariable=entry_1_r_exponential,
                                                      justify=CENTER,
                                                      font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(160, 260, window=entry_1_r_exp, width=60)
                                canvas_complex_1_1.create_window(200, 260,
                                                                 window=Label(canvas_complex_1_1, bg="black",
                                                                              fg="white", text="e", justify=CENTER,
                                                                              font=("Segoe", 15, "bold")),
                                                                 width=20)
                                canvas_complex_1_1.create_window(220, 230,
                                                                 window=Label(canvas_complex_1_1, bg="black",
                                                                              fg="white", text="j", justify=CENTER,
                                                                              font=("Segoe", 9, "bold")),
                                                                 width=20)
                                entry_1_tita_exp = Entry(canvas_complex_1_1, textvariable=entry_1_tita_exponential,
                                                         justify=CENTER,
                                                         font=("Cambria", 9, "bold"))
                                canvas_complex_1_1.create_window(260, 230, window=entry_1_tita_exp, width=60)

                                def disable_cartesian():
                                    entry_1_a_cartesian.configure(state=DISABLED)
                                    entry_1_op_cartesian.configure(state=DISABLED)
                                    entry_1_b_cartesian.configure(state=DISABLED)

                                def disable_polar():
                                    entry_1_r_pol.configure(state=DISABLED)
                                    entry_1_tita_cos_pol.configure(state=DISABLED)
                                    entry_1_tita_sin_pol.configure(state=DISABLED)

                                def disable_exponential():
                                    entry_1_r_exp.configure(state=DISABLED)
                                    entry_1_tita_exp.configure(state=DISABLED)

                                def enable_cartesian():
                                    entry_1_a_cartesian.configure(state=NORMAL)
                                    entry_1_op_cartesian.configure(state=NORMAL)
                                    entry_1_b_cartesian.configure(state=NORMAL)

                                def enable_polar():
                                    entry_1_r_pol.configure(state=NORMAL)
                                    entry_1_tita_cos_pol.configure(state=NORMAL)
                                    entry_1_tita_sin_pol.configure(state=NORMAL)

                                def enable_exponential():
                                    entry_1_r_exp.configure(state=NORMAL)
                                    entry_1_tita_exp.configure(state=NORMAL)

                                disable_polar()
                                disable_exponential()
                                enable_cartesian()

                                def continue_complex_2_bind(event):
                                    continue_complex_2(radio_but_var.get())

                                def change_state_type(selected_1):
                                    if selected_1 == "cartesian":
                                        disable_polar()
                                        disable_exponential()
                                        enable_cartesian()
                                    elif selected_1 == "polar":
                                        disable_cartesian()
                                        disable_exponential()
                                        enable_polar()
                                    elif selected_1 == "exponential":
                                        disable_cartesian()
                                        disable_polar()
                                        enable_exponential()

                                entry_1_a_cartesian.bind("<Return>", continue_complex_2_bind)
                                entry_1_op_cartesian.bind("<Return>", continue_complex_2_bind)
                                entry_1_b_cartesian.bind("<Return>", continue_complex_2_bind)
                                entry_1_r_pol.bind("<Return>", continue_complex_2_bind)
                                entry_1_tita_cos_pol.bind("<Return>", continue_complex_2_bind)
                                entry_1_tita_sin_pol.bind("<Return>", continue_complex_2_bind)
                                entry_1_r_exp.bind("<Return>", continue_complex_2_bind)
                                entry_1_tita_exp.bind("<Return>", continue_complex_2_bind)

                                def continue_complex_2(selected_1):
                                    if input != "None":
                                        if selected_1 == "cartesian":
                                            try:
                                                a_1 = float(eval(entry_1_a_cartesian.get()))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_a_cartesian.focus_force()
                                                return
                                            try:
                                                b_1 = float(eval(entry_1_b_cartesian.get()))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_b_cartesian.focus_force()
                                                return
                                            if entry_1_op_cartesian.get() in ["+", "-"]:
                                                if entry_1_op_cartesian.get() == "+":
                                                    b_1 = 1 * b_1
                                                else:
                                                    b_1 = -1 * b_1
                                            else:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_op_cartesian.focus_force()
                                                return
                                            if rpn(a_1) == "positive" and rpn(b_1) == "positive":
                                                argument_1 = radians_to_degrees(atan(abso(b_1) / abso(a_1)))
                                            elif rpn(a_1) == "negative" and rpn(b_1) == "positive":
                                                argument_1 = radians_to_degrees(atan(abso(b_1) / abso(a_1)))
                                                argument_1 = 180 - argument_1
                                            elif rpn(a_1) == "negative" and rpn(b_1) == "negative":
                                                argument_1 = radians_to_degrees(atan(abso(b_1) / abso(a_1)))
                                                argument_1 = 180 + argument_1
                                            elif rpn(a_1) == "positive" and rpn(b_1) == "negative":
                                                argument_1 = radians_to_degrees(atan(abso(b_1) / abso(a_1)))
                                                argument_1 = 360 - argument_1
                                            modulus_1 = round(pow((pow(abso(a_1), 2) + pow(abso(b_1), 2)), 0.5), 4)
                                        elif selected_1 == "polar":
                                            try:
                                                modulus_1 = float(eval(entry_1_r_pol.get()))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_r_pol.focus_force()
                                                return
                                            try:
                                                argument_1 = float(eval(entry_1_tita_cos_pol.get()))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_tita_cos_pol.focus_force()
                                                return
                                            try:
                                                argument_1_2 = float(eval(entry_1_tita_sin_pol.get()))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_tita_sin_pol.focus_force()
                                                return
                                            if argument_1_2 != argument_1:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_tita_cos_pol.focus_force()
                                                return
                                            a_1 = round(modulus_1 * cos(degrees_to_radians(argument_1)), 3)
                                            b_1 = round(modulus_1 * sin(degrees_to_radians(argument_1)), 3)
                                        elif selected_1 == "exponential":
                                            try:
                                                modulus_1 = float(eval(entry_1_r_exp.get()))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_r_exp.focus_force()
                                                return
                                            try:
                                                argument_1 = radians_to_degrees(float(eval(entry_1_tita_exp.get())))
                                            except:
                                                messagebox.showerror("Error", "Value Error")
                                                complex_1_1_window.wm_attributes("-topmost", 1)
                                                complex_1_1_window.focus_force()
                                                complex_1_1_window.wm_attributes("-topmost", 0)
                                                entry_1_tita_exp.focus_force()
                                                return
                                            a_1 = round(modulus_1 * cos(degrees_to_radians(argument_1)), 3)
                                            b_1 = round(modulus_1 * sin(degrees_to_radians(argument_1)), 3)
                                        if input == "add":
                                            a_final = a + a_1
                                            b_final = b + b_1
                                            if rpn(a_final) == "positive" and rpn(b_final) == "positive":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                            elif rpn(a_final) == "negative" and rpn(b_final) == "positive":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                                argument_final = 180 - argument_final
                                            elif rpn(a_final) == "negative" and rpn(b_final) == "negative":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                                argument_final = 180 + argument_final
                                            elif rpn(a_final) == "positive" and rpn(b_final) == "negative":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                                argument_final = 360 - argument_final
                                            modulus_final = round(
                                                pow((pow(abso(a_final), 2) + pow(abso(b_final), 2)), 0.5), 4)
                                        elif input == "subtract":
                                            a_final = a - a_1
                                            b_final = b - b_1
                                            if rpn(a_final) == "positive" and rpn(b_final) == "positive":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                            elif rpn(a_final) == "negative" and rpn(b_final) == "positive":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                                argument_final = 180 - argument_final
                                            elif rpn(a_final) == "negative" and rpn(b_final) == "negative":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                                argument_final = 180 + argument_final
                                            elif rpn(a_final) == "positive" and rpn(b_final) == "negative":
                                                argument_final = radians_to_degrees(atan(abso(b_final) / abso(a_final)))
                                                argument_final = 360 - argument_final
                                            modulus_final = round(
                                                pow((pow(abso(a_final), 2) + pow(abso(b_final), 2)), 0.5), 4)
                                        elif input == "divide":
                                            argument_final = argument - argument_1
                                            modulus_final = round(modulus / modulus_1, 3)
                                            a_final = round(modulus_final * cos(degrees_to_radians(argument_final)), 3)
                                            b_final = round(modulus_final * sin(degrees_to_radians(argument_final)), 3)
                                        elif input == "multiply":
                                            argument_final = argument + argument_1
                                            modulus_final = round(modulus * modulus_1, 3)
                                            a_final = round(modulus_final * cos(degrees_to_radians(argument_final)), 3)
                                            b_final = round(modulus_final * sin(degrees_to_radians(argument_final)), 3)
                                        complex_1_1_window.destroy()
                                        finish_arth(modulus_final, argument_final, a_final, b_final)

                            def finish_arth(modulus_final, argument_final, a_final, b_final):
                                complex_power_form_width = 300

                                complex_power_form_height = 160
                                complex_power_form_window = Toplevel()

                                complex_power_form_window.geometry(
                                    "{}x{}+{}+{}".format(complex_power_form_width, complex_power_form_height,

                                                         int((
                                                                     complex_power_form_window.winfo_screenwidth() - complex_power_form_width) / 2),

                                                         int((
                                                                     complex_power_form_window.winfo_screenheight() - complex_power_form_height) / 2)))

                                complex_power_form_window.configure(bg="#ECF3FB")

                                complex_power_form_window.resizable(0, 0)

                                complex_power_form_window.wm_attributes("-topmost", 1)

                                complex_power_form_window.focus_force()

                                complex_power_form_window.wm_attributes("-topmost", 0)

                                complex_power_form_window.title("Arithmetic Operations of Complex No: Result Form")
                                complex_power_form_window.iconbitmap(os.path.join("data", "icon.ico"))
                                complex_1_1_window.iconbitmap(os.path.join("data", "icon.ico"))

                                canvas_complex_power_form = Canvas(complex_power_form_window,
                                                                   width=complex_power_form_width, bg="#ECF3FB",
                                                                   height=complex_power_form_height)

                                canvas_complex_power_form.pack()

                                global image_complex_form
                                canvas_complex_power_form.create_image(150, 80, image=image_complex_form)
                                canvas_complex_power_form.create_text(150, 10,
                                                                      fill="black",
                                                                      text="Select the form you want your results",
                                                                      justify=CENTER, font=("Times", 9, "bold"))

                                canvas_complex_power_form.create_window(150, 40,
                                                                        window=Button(canvas_complex_power_form,
                                                                                      text="Cartesian Form",
                                                                                      command=lambda: continue_complex_power_form_1(
                                                                                          "c_form", modulus_final,
                                                                                          argument_final, a_final,
                                                                                          b_final),
                                                                                      bg="Black",
                                                                                      fg="White", font=(
                                                                                "Segoe", 9, "bold")),
                                                                        width=250)

                                canvas_complex_power_form.create_window(150, 80,
                                                                        window=Button(canvas_complex_power_form,
                                                                                      text="Polar Form",

                                                                                      command=lambda: continue_complex_power_form_1(
                                                                                          "p_form", modulus_final,
                                                                                          argument_final, a_final,
                                                                                          b_final),
                                                                                      bg="Black",

                                                                                      fg="White", font=(
                                                                                "Segoe", 9, "bold")),
                                                                        width=250)
                                canvas_complex_power_form.create_window(150, 120,
                                                                        window=Button(canvas_complex_power_form,
                                                                                      text="Exponential Form",

                                                                                      command=lambda: continue_complex_power_form_1(
                                                                                          "e_form", modulus_final,
                                                                                          argument_final, a_final,
                                                                                          b_final),
                                                                                      bg="Black",

                                                                                      fg="White", font=(
                                                                                "Segoe", 9, "bold")),
                                                                        width=250)

                                def continue_complex_power_form_1(form, modulus, argument, a, b):
                                    if form == "c_form":
                                        a = str(a) + " "
                                        if rpn(b) == "negative":
                                            op = "- "
                                        else:
                                            op = "+ "
                                        b = str(abso(b))
                                        pow_solve = a + op + "j" + b
                                    elif form == "p_form":
                                        pow_solve = str(modulus) + "(cos(" + str(round(argument, 3)) + ")+jsin(" + str(
                                            round(argument, 3)) + "))"
                                    elif form == "e_form":
                                        pow_solve = str(modulus) + "e^(j" + str(
                                            round(degrees_to_radians(argument), 3)) + ")"
                                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                        label_display_1_var.set("(" + str(pow_solve) + ")")

                                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")

                                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                        label_display_1_var.set("(" + str(pow_solve) + ")")

                                        label_display_2_var.set("")

                                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                        label_display_1_var.set("(" + str(pow_solve) + ")")

                                        label_display_2_var.set("")
                                    update_label_1()

                                    old_label_display_1_var.set(label_display_1_var.get())
                                    root.wm_attributes("-topmost", 1)

                                    root.focus_force()

                                    root.wm_attributes("-topmost", 0)
                                    return

                            if input == "modulus":
                                pow_solve = str(modulus)
                            elif input == "arg":
                                pow_solve = str(argument)
                            elif input == "roots":
                                complex_roots_width = 300

                                complex_roots_height = 70

                                complex_roots_window = Toplevel()

                                complex_roots_window.geometry(
                                    "{}x{}+{}+{}".format(complex_roots_width, complex_roots_height,

                                                         int((
                                                                     complex_roots_window.winfo_screenwidth() - complex_roots_width) / 2),

                                                         int((
                                                                     complex_roots_window.winfo_screenheight() - complex_roots_height) / 2)))

                                complex_roots_window.configure(bg="#ECF3FB")

                                complex_roots_window.resizable(0, 0)

                                complex_roots_window.wm_attributes("-topmost", 1)

                                complex_roots_window.focus_force()

                                complex_roots_window.wm_attributes("-topmost", 0)

                                complex_roots_window.title("Roots")
                                complex_roots_window.iconbitmap(os.path.join("data", "icon.ico"))

                                canvas_complex_roots = Canvas(complex_roots_window, width=complex_roots_width,
                                                              bg="#ECF3FB",
                                                              height=complex_roots_height)

                                canvas_complex_roots.pack()
                                canvas_complex_roots.create_image(150, 35, image=image_complex_root)
                                canvas_complex_roots.create_text(150, 10, fill="black", text="Enter the root below",
                                                                 justify=CENTER,
                                                                 font=("Segoe", 9, "bold"))
                                canvas_complex_roots.create_window(120, 40,
                                                                   window=Label(canvas_complex_roots, justify=RIGHT,
                                                                                bg="#7198A7", fg="white",
                                                                                font=("Segoe", 9, "bold"),
                                                                                text="Root:"), width=60)
                                entry_root_complex = Entry(canvas_complex_roots, justify=CENTER,
                                                           font=("Cambria", 9, "bold"))
                                entry_root_complex.focus_force()
                                canvas_complex_roots.create_window(180, 40, window=entry_root_complex, width=60)

                                def continue_complex_roots_bind(event):
                                    continue_complex_roots()

                                entry_root_complex.bind("<Return>", continue_complex_roots_bind)

                                def continue_complex_roots():
                                    if "." in str(entry_root_complex.get()):
                                        messagebox.showerror("Error", "Value Error")
                                        complex_roots_window.wm_attributes("-topmost", 1)
                                        complex_roots_window.focus_force()
                                        complex_roots_window.wm_attributes("-topmost", 0)
                                        entry_root_complex.focus_force()
                                        return
                                    try:
                                        roots = int(entry_root_complex.get())
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        complex_roots_window.wm_attributes("-topmost", 1)
                                        complex_roots_window.focus_force()
                                        complex_roots_window.wm_attributes("-topmost", 0)
                                        entry_root_complex.focus_force()
                                        return
                                    ang_add = round(360 / roots, 2)
                                    init_modulus = round(pow(modulus, pow(roots, -1)), 3)
                                    init_arg = round(argument / roots, 2)
                                    list_arg = []
                                    list_arg.append(init_arg)
                                    complex_roots_form_width = 300

                                    complex_roots_form_height = 160
                                    complex_roots_form_window = Toplevel()

                                    complex_roots_form_window.geometry(
                                        "{}x{}+{}+{}".format(complex_roots_form_width, complex_roots_form_height,

                                                             int((
                                                                         complex_roots_form_window.winfo_screenwidth() - complex_roots_form_width) / 2),

                                                             int((
                                                                         complex_roots_form_window.winfo_screenheight() - complex_roots_form_height) / 2)))

                                    complex_roots_form_window.configure(bg="#ECF3FB")

                                    complex_roots_form_window.resizable(0, 0)

                                    complex_roots_form_window.wm_attributes("-topmost", 1)

                                    complex_roots_form_window.focus_force()

                                    complex_roots_form_window.wm_attributes("-topmost", 0)

                                    complex_roots_form_window.title("Roots of Complex No")
                                    complex_roots_form_window.iconbitmap(os.path.join("data", "icon.ico"))

                                    canvas_complex_roots_form = Canvas(complex_roots_form_window,
                                                                       width=complex_roots_form_width, bg="#ECF3FB",
                                                                       height=complex_roots_form_height)

                                    canvas_complex_roots_form.pack()

                                    global image_complex_form
                                    canvas_complex_roots_form.create_image(150, 80, image=image_complex_form)
                                    canvas_complex_roots_form.create_text(150, 10,
                                                                          fill="black",
                                                                          text="Select the form you want your results",
                                                                          justify=CENTER, font=("Times", 9, "bold"))

                                    canvas_complex_roots_form.create_window(150, 40,
                                                                            window=Button(canvas_complex_roots_form,
                                                                                          text="Cartesian Form",
                                                                                          command=lambda: continue_complex_roots_form_1(
                                                                                              "c_form", init_arg, roots,
                                                                                              ang_add, init_modulus),
                                                                                          bg="Black",
                                                                                          fg="White", font=(
                                                                                    "Segoe", 9, "bold")),
                                                                            width=250)

                                    canvas_complex_roots_form.create_window(150, 80,
                                                                            window=Button(canvas_complex_roots_form,
                                                                                          text="Polar Form",

                                                                                          command=lambda: continue_complex_roots_form_1(
                                                                                              "p_form", init_arg, roots,
                                                                                              ang_add, init_modulus),
                                                                                          bg="Black",

                                                                                          fg="White", font=(
                                                                                    "Segoe", 9, "bold")),
                                                                            width=250)
                                    canvas_complex_roots_form.create_window(150, 120,
                                                                            window=Button(canvas_complex_roots_form,
                                                                                          text="Exponential Form",

                                                                                          command=lambda: continue_complex_roots_form_1(
                                                                                              "e_form", init_arg, roots,
                                                                                              ang_add, init_modulus),
                                                                                          bg="Black",

                                                                                          fg="White", font=(
                                                                                    "Segoe", 9, "bold")),
                                                                            width=250)

                                    def continue_complex_roots_form_1(form, init_arg, roots, ang_add, init_modulus):
                                        if form == "p_form":
                                            pow_solve = str(init_modulus) + "(cos(" + str(init_arg) + ") + jsin(" + str(
                                                init_arg) + "))"
                                            for num in range(1, roots):
                                                init_arg += ang_add
                                                list_arg.append(init_arg)
                                                pow_solve += "; " + str(init_modulus) + "(cos(" + str(
                                                    init_arg) + ") + jsin(" + str(init_arg) + "))"
                                            principal_arg_id = highest_val_in_lst_id(arg_dist_conv(list_arg))
                                            principal_arg = list_arg[principal_arg_id]
                                            pow_solve += "; Principal Root: " + str(init_modulus) + "(cos(" + str(
                                                principal_arg) + ") + jsin(" + str(
                                                principal_arg) + "))"
                                        elif form == "c_form":
                                            a = str(round(init_modulus * cos(degrees_to_radians(init_arg)), 3)) + " "
                                            b = round(init_modulus * sin(degrees_to_radians(init_arg)), 3)
                                            if rpn(b) == "negative":
                                                op = "- "
                                            else:
                                                op = "+ "
                                            b = str(abso(b))
                                            pow_solve = a + op + "j" + b
                                            for num in range(1, roots):
                                                init_arg += ang_add
                                                list_arg.append(init_arg)
                                                a = str(
                                                    round(init_modulus * cos(degrees_to_radians(init_arg)), 3)) + " "
                                                b = round(init_modulus * sin(degrees_to_radians(init_arg)), 3)
                                                if rpn(b) == "negative":
                                                    op = "- "
                                                else:
                                                    op = "+ "
                                                b = str(abso(b))
                                                pow_solve += "; " + a + op + "j" + b
                                            principal_arg_id = highest_val_in_lst_id(arg_dist_conv(list_arg))
                                            principal_arg = list_arg[principal_arg_id]
                                            a = str(
                                                round(init_modulus * cos(degrees_to_radians(principal_arg)), 3)) + " "
                                            b = round(init_modulus * sin(degrees_to_radians(principal_arg)), 3)
                                            if rpn(b) == "negative":
                                                op = "- "
                                            else:
                                                op = "+ "
                                            b = str(abso(b))
                                            pow_solve += "; Principal Root: " + a + op + "j" + b
                                        elif form == "e_form":
                                            pow_solve = str(init_modulus) + "(e^(j" + str(
                                                round(degrees_to_radians(init_arg), 3)) + ")"
                                            for num in range(1, roots):
                                                init_arg += ang_add
                                                list_arg.append(init_arg)
                                                pow_solve += "; " + str(init_modulus) + "(e^(j" + str(
                                                    round(degrees_to_radians(init_arg), 3)) + ")"
                                            principal_arg_id = highest_val_in_lst_id(arg_dist_conv(list_arg))
                                            principal_arg = list_arg[principal_arg_id]
                                            pow_solve += "; Principal Root: " + str(init_modulus) + "(e^(j" + str(
                                                round(degrees_to_radians(principal_arg), 3)) + ")"
                                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                            label_display_1_var.set("(" + str(pow_solve) + ")")

                                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                            label_display_1_var.set(
                                                label_display_1_var.get() + "(" + str(pow_solve) + ")")

                                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                            label_display_1_var.set("(" + str(pow_solve) + ")")

                                            label_display_2_var.set("")

                                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                            label_display_1_var.set("(" + str(pow_solve) + ")")

                                            label_display_2_var.set("")
                                        update_label_1()

                                        old_label_display_1_var.set(label_display_1_var.get())

                                        complex_1_window.destroy()
                                        complex_roots_window.destroy()
                                        complex_roots_form_window.destroy()

                                        root.wm_attributes("-topmost", 1)

                                        root.focus_force()

                                        root.wm_attributes("-topmost", 0)
                                        return
                            elif input == "conv":
                                if selected == "cartesian":
                                    entry_r_polar.set(modulus)
                                    entry_tita_cos_polar.set(argument)
                                    entry_tita_sin_polar.set(argument)
                                    entry_r_exponential.set(modulus)
                                    entry_tita_exponential.set(degrees_to_radians(argument))
                                elif selected == "polar":
                                    entry_a_cart.set(a)
                                    if rpn(b) == "negative":
                                        entry_op_cart.set("-")
                                    else:
                                        entry_op_cart.set("+")
                                    entry_b_cart.set(abso(b))
                                    entry_r_exponential.set(modulus)
                                    entry_tita_exponential.set(degrees_to_radians(argument))
                                elif selected == "exponential":
                                    entry_a_cart.set(a)
                                    if rpn(b) == "negative":
                                        entry_op_cart.set("-")
                                    else:
                                        entry_op_cart.set("+")
                                    entry_b_cart.set(abso(b))
                                    entry_r_polar.set(modulus)
                                    entry_tita_cos_polar.set(argument)
                                    entry_tita_sin_polar.set(argument)
                            if input != "conv" and input != "roots" and input not in ["add", "subtract", "multiply",
                                                                                      "divide", "power"]:
                                if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                    label_display_1_var.set("(" + str(pow_solve) + ")")

                                elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                    label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")

                                elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                    label_display_1_var.set("(" + str(pow_solve) + ")")

                                    label_display_2_var.set("")

                                elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                    label_display_1_var.set("(" + str(pow_solve) + ")")

                                    label_display_2_var.set("")
                                update_label_1()

                                old_label_display_1_var.set(label_display_1_var.get())

                                complex_1_window.destroy()

                                root.wm_attributes("-topmost", 1)

                                root.focus_force()

                                root.wm_attributes("-topmost", 0)
                                return











            elif input == "integral":
                integral_width = 300

                integral_height = 320

                integral_window = Toplevel()

                integral_window.geometry("{}x{}+{}+{}".format(integral_width, integral_height,

                                                              int((
                                                                          integral_window.winfo_screenwidth() - integral_width) / 2),

                                                              int((
                                                                          integral_window.winfo_screenheight() - integral_height) / 2)))

                integral_window.configure(bg="#ECF3FB")

                integral_window.resizable(0, 0)

                integral_window.wm_attributes("-topmost", 1)

                integral_window.focus_force()

                integral_window.wm_attributes("-topmost", 0)

                integral_window.title("Integral")
                integral_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_integral = Canvas(integral_window, width=integral_width, bg="#ECF3FB", height=integral_height)

                canvas_integral.pack()
                canvas_integral.create_text(150, 20, text="Integral", font=("Segoe", 12, "bold"))
                canvas_integral.create_window(40, 100, window=Label(canvas_integral, bg="#ECF3FB", text=chr(0x222B),
                                                                    font=("Segoe", 30, "bold")), width=40,
                                              height=80)
                entry_a = Entry(canvas_integral, bg="#ECF3FB", justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_integral.create_window(12, 120, window=entry_a, width=20, height=20)
                entry_b = Entry(canvas_integral, bg="#ECF3FB", justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_integral.create_window(65, 80, window=entry_b, width=20, height=20)
                textbox_equation = Text(canvas_integral, bg="#ECF3FB", font=("Segoe", 9, "bold"))
                canvas_integral.create_window(180, 100, window=textbox_equation, width=200, height=20)
                entry_c = Entry(canvas_integral, bg="#ECF3FB", justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_integral.create_window(280, 70, window=entry_c, width=20, height=20)
                canvas_integral.create_text(150, 150, text="Variable:", font=("Segoe", 9, "bold"))
                entry_variable = Entry(canvas_integral, bg="#ECF3FB", justify=CENTER, font=("Segoe", 9, "bold"))
                canvas_integral.create_window(200, 150, window=entry_variable, width=20, height=20)


            elif input == "matrix":

                global image_mat_main
                global image_mat_2
                global image_mat_arith
                matrix_width = 300

                matrix_height = 320

                matrix_window = Toplevel()

                matrix_window.geometry("{}x{}+{}+{}".format(matrix_width, matrix_height,

                                                            int((matrix_window.winfo_screenwidth() - matrix_width) / 2),

                                                            int((
                                                                        matrix_window.winfo_screenheight() - matrix_height) / 2)))

                matrix_window.configure(bg="#ECF3FB")

                matrix_window.resizable(0, 0)

                matrix_window.wm_attributes("-topmost", 1)

                matrix_window.focus_force()

                matrix_window.wm_attributes("-topmost", 0)

                matrix_window.title("Matrix")
                matrix_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_matrix = Canvas(matrix_window, width=matrix_width, bg="#ECF3FB", height=matrix_height)

                canvas_matrix.pack()

                canvas_matrix.create_image(150, 160, image=image_mat_main)
                canvas_matrix.create_text(150, 10, fill="black", text="Select Operation", justify=CENTER,
                                          font=("Times", 9, "bold"))

                canvas_matrix.create_window(150, 40, window=Button(canvas_matrix, text="Adjoint of a Matrix",
                                                                   command=lambda: continue_matrix_1("adjoint"),
                                                                   bg="Black",
                                                                   fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                canvas_matrix.create_window(150, 80, window=Button(canvas_matrix, text="Inverse of A Matix",

                                                                   command=lambda: continue_matrix_1("inverse"),
                                                                   bg="Black",

                                                                   fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                canvas_matrix.create_window(150, 120, window=Button(canvas_matrix, text="Determinant of a Matrix",

                                                                    command=lambda: continue_matrix_1("det"),
                                                                    bg="Black",

                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                canvas_matrix.create_window(150, 160, window=Button(canvas_matrix, text="EigenValues",

                                                                    command=lambda: continue_matrix_1("evalues"),
                                                                    bg="Black",

                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                canvas_matrix.create_window(150, 200, window=Button(canvas_matrix, text="EigenVectors(coming soon)",
                                                                    bg="Black",

                                                                    fg="White", font=("Segoe", 7, "bold")),
                                            width=200)

                canvas_matrix.create_window(150, 240, window=Button(canvas_matrix, text="Arithmetic Operations",
                                                                    bg="Black",
                                                                    command=lambda: continue_matrix_1_arith(),

                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                canvas_matrix.create_window(150, 280, window=Button(canvas_matrix, text="Transpose of A Matrix",

                                                                    command=lambda: continue_matrix_1("transpose"),
                                                                    bg="Black",

                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                def continue_matrix_1_arith():
                    matrix_arith_type_width = 300

                    matrix_arith_type_height = 160
                    matrix_arith_type_window = Toplevel()

                    matrix_window.destroy()
                    matrix_arith_type_window.geometry(
                        "{}x{}+{}+{}".format(matrix_arith_type_width, matrix_arith_type_height,

                                             int((
                                                         matrix_arith_type_window.winfo_screenwidth() - matrix_arith_type_width) / 2),

                                             int((
                                                         matrix_arith_type_window.winfo_screenheight() - matrix_arith_type_height) / 2)))

                    matrix_arith_type_window.configure(bg="#ECF3FB")

                    matrix_arith_type_window.resizable(0, 0)

                    matrix_arith_type_window.wm_attributes("-topmost", 1)

                    matrix_arith_type_window.focus_force()

                    matrix_arith_type_window.wm_attributes("-topmost", 0)

                    matrix_arith_type_window.title("Arithmetic")
                    matrix_arith_type_window.iconbitmap(os.path.join("data", "icon.ico"))

                    canvas_matrix_arith_type = Canvas(matrix_arith_type_window, width=matrix_arith_type_width,
                                                      bg="#ECF3FB",
                                                      height=matrix_arith_type_height)

                    canvas_matrix_arith_type.pack()

                    canvas_matrix_arith_type.create_image(150, 80, image=image_mat_arith)
                    canvas_matrix_arith_type.create_text(150, 10, fill="black",
                                                         text="Select the type of arithmetic operation",
                                                         justify=CENTER, font=("Times", 9, "bold"))

                    canvas_matrix_arith_type.create_window(150, 40, window=Button(canvas_matrix_arith_type,
                                                                                  text="Addition",
                                                                                  command=lambda: continue_matrix_arith_type_1(
                                                                                      "add"),
                                                                                  bg="Black",
                                                                                  fg="White",
                                                                                  font=("Segoe", 9, "bold")),
                                                           width=250)

                    canvas_matrix_arith_type.create_window(150, 80, window=Button(canvas_matrix_arith_type,
                                                                                  text="Subtraction",

                                                                                  command=lambda: continue_matrix_arith_type_1(
                                                                                      "subtract"),
                                                                                  bg="Black",

                                                                                  fg="White",
                                                                                  font=("Segoe", 9, "bold")),
                                                           width=250)
                    canvas_matrix_arith_type.create_window(150, 120, window=Button(canvas_matrix_arith_type,
                                                                                   text="Multiplication",

                                                                                   command=lambda: continue_matrix_arith_type_1(
                                                                                       "multiply"),
                                                                                   bg="Black",

                                                                                   fg="White",
                                                                                   font=("Segoe", 9, "bold")),
                                                           width=250)

                    def continue_matrix_arith_type_1(type):
                        matrix_arith_type_window.destroy()
                        continue_matrix_1(type)

                def continue_matrix_1(input):

                    if input == "evalues":

                        title = "EigenValues of a Matrix"

                    elif input == "evectors":

                        title = "EigenVectors of a Matrix"

                    elif input == "transpose":

                        title = "Transpose of a Matrix"

                    elif input == "add" or input == "subtract" or input == "multiply":

                        title = "Arithmetic 1st: " + input[0].upper() + input[1:].lower()

                    elif input == "det":

                        title = "Determinant of a Matrix"

                    elif input == "adjoint":

                        title = "Adjoint of a Matrix"

                    elif input == "inverse":

                        title = "Inverse of a Matrix"

                    matrix_1_width = 300

                    matrix_1_height = 400

                    matrix_1_window = Toplevel()

                    matrix_1_window.geometry("{}x{}+{}+{}".format(matrix_1_width, matrix_1_height,

                                                                  int((

                                                                              matrix_1_window.winfo_screenwidth() - matrix_1_width) / 2),

                                                                  int((

                                                                              matrix_1_window.winfo_screenheight() - matrix_1_height) / 2)))

                    matrix_1_window.configure(bg="#ECF3FB")

                    matrix_1_window.resizable(0, 0)

                    matrix_1_window.wm_attributes("-topmost", 1)

                    matrix_1_window.focus_force()

                    matrix_1_window.wm_attributes("-topmost", 0)

                    matrix_1_window.title(title)
                    matrix_1_window.iconbitmap(os.path.join("data", "icon.ico"))

                    matrix_window.destroy()

                    canvas_matrix_1 = Canvas(matrix_1_window, width=matrix_1_width, bg="#ECF3FB",
                                             height=matrix_1_height)

                    canvas_matrix_1.pack()

                    canvas_matrix_1.create_image(150, 200, image=image_mat_2)
                    canvas_matrix_1.create_text(150, 10, fill="black", text=title + ": Enter The Values",
                                                justify=CENTER,
                                                font=("Times", 9, "bold"))
                    canvas_matrix_1.create_rectangle(20, 80, 22, 220, fill="black")
                    canvas_matrix_1.create_rectangle(278, 80, 280, 220, fill="black")
                    entry_1_1_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(60, 100, window=entry_1_1_3_by_3, width=60)
                    entry_1_2_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(150, 100, window=entry_1_2_3_by_3, width=60)
                    entry_1_3_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(240, 100, window=entry_1_3_3_by_3, width=60)
                    entry_2_1_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(60, 140, window=entry_2_1_3_by_3, width=60)
                    entry_2_2_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(150, 140, window=entry_2_2_3_by_3, width=60)
                    entry_2_3_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(240, 140, window=entry_2_3_3_by_3, width=60)
                    entry_3_1_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(60, 180, window=entry_3_1_3_by_3, width=60)
                    entry_3_2_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(150, 180, window=entry_3_2_3_by_3, width=60)
                    entry_3_3_3_by_3 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(240, 180, window=entry_3_3_3_by_3, width=60)
                    canvas_matrix_1.create_rectangle(50, 300, 52, 380, fill="black")
                    canvas_matrix_1.create_rectangle(248, 300, 250, 380, fill="black")
                    entry_1_1_2_by_2 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(90, 320, window=entry_1_1_2_by_2, width=60)
                    entry_1_2_2_by_2 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(210, 320, window=entry_1_2_2_by_2, width=60)
                    entry_2_1_2_by_2 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(90, 360, window=entry_2_1_2_by_2, width=60)
                    entry_2_2_2_by_2 = Entry(canvas_matrix_1, width=60, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_matrix_1.create_window(210, 360, window=entry_2_2_2_by_2, width=60)
                    type_of_mat = StringVar()
                    type_of_mat.set("2_by_2")
                    canvas_matrix_1.update()
                    canvas_matrix_1.update_idletasks()
                    canvas_matrix_1.create_window(150, 60, window=Radiobutton(canvas_matrix_1,
                                                                              command=lambda: select_r_but_type(
                                                                                  type_of_mat.get()), value="3_by_3",
                                                                              variable=type_of_mat,
                                                                              text="3 by 3 Matrix",
                                                                              font=("Segoe", 9, "bold"),
                                                                              bg="#ECF3FB", activebackground="#ECF3FB"))
                    canvas_matrix_1.create_window(150, 280, window=Radiobutton(canvas_matrix_1,
                                                                               command=lambda: select_r_but_type(
                                                                                   type_of_mat.get()), value="2_by_2",
                                                                               variable=type_of_mat,
                                                                               text="2 by 2 Matrix",
                                                                               font=("Segoe", 9, "bold"),
                                                                               bg="#ECF3FB",
                                                                               activebackground="#ECF3FB"))

                    def disable_3_by_3():
                        entry_1_1_3_by_3.configure(state=DISABLED)
                        entry_1_2_3_by_3.configure(state=DISABLED)
                        entry_1_3_3_by_3.configure(state=DISABLED)
                        entry_2_1_3_by_3.configure(state=DISABLED)
                        entry_2_2_3_by_3.configure(state=DISABLED)
                        entry_2_3_3_by_3.configure(state=DISABLED)
                        entry_3_1_3_by_3.configure(state=DISABLED)
                        entry_3_2_3_by_3.configure(state=DISABLED)
                        entry_3_3_3_by_3.configure(state=DISABLED)

                    def enable_3_by_3():
                        entry_1_1_3_by_3.configure(state=NORMAL)
                        entry_1_2_3_by_3.configure(state=NORMAL)
                        entry_1_3_3_by_3.configure(state=NORMAL)
                        entry_2_1_3_by_3.configure(state=NORMAL)
                        entry_2_2_3_by_3.configure(state=NORMAL)
                        entry_2_3_3_by_3.configure(state=NORMAL)
                        entry_3_1_3_by_3.configure(state=NORMAL)
                        entry_3_2_3_by_3.configure(state=NORMAL)
                        entry_3_3_3_by_3.configure(state=NORMAL)

                    def disable_2_by_2():
                        entry_1_1_2_by_2.configure(state=DISABLED)
                        entry_1_2_2_by_2.configure(state=DISABLED)
                        entry_2_1_2_by_2.configure(state=DISABLED)
                        entry_2_2_2_by_2.configure(state=DISABLED)

                    def enable_2_by_2():
                        entry_1_1_2_by_2.configure(state=NORMAL)
                        entry_1_2_2_by_2.configure(state=NORMAL)
                        entry_2_1_2_by_2.configure(state=NORMAL)
                        entry_2_2_2_by_2.configure(state=NORMAL)

                    def select_r_but_type(select):
                        if select == "2_by_2":
                            disable_3_by_3()
                            enable_2_by_2()
                        else:
                            disable_2_by_2()
                            enable_3_by_3()

                    def ret_ent_bind(evt):
                        continue_matrix_2(type_of_mat.get())

                    select_r_but_type("2_by_2")

                    entry_1_1_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_1_2_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_1_3_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_2_1_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_2_2_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_2_3_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_3_1_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_3_2_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_3_3_3_by_3.bind("<Return>", ret_ent_bind)
                    entry_1_1_2_by_2.bind("<Return>", ret_ent_bind)
                    entry_1_2_2_by_2.bind("<Return>", ret_ent_bind)
                    entry_2_1_2_by_2.bind("<Return>", ret_ent_bind)
                    entry_2_2_2_by_2.bind("<Return>", ret_ent_bind)

                    def continue_matrix_2(sel):
                        cwk_am.set(sel)
                        if sel == "2_by_2":
                            try:
                                a = float(eval(entry_1_1_2_by_2.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_1_1_2_by_2.focus_force()
                                return
                            try:
                                b = float(eval(entry_1_2_2_by_2.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_1_2_2_by_2.focus_force()
                                return
                            try:
                                c = float(eval(entry_2_1_2_by_2.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_2_1_2_by_2.focus_force()
                                return
                            try:
                                d = float(eval(entry_2_2_2_by_2.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_2_2_2_by_2.focus_force()
                                return
                        else:
                            try:
                                a = float(eval(entry_1_1_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_1_1_3_by_3.focus_force()
                                return
                            try:
                                b = float(eval(entry_1_2_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_1_2_3_by_3.focus_force()
                                return
                            try:
                                c = float(eval(entry_1_3_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_1_3_3_by_3.focus_force()
                                return
                            try:
                                d = float(eval(entry_2_1_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_2_1_3_by_3.focus_force()
                                return
                            try:
                                e = float(eval(entry_2_2_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_2_2_3_by_3.focus_force()
                                return
                            try:
                                f = float(eval(entry_2_3_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_2_3_3_by_3.focus_force()
                                return
                            try:
                                g = float(eval(entry_3_1_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_3_1_3_by_3.focus_force()
                                return
                            try:
                                h = float(eval(entry_3_2_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_3_2_3_by_3.focus_force()
                                return
                            try:
                                i = float(eval(entry_3_3_3_by_3.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                matrix_1_window.wm_attributes("-topmost", 1)
                                matrix_1_window.focus_force()
                                matrix_1_window.wm_attributes("-topmost", 0)
                                entry_3_3_3_by_3.focus_force()
                                return

                        def cofactors(a, b, c, d, e, f, g, h, i):
                            if sel == "2_by_2":
                                return "Error"
                            cofac_a = t_by_2_md(e, f, h, i)
                            cofac_b = -1 * t_by_2_md(d, f, g, i)
                            cofac_c = t_by_2_md(d, e, g, h)
                            cofac_d = -1 * t_by_2_md(b, c, h, i)
                            cofac_e = t_by_2_md(a, c, g, i)
                            cofac_f = -1 * t_by_2_md(a, b, g, h)
                            cofac_g = t_by_2_md(b, c, e, f)
                            cofac_h = -1 * t_by_2_md(a, c, d, f)
                            cofac_i = t_by_2_md(a, b, d, e)
                            return cofac_a, cofac_b, cofac_c, cofac_d, cofac_e, cofac_f, cofac_g, cofac_h, cofac_i

                        def transpose(a, b, c, d, e, f, g, h, i):
                            if sel == "2_by_2":
                                return a, c, b, d
                            elif sel == "3_by_3":
                                return a, d, g, b, e, h, c, f, i

                        def adjoint(a, b, c, d, e, f, g, h, i):
                            if sel == "2_by_2":
                                return "Error"
                            else:
                                ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i = cofactors(a, b, c,
                                                                                                          d, e, f, g, h,
                                                                                                          i)
                                ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i = transpose(ans_a,
                                                                                                          ans_b, ans_c,
                                                                                                          ans_d, ans_e,
                                                                                                          ans_f, ans_g,
                                                                                                          ans_h, ans_i)
                                return ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i

                        def det(a, b, c, d, e, f, g, h, i):
                            if sel == "2_by_2":
                                det = t_by_2_md(a, b, c, d)
                                return det
                            else:
                                det = t_by_3_md(a, b, c, d, e, f, g, h, i)
                                return det

                        def inverse(a, b, c, d, e, f, g, h, i):
                            if sel == "2_by_2":
                                return d, -1 * b, -1 * c, a
                            else:
                                ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i = adjoint(a, b, c, d, e,
                                                                                                        f, g,
                                                                                                        h, i)
                                deter = det(a, b, c, d, e, f, g, h, i)
                                if deter == 0:
                                    ans_a = 0
                                    ans_b = 0
                                    ans_c = 0
                                    ans_d = 0
                                    ans_e = 0
                                    ans_f = 0
                                    ans_g = 0
                                    ans_h = 0
                                    ans_i = 0
                                else:
                                    ans_a = str(ans_a) + " / " + str(deter)
                                    ans_b = str(ans_b) + " / " + str(deter)
                                    ans_c = str(ans_c) + " / " + str(deter)
                                    ans_d = str(ans_d) + " / " + str(deter)
                                    ans_e = str(ans_e) + " / " + str(deter)
                                    ans_f = str(ans_f) + " / " + str(deter)
                                    ans_g = str(ans_g) + " / " + str(deter)
                                    ans_h = str(ans_h) + " / " + str(deter)
                                    ans_i = str(ans_i) + " / " + str(deter)
                                return ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i

                        def eigen_values(a, b, c, d, e, f, g, h, i):
                            if sel == "2_by_2":
                                eig_val = quadratic_formula(1, (-1 * a) + (-1 * d), (a * d) - (b * c))
                                return eig_val
                            else:
                                p_3_c = -1
                                p_2_c = a + e + i
                                p_1_c = (-1 * a * e) + (-1 * a * i) + (-1 * e * i) + (f * h) + (b * d) + (c * g)
                                p_0_c = (a * e * i) - (a * f * h) - (b * d * i) + (b * f * g) + (c * d * h) - (
                                        c * g * e)
                                eig_val = find_roots(p_3_c, 3, p_2_c, 2, p_1_c, 1, p_0_c, 0, 0, 0, 0, 0)
                                return eig_val

                        def continue_matrix_3(ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i):
                            try:
                                matrix_1_window.destroy()
                            except:
                                pass
                            if input == "evalues":
                                pow_solve = ""
                                line_no = 0
                                for data in ans_a:
                                    if line_no == len(ans_a) - 1:
                                        pow_solve += str(data)
                                    else:
                                        pow_solve += str(data) + ", "
                                    line_no += 1
                                ans_a = 0
                            elif input == "det":
                                pow_solve = str(ans_a)
                                ans_a = 0
                            if ans_a == 0 and ans_b == 0 and ans_c == 0 and ans_d == 0 and ans_e == 0 and ans_f == 0 and ans_g == 0 and ans_h == 0 and ans_i == 0:
                                if input == "det":
                                    pass
                                elif input == "evalues":
                                    pass
                                else:
                                    pow_solve = "Error"
                                if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                    label_display_1_var.set("(" + str(pow_solve) + ")")

                                elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                    label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")

                                elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                    label_display_1_var.set("(" + str(pow_solve) + ")")

                                    label_display_2_var.set("")

                                elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                    label_display_1_var.set("(" + str(pow_solve) + ")")

                                    label_display_2_var.set("")
                                update_label_1()

                                old_label_display_1_var.set(label_display_1_var.get())

                                root.wm_attributes("-topmost", 1)

                                root.focus_force()

                                root.wm_attributes("-topmost", 0)
                                return

                            if input == "inverse" or input == "adjoint" or input == "transpose" or input == "add" or input == "subtract" or input == "multiply":
                                if input == "inverse":
                                    title = "Answer: Inverse of a Matrix"
                                elif input == "adjoint":
                                    title = "Answer: Adjoint of a Matrix"
                                elif input == "transpose":
                                    title = "Answer: Transpose of a Matrix"
                                elif input == "add":
                                    title = "Answer: Addition of Matrices"
                                elif input == "subtract":
                                    title = "Answer: Subtraction of Matrices"
                                elif input == "multiply":
                                    title = "Answer: Multiplication of Matrices"
                                matrix_3_width = 300

                                matrix_3_height = 400

                                matrix_3_window = Toplevel()

                                matrix_3_window.geometry("{}x{}+{}+{}".format(matrix_3_width, matrix_3_height,

                                                                              int((

                                                                                          matrix_3_window.winfo_screenwidth() - matrix_3_width) / 2),

                                                                              int((

                                                                                          matrix_3_window.winfo_screenheight() - matrix_3_height) / 2)))

                                matrix_3_window.configure(bg="#ECF3FB")

                                matrix_3_window.resizable(0, 0)

                                matrix_3_window.wm_attributes("-topmost", 1)

                                matrix_3_window.focus_force()

                                matrix_3_window.wm_attributes("-topmost", 0)

                                matrix_3_window.title(title)
                                matrix_3_window.iconbitmap(os.path.join("data", "icon.ico"))

                                matrix_window.destroy()

                                canvas_matrix_3 = Canvas(matrix_3_window, width=matrix_3_width, bg="#ECF3FB",
                                                         height=matrix_3_height)

                                canvas_matrix_3.pack()
                                canvas_matrix_3.create_image(150, 200, image=image_mat_2)

                                canvas_matrix_3.create_text(150, 10, fill="black", text=title, justify=CENTER,
                                                            font=("Times", 9, "bold"))
                                if sel == "3_by_3":
                                    canvas_matrix_3.create_rectangle(20, 80, 22, 220, fill="black")
                                    canvas_matrix_3.create_rectangle(278, 80, 280, 220, fill="black")
                                    entry_1_1_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_a)
                                    canvas_matrix_3.create_window(60, 100, window=entry_1_1_3_by_3, width=60)
                                    entry_1_2_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_b)
                                    canvas_matrix_3.create_window(150, 100, window=entry_1_2_3_by_3, width=60)
                                    entry_1_3_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_c)
                                    canvas_matrix_3.create_window(240, 100, window=entry_1_3_3_by_3, width=60)
                                    entry_2_1_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_d)
                                    canvas_matrix_3.create_window(60, 140, window=entry_2_1_3_by_3, width=60)
                                    entry_2_2_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_e)
                                    canvas_matrix_3.create_window(150, 140, window=entry_2_2_3_by_3, width=60)
                                    entry_2_3_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_f)
                                    canvas_matrix_3.create_window(240, 140, window=entry_2_3_3_by_3, width=60)
                                    entry_3_1_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_g)
                                    canvas_matrix_3.create_window(60, 180, window=entry_3_1_3_by_3, width=60)
                                    entry_3_2_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_h)
                                    canvas_matrix_3.create_window(150, 180, window=entry_3_2_3_by_3, width=60)
                                    entry_3_3_3_by_3 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_i)
                                    canvas_matrix_3.create_window(240, 180, window=entry_3_3_3_by_3, width=60)
                                else:
                                    canvas_matrix_3.create_rectangle(50, 80, 52, 160, fill="black")
                                    canvas_matrix_3.create_rectangle(248, 80, 250, 160, fill="black")
                                    entry_1_1_2_by_2 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_a)
                                    canvas_matrix_3.create_window(90, 100, window=entry_1_1_2_by_2, width=60)
                                    entry_1_2_2_by_2 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_b)
                                    canvas_matrix_3.create_window(210, 100, window=entry_1_2_2_by_2, width=60)
                                    entry_2_1_2_by_2 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_c)
                                    canvas_matrix_3.create_window(90, 150, window=entry_2_1_2_by_2, width=60)
                                    entry_2_2_2_by_2 = Label(canvas_matrix_3, width=60, font=("Cambria", 7, "bold"),
                                                             justify=CENTER, text=ans_d)
                                    canvas_matrix_3.create_window(210, 150, window=entry_2_2_2_by_2, width=60)

                        if input == "add" or input == "subtract" or input == "multiply":
                            matrix_1_window.destroy()
                            matrix_1_1_width = 300

                            matrix_1_1_height = 400

                            matrix_1_1_window = Toplevel()

                            matrix_1_1_window.geometry("{}x{}+{}+{}".format(matrix_1_1_width, matrix_1_1_height,

                                                                            int((

                                                                                        matrix_1_1_window.winfo_screenwidth() - matrix_1_1_width) / 2),

                                                                            int((

                                                                                        matrix_1_1_window.winfo_screenheight() - matrix_1_1_height) / 2)))

                            matrix_1_1_window.configure(bg="#ECF3FB")

                            matrix_1_1_window.resizable(0, 0)

                            matrix_1_1_window.wm_attributes("-topmost", 1)

                            matrix_1_1_window.focus_force()

                            matrix_1_1_window.wm_attributes("-topmost", 0)

                            matrix_1_1_window.title(title.replace("1st", "2nd"))
                            matrix_1_1_window.iconbitmap(os.path.join("data", "icon.ico"))

                            matrix_window.destroy()

                            canvas_matrix_1_1 = Canvas(matrix_1_1_window, width=matrix_1_1_width, bg="#ECF3FB",
                                                       height=matrix_1_1_height)

                            canvas_matrix_1_1.pack()
                            canvas_matrix_1_1.create_image(150, 200, image=image_mat_2)

                            canvas_matrix_1_1.create_text(150, 10, fill="black",
                                                          text=title.replace("1st", "2nd") + ": Enter The Values",
                                                          justify=CENTER,
                                                          font=("Times", 9, "bold"))
                            canvas_matrix_1_1.create_rectangle(20, 80, 22, 220, fill="black")
                            canvas_matrix_1_1.create_rectangle(278, 80, 280, 220, fill="black")
                            entry_1_1_1_1_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                         justify=CENTER)
                            canvas_matrix_1_1.create_window(60, 100, window=entry_1_1_1_1_3_by_3, width=60)
                            entry_1_1_1_2_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                         justify=CENTER)
                            canvas_matrix_1_1.create_window(150, 100, window=entry_1_1_1_2_3_by_3, width=60)
                            entry_1_1_1_3_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                         justify=CENTER)
                            canvas_matrix_1_1.create_window(240, 100, window=entry_1_1_1_3_3_by_3, width=60)
                            entry_1_2_1_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(60, 140, window=entry_1_2_1_3_by_3, width=60)
                            entry_1_2_2_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(150, 140, window=entry_1_2_2_3_by_3, width=60)
                            entry_1_2_3_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(240, 140, window=entry_1_2_3_3_by_3, width=60)
                            entry_1_3_1_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(60, 180, window=entry_1_3_1_3_by_3, width=60)
                            entry_1_3_2_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(150, 180, window=entry_1_3_2_3_by_3, width=60)
                            entry_1_3_3_3_by_3 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(240, 180, window=entry_1_3_3_3_by_3, width=60)
                            canvas_matrix_1_1.create_rectangle(50, 300, 52, 380, fill="black")
                            canvas_matrix_1_1.create_rectangle(248, 300, 250, 380, fill="black")
                            entry_1_1_1_1_2_by_2 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                         justify=CENTER)
                            canvas_matrix_1_1.create_window(90, 320, window=entry_1_1_1_1_2_by_2, width=60)
                            entry_1_1_1_2_2_by_2 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                         justify=CENTER)
                            canvas_matrix_1_1.create_window(210, 320, window=entry_1_1_1_2_2_by_2, width=60)
                            entry_1_2_1_2_by_2 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(90, 360, window=entry_1_2_1_2_by_2, width=60)
                            entry_1_2_2_2_by_2 = Entry(canvas_matrix_1_1, width=60, font=("Cambria", 9, "bold"),
                                                       justify=CENTER)
                            canvas_matrix_1_1.create_window(210, 360, window=entry_1_2_2_2_by_2, width=60)
                            type_of_mat_1 = StringVar()
                            type_of_mat_1.set("2_by_2")
                            canvas_matrix_1_1.update()
                            canvas_matrix_1_1.update_idletasks()
                            canvas_matrix_1_1.create_window(150, 60, window=Radiobutton(canvas_matrix_1_1,
                                                                                        command=lambda: sel_1ect_1_r_but_type_1(
                                                                                            type_of_mat_1.get()),
                                                                                        value="3_by_3",
                                                                                        variable=type_of_mat_1,
                                                                                        text="3 by 3 Matrix",
                                                                                        font=(
                                                                                            "Segoe", 9, "bold"),
                                                                                        bg="#ECF3FB",
                                                                                        activebackground="#ECF3FB"))
                            canvas_matrix_1_1.create_window(150, 280, window=Radiobutton(canvas_matrix_1_1,
                                                                                         command=lambda: sel_1ect_1_r_but_type_1(
                                                                                             type_of_mat_1.get()),
                                                                                         value="2_by_2",
                                                                                         variable=type_of_mat_1,
                                                                                         text="2 by 2 Matrix",
                                                                                         font=(
                                                                                             "Segoe", 9, "bold"),
                                                                                         bg="#ECF3FB",
                                                                                         activebackground="#ECF3FB"))

                            def disable_3_by_3_1():
                                entry_1_1_1_1_3_by_3.configure(state=DISABLED)
                                entry_1_1_1_2_3_by_3.configure(state=DISABLED)
                                entry_1_1_1_3_3_by_3.configure(state=DISABLED)
                                entry_1_2_1_3_by_3.configure(state=DISABLED)
                                entry_1_2_2_3_by_3.configure(state=DISABLED)
                                entry_1_2_3_3_by_3.configure(state=DISABLED)
                                entry_1_3_1_3_by_3.configure(state=DISABLED)
                                entry_1_3_2_3_by_3.configure(state=DISABLED)
                                entry_1_3_3_3_by_3.configure(state=DISABLED)

                            def enable_3_by_3_1():
                                entry_1_1_1_1_3_by_3.configure(state=NORMAL)
                                entry_1_1_1_2_3_by_3.configure(state=NORMAL)
                                entry_1_1_1_3_3_by_3.configure(state=NORMAL)
                                entry_1_2_1_3_by_3.configure(state=NORMAL)
                                entry_1_2_2_3_by_3.configure(state=NORMAL)
                                entry_1_2_3_3_by_3.configure(state=NORMAL)
                                entry_1_3_1_3_by_3.configure(state=NORMAL)
                                entry_1_3_2_3_by_3.configure(state=NORMAL)
                                entry_1_3_3_3_by_3.configure(state=NORMAL)

                            def disable_2_by_2_1():
                                entry_1_1_1_1_2_by_2.configure(state=DISABLED)
                                entry_1_1_1_2_2_by_2.configure(state=DISABLED)
                                entry_1_2_1_2_by_2.configure(state=DISABLED)
                                entry_1_2_2_2_by_2.configure(state=DISABLED)

                            def enable_2_by_2_1():
                                entry_1_1_1_1_2_by_2.configure(state=NORMAL)
                                entry_1_1_1_2_2_by_2.configure(state=NORMAL)
                                entry_1_2_1_2_by_2.configure(state=NORMAL)
                                entry_1_2_2_2_by_2.configure(state=NORMAL)

                            def sel_1ect_1_r_but_type_1(sel_1ect_1):
                                if sel_1ect_1 == "2_by_2":
                                    disable_3_by_3_1()
                                    enable_2_by_2_1()
                                else:
                                    disable_2_by_2_1()
                                    enable_3_by_3_1()

                            def ret_ent_bind(evt):
                                continue_matrix_2_1(type_of_mat_1.get())

                            sel_1ect_1_r_but_type_1("2_by_2")

                            entry_1_1_1_1_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_1_1_2_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_1_1_3_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_2_1_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_2_2_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_2_3_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_3_1_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_3_2_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_3_3_3_by_3.bind("<Return>", ret_ent_bind)
                            entry_1_1_1_1_2_by_2.bind("<Return>", ret_ent_bind)
                            entry_1_1_1_2_2_by_2.bind("<Return>", ret_ent_bind)
                            entry_1_2_1_2_by_2.bind("<Return>", ret_ent_bind)
                            entry_1_2_2_2_by_2.bind("<Return>", ret_ent_bind)

                            def continue_matrix_2_1(sel_1):
                                if cwk_am.get() == sel_1:
                                    pass
                                else:
                                    messagebox.showerror("Error", "Matrices Do Not Match")
                                    matrix_1_1_window.wm_attributes("-topmost", 1)
                                    matrix_1_1_window.focus_force()
                                    matrix_1_1_window.wm_attributes("-topmost", 0)
                                    return
                                if sel_1 == "2_by_2":
                                    try:
                                        a_1 = float(eval(entry_1_1_1_1_2_by_2.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_1_1_1_2_by_2.focus_force()
                                        return
                                    try:
                                        b_1 = float(eval(entry_1_1_1_2_2_by_2.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_1_1_2_2_by_2.focus_force()
                                        return
                                    try:
                                        c_1 = float(eval(entry_1_2_1_2_by_2.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_2_1_2_by_2.focus_force()
                                        return
                                    try:
                                        d_1 = float(eval(entry_1_2_2_2_by_2.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_2_2_2_by_2.focus_force()
                                        return
                                else:
                                    try:
                                        a_1 = float(eval(entry_1_1_1_1_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_1_1_1_3_by_3.focus_force()
                                        return
                                    try:
                                        b_1 = float(eval(entry_1_1_1_2_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_1_1_2_3_by_3.focus_force()
                                        return
                                    try:
                                        c_1 = float(eval(entry_1_1_1_3_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_1_1_3_3_by_3.focus_force()
                                        return
                                    try:
                                        d_1 = float(eval(entry_1_2_1_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_2_1_3_by_3.focus_force()
                                        return
                                    try:
                                        e_1 = float(eval(entry_1_2_2_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_2_2_3_by_3.focus_force()
                                        return
                                    try:
                                        f_1 = float(eval(entry_1_2_3_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_2_3_3_by_3.focus_force()
                                        return
                                    try:
                                        g_1 = float(eval(entry_1_3_1_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_3_1_3_by_3.focus_force()
                                        return
                                    try:
                                        h_1 = float(eval(entry_1_3_2_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_3_2_3_by_3.focus_force()
                                        return
                                    try:
                                        i_1 = float(eval(entry_1_3_3_3_by_3.get()))
                                    except:
                                        messagebox.showerror("Error", "Value Error")
                                        matrix_1_1_window.wm_attributes("-topmost", 1)
                                        matrix_1_1_window.focus_force()
                                        matrix_1_1_window.wm_attributes("-topmost", 0)
                                        entry_1_3_3_3_by_3.focus_force()
                                        return
                                matrix_1_1_window.destroy()

                                if input == "add":
                                    if sel_1 == "2_by_2":
                                        continue_matrix_3(a + a_1, b + b_1, c + c_1, d + d_1, 0, 0, 0, 0, 0)
                                    else:
                                        continue_matrix_3(a + a_1, b + b_1, c + c_1, d + d_1, e + e_1, f + f_1, g + g_1,
                                                          h + h_1, i + i_1)
                                elif input == "subtract":
                                    if sel_1 == "2_by_2":
                                        continue_matrix_3(a - a_1, b - b_1, c - c_1, d - d_1, 0, 0, 0, 0, 0)
                                    else:
                                        continue_matrix_3(a - a_1, b - b_1, c - c_1, d - d_1, e - e_1, f - f_1, g - g_1,
                                                          h - h_1, i - i_1)
                                elif input == "multiply":
                                    if sel_1 == "3_by_3":
                                        a_f = (a * a_1) + (b * d_1) + (c * g_1)
                                        b_f = (a * b_1) + (b * e_1) + (c * h_1)
                                        c_f = (a * c_1) + (b * f_1) + (c * i_1)
                                        d_f = (d * a_1) + (e * d_1) + (f * g_1)
                                        e_f = (d * b_1) + (e * e_1) + (f * h_1)
                                        f_f = (d * c_1) + (e * f_1) + (f * i_1)
                                        g_f = (g * a_1) + (h * d_1) + (i * g_1)
                                        h_f = (g * b_1) + (h * e_1) + (i * h_1)
                                        i_f = (g * c_1) + (h * f_1) + (i * i_1)
                                        continue_matrix_3(a_f, b_f, c_f, d_f, e_f, f_f, g_f, h_f, i_f)
                                    else:
                                        a_f = (a * a_1) + (b * c_1)
                                        b_f = (a * b_1) + (b * d_1)
                                        c_f = (c * a_1) + (d * c_1)
                                        d_f = (c * b_1) + (d * d_1)
                                        continue_matrix_3(a_f, b_f, c_f, d_f, 0, 0, 0, 0, 0)

                        elif input == "inverse":
                            if sel == "2_by_2":
                                ans_a, ans_b, ans_c, ans_d = inverse(a, b, c, d, 0, 0, 0, 0, 0)
                                continue_matrix_3(ans_a, ans_b, ans_c, ans_d, 0, 0, 0, 0, 0)
                            else:
                                ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i = inverse(a, b, c, d, e,
                                                                                                        f, g, h, i)
                                continue_matrix_3(ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i)
                        elif input == "adjoint":
                            if sel == "2_by_2":
                                continue_matrix_3(0, 0, 0, 0, 0, 0, 0, 0, 0)
                            else:
                                ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i = adjoint(a, b, c, d, e,
                                                                                                        f, g, h, i)
                                continue_matrix_3(ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i)
                        elif input == "det":
                            if sel == "2_by_2":
                                ans = det(a, b, c, d, 0, 0, 0, 0, 0)
                                continue_matrix_3(ans, 0, 0, 0, 0, 0, 0, 0, 0)
                            else:
                                ans = det(a, b, c, d, e, f, g, h, i)
                                continue_matrix_3(ans, 0, 0, 0, 0, 0, 0, 0, 0)
                        elif input == "transpose":
                            if sel == "2_by_2":
                                ans_a, ans_b, ans_c, ans_d = transpose(a, b, c, d, 0, 0, 0, 0, 0)
                                continue_matrix_3(ans_a, ans_b, ans_c, ans_d, 0, 0, 0, 0, 0)
                            else:
                                ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i = transpose(a, b, c, d, e,
                                                                                                          f, g, h, i)
                                continue_matrix_3(ans_a, ans_b, ans_c, ans_d, ans_e, ans_f, ans_g, ans_h, ans_i)
                        elif input == "evalues":
                            if sel == "2_by_2":
                                ans = eigen_values(a, b, c, d, 0, 0, 0, 0, 0)
                                continue_matrix_3(ans, 0, 0, 0, 0, 0, 0, 0, 0)
                            else:
                                ans = eigen_values(a, b, c, d, e, f, g, h, i)
                                continue_matrix_3(ans, 0, 0, 0, 0, 0, 0, 0, 0)


            elif input == "constant":
                constant_width = 600
                constant_height = 400
                constant_window = Toplevel()
                constant_window.geometry("{}x{}+{}+{}".format(constant_width, constant_height,
                                                              int((
                                                                          constant_window.winfo_screenwidth() - constant_width) / 2),
                                                              int((
                                                                          constant_window.winfo_screenheight() - constant_height) / 2)))
                constant_window.configure(bg="#ECF3FB")
                constant_window.resizable(0, 0)
                constant_window.wm_attributes("-topmost", 1)
                constant_window.focus_force()
                constant_window.wm_attributes("-topmost", 0)
                constant_window.title("Constants")
                constant_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_constant = Canvas(constant_window, width=constant_width, bg="#ECF3FB", height=constant_height)
                canvas_constant.pack()
                global image_constants_main
                canvas_constant.create_image(300, 200, image=image_constants_main)
                canvas_constant.create_text(300, 10, fill="black", text="Constants",
                                            font=("Segoe", 12, "bold"))
                button_y_coord = 40
                button_x_coord = 150
                canvas_constant.create_window(150, 40,
                                              window=Button(canvas_constant, bg="Black", fg="White",
                                                            text="Periodic Table",
                                                            font=("Segoe", 9, "bold"),
                                                            command=lambda: continue_constant("periodic")), width=100,
                                              height=20)
                start_var = 0
                height_y = 80
                radio_var = IntVar()
                radio_var.set(0)
                for data in constants_label[0:9]:
                    canvas_constant.create_window(150, height_y,
                                                  window=Radiobutton(canvas_constant, justify=LEFT, anchor=W,
                                                                     bg="Black", fg="White",
                                                                     text=data,
                                                                     font=("Segoe", 9, "bold"), variable=radio_var,
                                                                     value=start_var,
                                                                     command=lambda: continue_constant(
                                                                         radio_var.get())),
                                                  width=280,
                                                  height=20)

                    start_var += 1
                    height_y += 30
                start_var = 9
                height_y = 80
                for data in constants_label[9:]:
                    canvas_constant.create_window(450, height_y,
                                                  window=Radiobutton(canvas_constant, justify=LEFT, anchor=W,
                                                                     bg="Black", fg="White",
                                                                     text=data,
                                                                     font=("Segoe", 9, "bold"), variable=radio_var,
                                                                     value=start_var,
                                                                     command=lambda: continue_constant(
                                                                         radio_var.get())),
                                                  width=280,
                                                  height=20)

                    start_var += 1
                    height_y += 30
                root.update()
                root.update_idletasks()
                canvas_constant.update()
                canvas_constant.update_idletasks()

                def continue_constant(input):
                    if input == "periodic":
                        constant_2_width = 1000
                        constant_2_height = 550
                        constant_2_window = Toplevel()
                        constant_2_window.geometry("{}x{}+{}+{}".format(constant_2_width, constant_2_height,
                                                                        int((
                                                                                    constant_2_window.winfo_screenwidth() - constant_2_width) / 2),
                                                                        int((
                                                                                    constant_2_window.winfo_screenheight() - constant_2_height) / 2)))
                        constant_2_window.configure(bg="#ECF3FB")
                        constant_2_window.resizable(0, 0)
                        constant_2_window.wm_attributes("-topmost", 1)
                        constant_2_window.focus_force()
                        constant_2_window.wm_attributes("-topmost", 0)
                        constant_2_window.title("Elements")
                        constant_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_constant_2 = Canvas(constant_2_window, width=constant_2_width, bg="#ECF3FB",
                                                   height=constant_2_height)
                        canvas_constant_2.pack()
                        global image_constants_periodic
                        canvas_constant_2.create_image(500, 275, image=image_constants_periodic)
                        canvas_constant_2.create_text(512, 10, fill="black", text="Elements",
                                                      font=("Segoe", 12, "bold"))
                        start_var = 0
                        height_y = 40
                        radio_2_var = IntVar()
                        for data in list_element[0:25]:
                            elements_name = data[0:data.find("symbol")]
                            canvas_constant_2.create_window(100, height_y,
                                                            window=Radiobutton(canvas_constant_2, justify=LEFT,
                                                                               anchor=W, bg="Black", fg="White",
                                                                               text=elements_name,
                                                                               font=("Lucida", 7, "bold"),
                                                                               variable=radio_var, value=start_var,
                                                                               command=lambda: continue_constant_2(
                                                                                   radio_var.get())),
                                                            width=180,
                                                            height=15)

                            start_var += 1
                            height_y += 20
                            canvas_constant_2.update()
                            canvas_constant_2.update_idletasks()
                            root.update()
                            root.update_idletasks()
                        start_var = 25
                        height_y = 40
                        for data in list_element[25:50]:
                            elements_name = data[0:data.find("symbol")]
                            canvas_constant_2.create_window(300, height_y,
                                                            window=Radiobutton(canvas_constant_2, justify=LEFT,
                                                                               anchor=W, bg="Black", fg="White",
                                                                               text=elements_name,
                                                                               font=("Lucida", 7, "bold"),
                                                                               variable=radio_var, value=start_var,
                                                                               command=lambda: continue_constant_2(
                                                                                   radio_var.get())),
                                                            width=180,
                                                            height=15)

                            start_var += 1
                            height_y += 20
                            canvas_constant_2.update()
                            canvas_constant_2.update_idletasks()
                            root.update()
                            root.update_idletasks()
                        start_var = 50
                        height_y = 40
                        for data in list_element[50:75]:
                            elements_name = data[0:data.find("symbol")]
                            canvas_constant_2.create_window(500, height_y,
                                                            window=Radiobutton(canvas_constant_2, justify=LEFT,
                                                                               anchor=W, bg="Black", fg="White",
                                                                               text=elements_name,
                                                                               font=("Lucida", 7, "bold"),
                                                                               variable=radio_var, value=start_var,
                                                                               command=lambda: continue_constant_2(
                                                                                   radio_var.get())),
                                                            width=180,
                                                            height=15)

                            start_var += 1
                            height_y += 20
                            canvas_constant_2.update()
                            canvas_constant_2.update_idletasks()
                            root.update()
                            root.update_idletasks()
                        start_var = 75
                        height_y = 40
                        for data in list_element[75:100]:
                            elements_name = data[0:data.find("symbol")]
                            canvas_constant_2.create_window(700, height_y,
                                                            window=Radiobutton(canvas_constant_2, justify=LEFT,
                                                                               anchor=W, bg="Black", fg="White",
                                                                               text=elements_name,
                                                                               font=("Lucida", 7, "bold"),
                                                                               variable=radio_var, value=start_var,
                                                                               command=lambda: continue_constant_2(
                                                                                   radio_var.get())),
                                                            width=180,
                                                            height=15)

                            start_var += 1
                            height_y += 20
                            canvas_constant_2.update()
                            canvas_constant_2.update_idletasks()
                            root.update()
                            root.update_idletasks()
                        start_var = 100
                        height_y = 40
                        for data in list_element[100:]:
                            elements_name = data[0:data.find("symbol")]
                            canvas_constant_2.create_window(900, height_y,
                                                            window=Radiobutton(canvas_constant_2, justify=LEFT,
                                                                               anchor=W, bg="Black", fg="White",
                                                                               text=elements_name,
                                                                               font=("Lucida", 7, "bold"),
                                                                               variable=radio_var, value=start_var,
                                                                               command=lambda: continue_constant_2(
                                                                                   radio_var.get())),
                                                            width=180,
                                                            height=15)

                            start_var += 1
                            height_y += 20
                            canvas_constant_2.update()
                            canvas_constant_2.update_idletasks()
                            root.update()
                            root.update_idletasks()

                        constant_window.destroy()

                        def continue_constant_2(input):
                            working_line = list_element[input]
                            element_name = working_line[0:working_line.find("symbol")]
                            constant_3_width = 300
                            constant_3_height = 280
                            constant_3_window = Toplevel()
                            constant_3_window.geometry("{}x{}+{}+{}".format(constant_3_width, constant_3_height,
                                                                            int((
                                                                                        constant_3_window.winfo_screenwidth() - constant_3_width) / 2),
                                                                            int((
                                                                                        constant_3_window.winfo_screenheight() - constant_3_height) / 2)))
                            constant_3_window.configure(bg="#ECF3FB")
                            constant_3_window.resizable(0, 0)
                            constant_3_window.wm_attributes("-topmost", 1)
                            constant_3_window.focus_force()
                            constant_3_window.wm_attributes("-topmost", 0)
                            constant_3_window.title(element_name)
                            constant_3_window.iconbitmap(os.path.join("data", "icon.ico"))
                            canvas_constant_3 = Canvas(constant_3_window, width=constant_3_width, bg="#ECF3FB",
                                                       height=constant_3_height)
                            canvas_constant_3.pack()
                            global image_constants_element
                            canvas_constant_3.create_image(150, 140, image=image_constants_element)
                            canvas_constant_3.create_text(150, 10, fill="black", text=element_name,
                                                          font=("Segoe", 12, "bold"))

                            canvas_constant_3.create_window(150, 40,
                                                            window=Button(canvas_constant_3, justify=CENTER,
                                                                          anchor=CENTER, bg="Black", fg="White",
                                                                          text="Atomic Number",
                                                                          font=("Segoe", 10, "bold"),
                                                                          command=lambda: continue_constant_3("AN",
                                                                                                              element_name,
                                                                                                              input)),
                                                            width=200,
                                                            height=20)

                            canvas_constant_3.create_window(150, 80,
                                                            window=Button(canvas_constant_3, justify=CENTER,
                                                                          anchor=CENTER, bg="Black", fg="White",
                                                                          text="Relative Molecular Mass",
                                                                          font=("Segoe", 10, "bold"),
                                                                          command=lambda: continue_constant_3("RMM",
                                                                                                              element_name,
                                                                                                              input)),
                                                            width=200,
                                                            height=20)

                            canvas_constant_3.create_window(150, 120,
                                                            window=Button(canvas_constant_3, justify=CENTER,
                                                                          anchor=CENTER, bg="Black", fg="White",
                                                                          text="Melting Point",
                                                                          font=("Segoe", 10, "bold"),
                                                                          command=lambda: continue_constant_3("MP",
                                                                                                              element_name,
                                                                                                              input)),
                                                            width=200,
                                                            height=20)

                            canvas_constant_3.create_window(150, 160,
                                                            window=Button(canvas_constant_3, justify=CENTER,
                                                                          anchor=CENTER, bg="Black", fg="White",
                                                                          text="Boiling Point",
                                                                          font=("Segoe", 10, "bold"),
                                                                          command=lambda: continue_constant_3("BP",
                                                                                                              element_name,
                                                                                                              input)),
                                                            width=200,
                                                            height=20)

                            canvas_constant_3.create_window(150, 200,
                                                            window=Button(canvas_constant_3, justify=CENTER,
                                                                          anchor=CENTER, bg="Black", fg="White",
                                                                          text="Electronegativity",
                                                                          font=("Segoe", 10, "bold"),
                                                                          command=lambda: continue_constant_3("EN",
                                                                                                              element_name,
                                                                                                              input)),
                                                            width=200,
                                                            height=20)

                            canvas_constant_3.create_window(150, 240,
                                                            window=Button(canvas_constant_3, justify=CENTER,
                                                                          anchor=CENTER, bg="Black", fg="White",
                                                                          text="Possible Charges",
                                                                          font=("Segoe", 10, "bold"),
                                                                          command=lambda: continue_constant_3("PC",
                                                                                                              element_name,
                                                                                                              input)),
                                                            width=200,
                                                            height=20)

                            def continue_constant_3(input, name, line_no):
                                print(input, name)
                                if input == "AN":
                                    line = list_element[line_no]
                                    atomic_no = line[line.find("atomic_no") + 10:line.find("molecular_mass")].replace(
                                        " ", "")
                                    pow_solve = "(Atomic No: " + atomic_no + ")"
                                elif input == "RMM":
                                    line = list_element[line_no]
                                    molecular_mass = line[line.find("molecular_mass") + 15:line.find(
                                        "melting_point")].replace(" ", "")
                                    if "(" in molecular_mass:
                                        molecular_mass = molecular_mass[0:molecular_mass.find("(")]
                                    pow_solve = "(" + molecular_mass + ")"
                                elif input == "MP":
                                    line = list_element[line_no]
                                    melting_point = line[
                                                    line.find("melting_point") + 14:line.find("boiling_point")].replace(
                                        " ", "")
                                    if "Unknown" not in melting_point:
                                        pow_solve = "(Melting Point: " + melting_point + chr(0x00B0) + "C)"
                                    else:
                                        pow_solve = melting_point
                                elif input == "BP":
                                    line = list_element[line_no]
                                    boiling_point = line[line.find("boiling_point") + 14:].replace(" ", "")
                                    if "Unknown" not in boiling_point:
                                        pow_solve = "(Boiling Point: " + boiling_point + chr(0x00B0) + "C)"
                                    else:
                                        pow_solve = boiling_point
                                elif input == "EN":
                                    line_no = 0
                                    line = ""
                                    for data in electronegativity_data:
                                        if name.lower() in data.lower():
                                            line = electronegativity_data[line_no]
                                            break
                                        line_no += 1
                                    if line != "":
                                        electronegativity = line[line.lower().find(name.lower()) + len(name):].replace(
                                            " ", "")
                                        if "no" in electronegativity.lower():
                                            pow_solve = "Unknown"
                                        else:
                                            pow_solve = "(" + electronegativity + ")"
                                    else:
                                        pow_solve = "Unknown"
                                elif input == "PC":
                                    line_no = 0
                                    line = ""
                                    for data in charges_data:
                                        if name.lower() in data.lower():
                                            line = charges_data[line_no]
                                            break
                                        line_no += 1
                                    if line != "":
                                        charges = line[line.lower().find(name.lower()) + len(name):].replace(" ", "")
                                        pow_solve = "(Possible Charges: " + charges + ")"
                                    else:
                                        pow_solve = "Unknown"
                                if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                    label_display_1_var.set(str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                    label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                    label_display_1_var.set(str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                    label_display_2_var.set("")
                                elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                    label_display_1_var.set(str(pow_solve))
                                    label_display_2_var.set("")
                                    old_label_display_1_var.set(label_display_1_var)
                                update_label_1()
                                constant_3_window.destroy()
                                constant_2_window.destroy()
                                root.wm_attributes("-topmost", 1)
                                root.focus_force()
                                root.wm_attributes("-topmost", 0)


                    else:
                        pow_solve = "(" + str(eval(constants[input])) + ")"
                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                            label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                            label_display_2_var.set("")
                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                            old_label_display_1_var.set(label_display_1_var)
                        update_label_1()
                        constant_window.destroy()
                        root.wm_attributes("-topmost", 1)
                        root.focus_force()
                        root.wm_attributes("-topmost", 0)


            elif input == "vector":
                vector_width = 300
                vector_height = 280
                vector_window = Toplevel()
                vector_window.geometry("{}x{}+{}+{}".format(vector_width, vector_height,
                                                            int((vector_window.winfo_screenwidth() - vector_width) / 2),
                                                            int((
                                                                        vector_window.winfo_screenheight() - vector_height) / 2)))
                vector_window.configure(bg="#ECF3FB")
                vector_window.resizable(0, 0)
                vector_window.wm_attributes("-topmost", 1)
                vector_window.focus_force()
                vector_window.wm_attributes("-topmost", 0)
                vector_window.title("Vector")
                vector_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_vector = Canvas(vector_window, width=vector_width, bg="#ECF3FB", height=vector_height)
                canvas_vector.pack()
                global image_vec_main
                canvas_vector.create_image(150, 140, image=image_vec_main)
                canvas_vector.create_text(150, 10, text="Select Operation", fill="black", justify=CENTER,
                                          font=("Times", 9, "bold"))
                canvas_vector.create_window(150, 40, window=Button(canvas_vector, text="Scalar/Dot Product",
                                                                   command=lambda: continue_vector_1("dot"), bg="Black",
                                                                   fg="White", font=("Segoe", 9, "bold")),
                                            width=200)
                canvas_vector.create_window(150, 80, window=Button(canvas_vector, text="Vector/Cross Product",
                                                                   command=lambda: continue_vector_1("vector"),
                                                                   bg="Black",
                                                                   fg="White", font=("Segoe", 9, "bold")),
                                            width=200)
                canvas_vector.create_window(150, 120, window=Button(canvas_vector, text="Magnitude/Modulus",
                                                                    command=lambda: continue_vector_1("modulus"),
                                                                    bg="Black",
                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)
                canvas_vector.create_window(150, 160, window=Button(canvas_vector, text="Angle Between Two Vectors",
                                                                    command=lambda: continue_vector_1("angle"),
                                                                    bg="Black",
                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)
                canvas_vector.create_window(150, 200, window=Button(canvas_vector, text="Arithmetic Operations",
                                                                    command=lambda: continue_vector_1("arithmetic"),
                                                                    bg="Black",
                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)
                canvas_vector.create_window(150, 240, window=Button(canvas_vector, text="Unit Vector",
                                                                    command=lambda: continue_vector_1("unit"),
                                                                    bg="Black",
                                                                    fg="White", font=("Segoe", 9, "bold")),
                                            width=200)

                def continue_vector_1(input):
                    if input == "dot":
                        title = "Scalar Product"
                    elif input == "vector":
                        title = "Vector Product"
                    elif input == "unit":
                        title = "Unit Vector"
                    elif input == "modulus":
                        title = "Modulus of a Vector"
                    elif input == "arithmetic":
                        title = "Arithmetic Operations"
                    elif input == "angle":
                        title = "Angle Between two Vectors"
                    if input == "arithmetic":
                        vector_1_width = 300
                        vector_1_height = 400
                        global image_vec_arith
                        image_bg = image_vec_arith
                    else:
                        vector_1_width = 300
                        vector_1_height = 300
                        global image_vec_2
                        image_bg = image_vec_2
                    vector_1_window = Toplevel()
                    vector_1_window.geometry("{}x{}+{}+{}".format(vector_1_width, vector_1_height,
                                                                  int((
                                                                              vector_1_window.winfo_screenwidth() - vector_1_width) / 2),
                                                                  int((
                                                                              vector_1_window.winfo_screenheight() - vector_1_height) / 2)))
                    vector_1_window.configure(bg="#ECF3FB")
                    vector_1_window.resizable(0, 0)
                    vector_1_window.wm_attributes("-topmost", 1)
                    vector_1_window.focus_force()
                    vector_1_window.wm_attributes("-topmost", 0)
                    vector_1_window.title(title)
                    vector_1_window.iconbitmap(os.path.join("data", "icon.ico"))
                    vector_window.destroy()
                    canvas_vector_1 = Canvas(vector_1_window, width=vector_1_width, bg="#ECF3FB",
                                             height=vector_1_height)
                    canvas_vector_1.pack()
                    canvas_vector_1.create_image(vector_1_width / 2, vector_1_height / 2, image=image_bg)
                    canvas_vector_1.create_text(150, 10, fill="black", text=title + ": Enter The Values",
                                                justify=CENTER, font=("Times", 9, "bold"))
                    type_of_vec_var = StringVar()
                    type_of_vec_var.set("plane")
                    canvas_vector_1.create_window(150, 40,
                                                  window=Radiobutton(canvas_vector_1, font=("Segoe", 9, "bold"),
                                                                     text="Vector in Plane(2 Dimensional Vector)",
                                                                     bg="#ECF3FB", activebackground="#ECF3FB",
                                                                     fg="Black", activeforeground="Black",
                                                                     value="plane", variable=type_of_vec_var,
                                                                     command=lambda: selct_type_of_vec(
                                                                         type_of_vec_var)))
                    canvas_vector_1.create_window(43, 80, window=Label(canvas_vector_1, bg="black", fg="white",
                                                                       text="1st Vector",
                                                                       font=("Segoe", 9, "bold"), justify=CENTER,
                                                                       anchor=CENTER), width=80)
                    canvas_vector_1.create_window(125 + 25, 80,
                                                  window=Label(canvas_vector_1, text="i", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    canvas_vector_1.create_window(195 + 25, 80,
                                                  window=Label(canvas_vector_1, text="j", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    entry_i_plane_1st = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(125 - 5, 80, window=entry_i_plane_1st, width=40)
                    entry_j_plane_1st = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(195 - 5, 80, window=entry_j_plane_1st, width=40)
                    canvas_vector_1.create_window(43, 120, window=Label(canvas_vector_1, bg="black", fg="white",
                                                                        text="2nd Vector",
                                                                        font=("Segoe", 9, "bold"),
                                                                        justify=CENTER, anchor=CENTER), width=80)
                    canvas_vector_1.create_window(125 + 25, 120,
                                                  window=Label(canvas_vector_1, text="i", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    canvas_vector_1.create_window(195 + 25, 120,
                                                  window=Label(canvas_vector_1, text="j", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    entry_i_plane_2nd = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(125 - 5, 120, window=entry_i_plane_2nd, width=40)
                    entry_j_plane_2nd = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(195 - 5, 120, window=entry_j_plane_2nd, width=40)
                    canvas_vector_1.create_window(43, 220, window=Label(canvas_vector_1, bg="black", fg="white",
                                                                        text="1st Vector",
                                                                        font=("Segoe", 9, "bold"),
                                                                        justify=CENTER, anchor=CENTER), width=80)
                    canvas_vector_1.create_window(125 + 25, 220,
                                                  window=Label(canvas_vector_1, text="i", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    canvas_vector_1.create_window(195 + 25, 220,
                                                  window=Label(canvas_vector_1, text="j", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    canvas_vector_1.create_window(265 + 25, 220,
                                                  window=Label(canvas_vector_1, text="k", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    entry_i_space_1st = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(125 - 5, 220, window=entry_i_space_1st, width=40)
                    entry_j_space_1st = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(195 - 5, 220, window=entry_j_space_1st, width=40)
                    entry_k_space_1st = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(265 - 5, 220, window=entry_k_space_1st, width=40)
                    canvas_vector_1.create_window(43, 260, window=Label(canvas_vector_1, bg="black", fg="white",
                                                                        text="2nd Vector",
                                                                        font=("Segoe", 9, "bold"),
                                                                        justify=CENTER, anchor=CENTER), width=80)
                    canvas_vector_1.create_window(125 + 25, 260,
                                                  window=Label(canvas_vector_1, text="i", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    canvas_vector_1.create_window(195 + 25, 260,
                                                  window=Label(canvas_vector_1, text="j", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    canvas_vector_1.create_window(265 + 25, 260,
                                                  window=Label(canvas_vector_1, text="k", bg="black", fg="white",
                                                               font=("Segoe", 9, "bold"), justify=CENTER,
                                                               anchor=CENTER), width=20)
                    entry_i_space_2nd = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(125 - 5, 260, window=entry_i_space_2nd, width=40)
                    entry_j_space_2nd = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(195 - 5, 260, window=entry_j_space_2nd, width=40)
                    entry_k_space_2nd = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                    canvas_vector_1.create_window(265 - 5, 260, window=entry_k_space_2nd, width=40)
                    canvas_vector_1.create_window(150, 180,
                                                  window=Radiobutton(canvas_vector_1, font=("Segoe", 9, "bold"),
                                                                     text="Vector in Space(3 Dimensional Vector)",
                                                                     bg="#ECF3FB", activebackground="#ECF3FB",
                                                                     fg="Black", activeforeground="Black",
                                                                     value="space", variable=type_of_vec_var,
                                                                     command=lambda: selct_type_of_vec(
                                                                         type_of_vec_var)))
                    if input == "arithmetic":
                        canvas_vector_1.create_window(150, 320,
                                                      window=Label(canvas_vector_1, font=("Segoe", 9, "bold"),
                                                                   text="Operator", fg="Black", bg="#ECF3FB",
                                                                   justify=CENTER))

                        canvas_vector_1.create_window(105, 360, window=Label(canvas_vector_1, bg="black", fg="white",
                                                                             text="Operation(+, -)",
                                                                             font=("Segoe", 9, "bold"),
                                                                             justify=CENTER, anchor=CENTER), width=200)
                        entry_operator = Entry(canvas_vector_1, font=("Cambria", 9, "bold"), justify=CENTER)
                        canvas_vector_1.create_window(230, 360, window=entry_operator, width=40)

                    def disable_vec_in_plane():
                        entry_i_plane_1st.configure(state=DISABLED)
                        entry_j_plane_1st.configure(state=DISABLED)
                        entry_i_plane_2nd.configure(state=DISABLED)
                        entry_j_plane_2nd.configure(state=DISABLED)
                        root.update()
                        root.update_idletasks()
                        canvas_vector_1.update()
                        canvas_vector_1.update_idletasks()

                    def enable_vec_in_plane():
                        entry_i_plane_1st.configure(state=NORMAL)
                        entry_j_plane_1st.configure(state=NORMAL)
                        if input == "modulus" or input == "unit":
                            entry_i_plane_2nd.configure(state=DISABLED)
                            entry_j_plane_2nd.configure(state=DISABLED)
                        else:
                            entry_i_plane_2nd.configure(state=NORMAL)
                            entry_j_plane_2nd.configure(state=NORMAL)
                        root.update()
                        root.update_idletasks()
                        canvas_vector_1.update()
                        canvas_vector_1.update_idletasks()

                    def disable_vec_in_space():
                        entry_i_space_1st.configure(state=DISABLED)
                        entry_j_space_1st.configure(state=DISABLED)
                        entry_k_space_1st.configure(state=DISABLED)
                        entry_i_space_2nd.configure(state=DISABLED)
                        entry_j_space_2nd.configure(state=DISABLED)
                        entry_k_space_2nd.configure(state=DISABLED)
                        root.update()
                        root.update_idletasks()
                        canvas_vector_1.update()
                        canvas_vector_1.update_idletasks()

                    def enable_vec_in_space():
                        entry_i_space_1st.configure(state=NORMAL)
                        entry_j_space_1st.configure(state=NORMAL)
                        entry_k_space_1st.configure(state=NORMAL)
                        if input == "modulus" or input == "unit":
                            entry_i_space_2nd.configure(state=DISABLED)
                            entry_j_space_2nd.configure(state=DISABLED)
                            entry_k_space_2nd.configure(state=DISABLED)
                        else:
                            entry_i_space_2nd.configure(state=NORMAL)
                            entry_j_space_2nd.configure(state=NORMAL)
                            entry_k_space_2nd.configure(state=NORMAL)
                        root.update()
                        root.update_idletasks()
                        canvas_vector_1.update()
                        canvas_vector_1.update_idletasks()

                    # bind
                    def vector_bind(event):
                        continue_vector_2(type_of_vec_var.get())

                    entry_i_plane_1st.bind("<Return>", vector_bind)
                    entry_j_plane_1st.bind("<Return>", vector_bind)
                    entry_i_plane_2nd.bind("<Return>", vector_bind)
                    entry_j_plane_2nd.bind("<Return>", vector_bind)
                    entry_i_space_1st.bind("<Return>", vector_bind)
                    entry_j_space_1st.bind("<Return>", vector_bind)
                    entry_k_space_1st.bind("<Return>", vector_bind)
                    entry_i_space_2nd.bind("<Return>", vector_bind)
                    entry_j_space_2nd.bind("<Return>", vector_bind)
                    entry_k_space_2nd.bind("<Return>", vector_bind)
                    if input == "arithmetic":
                        entry_operator.bind("<Return>", vector_bind)

                    def selct_type_of_vec(input):
                        if input.get() == "plane":
                            disable_vec_in_space()
                            enable_vec_in_plane()
                        elif input.get() == "space":
                            disable_vec_in_plane()
                            enable_vec_in_space()

                    disable_vec_in_space()
                    enable_vec_in_plane()

                    def continue_vector_2(input_2):
                        if input_2 == "plane":
                            try:
                                a = float(eval(entry_i_plane_1st.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                vector_1_window.wm_attributes("-topmost", 1)
                                entry_i_plane_1st.focus_force()
                                vector_1_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_j_plane_1st.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                vector_1_window.wm_attributes("-topmost", 1)
                                entry_j_plane_1st.focus_force()
                                vector_1_window.wm_attributes("-topmost", 0)
                                return
                            if input == "modulus" or input == "unit":
                                pass
                            else:
                                try:
                                    c = float(eval(entry_i_plane_2nd.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    vector_1_window.wm_attributes("-topmost", 1)
                                    entry_i_plane_2nd.focus_force()
                                    vector_1_window.wm_attributes("-topmost", 0)
                                    return
                                try:
                                    d = float(eval(entry_j_plane_2nd.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    vector_1_window.wm_attributes("-topmost", 1)
                                    entry_j_plane_2nd.focus_force()
                                    vector_1_window.wm_attributes("-topmost", 0)
                                    return
                        elif input_2 == "space":
                            ent_count = 1
                            try:
                                a = float(eval(entry_i_space_1st.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                vector_1_window.wm_attributes("-topmost", 1)
                                entry_i_space_1st.focus_force()
                                vector_1_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_j_space_1st.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                vector_1_window.wm_attributes("-topmost", 1)
                                entry_j_space_1st.focus_force()
                                vector_1_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                c = float(eval(entry_k_space_1st.get()))
                            except:
                                messagebox.showerror("Error", "Value Error")
                                vector_1_window.wm_attributes("-topmost", 1)
                                entry_k_space_1st.focus_force()
                                vector_1_window.wm_attributes("-topmost", 0)
                                return
                            if input == "modulus" or input == "unit":
                                pass
                            else:
                                try:
                                    d = float(eval(entry_i_space_2nd.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    vector_1_window.wm_attributes("-topmost", 1)
                                    entry_i_space_2nd.focus_force()
                                    vector_1_window.wm_attributes("-topmost", 0)
                                    return
                                try:
                                    e = float(eval(entry_j_space_2nd.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    vector_1_window.wm_attributes("-topmost", 1)
                                    entry_j_space_2nd.focus_force()
                                    vector_1_window.wm_attributes("-topmost", 0)
                                    return
                                try:
                                    f = float(eval(entry_k_space_2nd.get()))
                                except:
                                    messagebox.showerror("Error", "Value Error")
                                    vector_1_window.wm_attributes("-topmost", 1)
                                    entry_k_space_2nd.focus_force()
                                    vector_1_window.wm_attributes("-topmost", 0)
                                    return
                        if input == "arithmetic":
                            operator = entry_operator.get()
                            if operator not in ["+", "-"]:
                                messagebox.showerror("Error", "Operator Error")
                                vector_1_window.wm_attributes("-topmost", 1)
                                entry_operator.focus_force()
                                vector_1_window.wm_attributes("-topmost", 0)
                                return
                            if input_2 == "plane":
                                answer_i = round(eval(str(a) + operator + str(c)), approximate_val.get())
                                answer_j = round(eval(str(b) + operator + str(d)), approximate_val.get())
                                if answer_j < 0:
                                    answer = str(answer_i) + "i " + " - " + str(answer_j * (-1)) + "j"
                                else:
                                    answer = str(answer_i) + "i " + " + " + str(answer_j) + "j"
                            elif input_2 == "space":
                                answer_i = round(eval(str(a) + operator + str(d)), approximate_val.get())
                                answer_j = round(eval(str(b) + operator + str(e)), approximate_val.get())
                                answer_k = round(eval(str(c) + operator + str(f)), approximate_val.get())
                                if answer_j < 0:
                                    answer = str(answer_i) + "i " + " - " + str(answer_j * (-1)) + "j"
                                else:
                                    answer = str(answer_i) + "i " + " + " + str(answer_j) + "j"
                                if answer_k < 0:
                                    answer = str(answer) + " - " + str(answer_k * (-1)) + "k"
                                else:
                                    answer = str(answer) + " + " + str(answer_k) + "k"
                            pow_solve = answer
                        elif input == "modulus":
                            if input_2 == "plane":
                                answer = round(pow(round(pow(a, 2) + pow(b, 2), approximate_val.get()), 0.5),
                                               approximate_val.get())
                            elif input_2 == "space":
                                answer = round(
                                    pow(round(pow(a, 2) + pow(b, 2) + pow(c, 2), approximate_val.get()), 0.5),
                                    approximate_val.get())
                            pow_solve = str(answer)
                        elif input == "unit":
                            if input_2 == "plane":
                                answer = round(pow(round(pow(a, 2) + pow(b, 2), approximate_val.get()), 0.5),
                                               approximate_val.get())
                                rn = approximate_val.get()
                                numerator = str(round(a, rn)) + "i"
                                if b < 0:
                                    numerator = numerator + " - " + str(round(b * (-1), rn)) + "j"
                                else:
                                    numerator = numerator + " + " + str(round(b, rn)) + "j"
                                pow_solve = "(" + numerator + ")" + "/" + str(answer)
                            elif input_2 == "space":
                                answer = round(
                                    pow(round(pow(a, 2) + pow(b, 2) + pow(c, 2), approximate_val.get()), 0.5),
                                    approximate_val.get())
                                rn = approximate_val.get()
                                numerator = str(round(a, rn)) + "i"
                                if b < 0:
                                    numerator = numerator + " - " + str(round(b * (-1), rn)) + "j"
                                else:
                                    numerator = numerator + " + " + str(round(b, rn)) + "j"
                                if c < 0:
                                    numerator = numerator + " - " + str(round(c * (-1), rn)) + "k"
                                else:
                                    numerator = numerator + " + " + str(round(c, rn)) + "k"
                                pow_solve = "(" + numerator + ")" + "/" + str(answer)

                        elif input == "dot":
                            if input_2 == "plane":
                                answer = (a * c) + (b * d)
                            elif input_2 == "space":
                                answer = (a * d) + (b * e) + (c * f)
                            pow_solve = str(answer)
                        elif input == "vector":
                            if input_2 == "plane":
                                pow_solve = "Error"
                            elif input_2 == "space":
                                answer = vector_product_calc(a, b, c, d, e, f)
                                pow_solve = answer
                        elif input == "angle":
                            if input_2 == "plane":
                                mag_1st = round(pow(round(pow(a, 2) + pow(b, 2), approximate_val.get()), 0.5),
                                                approximate_val.get())
                                mag_2nd = round(pow(round(pow(c, 2) + pow(d, 2), approximate_val.get()), 0.5),
                                                approximate_val.get())
                            elif input_2 == "space":
                                mag_1st = round(
                                    pow(round(pow(a, 2) + pow(b, 2) + pow(c, 2), approximate_val.get()), 0.5),
                                    approximate_val.get())
                                mag_2nd = round(
                                    pow(round(pow(d, 2) + pow(e, 2) + pow(f, 2), approximate_val.get()), 0.5),
                                    approximate_val.get())
                            if input_2 == "plane":
                                dot_prod = (a * c) + (b * d)
                            elif input_2 == "space":
                                dot_prod = (a * d) + (b * e) + (c * f)
                            cos_ang = dot_prod / (mag_1st * mag_2nd)
                            ang = (round((acos(cos_ang) / pi) * 180, approximate_val.get()))
                            pow_solve = str(ang) + chr(0x00B0)

                        if pow_solve != "Error":
                            pow_solve = "(" + pow_solve + ")"
                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                            label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                            label_display_2_var.set("")
                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                            old_label_display_1_var.set(label_display_1_var)
                        update_label_1()
                        vector_1_window.destroy()
                        root.wm_attributes("-topmost", 1)
                        root.focus_force()
                        root.wm_attributes("-topmost", 0)





            elif input == "simultaneous":
                simultaneous_width = 300
                simultaneous_height = 150
                simultaneous_window = Toplevel()
                simultaneous_window.geometry("{}x{}+{}+{}".format(simultaneous_width, simultaneous_height,
                                                                  int((
                                                                              simultaneous_window.winfo_screenwidth() - simultaneous_width) / 2),
                                                                  int((
                                                                              simultaneous_window.winfo_screenheight() - simultaneous_height) / 2)))
                simultaneous_window.configure(bg="#ECF3FB")
                simultaneous_window.resizable(0, 0)
                simultaneous_window.wm_attributes("-topmost", 1)
                simultaneous_window.focus_force()
                simultaneous_window.wm_attributes("-topmost", 0)
                simultaneous_window.title("Simultaneous Equation")
                simultaneous_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_simultaneous = Canvas(simultaneous_window, width=simultaneous_width, bg="#ECF3FB",
                                             height=simultaneous_height)
                canvas_simultaneous.pack()
                canvas_simultaneous.create_image(150, 75, image=image_simul_m)
                canvas_simultaneous.create_text(150, 10, text="Select the order of the simultaneous equation",
                                                font=("Segoe", 9, "bold"))
                button_y_coord = 40
                button_x_coord = 150
                canvas_simultaneous.create_window(button_x_coord, button_y_coord,
                                                  window=Button(canvas_simultaneous, bg="Black", fg="White",
                                                                text="Second Order",
                                                                font=("Segoe", 9, "bold"),
                                                                command=lambda: continue_simultaneous("2")), width=200,
                                                  height=20)
                button_y_coord += 40
                canvas_simultaneous.create_window(button_x_coord, button_y_coord,
                                                  window=Button(canvas_simultaneous, bg="Black", fg="White",
                                                                text="Third Order",
                                                                font=("Segoe", 9, "bold"),
                                                                command=lambda: continue_simultaneous("3")), width=200,
                                                  height=20)
                button_y_coord += 40
                canvas_simultaneous.create_window(button_x_coord, button_y_coord,
                                                  window=Button(canvas_simultaneous, bg="Black", fg="White",
                                                                text="Fouth Order",
                                                                font=("Segoe", 9, "bold"),
                                                                command=lambda: continue_simultaneous("4")), width=200,
                                                  height=20)

                def continue_simultaneous(input):
                    simultaneous_window.destroy()
                    if input == "2":
                        simultaneous_2_width = 600
                        simultaneous_2_height = 180
                        simultaneous_2_window = Toplevel()
                        simultaneous_2_window.geometry("{}x{}+{}+{}".format(simultaneous_2_width, simultaneous_2_height,
                                                                            int((
                                                                                        simultaneous_2_window.winfo_screenwidth() - simultaneous_2_width) / 2),
                                                                            int((
                                                                                        simultaneous_2_window.winfo_screenheight() - simultaneous_2_height) / 2)))
                        simultaneous_2_window.configure(bg="#ECF3FB")
                        simultaneous_2_window.resizable(0, 0)
                        simultaneous_2_window.wm_attributes("-topmost", 1)
                        simultaneous_2_window.focus_force()
                        simultaneous_2_window.wm_attributes("-topmost", 0)
                        simultaneous_2_window.title("Second Order")
                        simultaneous_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_simultaneous_2 = Canvas(simultaneous_2_window, bg="#ECF3FB", width=simultaneous_2_width,
                                                       height=simultaneous_2_height)
                        canvas_simultaneous_2.pack()
                        canvas_simultaneous_2.create_image(300, 90, image=image_simul_2nd)
                        entry_value_a = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_a.focus_force()
                        entry_value_b = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_c = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_d = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_e = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_f = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 30, justify=CENTER,
                                                          text="Enter the Coefficients(a, b, c) of the two simultaneous equations 'Format; ax+by=c' or ap+bq=c etc.\n if any of the required value is not given in the equation, just enter 0 \nPress enter to continue",
                                                          font=("Segoe", 8, "bold"))
                        canvas_simultaneous_2.create_window(60, 70,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="First Equation",
                                                                         font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(200, 60,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="a", font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(300, 60,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="b", font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(400, 60,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="c", font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(200, 80, window=entry_value_a, width=80)
                        canvas_simultaneous_2.create_window(300, 80, window=entry_value_b, width=80)
                        canvas_simultaneous_2.create_window(400, 80, window=entry_value_c, width=80)
                        canvas_simultaneous_2.create_window(60, 120,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="Second Equation",
                                                                         font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(200, 120,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="a", font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(300, 120,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="b", font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(400, 120,
                                                            window=Label(canvas_simultaneous_2, bg="black", fg="white",
                                                                         text="c", font=("Segoe", 9, "bold")))
                        canvas_simultaneous_2.create_window(200, 140, window=entry_value_d, width=80)
                        canvas_simultaneous_2.create_window(300, 140, window=entry_value_e, width=80)
                        canvas_simultaneous_2.create_window(400, 140, window=entry_value_f, width=80)

                        def simultaneous_2_cont_bind(event):
                            continue_simultaneous_2()

                        entry_value_a.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_b.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_c.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_d.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_e.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_f.bind("<Return>", simultaneous_2_cont_bind)

                        def continue_simultaneous_2():
                            try:
                                a = float(eval(entry_value_a.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_a.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_value_b.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_b.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                c = float(eval(entry_value_c.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_c.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                d = float(eval(entry_value_d.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_d.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                e = float(eval(entry_value_e.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_e.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                f = float(eval(entry_value_f.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_f.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            print(a, b, c, d, e, f)
                            det = t_by_2_md(a, b, d, e)
                            det_x = t_by_2_md(c, b, f, e)
                            det_y = t_by_2_md(a, c, d, f)
                            try:
                                val_x = round((det_x / det), approximate_val.get())
                                val_y = round((det_y / det), approximate_val.get())
                                answer = "(x = " + str(val_x) + "); " + "(y = " + str(val_y) + ")"
                            except:
                                answer = "Invalid Equation"
                            pow_solve = answer
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                label_display_2_var.set("")
                                old_label_display_1_var.set(label_display_1_var)
                            update_label_1()
                            simultaneous_2_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()
                            root.wm_attributes("-topmost", 0)

                    elif input == "3":
                        simultaneous_2_width = 700
                        simultaneous_2_height = 250
                        simultaneous_2_window = Toplevel()
                        simultaneous_2_window.geometry("{}x{}+{}+{}".format(simultaneous_2_width, simultaneous_2_height,
                                                                            int((
                                                                                        simultaneous_2_window.winfo_screenwidth() - simultaneous_2_width) / 2),
                                                                            int((
                                                                                        simultaneous_2_window.winfo_screenheight() - simultaneous_2_height) / 2)))
                        simultaneous_2_window.configure(bg="#ECF3FB")
                        simultaneous_2_window.resizable(0, 0)
                        simultaneous_2_window.wm_attributes("-topmost", 1)
                        simultaneous_2_window.focus_force()
                        simultaneous_2_window.wm_attributes("-topmost", 0)
                        simultaneous_2_window.title("Third Order")
                        simultaneous_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_simultaneous_2 = Canvas(simultaneous_2_window, bg="#ECF3FB", width=simultaneous_2_width,
                                                       height=simultaneous_2_height)
                        canvas_simultaneous_2.pack()
                        canvas_simultaneous_2.create_image(350, 125, image=image_simul_3rd)
                        entry_value_a = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_a.focus_force()
                        entry_value_b = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_c = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_d = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_e = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_f = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_g = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_h = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_i = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_j = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_k = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_l = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        canvas_simultaneous_2.create_text(350, 30, justify=CENTER, fill="black",
                                                          text="Enter the Coefficients(a, b, c, d) of the three simultaneous equations 'Format; ax+by+cz=d' or ap+bq+cr=d etc.\n if any of the required value is not given in the equation, just enter 0 \nPress enter to continue",
                                                          font=("Segoe", 8, "bold"))
                        canvas_simultaneous_2.create_text(60, 60, fill="black", text="First Equation",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 60, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 60, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 60, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 60, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 80, window=entry_value_a, width=80)
                        canvas_simultaneous_2.create_window(300, 80, window=entry_value_b, width=80)
                        canvas_simultaneous_2.create_window(400, 80, window=entry_value_c, width=80)
                        canvas_simultaneous_2.create_window(500, 80, window=entry_value_d, width=80)
                        canvas_simultaneous_2.create_text(60, 120, fill="black", text="Second Equation",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 120, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 120, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 120, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 120, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 140, window=entry_value_e, width=80)
                        canvas_simultaneous_2.create_window(300, 140, window=entry_value_f, width=80)
                        canvas_simultaneous_2.create_window(400, 140, window=entry_value_g, width=80)
                        canvas_simultaneous_2.create_window(500, 140, window=entry_value_h, width=80)
                        canvas_simultaneous_2.create_text(60, 180, fill="black", text="Third Equation",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 180, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 180, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 180, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 180, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 200, window=entry_value_i, width=80)
                        canvas_simultaneous_2.create_window(300, 200, window=entry_value_j, width=80)
                        canvas_simultaneous_2.create_window(400, 200, window=entry_value_k, width=80)
                        canvas_simultaneous_2.create_window(500, 200, window=entry_value_l, width=80)

                        def simultaneous_2_cont_bind(event):
                            continue_simultaneous_2()

                        entry_value_a.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_b.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_c.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_d.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_e.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_f.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_g.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_h.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_i.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_j.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_k.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_l.bind("<Return>", simultaneous_2_cont_bind)

                        def continue_simultaneous_2():
                            try:
                                a = float(eval(entry_value_a.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_a.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_value_b.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_b.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                c = float(eval(entry_value_c.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_c.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                d = float(eval(entry_value_d.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_d.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                e = float(eval(entry_value_e.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_e.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                f = float(eval(entry_value_f.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_f.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                g = float(eval(entry_value_g.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_g.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                h = float(eval(entry_value_h.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_h.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                i = float(eval(entry_value_i.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_i.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                j = float(eval(entry_value_j.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_j.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                k = float(eval(entry_value_k.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_k.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                l = float(eval(entry_value_l.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_l.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            print(a, b, c, d, e, f, g, h, i, j, k, l)
                            det = t_by_3_md(a, b, c, e, f, g, i, j, k)
                            det_x = t_by_3_md(d, b, c, h, f, g, l, j, k)
                            det_y = t_by_3_md(a, d, c, e, h, g, i, l, k)
                            det_z = t_by_3_md(a, b, d, e, f, h, i, j, l)
                            try:
                                val_x = round((det_x / det), approximate_val.get())
                                val_y = round((det_y / det), approximate_val.get())
                                val_z = round((det_z / det), approximate_val.get())
                                answer = "(x = " + str(val_x) + "); " + "(y = " + str(val_y) + "); " + "(z = " + str(
                                    val_z) + ")"
                            except:
                                answer = "Invalid Equation"
                            pow_solve = answer
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                label_display_2_var.set("")
                                old_label_display_1_var.set(label_display_1_var)
                            update_label_1()
                            simultaneous_2_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()

                    elif input == "4":
                        simultaneous_2_width = 800
                        simultaneous_2_height = 320
                        simultaneous_2_window = Toplevel()
                        simultaneous_2_window.geometry("{}x{}+{}+{}".format(simultaneous_2_width, simultaneous_2_height,
                                                                            int((
                                                                                        simultaneous_2_window.winfo_screenwidth() - simultaneous_2_width) / 2),
                                                                            int((
                                                                                        simultaneous_2_window.winfo_screenheight() - simultaneous_2_height) / 2)))
                        simultaneous_2_window.configure(bg="#ECF3FB")
                        simultaneous_2_window.resizable(0, 0)
                        simultaneous_2_window.wm_attributes("-topmost", 1)
                        simultaneous_2_window.focus_force()
                        simultaneous_2_window.wm_attributes("-topmost", 0)
                        simultaneous_2_window.title("Fouth Order")
                        simultaneous_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_simultaneous_2 = Canvas(simultaneous_2_window, bg="#ECF3FB", width=simultaneous_2_width,
                                                       height=simultaneous_2_height)
                        canvas_simultaneous_2.pack()
                        canvas_simultaneous_2.create_image(400, 160, image=image_simul_4th)
                        entry_value_a = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_a.focus_force()
                        entry_value_b = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_c = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_d = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_e = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_f = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_g = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_h = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_i = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_j = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_k = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_l = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_m = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_n = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_o = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_p = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_q = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_r = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_s = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_t = Entry(canvas_simultaneous_2, justify=CENTER, font=("Cambria", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 30, justify=CENTER, fill="black",
                                                          text="Enter the Coefficients(a, b, c, d, e) of the four simultaneous equations 'Format; aw+bx+cy+dz=e' \n if any of the required value is not given in the equation, just enter 0 \nPress enter to continue",
                                                          font=("Segoe", 8, "bold"))
                        canvas_simultaneous_2.create_text(60, 60, text="First Equation", fill="black",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 60, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 60, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 60, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 60, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(600, 60, fill="black", text="e",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 80, window=entry_value_a, width=80)
                        canvas_simultaneous_2.create_window(300, 80, window=entry_value_b, width=80)
                        canvas_simultaneous_2.create_window(400, 80, window=entry_value_c, width=80)
                        canvas_simultaneous_2.create_window(500, 80, window=entry_value_d, width=80)
                        canvas_simultaneous_2.create_window(600, 80, window=entry_value_e, width=80)
                        canvas_simultaneous_2.create_text(60, 120, fill="black", text="Second Equation",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 120, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 120, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 120, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 120, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(600, 120, fill="black", text="e",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 140, window=entry_value_f, width=80)
                        canvas_simultaneous_2.create_window(300, 140, window=entry_value_g, width=80)
                        canvas_simultaneous_2.create_window(400, 140, window=entry_value_h, width=80)
                        canvas_simultaneous_2.create_window(500, 140, window=entry_value_i, width=80)
                        canvas_simultaneous_2.create_window(600, 140, window=entry_value_j, width=80)
                        canvas_simultaneous_2.create_text(60, 180, fill="black", text="Third Equation",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 180, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 180, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 180, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 180, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(600, 180, fill="black", text="e",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 220, window=entry_value_k, width=80)
                        canvas_simultaneous_2.create_window(300, 220, window=entry_value_l, width=80)
                        canvas_simultaneous_2.create_window(400, 220, window=entry_value_m, width=80)
                        canvas_simultaneous_2.create_window(500, 220, window=entry_value_n, width=80)
                        canvas_simultaneous_2.create_window(600, 220, window=entry_value_o, width=80)
                        canvas_simultaneous_2.create_text(60, 240, fill="black", text="Fourth Equation",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(200, 240, fill="black", text="a",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(300, 240, fill="black", text="b",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(400, 240, fill="black", text="c",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(500, 240, fill="black", text="d",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_text(600, 240, fill="black", text="e",
                                                          font=("Segoe", 9, "bold"))
                        canvas_simultaneous_2.create_window(200, 280, window=entry_value_p, width=80)
                        canvas_simultaneous_2.create_window(300, 280, window=entry_value_q, width=80)
                        canvas_simultaneous_2.create_window(400, 280, window=entry_value_r, width=80)
                        canvas_simultaneous_2.create_window(500, 280, window=entry_value_s, width=80)
                        canvas_simultaneous_2.create_window(600, 280, window=entry_value_t, width=80)

                        def simultaneous_2_cont_bind(event):
                            continue_simultaneous_2()

                        entry_value_a.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_b.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_c.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_d.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_e.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_f.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_g.bind("<Return>", simultaneous_2_cont_bind)

                        entry_value_h.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_i.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_j.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_k.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_l.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_m.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_n.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_o.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_p.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_q.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_r.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_s.bind("<Return>", simultaneous_2_cont_bind)
                        entry_value_t.bind("<Return>", simultaneous_2_cont_bind)

                        def continue_simultaneous_2():
                            try:
                                a = float(eval(entry_value_a.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_a.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_value_b.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_b.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                c = float(eval(entry_value_c.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_c.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                d = float(eval(entry_value_d.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_d.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                e = float(eval(entry_value_e.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_e.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                f = float(eval(entry_value_f.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_f.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                g = float(eval(entry_value_g.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_g.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                h = float(eval(entry_value_h.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_h.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                i = float(eval(entry_value_i.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_i.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                j = float(eval(entry_value_j.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_j.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                k = float(eval(entry_value_k.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_k.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                l = float(eval(entry_value_l.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_l.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                m = float(eval(entry_value_m.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_m.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                n = float(eval(entry_value_n.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_n.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                o = float(eval(entry_value_o.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_o.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                p = float(eval(entry_value_p.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_p.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                q = float(eval(entry_value_q.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_q.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                r = float(eval(entry_value_r.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_r.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                s = float(eval(entry_value_s.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_s.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                t = float(eval(entry_value_t.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Coefficient Value")
                                simultaneous_2_window.wm_attributes("-topmost", 1)
                                simultaneous_2_window.focus_force()
                                entry_value_t.focus_force()
                                simultaneous_2_window.wm_attributes("-topmost", 0)
                                return
                            print(a, b, c, d, e, f, g, h, i, j, k, l)
                            det = t_by_4_md(a, b, c, d, f, g, h, i, k, l, m, n, p, q, r, s)
                            det_w = t_by_4_md(e, b, c, d, j, g, h, i, o, l, m, n, t, q, r, s)
                            det_x = t_by_4_md(a, e, c, d, f, j, h, i, k, o, m, n, p, t, r, s)
                            det_y = t_by_4_md(a, b, e, d, f, g, j, i, k, l, o, n, p, q, t, s)
                            det_z = t_by_4_md(a, b, c, e, f, g, h, j, k, l, m, o, p, q, r, t)
                            try:
                                val_w = round((det_w / det), approximate_val.get())
                                val_x = round((det_x / det), approximate_val.get())
                                val_y = round((det_y / det), approximate_val.get())
                                val_z = round((det_z / det), approximate_val.get())
                                answer = "(w = " + str(val_w) + "); " + "(x = " + str(val_x) + "); " + "(y = " + str(
                                    val_y) + "); " + "(z = " + str(val_z) + ")"
                            except:
                                answer = "Invalid Equation"
                            pow_solve = answer
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                label_display_2_var.set("")
                                old_label_display_1_var.set(label_display_1_var)
                            update_label_1()
                            simultaneous_2_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()

            elif input == "permutation":
                permutation_width = 200
                permutation_height = 120
                permutation_window = Toplevel()
                permutation_window.geometry("{}x{}+{}+{}".format(permutation_width, permutation_height,
                                                                 int((
                                                                             permutation_window.winfo_screenwidth() - permutation_width) / 2),
                                                                 int((
                                                                             permutation_window.winfo_screenheight() - permutation_height) / 2)))
                permutation_window.configure(bg="#ECF3FB")
                permutation_window.resizable(0, 0)
                permutation_window.wm_attributes("-topmost", 1)
                permutation_window.focus_force()
                permutation_window.wm_attributes("-topmost", 0)
                permutation_window.title("Permutation")
                permutation_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_permutation = Canvas(permutation_window, width=permutation_width,
                                            height=permutation_height)
                canvas_permutation.pack()

                canvas_permutation.create_image(100, 60, image=image_modulo)

                canvas_permutation.create_window(100, 10,
                                                 window=Label(canvas_permutation, text="Press Enter to Continue",
                                                              bg="black",
                                                              fg="white",
                                                              font=("Segoe", 9, "bold")), height=20)
                canvas_permutation.create_window(100 - 20, 40,
                                                 window=Label(canvas_permutation, text="n", bg="black", fg="white",
                                                              font=("Segoe", 11, "bold")), width=20,
                                                 height=20)

                canvas_permutation.create_window(100 - 20, 80,
                                                 window=Label(canvas_permutation, text="x", bg="black", fg="white",
                                                              font=("Segoe", 11, "bold")), width=20,
                                                 height=20)
                entry_value_x = Entry(canvas_permutation, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_permutation, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_permutation.create_window(100 + 20, 40, window=entry_value_x, width=40)
                canvas_permutation.create_window(100 + 20, 80, window=entry_value_y, width=40)

                def permutation_cont_bind(event):
                    continue_permutation()

                entry_value_x.bind("<Return>", permutation_cont_bind)
                entry_value_y.bind("<Return>", permutation_cont_bind)

                def continue_permutation():
                    if "." in entry_value_x.get():
                        messagebox.showerror("Error", "Invalid n value")
                        permutation_window.wm_attributes("-topmost", 1)
                        permutation_window.focus_force()
                        permutation_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if "." in entry_value_y.get():
                        messagebox.showerror("Error", "Invalid x value")
                        permutation_window.wm_attributes("-topmost", 1)
                        permutation_window.focus_force()
                        permutation_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    try:
                        value_x = int(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid n value")
                        permutation_window.wm_attributes("-topmost", 1)
                        permutation_window.focus_force()
                        permutation_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = int(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        permutation_window.wm_attributes("-topmost", 1)
                        permutation_window.focus_force()
                        permutation_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    answer = find_permutation(value_x, value_y)
                    pow_solve = answer
                    try:
                        pow_solve = str(int(pow_solve))
                    except:
                        pass
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    update_label_1()
                    old_label_display_1_var.set(label_display_1_var.get())
                    permutation_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)


            elif input == "combination":
                combination_width = 200
                combination_height = 120
                combination_window = Toplevel()
                combination_window.geometry("{}x{}+{}+{}".format(combination_width, combination_height,
                                                                 int((
                                                                             combination_window.winfo_screenwidth() - combination_width) / 2),
                                                                 int((
                                                                             combination_window.winfo_screenheight() - combination_height) / 2)))
                combination_window.configure(bg="#ECF3FB")
                combination_window.resizable(0, 0)
                combination_window.wm_attributes("-topmost", 1)
                combination_window.focus_force()
                combination_window.wm_attributes("-topmost", 0)
                combination_window.title("Combination")
                combination_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_combination = Canvas(combination_window, width=combination_width,
                                            height=combination_height)
                canvas_combination.pack()

                canvas_combination.create_image(100, 60, image=image_modulo)

                canvas_combination.create_window(100, 10,
                                                 window=Label(canvas_combination, text="Press Enter to Continue",
                                                              bg="black",
                                                              fg="white",
                                                              font=("Segoe", 9, "bold")), height=20)
                canvas_combination.create_window(100 - 20, 40,
                                                 window=Label(canvas_combination, text="n", bg="black", fg="white",
                                                              font=("Segoe", 11, "bold")), width=20,
                                                 height=20)

                canvas_combination.create_window(100 - 20, 80,
                                                 window=Label(canvas_combination, text="x", bg="black", fg="white",
                                                              font=("Segoe", 11, "bold")), width=20,
                                                 height=20)
                entry_value_x = Entry(canvas_combination, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_combination, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_combination.create_window(100 + 20, 40, window=entry_value_x, width=40)
                canvas_combination.create_window(100 + 20, 80, window=entry_value_y, width=40)

                def combination_cont_bind(event):
                    continue_combination()

                entry_value_x.bind("<Return>", combination_cont_bind)
                entry_value_y.bind("<Return>", combination_cont_bind)

                def continue_combination():
                    if "." in entry_value_x.get():
                        messagebox.showerror("Error", "Invalid n value")
                        combination_window.wm_attributes("-topmost", 1)
                        combination_window.focus_force()
                        combination_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if "." in entry_value_y.get():
                        messagebox.showerror("Error", "Invalid x value")
                        combination_window.wm_attributes("-topmost", 1)
                        combination_window.focus_force()
                        combination_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    try:
                        value_x = int(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid n value")
                        combination_window.wm_attributes("-topmost", 1)
                        combination_window.focus_force()
                        combination_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = int(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        combination_window.wm_attributes("-topmost", 1)
                        combination_window.focus_force()
                        combination_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    answer = find_combination(value_x, value_y)
                    pow_solve = answer
                    try:
                        pow_solve = str(int(pow_solve))
                    except:
                        pass
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    update_label_1()
                    old_label_display_1_var.set(label_display_1_var.get())
                    combination_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)


            elif input == "deg_to_rad":

                deg_to_rad_0_width = 300

                deg_to_rad_0_height = 100

                deg_to_rad_0_window = Toplevel()

                deg_to_rad_0_window.geometry("{}x{}+{}+{}".format(deg_to_rad_0_width, deg_to_rad_0_height,

                                                                  int((

                                                                              deg_to_rad_0_window.winfo_screenwidth() - deg_to_rad_0_width) / 2),

                                                                  int((

                                                                              deg_to_rad_0_window.winfo_screenheight() - deg_to_rad_0_height) / 2)))

                deg_to_rad_0_window.configure(bg="#ECF3FB")

                deg_to_rad_0_window.resizable(0, 0)

                deg_to_rad_0_window.wm_attributes("-topmost", 1)

                deg_to_rad_0_window.focus_force()

                deg_to_rad_0_window.wm_attributes("-topmost", 0)

                deg_to_rad_0_window.title("Conversion Between rad and deg")
                deg_to_rad_0_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_deg_to_rad_0 = Canvas(deg_to_rad_0_window, width=deg_to_rad_0_width, bg="#ECF3FB",

                                             height=deg_to_rad_0_height)

                canvas_deg_to_rad_0.pack()

                global image_deg_rad
                global image_deg_rad_2
                canvas_deg_to_rad_0.create_image(150, 50, image=image_deg_rad)
                canvas_deg_to_rad_0.create_text(150, 10, fill="black", text="Select Operation",

                                                font=("Segoe", 9, "bold"))

                button_y_coord = 40

                button_x_coord = 150

                canvas_deg_to_rad_0.create_window(button_x_coord, button_y_coord,

                                                  window=Button(canvas_deg_to_rad_0, bg="Black", fg="White",

                                                                text="Degree to Radians",

                                                                font=("Segoe", 9, "bold"),

                                                                command=lambda: continue_deg_to_rad_0("deg_to_rad")),
                                                  width=200,

                                                  height=20)

                button_y_coord += 40

                canvas_deg_to_rad_0.create_window(button_x_coord, button_y_coord,

                                                  window=Button(canvas_deg_to_rad_0, bg="Black", fg="White",

                                                                text="Radians to Degrees",

                                                                font=("Segoe", 9, "bold"),

                                                                command=lambda: continue_deg_to_rad_0("rad_to_deg")),
                                                  width=200,

                                                  height=20)

                def continue_deg_to_rad_0(input):

                    deg_to_rad_0_window.destroy()
                    if input == "deg_to_rad":
                        deg_to_rad_width = 200
                        deg_to_rad_height = 80
                        deg_to_rad_window = Toplevel()
                        deg_to_rad_window.geometry("{}x{}+{}+{}".format(deg_to_rad_width, deg_to_rad_height,
                                                                        int((
                                                                                    deg_to_rad_window.winfo_screenwidth() - deg_to_rad_width) / 2),
                                                                        int((
                                                                                    deg_to_rad_window.winfo_screenheight() - deg_to_rad_height) / 2)))
                        deg_to_rad_window.configure(bg="#ECF3FB")
                        deg_to_rad_window.resizable(0, 0)
                        deg_to_rad_window.wm_attributes("-topmost", 1)
                        deg_to_rad_window.focus_force()
                        deg_to_rad_window.wm_attributes("-topmost", 0)
                        deg_to_rad_window.title("Degrees to Radians")
                        deg_to_rad_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_deg_to_rad = Canvas(deg_to_rad_window, width=deg_to_rad_width, height=deg_to_rad_height,
                                                   bg="#ECF3FB")
                        canvas_deg_to_rad.pack()
                        canvas_deg_to_rad.create_image(100, 40, image=image_deg_rad_2)
                        entry_value_x = Entry(canvas_deg_to_rad, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_x.focus_force()
                        canvas_deg_to_rad.create_text(100, 10, text="Press enter to continue",
                                                      font=("Segoe ", 9, "bold"))
                        canvas_deg_to_rad.create_text(100 - 40, 40, text="Angle in Degrees:",
                                                      font=("Segoe ", 9, "bold"))
                        canvas_deg_to_rad.create_window(100 + 60, 40, window=entry_value_x, width=60)

                        def deg_to_rad_cont_bind(event):
                            continue_deg_to_rad()

                        entry_value_x.bind("<Return>", deg_to_rad_cont_bind)

                        def continue_deg_to_rad():
                            if "." in entry_value_x.get():
                                try:
                                    value_x = float(entry_value_x.get())
                                except:
                                    messagebox.showerror("Error", "Invalid x value")
                                    deg_to_rad_window.wm_attributes("-topmost", 1)
                                    deg_to_rad_window.focus_force()
                                    deg_to_rad_window.wm_attributes("-topmost", 0)
                                    entry_value_x.focus_force()
                                    return
                            else:
                                try:
                                    value_x = int(entry_value_x.get())
                                except:
                                    messagebox.showerror("Error", "Invalid x value")
                                    deg_to_rad_window.wm_attributes("-topmost", 1)
                                    deg_to_rad_window.focus_force()
                                    deg_to_rad_window.wm_attributes("-topmost", 0)
                                    entry_value_x.focus_force()
                                    return

                            if "." in str(value_x):
                                pow_solve = str(round(value_x / 180, approximate_val.get()))
                                pow_solve += "(" + chr(0x03C0) + ")"
                            else:
                                divisor = gcd(value_x, 180)
                                if divisor > 1:
                                    pow_solve = str(int(value_x / divisor)) + "(" + chr(0x03C0) + ")" + "/" + str(
                                        int(180 / divisor))
                                else:
                                    pow_solve = str(round(value_x / 180, approximate_val.get()))
                                    pow_solve += "(" + chr(0x03C0) + ")"
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set("(" + str(pow_solve) + ")")
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set("(" + str(pow_solve) + ")")
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set("(" + str(pow_solve) + ")")
                                label_display_2_var.set("")
                            update_label_1()
                            old_label_display_1_var.set(label_display_1_var.get())
                            deg_to_rad_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()
                            root.wm_attributes("-topmost", 0)
                    elif input == "rad_to_deg":
                        rad_to_deg_width = 200
                        rad_to_deg_height = 120
                        rad_to_deg_window = Toplevel()
                        rad_to_deg_window.geometry("{}x{}+{}+{}".format(rad_to_deg_width, rad_to_deg_height,
                                                                        int((
                                                                                    rad_to_deg_window.winfo_screenwidth() - rad_to_deg_width) / 2),
                                                                        int((
                                                                                    rad_to_deg_window.winfo_screenheight() - rad_to_deg_height) / 2)))
                        rad_to_deg_window.configure(bg="#ECF3FB")
                        rad_to_deg_window.resizable(0, 0)
                        rad_to_deg_window.wm_attributes("-topmost", 1)
                        rad_to_deg_window.focus_force()
                        rad_to_deg_window.wm_attributes("-topmost", 0)
                        rad_to_deg_window.title("Radians to Degrees")
                        rad_to_deg_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_rad_to_deg = Canvas(rad_to_deg_window, width=rad_to_deg_width, height=rad_to_deg_height,
                                                   bg="#ECF3FB")
                        canvas_rad_to_deg.pack()
                        global image_rad_deg
                        canvas_rad_to_deg.create_image(100, 60, image=image_rad_deg)
                        entry_value_x = Entry(canvas_rad_to_deg, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_x.focus_force()
                        canvas_rad_to_deg.create_text(100, 30, text="Press enter to continue\nUse 'p' for " + chr(
                            0x03C0) + "e.g 2p/3",
                                                      font=("Segoe", 9, "bold"), justify=CENTER)
                        canvas_rad_to_deg.create_text(100 - 40, 80, text="Angle in Radians:",
                                                      font=("Segoe", 9, "bold"))
                        canvas_rad_to_deg.create_window(100 + 60, 80, window=entry_value_x, width=60)

                        def rad_to_deg_cont_bind(event):
                            continue_rad_to_deg()

                        entry_value_x.bind("<Return>", rad_to_deg_cont_bind)

                        def continue_rad_to_deg():
                            value_x = entry_value_x.get().replace(" ", "")
                            p_loc = value_x.find("p")
                            if p_loc != -1:
                                if len(value_x) == 1 and value_x[0] == "p":
                                    value_x = value_x.replace("p", "(" + str(pi) + ")")
                                elif value_x[0] == "p" and value_x[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                                          "0"]:
                                    value_x = value_x.replace("p", "(" + str(pi) + ")*")
                                elif value_x[0] == "p" and value_x[1] not in ["1", "2", "3", "4", "5", "6", "7", "8",
                                                                              "9", "0"]:
                                    value_x = value_x.replace("p", "(" + str(pi) + ")")
                                elif p_loc != -1 and value_x[p_loc - 1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                                            "0"]:
                                    value_x = value_x.replace("p", "*(" + str(pi) + ")")
                            try:
                                value_x = eval(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                rad_to_deg_window.wm_attributes("-topmost", 1)
                                rad_to_deg_window.focus_force()
                                rad_to_deg_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                            try:
                                pow_solve = str(round((value_x * 180) / pi, approximate_val.get()))
                            except:
                                pow_solve = "Error"
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set("(" + str(pow_solve) + ")")
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set("(" + str(pow_solve) + ")")
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set("(" + str(pow_solve) + ")")
                                label_display_2_var.set("")
                            old_label_display_1_var.set(label_display_1_var.get())
                            update_label_1()
                            rad_to_deg_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()
                            root.wm_attributes("-topmost", 0)






            elif input == "cel_to_far":

                cel_to_far_0_width = 300

                cel_to_far_0_height = 100

                cel_to_far_0_window = Toplevel()

                cel_to_far_0_window.geometry("{}x{}+{}+{}".format(cel_to_far_0_width, cel_to_far_0_height,

                                                                  int((

                                                                              cel_to_far_0_window.winfo_screenwidth() - cel_to_far_0_width) / 2),

                                                                  int((

                                                                              cel_to_far_0_window.winfo_screenheight() - cel_to_far_0_height) / 2)))

                cel_to_far_0_window.configure(bg="#ECF3FB")

                cel_to_far_0_window.resizable(0, 0)

                cel_to_far_0_window.wm_attributes("-topmost", 1)

                cel_to_far_0_window.focus_force()

                cel_to_far_0_window.wm_attributes("-topmost", 0)

                cel_to_far_0_window.title("Conversion Between Celcius and Faranheit")
                cel_to_far_0_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_cel_to_far_0 = Canvas(cel_to_far_0_window, width=cel_to_far_0_width, bg="#ECF3FB",

                                             height=cel_to_far_0_height)

                canvas_cel_to_far_0.pack()

                canvas_cel_to_far_0.create_image(150, 50, image=image_deg_rad)
                canvas_cel_to_far_0.create_text(150, 10, text="Select Operation",

                                                font=("Segoe", 9, "bold"))

                button_y_coord = 40

                button_x_coord = 150

                canvas_cel_to_far_0.create_window(button_x_coord, button_y_coord,

                                                  window=Button(canvas_cel_to_far_0, bg="Black", fg="White",

                                                                text="Celcius to Farenheit",

                                                                font=("Segoe", 9, "bold"),

                                                                command=lambda: continue_cel_to_far_0("cel_to_far")),

                                                  width=200,

                                                  height=20)

                button_y_coord += 40

                canvas_cel_to_far_0.create_window(button_x_coord, button_y_coord,

                                                  window=Button(canvas_cel_to_far_0, bg="Black", fg="White",

                                                                text="Farenheit to Celcius",

                                                                font=("Segoe", 9, "bold"),

                                                                command=lambda: continue_cel_to_far_0("far_to_cel")),

                                                  width=200,

                                                  height=20)

                def continue_cel_to_far_0(input):

                    cel_to_far_0_window.destroy()

                    if input == "cel_to_far":

                        cel_to_far_width = 200

                        cel_to_far_height = 80

                        cel_to_far_window = Toplevel()

                        cel_to_far_window.geometry("{}x{}+{}+{}".format(cel_to_far_width, cel_to_far_height,

                                                                        int((

                                                                                    cel_to_far_window.winfo_screenwidth() - cel_to_far_width) / 2),

                                                                        int((

                                                                                    cel_to_far_window.winfo_screenheight() - cel_to_far_height) / 2)))

                        cel_to_far_window.configure(bg="#ECF3FB")

                        cel_to_far_window.resizable(0, 0)

                        cel_to_far_window.wm_attributes("-topmost", 1)

                        cel_to_far_window.focus_force()

                        cel_to_far_window.wm_attributes("-topmost", 0)

                        cel_to_far_window.title("Celcius to Farenheit")
                        cel_to_far_window.iconbitmap(os.path.join("data", "icon.ico"))

                        canvas_cel_to_far = Canvas(cel_to_far_window, width=cel_to_far_width, height=cel_to_far_height,

                                                   bg="#ECF3FB")

                        canvas_cel_to_far.pack()

                        canvas_cel_to_far.create_image(100, 40, image=image_deg_rad_2)
                        entry_value_x = Entry(canvas_cel_to_far, justify=CENTER, font=("Cambria", 9, "bold"))

                        entry_value_x.focus_force()

                        canvas_cel_to_far.create_text(100, 10, text="Press enter to continue",

                                                      font=("Segoe", 9, "bold"))

                        canvas_cel_to_far.create_text(100 - 40, 40, text="Temperature in Celcius:",
                                                      font=("Segoe", 7, "bold"))

                        canvas_cel_to_far.create_window(100 + 60, 40, window=entry_value_x, width=60)

                        def cel_to_far_cont_bind(event):

                            continue_cel_to_far()

                        entry_value_x.bind("<Return>", cel_to_far_cont_bind)

                        def continue_cel_to_far():
                            try:

                                value_x = float(entry_value_x.get())

                            except:

                                messagebox.showerror("Error", "Invalid Value")

                                cel_to_far_window.wm_attributes("-topmost", 1)

                                cel_to_far_window.focus_force()

                                cel_to_far_window.wm_attributes("-topmost", 0)

                                entry_value_x.focus_force()

                                return
                            pow_solve = str(round((value_x * 1.8) + 32, approximate_val.get()))

                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")

                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")

                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")

                            old_label_display_1_var.set(label_display_1_var.get())
                            update_label_1()

                            cel_to_far_window.destroy()

                            root.wm_attributes("-topmost", 1)

                            root.focus_force()

                            root.wm_attributes("-topmost", 0)

                    elif input == "far_to_cel":

                        far_to_cel_width = 200

                        far_to_cel_height = 120

                        far_to_cel_window = Toplevel()

                        far_to_cel_window.geometry("{}x{}+{}+{}".format(far_to_cel_width, far_to_cel_height,

                                                                        int((

                                                                                    far_to_cel_window.winfo_screenwidth() - far_to_cel_width) / 2),

                                                                        int((

                                                                                    far_to_cel_window.winfo_screenheight() - far_to_cel_height) / 2)))

                        far_to_cel_window.configure(bg="#ECF3FB")

                        far_to_cel_window.resizable(0, 0)

                        far_to_cel_window.wm_attributes("-topmost", 1)

                        far_to_cel_window.focus_force()

                        far_to_cel_window.wm_attributes("-topmost", 0)

                        far_to_cel_window.title("Farenheit to Celcius")
                        far_to_cel_window.iconbitmap(os.path.join("data", "icon.ico"))

                        canvas_far_to_cel = Canvas(far_to_cel_window, width=far_to_cel_width, height=far_to_cel_height,

                                                   bg="#ECF3FB")

                        canvas_far_to_cel.pack()

                        canvas_far_to_cel.create_image(100, 60, image=image_rad_deg)

                        entry_value_x = Entry(canvas_far_to_cel, justify=CENTER, font=("Cambria", 9, "bold"))

                        entry_value_x.focus_force()

                        canvas_far_to_cel.create_text(100, 30, text="Press enter to continue",

                                                      font=("Segoe", 9, "bold"), justify=CENTER)

                        canvas_far_to_cel.create_text(100 - 40, 80, text="Temperature in Farenheit:",
                                                      font=("Segoe", 7, "bold"))

                        canvas_far_to_cel.create_window(100 + 60, 80, window=entry_value_x, width=60)

                        def far_to_cel_cont_bind(event):

                            continue_far_to_cel()

                        entry_value_x.bind("<Return>", far_to_cel_cont_bind)

                        def continue_far_to_cel():

                            try:

                                value_x = float(entry_value_x.get())

                            except:

                                messagebox.showerror("Error", "Invalid Value")

                                far_to_cel_window.wm_attributes("-topmost", 1)

                                far_to_cel_window.focus_force()

                                far_to_cel_window.wm_attributes("-topmost", 0)

                                entry_value_x.focus_force()

                                return

                            try:

                                pow_solve = str(round((value_x - 32) / 1.8, approximate_val.get()))

                            except:

                                pow_solve = "Error"

                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")

                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")

                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")

                            old_label_display_1_var.set(label_display_1_var.get())
                            update_label_1()

                            far_to_cel_window.destroy()

                            root.wm_attributes("-topmost", 1)

                            root.focus_force()

                            root.wm_attributes("-topmost", 0)



            elif input == "cel_to_kel":

                cel_to_kel_0_width = 300

                cel_to_kel_0_height = 100

                cel_to_kel_0_window = Toplevel()

                cel_to_kel_0_window.geometry("{}x{}+{}+{}".format(cel_to_kel_0_width, cel_to_kel_0_height,

                                                                  int((

                                                                              cel_to_kel_0_window.winfo_screenwidth() - cel_to_kel_0_width) / 2),

                                                                  int((

                                                                              cel_to_kel_0_window.winfo_screenheight() - cel_to_kel_0_height) / 2)))

                cel_to_kel_0_window.configure(bg="#ECF3FB")

                cel_to_kel_0_window.resizable(0, 0)

                cel_to_kel_0_window.wm_attributes("-topmost", 1)

                cel_to_kel_0_window.focus_force()

                cel_to_kel_0_window.wm_attributes("-topmost", 0)

                cel_to_kel_0_window.title("Conversion Between Celcius and Kelvin")
                cel_to_kel_0_window.iconbitmap(os.path.join("data", "icon.ico"))

                canvas_cel_to_kel_0 = Canvas(cel_to_kel_0_window, width=cel_to_kel_0_width, bg="#ECF3FB",

                                             height=cel_to_kel_0_height)

                canvas_cel_to_kel_0.pack()

                canvas_cel_to_kel_0.create_image(150, 50, image=image_deg_rad)
                canvas_cel_to_kel_0.create_text(150, 10, text="Select Operation",

                                                font=("Segoe", 9, "bold"))

                button_y_coord = 40

                button_x_coord = 150

                canvas_cel_to_kel_0.create_window(button_x_coord, button_y_coord,

                                                  window=Button(canvas_cel_to_kel_0, bg="Black", fg="White",

                                                                text="Celcius to Kelvin",

                                                                font=("Segoe", 9, "bold"),

                                                                command=lambda: continue_cel_to_kel_0("cel_to_kel")),

                                                  width=200,

                                                  height=20)

                button_y_coord += 40

                canvas_cel_to_kel_0.create_window(button_x_coord, button_y_coord,

                                                  window=Button(canvas_cel_to_kel_0, bg="Black", fg="White",

                                                                text="Kelvin to Celcius",

                                                                font=("Segoe", 9, "bold"),

                                                                command=lambda: continue_cel_to_kel_0("kel_to_cel")),

                                                  width=200,

                                                  height=20)

                def continue_cel_to_kel_0(input):

                    cel_to_kel_0_window.destroy()

                    if input == "cel_to_kel":

                        cel_to_kel_width = 200

                        cel_to_kel_height = 80

                        cel_to_kel_window = Toplevel()

                        cel_to_kel_window.geometry("{}x{}+{}+{}".format(cel_to_kel_width, cel_to_kel_height,

                                                                        int((

                                                                                    cel_to_kel_window.winfo_screenwidth() - cel_to_kel_width) / 2),

                                                                        int((

                                                                                    cel_to_kel_window.winfo_screenheight() - cel_to_kel_height) / 2)))

                        cel_to_kel_window.configure(bg="#ECF3FB")

                        cel_to_kel_window.resizable(0, 0)

                        cel_to_kel_window.wm_attributes("-topmost", 1)

                        cel_to_kel_window.focus_force()

                        cel_to_kel_window.wm_attributes("-topmost", 0)

                        cel_to_kel_window.title("Celcius to Kelvin")
                        cel_to_kel_window.iconbitmap(os.path.join("data", "icon.ico"))

                        canvas_cel_to_kel = Canvas(cel_to_kel_window, width=cel_to_kel_width, height=cel_to_kel_height,

                                                   bg="#ECF3FB")

                        canvas_cel_to_kel.pack()

                        canvas_cel_to_kel.create_image(100, 40, image=image_deg_rad_2)
                        entry_value_x = Entry(canvas_cel_to_kel, justify=CENTER, font=("Cambria", 9, "bold"))

                        entry_value_x.focus_force()

                        canvas_cel_to_kel.create_text(100, 10, text="Press enter to continue",

                                                      font=("Segoe", 9, "bold"))

                        canvas_cel_to_kel.create_text(100 - 40, 40, text="Temperature in Celcius:",

                                                      font=("Segoe", 7, "bold"))

                        canvas_cel_to_kel.create_window(100 + 60, 40, window=entry_value_x, width=60)

                        def cel_to_kel_cont_bind(event):

                            continue_cel_to_kel()

                        entry_value_x.bind("<Return>", cel_to_kel_cont_bind)

                        def continue_cel_to_kel():

                            try:

                                value_x = float(entry_value_x.get())


                            except:

                                messagebox.showerror("Error", "Invalid Value")

                                cel_to_kel_window.wm_attributes("-topmost", 1)

                                cel_to_kel_window.focus_force()

                                cel_to_kel_window.wm_attributes("-topmost", 0)

                                entry_value_x.focus_force()

                                return

                            pow_solve = str(value_x + 273)

                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")


                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")


                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")


                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")

                            old_label_display_1_var.set(label_display_1_var.get())
                            update_label_1()

                            cel_to_kel_window.destroy()

                            root.wm_attributes("-topmost", 1)

                            root.focus_force()

                            root.wm_attributes("-topmost", 0)


                    elif input == "kel_to_cel":

                        kel_to_cel_width = 200

                        kel_to_cel_height = 120

                        kel_to_cel_window = Toplevel()

                        kel_to_cel_window.geometry("{}x{}+{}+{}".format(kel_to_cel_width, kel_to_cel_height,

                                                                        int((

                                                                                    kel_to_cel_window.winfo_screenwidth() - kel_to_cel_width) / 2),

                                                                        int((

                                                                                    kel_to_cel_window.winfo_screenheight() - kel_to_cel_height) / 2)))

                        kel_to_cel_window.configure(bg="#ECF3FB")

                        kel_to_cel_window.resizable(0, 0)

                        kel_to_cel_window.wm_attributes("-topmost", 1)

                        kel_to_cel_window.focus_force()

                        kel_to_cel_window.wm_attributes("-topmost", 0)

                        kel_to_cel_window.title("Kelvin to Celcius")
                        kel_to_cel_window.iconbitmap(os.path.join("data", "icon.ico"))

                        canvas_kel_to_cel = Canvas(kel_to_cel_window, width=kel_to_cel_width, height=kel_to_cel_height,

                                                   bg="#ECF3FB")

                        canvas_kel_to_cel.pack()

                        canvas_kel_to_cel.create_image(100, 60, image=image_rad_deg)
                        entry_value_x = Entry(canvas_kel_to_cel, justify=CENTER, font=("Cambria", 9, "bold"))

                        entry_value_x.focus_force()

                        canvas_kel_to_cel.create_text(100, 30, text="Press enter to continue",

                                                      font=("Segoe", 9, "bold"), justify=CENTER)

                        canvas_kel_to_cel.create_text(100 - 40, 80, text="Temperature in Kelvin:",

                                                      font=("Segoe", 7, "bold"))

                        canvas_kel_to_cel.create_window(100 + 60, 80, window=entry_value_x, width=60)

                        def kel_to_cel_cont_bind(event):

                            continue_kel_to_cel()

                        entry_value_x.bind("<Return>", kel_to_cel_cont_bind)

                        def continue_kel_to_cel():

                            try:

                                value_x = float(entry_value_x.get())


                            except:

                                messagebox.showerror("Error", "Invalid Kelvin Value")

                                kel_to_cel_window.wm_attributes("-topmost", 1)

                                kel_to_cel_window.focus_force()

                                kel_to_cel_window.wm_attributes("-topmost", 0)

                                entry_value_x.focus_force()

                                return

                            try:

                                pow_solve = str(value_x - 273)


                            except:

                                pow_solve = "Error"

                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")


                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":

                                label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")


                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")


                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":

                                label_display_1_var.set("(" + str(pow_solve) + ")")

                                label_display_2_var.set("")

                            old_label_display_1_var.set(label_display_1_var.get())
                            update_label_1()

                            kel_to_cel_window.destroy()

                            root.wm_attributes("-topmost", 1)

                            root.focus_force()

                            root.wm_attributes("-topmost", 0)


            elif input == "quadratic":
                quadratic_0_width = 300
                quadratic_0_height = 100
                quadratic_0_window = Toplevel()
                quadratic_0_window.geometry("{}x{}+{}+{}".format(quadratic_0_width, quadratic_0_height,
                                                                 int((
                                                                             quadratic_0_window.winfo_screenwidth() - quadratic_0_width) / 2),
                                                                 int((
                                                                             quadratic_0_window.winfo_screenheight() - quadratic_0_height) / 2)))
                quadratic_0_window.configure(bg="#ECF3FB")
                quadratic_0_window.resizable(0, 0)
                quadratic_0_window.wm_attributes("-topmost", 1)
                quadratic_0_window.focus_force()
                quadratic_0_window.wm_attributes("-topmost", 0)
                quadratic_0_window.title("Quadratic Equation")
                quadratic_0_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_quadratic_0 = Canvas(quadratic_0_window, width=quadratic_0_width, bg="#ECF3FB",
                                            height=quadratic_0_height)
                canvas_quadratic_0.pack()
                global image_quad_main
                canvas_quadratic_0.create_image(150, 50, image=image_quad_main)
                canvas_quadratic_0.create_text(150, 10, fill="black", text="Select the order of the quadratic equation",
                                               font=("Segoe", 9, "bold"))
                button_y_coord = 40
                button_x_coord = 150
                canvas_quadratic_0.create_window(button_x_coord, button_y_coord,
                                                 window=Button(canvas_quadratic_0, bg="Black", fg="White",
                                                               text="Second Order",
                                                               font=("Segoe", 9, "bold"),
                                                               command=lambda: continue_quadratic_0("second")),
                                                 width=200,
                                                 height=20)
                button_y_coord += 40
                canvas_quadratic_0.create_window(button_x_coord, button_y_coord,
                                                 window=Button(canvas_quadratic_0, bg="Black", fg="White",
                                                               text="Other",
                                                               font=("Segoe", 9, "bold"),
                                                               command=lambda: continue_quadratic_0("other")),
                                                 width=200,
                                                 height=20)

                def continue_quadratic_0(input):
                    quadratic_0_window.destroy()
                    if input == "second":
                        quadratic_width = 500
                        quadratic_height = 200
                        quadratic_window = Toplevel()
                        quadratic_window.geometry("{}x{}+{}+{}".format(quadratic_width, quadratic_height,
                                                                       int((
                                                                                   quadratic_window.winfo_screenwidth() - quadratic_width) / 2),
                                                                       int((
                                                                                   quadratic_window.winfo_screenheight() - quadratic_height) / 2)))
                        quadratic_window.configure(bg="#ECF3FB")
                        quadratic_window.resizable(0, 0)
                        quadratic_window.wm_attributes("-topmost", 1)
                        quadratic_window.focus_force()
                        quadratic_window.wm_attributes("-topmost", 0)
                        quadratic_window.title("Quadratic Equation")
                        quadratic_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_quadratic = Canvas(quadratic_window, width=quadratic_width, bg="#ECF3FB",
                                                  height=quadratic_height)
                        canvas_quadratic.pack()
                        global image_quad_2nd
                        canvas_quadratic.create_image(250, 100, image=image_quad_2nd)
                        text_hint = Text(canvas_quadratic, bg="#7198A7")
                        canvas_quadratic.create_window(250, 20, window=text_hint, width=500, height=40)
                        text_hint.tag_configure("head", font=("Segoe", 9, "bold"), justify=CENTER,
                                                foreground="white")
                        text_hint.tag_configure("hint", font=("Segoe", 9, "bold"), justify=LEFT,
                                                foreground="white")
                        heading_text = "Enter the details about the quadratic equation"
                        hint_text = "Hint: Supposing we have a quadratic equation(ax" + chr(
                            0x00B2) + " + bx + c =0) a, b and c are the details needed, just enter their value and for the variable part, x is the variable."

                        text_hint.insert(END, heading_text, "head")
                        text_hint.insert(END, "\n" + hint_text, "hint")
                        text_hint.config(state=DISABLED)
                        entry_value_var = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_var.focus_force()
                        entry_value_a = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_b = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_c = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        canvas_quadratic.create_text(200, 60, fill="black", text="Variable",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(300, 60, window=entry_value_var, width=80)
                        canvas_quadratic.create_text(60, 100, fill="black", text="Equation",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 100, fill="black", text="a", font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 100, fill="black", text="b", font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(400, 100, fill="black", text="c", font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 120, window=entry_value_a, width=80)
                        canvas_quadratic.create_window(300, 120, window=entry_value_b, width=80)
                        canvas_quadratic.create_window(400, 120, window=entry_value_c, width=80)

                        def quadratic_2_cont_bind(event):
                            continue_quadratic_2()

                        entry_value_var.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_a.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_b.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_c.bind("<Return>", quadratic_2_cont_bind)

                        def continue_quadratic_2():
                            try:
                                var = float(eval(entry_value_var.get()))
                                messagebox.showerror("Error", "Invalid Variable")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_var.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            except:
                                if len(entry_value_var.get()) == 1:
                                    var = entry_value_var.get()
                                else:
                                    messagebox.showerror("Error", "Invalid Variable")
                                    quadratic_window.wm_attributes("-topmost", 1)
                                    quadratic_window.focus_force()
                                    entry_value_var.focus_force()
                                    quadratic_window.wm_attributes("-topmost", 0)
                                    return
                            try:
                                a = float(eval(entry_value_a.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_a.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_value_b.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_b.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                c = float(eval(entry_value_c.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_c.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            roots = quadratic_formula(a, b, c)
                            if roots == []:
                                pow_solve = "(Invalid Equation)"
                            else:
                                pow_solve = "(" + var + " = ["
                                id_no = 0
                                for num in roots:
                                    if id_no == len(roots) - 1:
                                        pow_solve += str(round(num, approximate_val.get())) + "])"
                                    elif id_no == 0:
                                        pow_solve += str(round(num, approximate_val.get())) + ", "
                                    else:
                                        pow_solve += str(round(num, approximate_val.get())) + ", "
                                    id_no += 1
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                label_display_2_var.set("")
                                old_label_display_1_var.set(label_display_1_var)
                            update_label_1()
                            quadratic_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()
                            root.wm_attributes("-topmost", 0)



                    else:
                        quadratic_width = 500
                        quadratic_height = 400
                        quadratic_window = Toplevel()
                        quadratic_window.geometry("{}x{}+{}+{}".format(quadratic_width, quadratic_height,
                                                                       int((
                                                                                   quadratic_window.winfo_screenwidth() - quadratic_width) / 2),
                                                                       int((
                                                                                   quadratic_window.winfo_screenheight() - quadratic_height) / 2)))
                        quadratic_window.configure(bg="#ECF3FB")
                        quadratic_window.resizable(0, 0)
                        quadratic_window.wm_attributes("-topmost", 1)
                        quadratic_window.focus_force()
                        quadratic_window.wm_attributes("-topmost", 0)
                        quadratic_window.title("Quadratic Equation")
                        quadratic_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_quadratic = Canvas(quadratic_window, width=quadratic_width, bg="#ECF3FB",
                                                  height=quadratic_height)
                        canvas_quadratic.pack()
                        global image_quad_other
                        canvas_quadratic.create_image(250, 200, image=image_quad_other)
                        text_hint = Text(canvas_quadratic, bg="#7198A7")
                        canvas_quadratic.create_window(250, 20, window=text_hint, width=500, height=40)
                        text_hint.tag_configure("head", font=("Segoe", 9, "bold"), justify=CENTER,
                                                foreground="white")
                        text_hint.tag_configure("hint", font=("Segoe", 9, "bold"), justify=LEFT,
                                                foreground="white")
                        heading_text = "Enter the details about the quadratic equation"
                        hint_text = "Hint: Supposing we have a quadratic equation(a+b+c+d+e+f=0) with six values a to f, where each of them actually mean a given variable raised to given power altogether having a given coefficient. e.g considering our first value coeficient is '3' and it's power is '2', with a variable 'y', this means our first value is 3y" + chr(
                            0x00B2) + ". To type coefficient alone e.g a First Value equal to '3'; enter the power equal to '0' and the coefficient equal to '3'. Enter the power and coefficient = '0' to indicate non-existing value.. Now using this particular quadratic equation " + "'4x" + chr(
                            0x00B3) + " - x" + chr(
                            0x00B2) + " + 2x - 3 = 0', this particular quadratic equation has a First Value '4x" + chr(
                            0x00B3) + "' ,Second Value '-x" + chr(
                            0x00B2) + "' , Third Value '2x' and Fourth Value '-3'. Now to enter this particular equation, enter your Variable as x, First Value power and coefficients as 3 and 4 respectively. Second Value power and coefficients as 2 and -1 respectively, Third Value power and coefficients as 1 and 2 respectively, Fouth Value power and coefficients as 0 and -3 respectively and Enter both Fifth and Sixth Value power and coefficients as 0 and 0 respectively since both of them does not exist."

                        text_hint.insert(END, heading_text, "head")
                        text_hint.insert(END, "\n" + hint_text, "hint")
                        text_hint.config(state=DISABLED)
                        entry_value_var = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_var.focus_force()
                        entry_value_ap = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_ac = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_bp = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_bc = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_cp = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_cc = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_dp = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_dc = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_ep = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_ec = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_fp = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        entry_value_fc = Entry(canvas_quadratic, justify=CENTER, font=("Cambria", 9, "bold"))
                        canvas_quadratic.create_text(200, 60, fill="black", text="Variable",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(300, 60, window=entry_value_var, width=80)
                        canvas_quadratic.create_text(60, 100, fill="black", text="First Value",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 100, fill="black", text="Coefficient",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 100, fill="black", text="Power",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 120, window=entry_value_ac, width=80)
                        canvas_quadratic.create_window(300, 120, window=entry_value_ap, width=80)
                        canvas_quadratic.create_text(60, 150, fill="black", text="Second Value",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 150, fill="black", text="Coefficient",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 150, fill="black", text="Power",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 170, window=entry_value_bc, width=80)
                        canvas_quadratic.create_window(300, 170, window=entry_value_bp, width=80)
                        canvas_quadratic.create_text(60, 200, fill="black", text="Third Value",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 200, fill="black", text="Coefficient",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 200, fill="black", text="Power",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 220, window=entry_value_cc, width=80)
                        canvas_quadratic.create_window(300, 220, window=entry_value_cp, width=80)
                        canvas_quadratic.create_text(60, 250, fill="black", text="Fourth Value",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 250, fill="black", text="Coefficient",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 250, fill="black", text="Power",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 270, window=entry_value_dc, width=80)
                        canvas_quadratic.create_window(300, 270, window=entry_value_dp, width=80)
                        canvas_quadratic.create_text(60, 300, fill="black", text="Fifth Value",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 300, fill="black", text="Coefficient",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 300, fill="black", text="Power",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 320, window=entry_value_ec, width=80)
                        canvas_quadratic.create_window(300, 320, window=entry_value_ep, width=80)
                        canvas_quadratic.create_text(60, 350, fill="black", text="Sixth Value",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(200, 350, fill="black", text="Coefficient",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_text(300, 350, fill="black", text="Power",
                                                     font=("Segoe", 9, "bold"))
                        canvas_quadratic.create_window(200, 370, window=entry_value_fc, width=80)
                        canvas_quadratic.create_window(300, 370, window=entry_value_fp, width=80)

                        def quadratic_2_cont_bind(event):
                            continue_quadratic_2()

                        entry_value_var.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_ac.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_ap.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_bc.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_bp.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_cc.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_cp.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_dc.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_dp.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_ec.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_ep.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_fc.bind("<Return>", quadratic_2_cont_bind)
                        entry_value_fp.bind("<Return>", quadratic_2_cont_bind)

                        def continue_quadratic_2():
                            try:
                                var = float(eval(entry_value_var.get()))
                                messagebox.showerror("Error", "Invalid Variable")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_var.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            except:
                                if len(entry_value_var.get()) == 1:
                                    var = entry_value_var.get()
                                else:
                                    messagebox.showerror("Error", "Invalid Variable")
                                    quadratic_window.wm_attributes("-topmost", 1)
                                    quadratic_window.focus_force()
                                    entry_value_var.focus_force()
                                    quadratic_window.wm_attributes("-topmost", 0)
                                    return
                            try:
                                a = float(eval(entry_value_ac.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_ac.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                b = float(eval(entry_value_ap.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_ap.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                c = float(eval(entry_value_bc.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_bc.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                d = float(eval(entry_value_bp.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_bp.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                e = float(eval(entry_value_cc.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_cc.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                f = float(eval(entry_value_cp.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_cp.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                g = float(eval(entry_value_dc.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_dc.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                h = float(eval(entry_value_dp.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_dp.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                i = float(eval(entry_value_ec.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_ec.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                j = float(eval(entry_value_ep.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_ep.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                k = float(eval(entry_value_fc.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_fc.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            try:
                                l = float(eval(entry_value_fp.get()))
                            except:
                                messagebox.showerror("Error", "Invalid Value")
                                quadratic_window.wm_attributes("-topmost", 1)
                                quadratic_window.focus_force()
                                entry_value_fp.focus_force()
                                quadratic_window.wm_attributes("-topmost", 0)
                                return
                            roots = find_roots(a, b, c, d, e, f, g, h, i, j, k, l)
                            if roots == []:
                                pow_solve = "(Invalid Equation)"
                            else:
                                pow_solve = "(" + var + " = ["
                                id_no = 0
                                for num in roots:
                                    if id_no == len(roots) - 1:
                                        pow_solve += str(num) + "])"
                                    elif id_no == 0:
                                        pow_solve += str(num) + ", "
                                    else:
                                        pow_solve += str(num) + ", "
                                    id_no += 1
                            if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                            elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                old_label_display_1_var.set(label_display_1_var)
                                label_display_2_var.set("")
                            elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                label_display_1_var.set(str(pow_solve))
                                label_display_2_var.set("")
                                old_label_display_1_var.set(label_display_1_var)
                            update_label_1()
                            quadratic_window.destroy()
                            root.wm_attributes("-topmost", 1)
                            root.focus_force()
                            root.wm_attributes("-topmost", 0)






            elif input == "statistics":
                statistics_0_width = 300
                statistics_0_height = 100
                statistics_0_window = Toplevel()
                statistics_0_window.geometry("{}x{}+{}+{}".format(statistics_0_width, statistics_0_height,
                                                                  int((
                                                                              statistics_0_window.winfo_screenwidth() - statistics_0_width) / 2),
                                                                  int((
                                                                              statistics_0_window.winfo_screenheight() - statistics_0_height) / 2)))
                statistics_0_window.configure(bg="#ECF3FB")
                statistics_0_window.resizable(0, 0)
                statistics_0_window.wm_attributes("-topmost", 1)
                statistics_0_window.focus_force()
                statistics_0_window.wm_attributes("-topmost", 0)
                statistics_0_window.title("Statistics")
                statistics_0_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_statistics_0 = Canvas(statistics_0_window, width=statistics_0_width, bg="#ECF3FB",
                                             height=statistics_0_height)
                canvas_statistics_0.pack()
                global image_stat_main
                canvas_statistics_0.create_image(150, 50, image=image_stat_main)
                canvas_statistics_0.create_text(150, 10, fill="black", text="Select the data arrangement type",
                                                font=("Segoe", 9, "bold"))
                button_y_coord = 40
                button_x_coord = 150
                canvas_statistics_0.create_window(button_x_coord, button_y_coord,
                                                  window=Button(canvas_statistics_0, bg="Black", fg="White",
                                                                text="Grouped Data",
                                                                font=("Segoe", 9, "bold"),
                                                                command=lambda: continue_statistics_0("grouped")),
                                                  width=200,
                                                  height=20)
                button_y_coord += 40
                canvas_statistics_0.create_window(button_x_coord, button_y_coord,
                                                  window=Button(canvas_statistics_0, bg="Black", fg="White",
                                                                text="Discrete Data",
                                                                font=("Segoe", 9, "bold"),
                                                                command=lambda: continue_statistics_0("discrete")),
                                                  width=200,
                                                  height=20)

                def continue_statistics_0(input):
                    statistics_0_window.destroy()
                    if input == "grouped":
                        statistics_width = 300
                        statistics_height = 220
                        statistics_window = Toplevel()
                        statistics_window.geometry("{}x{}+{}+{}".format(statistics_width, statistics_height,
                                                                        int((
                                                                                    statistics_window.winfo_screenwidth() - statistics_width) / 2),
                                                                        int((
                                                                                    statistics_window.winfo_screenheight() - statistics_height) / 2)))
                        statistics_window.configure(bg="#ECF3FB")
                        statistics_window.resizable(0, 0)
                        statistics_window.wm_attributes("-topmost", 1)
                        statistics_window.focus_force()
                        statistics_window.wm_attributes("-topmost", 0)
                        statistics_window.title("Grouped Data")
                        statistics_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_statistics = Canvas(statistics_window, width=statistics_width, bg="#ECF3FB",
                                                   height=statistics_height)
                        canvas_statistics.pack()
                        global image_stat_2
                        canvas_statistics.create_image(150, 110, image=image_stat_2)
                        text_hint = Text(canvas_statistics, bg="#7198A7")
                        canvas_statistics.create_window(150, 20, window=text_hint, width=298, height=30)
                        text_hint.tag_configure("head", font=("Calibri", 9, "bold"), justify=CENTER, foreground="black")
                        text_hint.tag_configure("hint", font=("Calibri", 9, "bold"), justify=LEFT, foreground="black")
                        heading_text = "Enter the data and press 'n' key to continue"
                        hint_text = "Format: (x-y, f) (x-y,f) (x-y,f) where x and y are the data and f is the frequency e.g (2-5,3) (4-10,2) (5-9,3)"

                        text_hint.insert(END, heading_text, "head")
                        text_hint.insert(END, "\n" + hint_text, "hint")
                        text_hint.config(state=DISABLED)
                        entry_data = Text(canvas_statistics, bg="#7198A7", font=("Cambria", 10, "bold"),
                                          foreground="white")
                        entry_data.focus_force()
                        canvas_statistics.create_window(150, 140, window=entry_data, width=298, height=160)

                        def statistics_2_cont_bind(event):
                            continue_statistics_2()

                        entry_data.bind("n", statistics_2_cont_bind)
                        entry_data.bind("N", statistics_2_cont_bind)

                        def continue_statistics_2():
                            entry_data.config(state=DISABLED)
                            stat_data = entry_data.get(1.0, END)
                            compiled_data = ""
                            data_list = []
                            for data in stat_data:
                                compiled_data += data.replace("\n", "").replace(" ", "")
                            compiled_data += " "
                            print(compiled_data)
                            txt_id = 0
                            for txt in compiled_data:
                                if txt == "(":
                                    data_list.append(compiled_data[txt_id:compiled_data.find(")", txt_id + 1) + 1])
                                txt_id += 1
                            if data_list == []:
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            len_hyphen = 0
                            len_dot = 0
                            len_comma = 0
                            len_lower = 0
                            len_upper = 0
                            len_freq = 0
                            for data in data_list:
                                if "-" in data:
                                    len_hyphen += 1
                                if "." in data:
                                    for text in data:
                                        if text == ".":
                                            len_dot += 1
                                if "," in data:
                                    len_comma += 1
                            if len_hyphen != len(data_list):
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            if len_dot != 0:
                                if len_dot != len(data_list) * 2:
                                    messagebox.showerror("Error", "Invalid Data")
                                    statistics_window.wm_attributes("-topmost", 1)
                                    statistics_window.focus_force()
                                    entry_data.focus_force()
                                    statistics_window.wm_attributes("-topmost", 0)
                                    entry_data.config(state=NORMAL)
                                    return
                            if len_comma != len(data_list):
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            for data in data_list:
                                if len_dot != 0:
                                    lower = data[data.find("(") + 1:data.find("-")]
                                    try:
                                        lower_data = float(lower)
                                        len_lower += 1
                                    except:
                                        pass
                                    upper = data[data.find("-") + 1:data.find(",")]
                                    try:
                                        upper_data = float(upper)
                                        len_upper += 1
                                    except:
                                        pass
                                    freq = data[data.find(",") + 1:data.find(")")]
                                    try:
                                        freq_data = int(freq)
                                        len_freq += 1
                                    except:
                                        pass
                                else:
                                    lower = data[data.find("(") + 1:data.find("-")]
                                    try:
                                        lower_data = int(lower)
                                        len_lower += 1
                                    except:
                                        pass
                                    upper = data[data.find("-") + 1:data.find(",")]
                                    try:
                                        upper_data = int(upper)
                                        len_upper += 1
                                    except:
                                        pass
                                    freq = data[data.find(",") + 1:data.find(")")]
                                    try:
                                        freq_data = int(freq)
                                        len_freq += 1
                                    except:
                                        pass

                            if len_upper != len(data_list):
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            if len_lower != len(data_list):
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            if len_freq != len(data_list):
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            list_lower_boundary = []
                            list_upper_bondary = []
                            list_central_value = []
                            list_frequency = []
                            if len_dot != 0:
                                decimal_places = 0
                                for data in data_list:
                                    lower = data[data.find("(") + 1:data.find("-")]
                                    if len(lower[lower.find("."):]) > decimal_places:
                                        decimal_places = len(lower[lower.find("."):])
                                    upper = data[data.find("-") + 1:data.find(",")]
                                    if len(upper[upper.find("."):]) > decimal_places:
                                        decimal_places = len(upper[upper.find("."):])
                                boundary = 5 / (pow(10, decimal_places + 1))
                            else:
                                boundary = 0.5
                            for data in data_list:
                                if len_dot != 0:
                                    lower = data[data.find("(") + 1:data.find("-")]
                                    lower_data = float(lower) - boundary
                                    list_lower_boundary.append(lower_data)
                                    upper = data[data.find("-") + 1:data.find(",")]
                                    upper_data = float(upper) + boundary
                                    list_upper_bondary.append(upper_data)
                                    freq = data[data.find(",") + 1:data.find(")")]
                                    freq_data = int(freq)
                                    list_frequency.append(freq_data)
                                    central_value = (lower_data + upper_data) / 2
                                    list_central_value.append(central_value)
                                else:
                                    print("a")
                                    lower = data[data.find("(") + 1:data.find("-")]
                                    lower_data = int(lower) - boundary
                                    list_lower_boundary.append(lower_data)
                                    upper = data[data.find("-") + 1:data.find(",")]
                                    upper_data = int(upper) + boundary
                                    list_upper_bondary.append(upper_data)
                                    freq = data[data.find(",") + 1:data.find(")")]
                                    freq_data = int(freq)
                                    list_frequency.append(freq_data)
                                    central_value = (lower_data + upper_data) / 2
                                    list_central_value.append(central_value)
                            print(list_lower_boundary)
                            print(list_upper_bondary)
                            print(list_central_value)
                            print(list_frequency)

                            statistics_2_width = 300
                            statistics_2_height = 280
                            statistics_2_window = Toplevel()
                            statistics_2_window.geometry(
                                "{}x{}+{}+{}".format(statistics_2_width, statistics_2_height,
                                                     int((
                                                                 statistics_2_window.winfo_screenwidth() - statistics_2_width) / 2),
                                                     int((
                                                                 statistics_2_window.winfo_screenheight() - statistics_2_height) / 2)))
                            statistics_2_window.configure(bg="#ECF3FB")
                            statistics_2_window.resizable(0, 0)
                            statistics_2_window.wm_attributes("-topmost", 1)
                            statistics_2_window.focus_force()
                            statistics_2_window.wm_attributes("-topmost", 0)
                            statistics_2_window.title("Operation")
                            statistics_2_window.iconbitmap(os.path.join("data", "icon.ico"))

                            def close_statistics_2_window():
                                try:
                                    statistics_2_window.destroy()
                                    entry_data.config(state=NORMAL)
                                except:
                                    statistics_2_window.destroy()

                            statistics_2_window.protocol("WM_DELETE_WINDOW", close_statistics_2_window)
                            canvas_statistics_2 = Canvas(statistics_2_window, width=statistics_2_width,
                                                         bg="#ECF3FB",
                                                         height=statistics_2_height)
                            canvas_statistics_2.pack()
                            global image_stat_op_1
                            canvas_statistics_2.create_image(150, 140, image=image_stat_op_1)
                            canvas_statistics_2.create_text(150, 10, fill="black", text="Select Operation",
                                                            font=("Segoe", 10, "bold"))

                            canvas_statistics_2.create_window(150, 40,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Mean",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "mean")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 80,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Median",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "median")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 120,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Mode",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "mode")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 160,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Variance",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "variance")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 200,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Standard Deviation",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "s.d")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 240,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Mean Deviation",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "m.d")),
                                                              width=200,
                                                              height=20)

                            def continue_statistics_2(input):
                                sum_frequency = 0
                                line_no = 0
                                for data in list_frequency:
                                    sum_frequency += data
                                    line_no += 1

                                sum_frequency_central = 0
                                line_no = 0
                                for data in list_central_value:
                                    sum_frequency_central += (data * list_frequency[line_no])
                                    line_no += 1
                                mean = round(sum_frequency_central / sum_frequency, 3)

                                sum_frequency_deviation_absolute = 0
                                line_no = 0
                                for data in list_central_value:
                                    sum_frequency_deviation_absolute += (
                                            list_frequency[line_no] * absolute(data - mean))
                                    line_no += 1

                                sum_frequency_deviation_square = 0
                                line_no = 0
                                for data in list_central_value:
                                    sum_frequency_deviation_square += (list_frequency[line_no] * pow((data - mean), 2))
                                    line_no += 1

                                if input == "mean":
                                    pow_solve = "(Mean = " + str(mean) + ")"
                                elif input == "variance":
                                    try:
                                        answer = round(sum_frequency_deviation_square / sum_frequency, 3)
                                        pow_solve = "(Variance = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"
                                elif input == "s.d":
                                    try:
                                        answer = round(sum_frequency_deviation_square / sum_frequency, 3)
                                        answer = round(pow(answer, 0.5), 3)
                                        pow_solve = "(Standard Deviation = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"
                                elif input == "m.d":
                                    try:
                                        answer = round(sum_frequency_deviation_absolute / sum_frequency, 3)
                                        answer = pow(answer, 0.5)
                                        pow_solve = "(Mean Deviation = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"
                                elif input == "mode":
                                    highest_frequency = 0
                                    modal_class_line = 0
                                    line_no = 0
                                    for data in list_frequency:
                                        if data > highest_frequency:
                                            modal_class_line = line_no
                                            highest_frequency = data
                                        line_no += 1
                                    if modal_class_line == 0:
                                        lower_bound_val = list_frequency[modal_class_line]
                                    else:
                                        lower_bound_val = list_frequency[modal_class_line] - list_frequency[
                                            modal_class_line - 1]
                                    if modal_class_line == len(list_frequency) - 1:
                                        upper_bound_val = list_frequency[modal_class_line]
                                    else:
                                        upper_bound_val = list_frequency[modal_class_line] - list_frequency[
                                            modal_class_line + 1]
                                    class_interval = list_upper_bondary[modal_class_line] - list_lower_boundary[
                                        modal_class_line]
                                    lower_class_boundary = list_lower_boundary[modal_class_line]
                                    try:
                                        answer = lower_class_boundary + (((lower_bound_val) / (
                                                lower_bound_val + upper_bound_val)) * class_interval)
                                        answer = round(answer, 3)
                                        pow_solve = "(Mode = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"

                                elif input == "median":
                                    middle_frequency = sum_frequency / 2
                                    median_class_line = 0
                                    counted_frequency = 0
                                    line_no = 0
                                    for data in list_frequency:
                                        counted_frequency += data
                                        if counted_frequency > middle_frequency:
                                            median_class_line = line_no
                                            counted_frequency -= data
                                            occupied_median_class_frequency = middle_frequency - counted_frequency
                                            break
                                        line_no += 1
                                    class_interval = list_upper_bondary[median_class_line] - list_lower_boundary[
                                        median_class_line]
                                    lower_class_boundary = list_lower_boundary[median_class_line]
                                    median_class_frequency = list_frequency[median_class_line]
                                    try:
                                        answer = lower_class_boundary + ((
                                                                                 occupied_median_class_frequency / median_class_frequency) * class_interval)
                                        answer = round(answer, 3)
                                        pow_solve = "(Median = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"

                                if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                    label_display_1_var.set(str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                    label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                    label_display_1_var.set(str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                    label_display_2_var.set("")
                                elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                    label_display_1_var.set(str(pow_solve))
                                    label_display_2_var.set("")
                                    old_label_display_1_var.set(label_display_1_var)
                                update_label_1()
                                statistics_window.destroy()
                                statistics_2_window.destroy()
                                root.wm_attributes("-topmost", 1)
                                root.focus_force()
                                root.wm_attributes("-topmost", 0)
                    elif input == "discrete":
                        statistics_width = 300
                        statistics_height = 220
                        statistics_window = Toplevel()
                        statistics_window.geometry("{}x{}+{}+{}".format(statistics_width, statistics_height,
                                                                        int((
                                                                                    statistics_window.winfo_screenwidth() - statistics_width) / 2),
                                                                        int((
                                                                                    statistics_window.winfo_screenheight() - statistics_height) / 2)))
                        statistics_window.configure(bg="#ECF3FB")
                        statistics_window.resizable(0, 0)
                        statistics_window.wm_attributes("-topmost", 1)
                        statistics_window.focus_force()
                        statistics_window.wm_attributes("-topmost", 0)
                        statistics_window.title("Discrete Data")
                        statistics_window.iconbitmap(os.path.join("data", "icon.ico"))
                        canvas_statistics = Canvas(statistics_window, width=statistics_width, bg="#ECF3FB",
                                                   height=statistics_height)
                        canvas_statistics.pack()
                        canvas_statistics.create_image(150, 110, image=image_stat_2)
                        text_hint = Text(canvas_statistics, bg="#7198A7")
                        canvas_statistics.create_window(150, 20, window=text_hint, width=298, height=30)
                        text_hint.tag_configure("head", font=("Calibri", 9, "bold"), justify=CENTER, foreground="black")
                        text_hint.tag_configure("hint", font=("Calibri", 9, "bold"), justify=LEFT, foreground="black")
                        heading_text = "Enter the data and press 'n' key to continue"
                        hint_text = "Format: x, x, x, x, x where x are the data e.g 2, 3, 5, 3, 8, 4"

                        text_hint.insert(END, heading_text, "head")
                        text_hint.insert(END, "\n" + hint_text, "hint")
                        text_hint.config(state=DISABLED)
                        entry_data = Text(canvas_statistics, bg="#7198A7", font=("Cambria", 10, "bold"),
                                          foreground="white")
                        entry_data.focus_force()
                        canvas_statistics.create_window(150, 140, window=entry_data, width=298, height=160)

                        def statistics_2_cont_bind(event):
                            continue_statistics_2()

                        entry_data.bind("n", statistics_2_cont_bind)
                        entry_data.bind("N", statistics_2_cont_bind)

                        def continue_statistics_2():
                            entry_data.config(state=DISABLED)
                            stat_data = entry_data.get(1.0, END)
                            compiled_data = ""
                            data_list = []
                            for data in stat_data:
                                compiled_data += data.replace("\n", "").replace(" ", "")
                            print(compiled_data)
                            txt_id = 0
                            for txt in compiled_data:
                                if txt_id == 0:
                                    data_list.append(compiled_data[txt_id:compiled_data.find(",", txt_id + 1)])
                                elif txt == ",":
                                    if compiled_data.find(",", txt_id + 1) == -1:
                                        data_list.append(compiled_data[txt_id + 1:])
                                    else:
                                        data_list.append(compiled_data[txt_id + 1:compiled_data.find(",", txt_id + 1)])
                                txt_id += 1
                            print(data_list)
                            if data_list == []:
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            len_values = 0
                            for data in data_list:
                                try:
                                    lower_data = float(data)
                                    len_values += 1
                                except:
                                    pass
                            if len_values != len(data_list):
                                messagebox.showerror("Error", "Invalid Data")
                                statistics_window.wm_attributes("-topmost", 1)
                                statistics_window.focus_force()
                                entry_data.focus_force()
                                statistics_window.wm_attributes("-topmost", 0)
                                entry_data.config(state=NORMAL)
                                return
                            list_central_value = []
                            list_frequency = []
                            for data in data_list:
                                value = float(data)
                                list_central_value.append(value)
                                list_frequency.append(1)
                            list_central_value = sort_list(list_central_value)
                            print(list_central_value)
                            statistics_2_width = 300
                            statistics_2_height = 320
                            statistics_2_window = Toplevel()
                            statistics_2_window.geometry(
                                "{}x{}+{}+{}".format(statistics_2_width, statistics_2_height,
                                                     int((
                                                                 statistics_2_window.winfo_screenwidth() - statistics_2_width) / 2),
                                                     int((
                                                                 statistics_2_window.winfo_screenheight() - statistics_2_height) / 2)))
                            statistics_2_window.configure(bg="#ECF3FB")
                            statistics_2_window.resizable(0, 0)
                            statistics_2_window.wm_attributes("-topmost", 1)
                            statistics_2_window.focus_force()
                            statistics_2_window.wm_attributes("-topmost", 0)
                            statistics_2_window.title("Operation")
                            statistics_2_window.iconbitmap(os.path.join("data", "icon.ico"))

                            def close_statistics_2_window():
                                try:
                                    statistics_2_window.destroy()
                                    entry_data.config(state=NORMAL)
                                except:
                                    statistics_2_window.destroy()

                            statistics_2_window.protocol("WM_DELETE_WINDOW", close_statistics_2_window)
                            canvas_statistics_2 = Canvas(statistics_2_window, width=statistics_2_width,
                                                         bg="#ECF3FB",
                                                         height=statistics_2_height)
                            canvas_statistics_2.pack()
                            global image_stat_op_2
                            canvas_statistics_2.create_image(150, 160, image=image_stat_op_2)
                            canvas_statistics_2.create_text(150, 10, fill="black", text="Select Operation",
                                                            font=("Segoe", 10, "bold"))

                            canvas_statistics_2.create_window(150, 40,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Mean",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "mean")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 80,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Median",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "median")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 120,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Mode",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "mode")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 160,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Variance",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "variance")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 200,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Standard Deviation",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "s.d")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 240,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Mean Deviation",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "m.d")),
                                                              width=200,
                                                              height=20)

                            canvas_statistics_2.create_window(150, 280,
                                                              window=Button(canvas_statistics_2, justify=CENTER,
                                                                            anchor=CENTER, bg="Black", fg="White",
                                                                            text="Range",
                                                                            font=("Segoe", 10, "bold"),
                                                                            command=lambda: continue_statistics_2(
                                                                                "range")),
                                                              width=200,
                                                              height=20)

                            def continue_statistics_2(input):
                                sum_frequency = 0
                                line_no = 0
                                for data in list_frequency:
                                    sum_frequency += data
                                    line_no += 1

                                sum_frequency_central = 0
                                line_no = 0
                                for data in list_central_value:
                                    sum_frequency_central += (data * list_frequency[line_no])
                                    line_no += 1
                                mean = round(sum_frequency_central / sum_frequency, 3)

                                sum_frequency_deviation_absolute = 0
                                line_no = 0
                                for data in list_central_value:
                                    sum_frequency_deviation_absolute += (
                                            list_frequency[line_no] * absolute(data - mean))
                                    line_no += 1

                                sum_frequency_deviation_square = 0
                                line_no = 0
                                for data in list_central_value:
                                    sum_frequency_deviation_square += (list_frequency[line_no] * pow((data - mean), 2))
                                    line_no += 1

                                if input == "mean":
                                    pow_solve = "(Mean = " + str(mean) + ")"
                                elif input == "variance":
                                    try:
                                        answer = round(sum_frequency_deviation_square / sum_frequency, 3)
                                        pow_solve = "(Variance = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"
                                elif input == "s.d":
                                    try:
                                        answer = round(sum_frequency_deviation_square / sum_frequency, 3)
                                        answer = round(pow(answer, 0.5), 3)
                                        pow_solve = "(Standard Deviation = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"
                                elif input == "m.d":
                                    try:
                                        answer = round(sum_frequency_deviation_absolute / sum_frequency, 3)
                                        answer = pow(answer, 0.5)
                                        pow_solve = "(Mean Deviation = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"
                                elif input == "mode":
                                    mode = get_mode(list_central_value)
                                    try:
                                        answer = round(mode, 3)
                                        pow_solve = "(Mode = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"

                                elif input == "median":
                                    if len(list_central_value) % 2 == 0:
                                        mid_value_a = list_central_value[int((len(list_central_value) / 2)) - 1]
                                        mid_value_b = list_central_value[int((len(list_central_value) / 2))]
                                        median = round((mid_value_a + mid_value_b) / 2, 3)
                                    else:
                                        mid_value = list_central_value[int((len(list_central_value) - 1) / 2)]
                                        median = round(mid_value, 3)
                                    try:
                                        answer = median
                                        pow_solve = "(Median = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"

                                elif input == "range":
                                    try:
                                        answer = list_central_value[len(list_central_value) - 1] - list_central_value[0]
                                        pow_solve = "(Range = " + str(answer) + ")"
                                    except:
                                        pow_solve = "Error"

                                if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                                    label_display_1_var.set(str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                                    label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                                    label_display_1_var.set(str(pow_solve))
                                    old_label_display_1_var.set(label_display_1_var)
                                    label_display_2_var.set("")
                                elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                                    label_display_1_var.set(str(pow_solve))
                                    label_display_2_var.set("")
                                    old_label_display_1_var.set(label_display_1_var)
                                update_label_1()
                                statistics_window.destroy()
                                statistics_2_window.destroy()
                                root.wm_attributes("-topmost", 1)
                                root.focus_force()
                                root.wm_attributes("-topmost", 0)

















            elif input == "trig":
                trig_width = 140
                trig_height = 120
                trig_window = Toplevel()
                trig_window.geometry("{}x{}+{}+{}".format(trig_width, trig_height,
                                                          int((trig_window.winfo_screenwidth() - trig_width) / 2),
                                                          int((trig_window.winfo_screenheight() - trig_height) / 2)))
                trig_window.configure(bg="#ECF3FB")
                trig_window.resizable(0, 0)
                trig_window.wm_attributes("-topmost", 1)
                trig_window.focus_force()
                trig_window.wm_attributes("-topmost", 0)
                trig_window.title("Trigonometric")
                trig_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_trig = Canvas(trig_window, width=trig_width, bg="#ECF3FB", height=trig_height)
                canvas_trig.pack()
                canvas_trig.create_image(70, 60, image=image_hyp)
                button_x_coord = -10
                button_y_coord = 20
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="sinx",
                                                        font=("Segoe", 9, "bold"),
                                                        command=lambda: continue_trig("sin")), width=35, height=20)
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="cosx",
                                                        font=("Segoe", 9, "bold"),
                                                        command=lambda: continue_trig("cos")), width=35, height=20)
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="tanx",
                                                        font=("Segoe", 9, "bold"),
                                                        command=lambda: continue_trig("tan")), width=35, height=20)
                button_x_coord = -10
                button_y_coord = 60
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="cosecx",
                                                        font=("Segoe", 7, "bold"),
                                                        command=lambda: continue_trig("cosec")), width=35, height=20)
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="secx",
                                                        font=("Segoe", 9, "bold"),
                                                        command=lambda: continue_trig("sec")), width=35, height=20)
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="cotx",
                                                        font=("Segoe", 9, "bold"),
                                                        command=lambda: continue_trig("cot")), width=35, height=20)
                button_x_coord = -10
                button_y_coord = 100
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="asinx",
                                                        font=("Segoe", 7, "bold"),
                                                        command=lambda: continue_trig("asin")), width=35, height=20)
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="acosx",
                                                        font=("Segoe", 7, "bold"),
                                                        command=lambda: continue_trig("acos")), width=35, height=20)
                button_x_coord += 40
                canvas_trig.create_window(button_x_coord, button_y_coord,
                                          window=Button(canvas_trig, bg="Black", fg="White", text="atanx",
                                                        font=("Segoe", 7, "bold"),
                                                        command=lambda: continue_trig("atan")), width=35, height=20)

                def continue_trig(input):
                    trig_window.destroy()
                    trig_2_width = 200
                    trig_2_height = 60
                    trig_2_window = Toplevel()
                    trig_2_window.geometry("{}x{}+{}+{}".format(trig_2_width, trig_2_height,
                                                                int((
                                                                            trig_2_window.winfo_screenwidth() - trig_2_width) / 2),
                                                                int((
                                                                            trig_2_window.winfo_screenheight() - trig_2_height) / 2)))
                    trig_2_window.configure(bg="#ECF3FB")
                    trig_2_window.resizable(0, 0)
                    trig_2_window.wm_attributes("-topmost", 1)
                    trig_2_window.focus_force()
                    trig_2_window.wm_attributes("-topmost", 0)
                    trig_2_window.title(input)
                    trig_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                    canvas_trig_2 = Canvas(trig_2_window, bg="#ECF3FB", width=trig_2_width, height=trig_2_height)
                    canvas_trig_2.pack()
                    canvas_trig_2.create_image(100, 30, image=image_factorial)

                    canvas_trig_2.create_window(100, 10,
                                                window=Label(canvas_trig_2, text="Press Enter to Continue", bg="black",
                                                             fg="white",
                                                             font=("Segoe", 9, "bold")), height=20)
                    canvas_trig_2.create_window(100 - 20, 40,
                                                window=Label(canvas_trig_2, text="x", bg="black", fg="white",
                                                             font=("Segoe", 11, "bold")), width=20, height=20)
                    entry_value_x = Entry(canvas_trig_2, justify=CENTER, font=("Cambria", 9, "bold"))
                    entry_value_x.focus_force()
                    canvas_trig_2.create_window(100 + 20, 40, window=entry_value_x, width=40)

                    def trig_2_cont_bind(event):
                        continue_trig_2()

                    entry_value_x.bind("<Return>", trig_2_cont_bind)

                    def continue_trig_2():
                        try:
                            value_x = float(entry_value_x.get())
                        except:
                            messagebox.showerror("Error", "Invalid x value")
                            trig_2_window.wm_attributes("-topmost", 1)
                            trig_2_window.focus_force()
                            trig_2_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return
                        if input == "sin":
                            try:
                                answer = sin((value_x * pi) / 180)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "cos":
                            try:
                                answer = cos((value_x * pi) / 180)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "tan":
                            try:
                                answer = tan((value_x * pi) / 180)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "cosec":
                            try:
                                answer = 1 / (sin((value_x * pi) / 180))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "sec":
                            try:
                                answer = 1 / (cos((value_x * pi) / 180))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "cot":
                            try:
                                answer = 1 / (tan((value_x * pi) / 180))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "asin":
                            try:
                                answer = degrees(asin(value_x))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "acos":
                            try:
                                answer = degrees(acos(value_x))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "atan":
                            try:
                                answer = degrees(atan(value_x))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                trig_2_window.wm_attributes("-topmost", 1)
                                trig_2_window.focus_force()
                                trig_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        pow_solve = answer
                        try:
                            pow_solve = "(" + str(round(pow_solve, approximate_val.get())) + ")"
                        except:
                            pow_solve = "(" + str(pow_solve) + ")"
                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                            label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                            label_display_2_var.set("")
                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                            old_label_display_1_var.set(label_display_1_var)
                        update_label_1()
                        trig_2_window.destroy()
                        root.wm_attributes("-topmost", 1)
                        root.focus_force()
                        root.wm_attributes("-topmost", 0)


            elif input == "hyp":
                hyp_width = 140
                hyp_height = 120
                hyp_window = Toplevel()
                hyp_window.geometry("{}x{}+{}+{}".format(hyp_width, hyp_height,
                                                         int((hyp_window.winfo_screenwidth() - hyp_width) / 2),
                                                         int((hyp_window.winfo_screenheight() - hyp_height) / 2)))
                hyp_window.configure(bg="#ECF3FB")
                hyp_window.resizable(0, 0)
                hyp_window.wm_attributes("-topmost", 1)
                hyp_window.focus_force()
                hyp_window.wm_attributes("-topmost", 0)
                hyp_window.title("Hyperbolic")
                hyp_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_hyp = Canvas(hyp_window, width=hyp_width, bg="#ECF3FB", height=hyp_height)
                canvas_hyp.pack()
                canvas_hyp.create_image(70, 60, image=image_hyp)
                button_x_coord = -10
                button_y_coord = 20
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="sinhx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("sinh")), width=35, height=20)
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="coshx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("cosh")), width=35, height=20)
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="tanhx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("tanh")), width=35, height=20)
                button_x_coord = -10
                button_y_coord = 60
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="cosechx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("cosech")), width=35, height=20)
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="sechx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("sech")), width=35, height=20)
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="cothx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("coth")), width=35, height=20)
                button_x_coord = -10
                button_y_coord = 100
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="asinhx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("asinh")), width=35, height=20)
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="acoshx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("acosh")), width=35, height=20)
                button_x_coord += 40
                canvas_hyp.create_window(button_x_coord, button_y_coord,
                                         window=Button(canvas_hyp, bg="Black", fg="White", text="atanhx",
                                                       font=("Segoe", 7, "bold"),
                                                       command=lambda: continue_hyp("atanh")), width=35, height=20)

                def continue_hyp(input):
                    hyp_window.destroy()
                    hyp_2_width = 200
                    hyp_2_height = 60
                    hyp_2_window = Toplevel()
                    hyp_2_window.geometry("{}x{}+{}+{}".format(hyp_2_width, hyp_2_height,
                                                               int((
                                                                           hyp_2_window.winfo_screenwidth() - hyp_2_width) / 2),
                                                               int((
                                                                           hyp_2_window.winfo_screenheight() - hyp_2_height) / 2)))
                    hyp_2_window.configure(bg="#ECF3FB")
                    hyp_2_window.resizable(0, 0)
                    hyp_2_window.wm_attributes("-topmost", 1)
                    hyp_2_window.focus_force()
                    hyp_2_window.wm_attributes("-topmost", 0)
                    hyp_2_window.title(input)
                    hyp_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                    canvas_hyp_2 = Canvas(hyp_2_window, bg="#ECF3FB", width=hyp_2_width, height=hyp_2_height)
                    canvas_hyp_2.pack()
                    canvas_hyp_2.create_image(100, 30, image=image_factorial)

                    canvas_hyp_2.create_window(100, 10,
                                               window=Label(canvas_hyp_2, text="Press Enter to Continue", bg="black",
                                                            fg="white",
                                                            font=("Segoe", 9, "bold")), height=20)
                    canvas_hyp_2.create_window(100 - 20, 40,
                                               window=Label(canvas_hyp_2, text="x", bg="black", fg="white",
                                                            font=("Segoe", 11, "bold")), width=20, height=20)
                    entry_value_x = Entry(canvas_hyp_2, justify=CENTER, font=("Cambria", 9, "bold"))
                    entry_value_x.focus_force()
                    canvas_hyp_2.create_window(100 + 20, 40, window=entry_value_x, width=40)

                    def hyp_2_cont_bind(event):
                        continue_hyp_2()

                    entry_value_x.bind("<Return>", hyp_2_cont_bind)

                    def continue_hyp_2():
                        try:
                            value_x = float(entry_value_x.get())
                        except:
                            messagebox.showerror("Error", "Invalid x value")
                            hyp_2_window.wm_attributes("-topmost", 1)
                            hyp_2_window.focus_force()
                            hyp_2_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return
                        if input == "sinh":
                            try:
                                answer = sinh(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "cosh":
                            try:
                                answer = cosh(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "tanh":
                            try:
                                answer = tanh(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "cosech":
                            try:
                                answer = 1 / (sinh(value_x))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "sech":
                            try:
                                answer = 1 / (cosh(value_x))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "coth":
                            try:
                                answer = 1 / (tanh(value_x))
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "asinh":
                            try:
                                answer = asinh(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "acosh":
                            try:
                                answer = acosh(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        elif input == "atanh":
                            try:
                                answer = atanh(value_x)
                            except:
                                messagebox.showerror("Error", "Invalid x value")
                                hyp_2_window.wm_attributes("-topmost", 1)
                                hyp_2_window.focus_force()
                                hyp_2_window.wm_attributes("-topmost", 0)
                                entry_value_x.focus_force()
                                return
                        pow_solve = answer
                        try:
                            pow_solve = "(" + str(round(pow_solve, approximate_val.get())) + ")"
                        except:
                            pow_solve = "(" + str(pow_solve) + ")"
                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                            label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                            label_display_2_var.set("")
                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                            old_label_display_1_var.set(label_display_1_var)
                        update_label_1()
                        hyp_2_window.destroy()
                        root.wm_attributes("-topmost", 1)
                        root.focus_force()
                        root.wm_attributes("-topmost", 0)

            elif input == "copy1":
                pyperclip.copy(label_display_1_var.get())
                messagebox.showinfo("Info", "Copied!")

            elif input == "copy2":
                pyperclip.copy(label_display_2_var.get())
                messagebox.showinfo("Info", "Copied!")

            elif input == "clear":
                label_display_1_var.set("")
                label_display_2_var.set("")
                update_label_1()
            elif input == "nbase":
                nbase_width = 200
                nbase_height = 120
                nbase_window = Toplevel()
                nbase_window.geometry("{}x{}+{}+{}".format(nbase_width, nbase_height,
                                                           int((nbase_window.winfo_screenwidth() - nbase_width) / 2),
                                                           int((nbase_window.winfo_screenheight() - nbase_height) / 2)))
                nbase_window.configure(bg="#ECF3FB")
                nbase_window.resizable(0, 0)
                nbase_window.wm_attributes("-topmost", 1)
                nbase_window.focus_force()
                nbase_window.wm_attributes("-topmost", 0)
                nbase_window.title("Number Base")
                nbase_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_nbase = Canvas(nbase_window, width=nbase_width, height=nbase_height, bg="#ECF3FB")
                canvas_nbase.pack()
                canvas_nbase.create_image(100, 60, image=image_modulo)
                button_convert = Button(canvas_nbase, bg="Black", fg="White", justify=CENTER,
                                        font=("Segoe", 9, "bold"), text="Convert!",
                                        command=lambda: nbase_convert())
                button_calculate = Button(canvas_nbase, bg="Black", fg="White", justify=CENTER,
                                          font=("Segoe", 9, "bold"), text="Calculate!",
                                          command=lambda: nbase_calculate())
                canvas_nbase.create_window(100, 40, window=button_convert, width=80)
                canvas_nbase.create_window(100, 80, window=button_calculate, width=80)

                def nbase_calculate():
                    nbase_calculate_width = 400
                    nbase_calculate_height = 240
                    nbase_calculate_window = Toplevel()
                    nbase_calculate_window.geometry("{}x{}+{}+{}".format(nbase_calculate_width, nbase_calculate_height,
                                                                         int((
                                                                                     nbase_calculate_window.winfo_screenwidth() - nbase_calculate_width) / 2),
                                                                         int((
                                                                                     nbase_calculate_window.winfo_screenheight() - nbase_calculate_height) / 2)))
                    nbase_calculate_window.configure(bg="#ECF3FB")
                    nbase_calculate_window.resizable(0, 0)
                    nbase_calculate_window.wm_attributes("-topmost", 1)
                    nbase_calculate_window.focus_force()
                    nbase_calculate_window.wm_attributes("-topmost", 0)
                    nbase_calculate_window.title("Number Base")
                    nbase_calculate_window.iconbitmap(os.path.join("data", "icon.ico"))
                    canvas_nbase_calculate = Canvas(nbase_calculate_window, width=nbase_calculate_width,
                                                    height=nbase_calculate_height)
                    canvas_nbase_calculate.pack()
                    global image_nbase_calculate
                    canvas_nbase_calculate.create_image(200, 120, image=image_nbase_calculate)
                    entry_value_w = Entry(canvas_nbase_calculate, justify=LEFT, font=("CordiaUPC", 11, "bold"))
                    entry_value_w.focus_force()
                    entry_value_x = Entry(canvas_nbase_calculate, justify=LEFT, font=("CordiaUPC", 11, "bold"))
                    entry_value_y = Entry(canvas_nbase_calculate, justify=CENTER, font=("Cambria", 9, "bold"))
                    entry_value_z = Entry(canvas_nbase_calculate, justify=CENTER, font=("Cambria", 9, "bold"))
                    label_answer_var = StringVar()
                    label_answer = Label(canvas_nbase_calculate, justify=CENTER, font=("CordiaUPC", 11, "bold"),
                                         textvariable=label_answer_var)
                    canvas_nbase_calculate.create_text(200, 10, fill="black", text="Press enter to continue",
                                                       font=("Segoe", 9, "bold"))
                    canvas_nbase_calculate.create_text(50, 40, fill="black", text="Value 1:",
                                                       font=("Segoe", 9, "bold"))
                    canvas_nbase_calculate.create_text(50, 80, fill="black", text="Value 2:",
                                                       font=("Segoe", 9, "bold"))
                    canvas_nbase_calculate.create_text(120, 120, fill="black", text="Operation(+, -, /, *):",
                                                       font=("Segoe", 9, "bold"))
                    canvas_nbase_calculate.create_text(200 - 40, 160, fill="black", text="Working Base:",
                                                       font=("Segoe", 9, "bold"))
                    canvas_nbase_calculate.create_window(220, 40, window=entry_value_w, width=280)
                    canvas_nbase_calculate.create_window(220, 80, window=entry_value_x, width=280)
                    canvas_nbase_calculate.create_window(280, 120, window=entry_value_y, width=40)
                    canvas_nbase_calculate.create_window(200 + 120, 160, window=entry_value_z, width=40)

                    def nbase_calculate_cont_bind(event):
                        continue_nbase_calculate()

                    entry_value_w.bind("<Return>", nbase_calculate_cont_bind)
                    entry_value_x.bind("<Return>", nbase_calculate_cont_bind)
                    entry_value_y.bind("<Return>", nbase_calculate_cont_bind)
                    entry_value_z.bind("<Return>", nbase_calculate_cont_bind)

                    def continue_nbase_calculate():
                        if "." not in entry_value_z.get():
                            pass
                        else:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_calculate_window.wm_attributes("-topmost", 1)
                            nbase_calculate_window.focus_force()
                            nbase_calculate_window.wm_attributes("-topmost", 0)
                            entry_value_z.focus_force()
                            return
                        try:
                            value_z = int(entry_value_z.get())
                        except:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_calculate_window.wm_attributes("-topmost", 1)
                            nbase_calculate_window.focus_force()
                            nbase_calculate_window.wm_attributes("-topmost", 0)
                            entry_value_z.focus_force()
                            return
                        if (value_z >= 2 and value_z <= 10) or value_z == 12 or value_z == 16:
                            pass
                        else:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_calculate_window.wm_attributes("-topmost", 1)
                            nbase_calculate_window.focus_force()
                            nbase_calculate_window.wm_attributes("-topmost", 0)
                            entry_value_z.focus_force()
                            return
                        if "-" in str(entry_value_w.get()) or "+" in str(entry_value_w.get()) or "*" in str(
                                entry_value_w.get()) or "/" in str(
                            entry_value_w.get()):
                            messagebox.showerror("Error", "Invalid Value 1")
                            nbase_calculate_window.wm_attributes("-topmost", 1)
                            nbase_calculate_window.focus_force()
                            nbase_calculate_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return

                        if "." in str(entry_value_w.get()):
                            for num in str(entry_value_w.get())[0:str(entry_value_w.get()).find(".")]:
                                try:
                                    if int(num) >= value_z:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_w.focus_force()
                                        return
                                except ValueError:
                                    pass
                            for num in str(entry_value_w.get())[str(entry_value_w.get()).find(".") + 1:]:
                                try:
                                    if int(num) >= value_z:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_w.focus_force()
                                        return
                                except ValueError:
                                    pass

                            try:
                                value_w = float(entry_value_w.get())
                                decimal_no_first = True
                            except:
                                if entry_value_z.get() == "16" or entry_value_z.get() == "12":
                                    if "A" in str(entry_value_w.get()) or "B" in str(entry_value_w.get()) or "C" in str(
                                            entry_value_w.get()) or "D" in str(entry_value_w.get()) or "E" in str(
                                        entry_value_w.get()) or "F" in str(entry_value_w.get()) or "X" in str(
                                        entry_value_w.get()) or "V" in str(entry_value_w.get()):
                                        value_w = str(entry_value_w.get())
                                        decimal_no_first = True
                                        pass
                                    else:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_w.focus_force()
                                        return
                                else:
                                    messagebox.showerror("Error", "Invalid Value")
                                    nbase_calculate_window.wm_attributes("-topmost", 1)
                                    nbase_calculate_window.focus_force()
                                    nbase_calculate_window.wm_attributes("-topmost", 0)
                                    entry_value_w.focus_force()
                                    return
                        else:
                            for num in str(entry_value_w.get()):
                                try:
                                    if int(num) >= value_z:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_w.focus_force()
                                        return
                                except ValueError:
                                    pass
                            try:
                                value_w = int(entry_value_w.get())
                                decimal_no_first = False
                            except:
                                if entry_value_z.get() == "16" or entry_value_z.get() == "12":
                                    if "A" in str(entry_value_w.get()) or "B" in str(entry_value_w.get()) or "C" in str(
                                            entry_value_w.get()) or "D" in str(entry_value_w.get()) or "E" in str(
                                        entry_value_w.get()) or "F" in str(entry_value_w.get()) or "X" in str(
                                        entry_value_w.get()) or "V" in str(entry_value_w.get()):
                                        value_w = str(entry_value_w.get())
                                        decimal_no_first = True
                                        pass
                                    else:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_w.focus_force()
                                        return
                                else:
                                    messagebox.showerror("Error", "Invalid Value")
                                    nbase_calculate_window.wm_attributes("-topmost", 1)
                                    nbase_calculate_window.focus_force()
                                    nbase_calculate_window.wm_attributes("-topmost", 0)
                                    entry_value_w.focus_force()
                                    return
                        if "-" in str(entry_value_x.get()) or "+" in str(entry_value_x.get()) or "*" in str(
                                entry_value_x.get()) or "/" in str(
                            entry_value_x.get()):
                            messagebox.showerror("Error", "Invalid Value 1")
                            nbase_calculate_window.wm_attributes("-topmost", 1)
                            nbase_calculate_window.focus_force()
                            nbase_calculate_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return

                        if "." in str(entry_value_x.get()):
                            for num in str(entry_value_x.get())[0:str(entry_value_x.get()).find(".")]:
                                try:
                                    if int(num) >= value_z:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_x.focus_force()
                                        return
                                except ValueError:
                                    pass
                            for num in str(entry_value_x.get())[str(entry_value_x.get()).find(".") + 1:]:
                                try:
                                    if int(num) >= value_z:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_x.focus_force()
                                        return
                                except ValueError:
                                    pass

                            try:
                                value_x = float(entry_value_x.get())
                                decimal_no_second = True
                            except:
                                if entry_value_z.get() == "16" or entry_value_z.get() == "12":
                                    if "A" in str(entry_value_x.get()) or "B" in str(entry_value_x.get()) or "C" in str(
                                            entry_value_x.get()) or "D" in str(entry_value_x.get()) or "E" in str(
                                        entry_value_x.get()) or "F" in str(entry_value_x.get()) or "X" in str(
                                        entry_value_x.get()) or "V" in str(entry_value_x.get()):
                                        value_x = str(entry_value_x.get())
                                        decimal_no_second = True
                                        pass
                                    else:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_x.focus_force()
                                        return
                                else:
                                    messagebox.showerror("Error", "Invalid Value")
                                    nbase_calculate_window.wm_attributes("-topmost", 1)
                                    nbase_calculate_window.focus_force()
                                    nbase_calculate_window.wm_attributes("-topmost", 0)
                                    entry_value_x.focus_force()
                                    return
                        else:
                            for num in str(entry_value_x.get()):
                                try:
                                    if int(num) >= value_z:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_x.focus_force()
                                        return
                                except ValueError:
                                    pass
                            try:
                                value_x = int(entry_value_x.get())
                                decimal_no_second = False
                            except:
                                if entry_value_z.get() == "16" or entry_value_z.get() == "12":
                                    if "A" in str(entry_value_x.get()) or "B" in str(entry_value_x.get()) or "V" in str(
                                            entry_value_x.get()) or "C" in str(entry_value_x.get()) or "D" in str(
                                        entry_value_x.get()) or "E" in str(entry_value_x.get()) or "F" in str(
                                        entry_value_x.get()) or "X" in str(entry_value_x.get()):
                                        value_x = str(entry_value_x.get())
                                        decimal_no_second = False
                                        pass
                                    else:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_calculate_window.wm_attributes("-topmost", 1)
                                        nbase_calculate_window.focus_force()
                                        nbase_calculate_window.wm_attributes("-topmost", 0)
                                        entry_value_x.focus_force()
                                        return
                                else:
                                    messagebox.showerror("Error", "Invalid Value")
                                    nbase_calculate_window.wm_attributes("-topmost", 1)
                                    nbase_calculate_window.focus_force()
                                    nbase_calculate_window.wm_attributes("-topmost", 0)
                                    entry_value_x.focus_force()
                                    return
                        if str(entry_value_y.get()) in ["+", "-", "*", "/"]:
                            operator = str(entry_value_y.get())
                            pass
                        else:
                            messagebox.showerror("Error", "Invalid Operator")
                            nbase_calculate_window.wm_attributes("-topmost", 1)
                            nbase_calculate_window.focus_force()
                            nbase_calculate_window.wm_attributes("-topmost", 0)
                            entry_value_y.focus_force()
                            return
                        try:
                            if decimal_no_first:
                                value_w_1 = str(int(str(value_w)[0:str(value_w).find(".")]))
                                value_w_2 = str(float("0" + str(value_w)[str(value_w).find("."):]))
                                value_w_3 = str(int(str(value_w)[str(value_w).find(".") + 1:]))
                            else:
                                value_w_1 = str(int(str(value_w)))
                                value_w_2 = "0.0"
                                value_w_3 = "0"
                        except ValueError:
                            if decimal_no_first:
                                value_w_1 = str(str(value_w)[0:str(value_w).find(".")])
                                value_w_2 = str("0" + str(value_w)[str(value_w).find("."):])
                                value_w_3 = str(str(value_w)[str(value_w).find(".") + 1:])
                            else:
                                value_w_1 = str(value_w)
                                value_w_2 = "0.0"
                                value_w_3 = "0"
                        # to base_10
                        start_pow = len(value_w_1) - 1
                        answer_first = 0
                        num_id = 0
                        while start_pow >= 0:
                            if value_w_1[num_id] == "A":
                                answer_first += (10 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "B":
                                answer_first += (11 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "C":
                                answer_first += (12 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "D":
                                answer_first += (13 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "E":
                                answer_first += (14 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "F":
                                answer_first += (15 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "X":
                                answer_first += (10 * (pow(value_z, start_pow)))
                            elif value_w_1[num_id] == "V":
                                answer_first += (11 * (pow(value_z, start_pow)))
                            else:
                                answer_first += (int(value_w_1[num_id]) * (pow(value_z, start_pow)))
                            start_pow -= 1
                            num_id += 1
                        start_pow = -1
                        for num in value_w_3:
                            if num == "A":
                                answer_first += round((10 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "B":
                                answer_first += round((11 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "C":
                                answer_first += round((12 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "D":
                                answer_first += round((13 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "E":
                                answer_first += round((14 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "F":
                                answer_first += round((15 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "X":
                                answer_first += round((10 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "V":
                                answer_first += round((11 * (pow(value_z, start_pow))), approximate_val.get())
                            else:
                                answer_first += round((int(num) * (pow(value_z, start_pow))), approximate_val.get())
                            start_pow -= 1

                        try:
                            if decimal_no_second:
                                value_x_1 = str(int(str(value_x)[0:str(value_x).find(".")]))
                                value_x_2 = str(float("0" + str(value_x)[str(value_x).find("."):]))
                                value_x_3 = str(int(str(value_x)[str(value_x).find(".") + 1:]))
                            else:
                                value_x_1 = str(int(str(value_x)))
                                value_x_2 = "0.0"
                                value_x_3 = "0"
                        except ValueError:
                            if decimal_no_second:
                                value_x_1 = str(str(value_x)[0:str(value_x).find(".")])
                                value_x_2 = str("0" + str(value_x)[str(value_x).find("."):])
                                value_x_3 = str(str(value_x)[str(value_x).find(".") + 1:])
                            else:
                                value_x_1 = str(value_x)
                                value_x_2 = "0.0"
                                value_x_3 = "0"
                        # to base_10
                        start_pow = len(value_x_1) - 1
                        answer_second = 0
                        num_id = 0
                        while start_pow >= 0:
                            if value_x_1[num_id] == "A":
                                answer_second += (10 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "B":
                                answer_second += (11 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "C":
                                answer_second += (12 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "D":
                                answer_second += (13 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "E":
                                answer_second += (14 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "F":
                                answer_second += (15 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "X":
                                answer_second += (10 * (pow(value_z, start_pow)))
                            elif value_x_1[num_id] == "V":
                                answer_second += (11 * (pow(value_z, start_pow)))
                            else:
                                answer_second += (int(value_x_1[num_id]) * (pow(value_z, start_pow)))
                            start_pow -= 1
                            num_id += 1
                        start_pow = -1
                        for num in value_x_3:
                            if num == "A":
                                answer_second += round((10 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "B":
                                answer_second += round((11 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "C":
                                answer_second += round((12 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "D":
                                answer_second += round((13 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "E":
                                answer_second += round((14 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "F":
                                answer_second += round((15 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "X":
                                answer_second += round((10 * (pow(value_z, start_pow))), approximate_val.get())
                            elif num == "V":
                                answer_second += round((11 * (pow(value_z, start_pow))), approximate_val.get())
                            else:
                                answer_second += round((int(num) * (pow(value_z, start_pow))), approximate_val.get())
                            start_pow -= 1

                        if operator == "+":
                            answer = float(answer_first + answer_second)
                        elif operator == "-":
                            answer = float(answer_first - answer_second)
                        elif operator == "*":
                            answer = float(answer_first * answer_second)
                        elif operator == "/":
                            answer = float(answer_first / answer_second)
                        answer_val_1 = str(int(str(answer)[0:str(answer).find(".")]))
                        answer_val_2 = str(float("0" + str(answer)[str(answer).find("."):]))
                        answer_val_3 = str(int(str(answer)[str(answer).find(".") + 1:]))
                        answer_1 = ""
                        temp_answer_val = int(answer_val_1)
                        while temp_answer_val != 0:
                            modulo = temp_answer_val % value_z
                            temp_answer_val = int(temp_answer_val / value_z)
                            if value_z == 12:
                                if modulo == 10:
                                    modulo = "X"
                                elif modulo == 11:
                                    modulo = chr(0x039B)
                            elif value_z == 16:
                                if modulo == 10:
                                    modulo = "A"
                                elif modulo == 11:
                                    modulo = "B"
                                elif modulo == 12:
                                    modulo = "C"
                                elif modulo == 13:
                                    modulo = "D"
                                elif modulo == 14:
                                    modulo = "E"
                                elif modulo == 15:
                                    modulo = "F"
                            answer_1 += str(modulo)
                        if answer_1 == "":
                            answer_1 = "0"
                        answer_1 = answer_1[::-1]
                        temp_answer_val = float(answer_val_2)
                        answer_2 = "."
                        dp = 0
                        while dp < 4:
                            modulo = int(temp_answer_val * value_z)
                            if value_z == 12:
                                if modulo == 10:
                                    modulo = "X"
                                elif modulo == 11:
                                    modulo = chr(0x039B)
                            elif value_z == 16:
                                if modulo == 10:
                                    modulo = "A"
                                elif modulo == 11:
                                    modulo = "B"
                                elif modulo == 12:
                                    modulo = "C"
                                elif modulo == 13:
                                    modulo = "D"
                                elif modulo == 14:
                                    modulo = "E"
                                elif modulo == 15:
                                    modulo = "F"
                            answer_2 += str(modulo)
                            temp_answer_val *= value_z
                            temp_answer_val = float("0" + str(temp_answer_val)[str(temp_answer_val).find("."):])
                            dp += 1
                        answer = answer_1 + answer_2
                        answer = "(" + str(answer) + ")"
                        pow_solve = answer
                        try:
                            pow_solve = str(round(eval(pow_solve), approximate_val.get()))
                        except:
                            pass
                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                            label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            old_label_display_1_var.set(label_display_1_var)
                            label_display_2_var.set("")
                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                            old_label_display_1_var.set(label_display_1_var)
                        update_label_1()
                        nbase_calculate_window.destroy()
                        root.wm_attributes("-topmost", 1)
                        root.focus_force()
                        root.wm_attributes("-topmost", 0)

                def nbase_convert():
                    nbase_convert_width = 200
                    nbase_convert_height = 180
                    nbase_convert_window = Toplevel()
                    nbase_convert_window.geometry("{}x{}+{}+{}".format(nbase_convert_width, nbase_convert_height,
                                                                       int((
                                                                                   nbase_convert_window.winfo_screenwidth() - nbase_convert_width) / 2),
                                                                       int((
                                                                                   nbase_convert_window.winfo_screenheight() - nbase_convert_height) / 2)))
                    nbase_convert_window.configure(bg="#ECF3FB")
                    nbase_convert_window.resizable(0, 0)
                    nbase_convert_window.wm_attributes("-topmost", 1)
                    nbase_convert_window.focus_force()
                    nbase_convert_window.wm_attributes("-topmost", 0)
                    nbase_convert_window.title("Number Base")
                    nbase_convert_window.iconbitmap(os.path.join("data", "icon.ico"))
                    canvas_nbase_convert = Canvas(nbase_convert_window, width=nbase_convert_width,
                                                  height=nbase_convert_height)
                    canvas_nbase_convert.pack()
                    global image_nbase_convert
                    canvas_nbase_convert.create_image(100, 90, image=image_nbase_convert)
                    entry_value_x = Entry(canvas_nbase_convert, justify=CENTER, font=("Cambria", 9, "bold"))
                    entry_value_x.focus_force()
                    entry_value_y = Entry(canvas_nbase_convert, justify=CENTER, font=("Cambria", 9, "bold"))
                    entry_value_z = Entry(canvas_nbase_convert, justify=CENTER, font=("CordiaUPC", 11, "bold"))
                    canvas_nbase_convert.create_text(100, 10, fill="black", text="Press enter to continue",
                                                     font=("Segoe", 9, "bold"))
                    canvas_nbase_convert.create_text(100 - 30, 40, fill="black", text="Convert from Base..:",
                                                     font=("Segoe", 9, "bold"))
                    canvas_nbase_convert.create_text(100 - 30, 80, fill="black", text="Convert to Base..:",
                                                     font=("Segoe", 9, "bold"))
                    canvas_nbase_convert.create_text(100 - 40, 120, fill="black", text="Value:",
                                                     font=("Segoe", 9, "bold"))
                    canvas_nbase_convert.create_text(100, 150, fill="black",
                                                     text="Use key 'V' for the character '" + chr(
                                                         0x039B) + "' \nwhile converting from base 12",
                                                     font=("Segoe", 7, "bold"), justify=CENTER)
                    canvas_nbase_convert.create_window(100 + 60, 40, window=entry_value_x, width=40)
                    canvas_nbase_convert.create_window(100 + 60, 80, window=entry_value_y, width=40)
                    canvas_nbase_convert.create_window(100 + 40, 120, window=entry_value_z, width=80)

                    def nbase_convert_cont_bind(event):
                        continue_nbase_convert()

                    entry_value_x.bind("<Return>", nbase_convert_cont_bind)
                    entry_value_y.bind("<Return>", nbase_convert_cont_bind)
                    entry_value_z.bind("<Return>", nbase_convert_cont_bind)

                    def continue_nbase_convert():
                        if "." not in entry_value_x.get() and "." not in entry_value_y.get():
                            pass
                        else:
                            messagebox.showerror("Error", "Invalid bases value")
                            nbase_convert_window.wm_attributes("-topmost", 1)
                            nbase_convert_window.focus_force()
                            nbase_convert_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return
                        try:
                            value_x = int(entry_value_x.get())
                        except:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_convert_window.wm_attributes("-topmost", 1)
                            nbase_convert_window.focus_force()
                            nbase_convert_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return
                        try:
                            value_y = int(entry_value_y.get())
                        except:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_convert_window.wm_attributes("-topmost", 1)
                            nbase_convert_window.focus_force()
                            nbase_convert_window.wm_attributes("-topmost", 0)
                            entry_value_y.focus_force()
                            return
                        if (value_x >= 2 and value_x <= 10) or value_x == 12 or value_x == 16:
                            pass
                        else:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_convert_window.wm_attributes("-topmost", 1)
                            nbase_convert_window.focus_force()
                            nbase_convert_window.wm_attributes("-topmost", 0)
                            entry_value_x.focus_force()
                            return
                        if (value_y >= 2 and value_y <= 10) or value_y == 12 or value_y == 16:
                            pass
                        else:
                            messagebox.showerror("Error", "Invalid base value")
                            nbase_convert_window.wm_attributes("-topmost", 1)
                            nbase_convert_window.focus_force()
                            nbase_convert_window.wm_attributes("-topmost", 0)
                            entry_value_y.focus_force()
                            return
                        if "-" in str(entry_value_z.get()) or "+" in str(entry_value_z.get()) or "*" in str(
                                entry_value_z.get()) or "/" in str(entry_value_z.get()):
                            messagebox.showerror("Error", "Invalid Value")
                            nbase_convert_window.wm_attributes("-topmost", 1)
                            nbase_convert_window.focus_force()
                            nbase_convert_window.wm_attributes("-topmost", 0)
                            entry_value_z.focus_force()
                            return
                        if "." in str(entry_value_z.get()):
                            for num in str(entry_value_z.get())[0:str(entry_value_z.get()).find(".")]:
                                try:
                                    if int(num) >= value_x:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_convert_window.wm_attributes("-topmost", 1)
                                        nbase_convert_window.focus_force()
                                        nbase_convert_window.wm_attributes("-topmost", 0)
                                        entry_value_z.focus_force()
                                        return
                                except ValueError:
                                    pass
                            for num in str(entry_value_z.get())[str(entry_value_z.get()).find(".") + 1:]:
                                try:
                                    if int(num) >= value_x:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_convert_window.wm_attributes("-topmost", 1)
                                        nbase_convert_window.focus_force()
                                        nbase_convert_window.wm_attributes("-topmost", 0)
                                        entry_value_z.focus_force()
                                        return
                                except ValueError:
                                    pass

                            try:
                                value_z = float(entry_value_z.get())
                                decimal_no = True
                            except:
                                if value_x == 16 or value_x == 12:
                                    if "A" in str(entry_value_z.get()) or "B" in str(entry_value_z.get()) or "C" in str(
                                            entry_value_z.get()) or "D" in str(entry_value_z.get()) or "E" in str(
                                        entry_value_z.get()) or "F" in str(entry_value_z.get()) or "X" in str(
                                        entry_value_z.get()) or "V" in str(entry_value_z.get()):
                                        value_z = str(entry_value_z.get())
                                        decimal_no = True
                                        pass
                                    else:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_convert_window.wm_attributes("-topmost", 1)
                                        nbase_convert_window.focus_force()
                                        nbase_convert_window.wm_attributes("-topmost", 0)
                                        entry_value_z.focus_force()
                                        return
                                else:
                                    messagebox.showerror("Error", "Invalid Value")
                                    nbase_convert_window.wm_attributes("-topmost", 1)
                                    nbase_convert_window.focus_force()
                                    nbase_convert_window.wm_attributes("-topmost", 0)
                                    entry_value_z.focus_force()
                                    return
                        else:
                            for num in str(entry_value_z.get()):
                                try:
                                    if int(num) >= value_x:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_convert_window.wm_attributes("-topmost", 1)
                                        nbase_convert_window.focus_force()
                                        nbase_convert_window.wm_attributes("-topmost", 0)
                                        entry_value_z.focus_force()
                                        return
                                except ValueError:
                                    pass
                            try:
                                value_z = int(entry_value_z.get())
                                decimal_no = False
                            except:
                                if value_x == 16 or value_x == 12:
                                    if "A" in str(entry_value_z.get()) or "B" in str(entry_value_z.get()) or "V" in str(
                                            entry_value_z.get()) or "C" in str(entry_value_z.get()) or "D" in str(
                                        entry_value_z.get()) or "E" in str(entry_value_z.get()) or "F" in str(
                                        entry_value_z.get()) or "X" in str(entry_value_z.get()):
                                        value_z = str(entry_value_z.get())
                                        decimal_no = False
                                        pass
                                    else:
                                        messagebox.showerror("Error", "Invalid Value")
                                        nbase_convert_window.wm_attributes("-topmost", 1)
                                        nbase_convert_window.focus_force()
                                        nbase_convert_window.wm_attributes("-topmost", 0)
                                        entry_value_z.focus_force()
                                        return
                                else:
                                    messagebox.showerror("Error", "Invalid Value")
                                    nbase_convert_window.wm_attributes("-topmost", 1)
                                    nbase_convert_window.focus_force()
                                    nbase_convert_window.wm_attributes("-topmost", 0)
                                    entry_value_z.focus_force()
                                    return
                        if decimal_no:
                            try:
                                value_z_1 = str(int(str(value_z)[0:str(value_z).find(".")]))
                                value_z_2 = str(float("0" + str(value_z)[str(value_z).find("."):]))
                                value_z_3 = str(int(str(value_z)[str(value_z).find(".") + 1:]))
                            except ValueError:
                                value_z_1 = str(str(value_z)[0:str(value_z).find(".")])
                                value_z_2 = str("0" + str(value_z)[str(value_z).find("."):])
                                value_z_3 = str(str(value_z)[str(value_z).find(".") + 1:])
                            # to base_10
                            start_pow = len(value_z_1) - 1
                            answer = 0
                            num_id = 0
                            while start_pow >= 0:
                                if value_z_1[num_id] == "A":
                                    answer += (10 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "B":
                                    answer += (11 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "C":
                                    answer += (12 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "D":
                                    answer += (13 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "E":
                                    answer += (14 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "F":
                                    answer += (15 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "X":
                                    answer += (10 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "V":
                                    answer += (11 * (pow(value_x, start_pow)))
                                else:
                                    answer += (int(value_z_1[num_id]) * (pow(value_x, start_pow)))
                                start_pow -= 1
                                num_id += 1
                            start_pow = -1
                            for num in value_z_3:
                                if num == "A":
                                    answer += round((10 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "B":
                                    answer += round((11 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "C":
                                    answer += round((12 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "D":
                                    answer += round((13 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "E":
                                    answer += round((14 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "F":
                                    answer += round((15 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "X":
                                    answer += round((10 * (pow(value_x, start_pow))), approximate_val.get())
                                elif num == "V":
                                    answer += round((11 * (pow(value_x, start_pow))), approximate_val.get())
                                else:
                                    answer += round((int(num) * (pow(value_x, start_pow))), approximate_val.get())
                                start_pow -= 1
                            if value_y != 10:
                                value_z_1 = str(int(str(answer)[0:str(answer).find(".")]))
                                value_z_2 = str(float("0" + str(answer)[str(answer).find("."):]))
                                value_z_3 = str(int(str(answer)[str(answer).find(".") + 1:]))
                                answer_1 = ""
                                temp_value_z = int(value_z_1)
                                while temp_value_z != 0:
                                    modulo = temp_value_z % value_y
                                    temp_value_z = int(temp_value_z / value_y)
                                    if value_y == 12:
                                        if modulo == 10:
                                            modulo = "X"
                                        elif modulo == 11:
                                            modulo = chr(0x039B)
                                    elif value_y == 16:
                                        if modulo == 10:
                                            modulo = "A"
                                        elif modulo == 11:
                                            modulo = "B"
                                        elif modulo == 12:
                                            modulo = "C"
                                        elif modulo == 13:
                                            modulo = "D"
                                        elif modulo == 14:
                                            modulo = "E"
                                        elif modulo == 15:
                                            modulo = "F"
                                    answer_1 += str(modulo)
                                if answer_1 == "":
                                    answer_1 = "0"
                                answer_1 = answer_1[::-1]
                                temp_value_z = float(value_z_2)
                                answer_2 = "."
                                dp = 0
                                while dp < 4:
                                    modulo = int(temp_value_z * value_y)
                                    if value_y == 12:
                                        if modulo == 10:
                                            modulo = "X"
                                        elif modulo == 11:
                                            modulo = chr(0x039B)
                                    elif value_y == 16:
                                        if modulo == 10:
                                            modulo = "A"
                                        elif modulo == 11:
                                            modulo = "B"
                                        elif modulo == 12:
                                            modulo = "C"
                                        elif modulo == 13:
                                            modulo = "D"
                                        elif modulo == 14:
                                            modulo = "E"
                                        elif modulo == 15:
                                            modulo = "F"
                                    answer_2 += str(modulo)
                                    temp_value_z *= value_y
                                    temp_value_z = float("0" + str(temp_value_z)[str(temp_value_z).find("."):])
                                    dp += 1
                                answer = answer_1 + answer_2
                            else:
                                pass
                            answer = "(" + str(answer) + ")"
                        else:
                            try:
                                value_z_1 = str(int(value_z))
                            except ValueError:
                                value_z_1 = str(value_z)
                            # to base_10
                            start_pow = len(value_z_1) - 1
                            answer = 0
                            num_id = 0
                            while start_pow >= 0:
                                if value_z_1[num_id] == "A":
                                    answer += (10 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "B":
                                    answer += (11 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "C":
                                    answer += (12 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "D":
                                    answer += (13 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "E":
                                    answer += (14 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "F":
                                    answer += (15 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "X":
                                    answer += (10 * (pow(value_x, start_pow)))
                                elif value_z_1[num_id] == "V":
                                    answer += (11 * (pow(value_x, start_pow)))
                                else:
                                    answer += (int(value_z_1[num_id]) * (pow(value_x, start_pow)))
                                start_pow -= 1
                                num_id += 1
                            start_pow = -1
                            if value_y != 10:
                                value_z_1 = str(int(answer))
                                answer_1 = ""
                                temp_value_z = int(value_z_1)
                                while temp_value_z != 0:
                                    modulo = temp_value_z % value_y
                                    temp_value_z = int(temp_value_z / value_y)
                                    if value_y == 12:
                                        if modulo == 10:
                                            modulo = "X"
                                        elif modulo == 11:
                                            modulo = chr(0x039B)
                                    elif value_y == 16:
                                        if modulo == 10:
                                            modulo = "A"
                                        elif modulo == 11:
                                            modulo = "B"
                                        elif modulo == 12:
                                            modulo = "C"
                                        elif modulo == 13:
                                            modulo = "D"
                                        elif modulo == 14:
                                            modulo = "E"
                                        elif modulo == 15:
                                            modulo = "F"
                                    answer_1 += str(modulo)
                                if answer_1 == "":
                                    answer_1 = "0"
                                answer_1 = answer_1[::-1]
                                answer = answer_1
                            else:
                                pass
                            answer = "(" + str(answer) + ")"
                        pow_solve = answer
                        try:
                            pow_solve = str(round(eval(pow_solve), approximate_val.get()))
                        except:
                            pass
                        if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                            label_display_1_var.set(str(pow_solve))
                        elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                            label_display_1_var.set(label_display_1_var.get() + str(pow_solve))
                        elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                        elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                            label_display_1_var.set(str(pow_solve))
                            label_display_2_var.set("")
                        old_label_display_1_var.set(label_display_1_var.get())
                        update_label_1()
                        nbase_convert_window.destroy()
                        root.wm_attributes("-topmost", 1)
                        root.focus_force()
                        root.wm_attributes("-topmost", 0)

            elif input == "expo":
                expo_width = 200
                expo_height = 60
                expo_window = Toplevel()
                expo_window.geometry("{}x{}+{}+{}".format(expo_width, expo_height,
                                                          int((expo_window.winfo_screenwidth() - expo_width) / 2),
                                                          int((expo_window.winfo_screenheight() - expo_height) / 2)))
                expo_window.configure(bg="#ECF3FB")
                expo_window.resizable(0, 0)
                expo_window.wm_attributes("-topmost", 1)
                expo_window.focus_force()
                expo_window.wm_attributes("-topmost", 0)
                expo_window.title("Exponential")
                expo_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_expo = Canvas(expo_window, width=expo_width, height=expo_height, bg="#ECF3FB")
                canvas_expo.pack()
                canvas_expo.create_image(100, 30, image=image_factorial)
                canvas_expo.create_text(100, 10,
                                        text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_expo.create_text(100 - 20, 40, text="n", font=("Segoe", 11, "bold"))
                entry_value_x = Entry(canvas_expo, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                canvas_expo.create_window(100 + 20, 40, window=entry_value_x, width=40)

                def expo_cont_bind(event):
                    continue_expo()

                entry_value_x.bind("<Return>", expo_cont_bind)

                def continue_expo():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid n value")
                        expo_window.wm_attributes("-topmost", 1)
                        expo_window.focus_force()
                        expo_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        pow_solve = pow(e, value_x)
                        try:
                            pow_solve = round(pow_solve, approximate_val.get())
                        except:
                            pass
                    except:
                        messagebox.showerror("Error", "Invalid n value")
                        expo_window.wm_attributes("-topmost", 1)
                        expo_window.focus_force()
                        expo_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    expo_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)

            elif input == "nlog":
                nlog_width = 200
                nlog_height = 60
                nlog_window = Toplevel()
                nlog_window.geometry("{}x{}+{}+{}".format(nlog_width, nlog_height,
                                                          int((nlog_window.winfo_screenwidth() - nlog_width) / 2),
                                                          int((nlog_window.winfo_screenheight() - nlog_height) / 2)))
                nlog_window.configure(bg="#ECF3FB")
                nlog_window.resizable(0, 0)
                nlog_window.wm_attributes("-topmost", 1)
                nlog_window.focus_force()
                nlog_window.wm_attributes("-topmost", 0)
                nlog_window.title("Natural Log")
                nlog_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_nlog = Canvas(nlog_window, width=nlog_width, height=nlog_height, bg="#ECF3FB")
                canvas_nlog.pack()

                canvas_nlog.create_image(100, 30, image=image_factorial)
                canvas_nlog.create_text(100, 10,
                                        text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_nlog.create_text(100 - 20, 40, text="x", font=("Segoe", 11, "bold"))
                entry_value_x = Entry(canvas_nlog, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                canvas_nlog.create_window(100 + 20, 40, window=entry_value_x, width=40)

                def nlog_cont_bind(event):
                    continue_nlog()

                entry_value_x.bind("<Return>", nlog_cont_bind)

                def continue_nlog():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        nlog_window.wm_attributes("-topmost", 1)
                        nlog_window.focus_force()
                        nlog_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        pow_solve = log(value_x, e)
                        try:
                            pow_solve = str(round(pow_solve, approximate_val.get()))
                        except:
                            pass
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        nlog_window.wm_attributes("-topmost", 1)
                        nlog_window.focus_force()
                        nlog_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    nlog_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)

            elif input == "log_a_base_b":
                log_a_base_b_width = 200
                log_a_base_b_height = 120
                log_a_base_b_window = Toplevel()
                log_a_base_b_window.geometry("{}x{}+{}+{}".format(log_a_base_b_width, log_a_base_b_height,
                                                                  int((
                                                                              log_a_base_b_window.winfo_screenwidth() - log_a_base_b_width) / 2),
                                                                  int((
                                                                              log_a_base_b_window.winfo_screenheight() - log_a_base_b_height) / 2)))
                log_a_base_b_window.configure(bg="#ECF3FB")
                log_a_base_b_window.resizable(0, 0)
                log_a_base_b_window.wm_attributes("-topmost", 1)
                log_a_base_b_window.focus_force()
                log_a_base_b_window.wm_attributes("-topmost", 0)
                log_a_base_b_window.title("Logarithm")
                log_a_base_b_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_log_a_base_b = Canvas(log_a_base_b_window, width=log_a_base_b_width, height=log_a_base_b_height,
                                             bg="#ECF3FB")
                canvas_log_a_base_b.pack()

                canvas_log_a_base_b.create_image(100, 60, image=image_modulo)
                canvas_log_a_base_b.create_text(100, 10,
                                                text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_log_a_base_b.create_text(100 - 20, 40, text="n", font=("Segoe", 11, "bold"))
                canvas_log_a_base_b.create_text(100 - 20, 80, text="x", font=("Segoe", 11, "bold"))
                entry_value_x = Entry(canvas_log_a_base_b, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_log_a_base_b, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_log_a_base_b.create_window(100 + 20, 40, window=entry_value_x, width=40)
                canvas_log_a_base_b.create_window(100 + 20, 80, window=entry_value_y, width=40)

                def log_a_base_b_cont_bind(event):
                    continue_log_a_base_b()

                entry_value_x.bind("<Return>", log_a_base_b_cont_bind)
                entry_value_y.bind("<Return>", log_a_base_b_cont_bind)

                def continue_log_a_base_b():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid n value")
                        log_a_base_b_window.wm_attributes("-topmost", 1)
                        log_a_base_b_window.focus_force()
                        log_a_base_b_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = float(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        log_a_base_b_window.wm_attributes("-topmost", 1)
                        log_a_base_b_window.focus_force()
                        log_a_base_b_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    pow_solve = log(value_y, value_x)
                    try:
                        pow_solve = str(round(pow_solve, approximate_val.get()))
                    except:
                        pass
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    log_a_base_b_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)


            elif input == "log_b_10":
                log_b_10_width = 200
                log_b_10_height = 60
                log_b_10_window = Toplevel()
                log_b_10_window.geometry("{}x{}+{}+{}".format(log_b_10_width, log_b_10_height,
                                                              int((
                                                                          log_b_10_window.winfo_screenwidth() - log_b_10_width) / 2),
                                                              int((
                                                                          log_b_10_window.winfo_screenheight() - log_b_10_height) / 2)))
                log_b_10_window.configure(bg="#ECF3FB")
                log_b_10_window.resizable(0, 0)
                log_b_10_window.wm_attributes("-topmost", 1)
                log_b_10_window.focus_force()
                log_b_10_window.wm_attributes("-topmost", 0)
                log_b_10_window.title("Logarithm")
                log_b_10_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_log_b_10 = Canvas(log_b_10_window, width=log_b_10_width, height=log_b_10_height, bg="#ECF3FB")
                canvas_log_b_10.pack()
                canvas_log_b_10.create_image(100, 30, image=image_factorial)

                canvas_log_b_10.create_text(100, 10,
                                            text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_log_b_10.create_text(100 - 20, 40, text="x", font=("Segoe", 11, "bold"))
                entry_value_x = Entry(canvas_log_b_10, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                canvas_log_b_10.create_window(100 + 20, 40, window=entry_value_x, width=40)

                def log_b_10_cont_bind(event):
                    continue_log_b_10()

                entry_value_x.bind("<Return>", log_b_10_cont_bind)

                def continue_log_b_10():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        log_b_10_window.wm_attributes("-topmost", 1)
                        log_b_10_window.focus_force()
                        log_b_10_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        pow_solve = log10(value_x)
                        try:
                            pow_solve = str(round(pow_solve, approximate_val.get()))
                        except:
                            pass
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        log_b_10_window.wm_attributes("-topmost", 1)
                        log_b_10_window.focus_force()
                        log_b_10_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    log_b_10_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)

            elif input == "!":
                factorial_width = 200
                factorial_height = 60
                factorial_window = Toplevel()
                factorial_window.geometry("{}x{}+{}+{}".format(factorial_width, factorial_height,
                                                               int((
                                                                           factorial_window.winfo_screenwidth() - factorial_width) / 2),
                                                               int((
                                                                           factorial_window.winfo_screenheight() - factorial_height) / 2)))
                factorial_window.configure(bg="#ECF3FB")
                factorial_window.resizable(0, 0)
                factorial_window.wm_attributes("-topmost", 1)
                factorial_window.focus_force()
                factorial_window.wm_attributes("-topmost", 0)
                factorial_window.title("Factorial")
                factorial_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_factorial = Canvas(factorial_window, width=factorial_width, height=factorial_height,
                                          bg="#ECF3FB")
                canvas_factorial.pack()
                canvas_factorial.create_image(100, 30, image=image_factorial)
                entry_value_x = Entry(canvas_factorial, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                canvas_factorial.create_text(100, 10,
                                             text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_factorial.create_text(100 - 20, 40, text="x", font=("Segoe", 11, "bold"))
                canvas_factorial.create_window(100 + 20, 40, window=entry_value_x, width=40)

                def factorial_cont_bind(event):
                    continue_factorial()

                entry_value_x.bind("<Return>", factorial_cont_bind)

                def continue_factorial():
                    if "." in str(entry_value_x.get()):
                        messagebox.showerror("Error", "Invalid x value")
                        factorial_window.wm_attributes("-topmost", 1)
                        factorial_window.focus_force()
                        factorial_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_x = int(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        factorial_window.wm_attributes("-topmost", 1)
                        factorial_window.focus_force()
                        factorial_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        pow_solve = factorial(value_x)
                        try:
                            pow_solve = str(round(pow_solve, approximate_val.get()))
                        except:
                            pass
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        factorial_window.wm_attributes("-topmost", 1)
                        factorial_window.focus_force()
                        factorial_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    factorial_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)

            elif input == "root":
                root_2_width = 200
                root_2_height = 120
                root_2_window = Toplevel()
                root_2_window.geometry("{}x{}+{}+{}".format(root_2_width, root_2_height,
                                                            int((root_2_window.winfo_screenwidth() - root_2_width) / 2),
                                                            int((
                                                                        root_2_window.winfo_screenheight() - root_2_height) / 2)))
                root_2_window.configure(bg="#ECF3FB")
                root_2_window.resizable(0, 0)
                root_2_window.wm_attributes("-topmost", 1)
                root_2_window.focus_force()
                root_2_window.wm_attributes("-topmost", 0)
                root_2_window.title("Root")
                root_2_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_root_2 = Canvas(root_2_window, width=root_2_width, height=root_2_height, bg="#ECF3FB")
                canvas_root_2.pack()
                canvas_root_2.create_image(100, 60, image=image_modulo)
                canvas_root_2.create_text(100, 10,
                                          text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_root_2.create_text(100 - 20, 40, text="n", font=("Segoe", 11, "bold"))
                canvas_root_2.create_text(100 - 20, 80, text="y", font=("Segoe", 11, "bold"))
                entry_value_x = Entry(canvas_root_2, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_root_2, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_root_2.create_window(100 + 20, 40, window=entry_value_x, width=40)
                canvas_root_2.create_window(100 + 20, 80, window=entry_value_y, width=40)

                def root_2_cont_bind(event):
                    continue_root_2()

                entry_value_x.bind("<Return>", root_2_cont_bind)
                entry_value_y.bind("<Return>", root_2_cont_bind)

                def continue_root_2():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid n value")
                        root_2_window.wm_attributes("-topmost", 1)
                        root_2_window.focus_force()
                        root_2_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = float(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        root_2_window.wm_attributes("-topmost", 1)
                        root_2_window.focus_force()
                        root_2_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    pow_solve = pow(value_y, pow(value_x, -1.0))
                    try:
                        pow_solve = str(round(pow_solve, approximate_val.get()))
                    except:
                        pass
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    root_2_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)


            elif input == "power" or input == "^":
                power_width = 200
                power_height = 120
                power_window = Toplevel()
                power_window.geometry("{}x{}+{}+{}".format(power_width, power_height,
                                                           int((power_window.winfo_screenwidth() - power_width) / 2),
                                                           int((power_window.winfo_screenheight() - power_height) / 2)))
                power_window.configure(bg="#ECF3FB")
                power_window.resizable(0, 0)
                power_window.wm_attributes("-topmost", 1)
                power_window.focus_force()
                power_window.wm_attributes("-topmost", 0)
                power_window.title("Power")
                power_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_power = Canvas(power_window, width=power_width, height=power_height, bg="#ECF3FB")
                canvas_power.pack()
                canvas_power.create_image(100, 60, image=image_modulo)
                entry_value_x = Entry(canvas_power, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_power, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_power.create_text(100, 10,
                                         text="Press Enter to Continue", font=("Segoe", 9, "bold"))
                canvas_power.create_text(100 - 20, 40, text="x", font=("Segoe", 11, "bold"))
                canvas_power.create_text(100 - 20, 80, text="y", font=("Segoe", 11, "bold"))
                canvas_power.create_window(100 + 20, 40, window=entry_value_x, width=40)
                canvas_power.create_window(100 + 20, 80, window=entry_value_y, width=40)

                def power_cont_bind(event):
                    continue_power()

                entry_value_x.bind("<Return>", power_cont_bind)
                entry_value_y.bind("<Return>", power_cont_bind)

                def continue_power():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        power_window.wm_attributes("-topmost", 1)
                        power_window.focus_force()
                        power_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = float(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid y value")
                        power_window.wm_attributes("-topmost", 1)
                        power_window.focus_force()
                        power_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    pow_solve = pow(value_x, value_y)
                    try:
                        pow_solve = str(round(pow_solve, approximate_val.get()))
                    except:
                        pass
                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    power_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)






            elif input == "mod" or input == "%":
                mod_width = 200
                mod_height = 120
                mod_window = Toplevel()
                mod_window.geometry("{}x{}+{}+{}".format(mod_width, mod_height,
                                                         int((mod_window.winfo_screenwidth() - mod_width) / 2),
                                                         int((mod_window.winfo_screenheight() - mod_height) / 2)))
                mod_window.configure(bg="#ECF3FB")
                mod_window.resizable(0, 0)
                mod_window.wm_attributes("-topmost", 1)
                mod_window.focus_force()
                mod_window.wm_attributes("-topmost", 0)
                mod_window.title("Modulo")
                mod_window.iconbitmap(os.path.join("data", "icon.ico"))
                canvas_mod = Canvas(mod_window, width=mod_width, height=mod_height, bg="#ECF3FB")
                canvas_mod.pack()
                canvas_mod.create_image(100, 60, image=image_modulo)
                entry_value_x = Entry(canvas_mod, justify=CENTER, font=("Cambria", 9, "bold"))
                entry_value_x.focus_force()
                entry_value_y = Entry(canvas_mod, justify=CENTER, font=("Cambria", 9, "bold"))
                canvas_mod.create_text(100, 10, text="Press enter to continue", font=("Segoe", 9, "bold"),
                                       fill="black")
                canvas_mod.create_window(100 - 20, 40, window=Label(canvas_mod, text="x", bg="black", fg="white",
                                                                    font=("Segoe", 11, "bold")), width=20,
                                         height=20)
                canvas_mod.create_window(100 - 20, 80, window=Label(canvas_mod, text="y", bg="black", fg="white",
                                                                    font=("Segoe", 11, "bold")), width=20,
                                         height=20)
                canvas_mod.create_window(100 + 20, 40, window=entry_value_x, width=40)
                canvas_mod.create_window(100 + 20, 80, window=entry_value_y, width=40)

                def mod_cont_bind(event):
                    continue_mod()

                entry_value_x.bind("<Return>", mod_cont_bind)
                entry_value_y.bind("<Return>", mod_cont_bind)

                def continue_mod():
                    try:
                        value_x = float(entry_value_x.get())
                    except:
                        messagebox.showerror("Error", "Invalid x value")
                        mod_window.wm_attributes("-topmost", 1)
                        mod_window.focus_force()
                        mod_window.wm_attributes("-topmost", 0)
                        entry_value_x.focus_force()
                        return
                    try:
                        value_y = float(entry_value_y.get())
                    except:
                        messagebox.showerror("Error", "Invalid y value")
                        mod_window.wm_attributes("-topmost", 1)
                        mod_window.focus_force()
                        mod_window.wm_attributes("-topmost", 0)
                        entry_value_y.focus_force()
                        return
                    pow_solve = str(round(value_x % value_y, approximate_val.get()))

                    if label_display_2_var.get() == "" and label_display_1_var.get() == "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() == "":
                        label_display_1_var.set(label_display_1_var.get() + "(" + str(pow_solve) + ")")
                    elif label_display_1_var.get() != "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    elif label_display_1_var.get == "" and label_display_2_var.get() != "":
                        label_display_1_var.set("(" + str(pow_solve) + ")")
                        label_display_2_var.set("")
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                    mod_window.destroy()
                    root.wm_attributes("-topmost", 1)
                    root.focus_force()
                    root.wm_attributes("-topmost", 0)




            elif input == "close":
                root.destroy()
                exit()
            elif input == "delete":
                if label_display_2_var.get() == "" and label_display_1_var.get() != "":
                    label_display_1_var.set(label_display_1_var.get()[0:len(label_display_1_var.get()) - 1])
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()

            elif input == "round":
                if label_display_2_var.get() != "" and "." in label_display_2_var.get():
                    round_width = 400
                    round_height = 80
                    round_window = Toplevel()
                    round_window.geometry("{}x{}+{}+{}".format(round_width, round_height,
                                                               int((
                                                                           round_window.winfo_screenwidth() - round_width) / 2),
                                                               int((
                                                                           round_window.winfo_screenheight() - round_height) / 2)))
                    round_window.configure(bg="#ECF3FB")
                    round_window.resizable(0, 0)
                    round_window.wm_attributes("-topmost", 1)
                    round_window.focus_force()
                    round_window.wm_attributes("-topmost", 0)
                    round_window.title("Round")
                    round_window.iconbitmap(os.path.join("data", "icon.ico"))
                    canvas_round = Canvas(round_window, width=round_width, height=round_height)
                    canvas_round.pack()
                    global image_chav
                    canvas_round.create_image(200, 40, image=image_chav)
                    entry_value = Entry(canvas_round, justify=CENTER, font=("Cambria", 9, "bold"))
                    canvas_round.create_text(200, 20, justify=CENTER,
                                             text="Enter the decimal places you want to round it up to, Enter '0' for whole no.\n Max=4, Min=0, Press enter to continue",
                                             font=("Segoe", 7, "bold"))
                    canvas_round.create_window(200, 60, window=entry_value, width=40)

                    def con_rnd(event):
                        continue_round()

                    entry_value.bind("<Return>", con_rnd)

                    def continue_round():
                        try:
                            value = int(entry_value.get())
                            if value <= 4 and value >= 0:
                                try:
                                    answer = float(label_display_2_var.get())
                                    if value != 0:
                                        answer = round(answer, value)
                                    else:
                                        answer = round(answer, None)
                                    label_display_2_var.set(str(answer))
                                    update_label_1()
                                    round_window.destroy()
                                    root.wm_attributes("-topmost", 1)
                                    root.focus_force()
                                    root.wm_attributes("-topmost", 0)
                                except:
                                    label_display_2_var.set("Math Error")
                                    update_label_1()
                                    round_window.destroy()
                                    root.wm_attributes("-topmost", 1)
                                    root.focus_force()
                                    root.wm_attributes("-topmost", 0)
                            else:
                                messagebox.showerror("Error", "Invalid Value")
                                round_window.wm_attributes("-topmost", 1)
                                round_window.focus_force()
                                round_window.wm_attributes("-topmost", 0)
                        except:
                            messagebox.showerror("Error", "Invalid Value")
                            round_window.wm_attributes("-topmost", 1)
                            round_window.focus_force()
                            round_window.wm_attributes("-topmost", 0)

                else:
                    label_display_2_var.set(label_display_2_var.get())
                    update_label_1()


            elif input == "solve":

                try:
                    answer = eval(label_display_1_var.get())
                    label_display_2_var.set(str(round(answer, approximate_val.get())))
                    update_label_1()
                except:
                    temp_in = StringVar()
                    temp_in.set(label_display_1_var.get())

                    def check():
                        check_broke = False
                        text_id = 0
                        for data in temp_in.get():
                            if text_id != len(temp_in.get()) - 1:
                                if data == ")":
                                    op_list = ["+", "-", "/", "*", ")"]
                                    if temp_in.get()[text_id + 1] in op_list:
                                        pass
                                    else:
                                        temp_in_1 = temp_in.get()[0:text_id + 1]
                                        temp_in_2 = temp_in.get()[text_id + 1:]
                                        temp_in_1 += "*"
                                        temp_in.set(temp_in_1 + temp_in_2)
                                        check_broke = True
                                        break
                            if text_id > 0:
                                if data == "(":
                                    op_list = ["+", "-", "/", "*", "("]
                                    if temp_in.get()[text_id - 1] in op_list:
                                        pass
                                    else:
                                        temp_in_1 = temp_in.get()[0:text_id]
                                        temp_in_2 = temp_in.get()[text_id:]
                                        temp_in_1 += "*"
                                        temp_in.set(temp_in_1 + temp_in_2)
                                        check_broke = True
                                        break
                            else:
                                pass
                            text_id += 1
                        if check_broke:
                            check()
                        else:
                            try:
                                answer = eval(temp_in.get())
                                label_display_2_var.set(str(round(answer, approximate_val.get())))
                                update_label_1()
                            except:
                                if chr(0x03C0) in temp_in.get():
                                    try:
                                        print(temp_in.get())
                                        temp_in.set(temp_in.get().replace(chr(0x03C0), str(pi)))
                                        answer = eval(temp_in.get())
                                        label_display_2_var.set(str(round(answer, approximate_val.get())))
                                        update_label_1()
                                    except:
                                        print(temp_in.get())
                                        label_display_2_var.set("Math Error")
                                        update_label_1()
                                else:
                                    print(temp_in.get())
                                    label_display_2_var.set("Math Error")
                                    update_label_1()

                    check()
            elif input == "replay":
                label_display_1_var.set(old_label_display_1_var.get())
                label_display_2_var.set("")
                update_label_1()
            elif input == "+" or input == "-" or input == "*" or input == "/":
                if label_display_2_var.get() == "":
                    label_display_1_var.set(label_display_1_var.get() + input)
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                else:
                    if "error" in label_display_2_var.get().lower():
                        label_display_1_var.set(label_display_1_var.get() + input)
                        label_display_2_var.set("")
                        old_label_display_1_var.set(label_display_1_var.get())
                        update_label_1()
                    else:
                        label_display_1_var.set(label_display_2_var.get() + input)
                        label_display_2_var.set("")
                        old_label_display_1_var.set(label_display_1_var.get())
                        update_label_1()
            else:
                if label_display_2_var.get() == "":
                    label_display_1_var.set(label_display_1_var.get() + input)
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()
                else:
                    label_display_2_var.set("")
                    label_display_1_var.set("")
                    label_display_1_var.set(label_display_1_var.get() + input)
                    old_label_display_1_var.set(label_display_1_var.get())
                    update_label_1()


Main()

root.mainloop()

