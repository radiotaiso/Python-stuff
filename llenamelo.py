#/bin/python

#  llenamelo --config
# llenamelo --tablita actividades
# llenamelo --tablita proyecto
# llenamelo --
# llenamelo --actividades
#SAVING FOR LATER https://atom.io/packages/atom-pair
VOY
from optparse import OptionParser


class NoNovaOptsParser(OptionParser):
    def __init__(self):#arre, abajo puse nuestro debraye de como sería el flow un poco más acomodado, como pseudo code line 70
        usage = "usage %prog [OPTIONS]"
        self.add_option("-c" "--la-conf", dest="config",
                  help="Set config file with user:pass")
        self.add_option("-A", "--de-actividades",
                  help="Print the activity options with ID")
        self.add_option("-P", "--de-proyectos",
                  help="Print your personal project options with ID, This requires CONF FILE ")

Atom tendrá esto?
Live xtreme programming verga,
WAIT. LO ENCONTRÉ!
jajaja
te lo escribi en
skype


def config():
    leyendo de este pedo, aqui ando


def test()



    todo el modulo pero, con debug mietnras lo estoy haciendo

def main()





    llamas funciones
    haces objetos

if __name__ == "__main__":






 llenamelo --config

 user
 pass
 Default Project:
 Default Activity:
Duracion [obligatorio]:

FLOW DEMBOW PARA LLENAR ACTIVIDADES:

user [default]:
project [default]:
activity [default]:
time?
Another? Y/n
Change something on next activity? Y/n
(add N number of activities)

Cambiar algo? y/N
if respuesta == y:
1
Proyecto / Actividad / Tiempo / Texto
2
Proyecto / Actividad / Tiempo / Texto
N
Proyecto / Actividad / Tiempo / Texto

    Which one? 1,2,3? 1

    prompt>
        login? y/N
        project?
        Activity
        Duracion?

Cambiar algo? y/N
if respuesta ==N:
Submitting o k ase

!!!error handling
Success, id1 id2 id3
O fail por que te la pelas










#REFERENCIAS AL NOVA CLI DE GOLANG

# nova-cli  /u ucoria@itexico.net /p itexico1 add /P 33 /t 8 /c 14 Training with Antonio

# /P Projects------------------------------------------
# ID      Name
# 6       iTexico MX Delivery
# 1056    Envoy Phase 2
# 1069    Almer Test Team
# 1078    Clarifire - Development
# 1081    Entitlement
# 1093    Tandyner - Test Team
# 1092    Ryder POD Mobile
# 1091    Pisa FarmacoVigilancia - Test Team
# 1079    Development phase
# 33      Carbon Black Enterprise Response

# /c Categories---------------------------------------
# ID      Name
# 1       Coding
# 2       Meeting w/Client
# 3       Design
# 4       Meeting
# 5       Support
# 6       Training
# 7       Fix/Debug
# 8       Project Hours
# 9       Research
# 11      Project Review
# 12      Project Management
# 13      Architect
# 14      Testing / QA
# 15      Estimation
# 16      PTO
# 17      Holiday
# 18      Analysis
# 19      UI Graphic Design
# 20      Code Redesign
# 21      iTexico MX Task
# 23      Interviewing
# 24      Recruting
# 25      Documentation
# 26      Environment Setup
# 27      Technical Advising
# 28      TL
# 29      Vacation