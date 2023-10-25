import pytz
from datetime import datetime

# lista de fusos horários que deseja monstrar
fusos_horarios = ['America/New_York', 'Europe/Lisbon', 'Asia/Tokyo', 'Australia/Sydney']

# obtema hora atual em UTC
hora_utc = datetime.now(pytz.utc)

# itera pelos fusos horarios e mostra a hora em cada um
for fuso in fusos_horarios:
    fuso_horario = pytz.timezone(fuso)
    hora_local = hora_utc.astimezone(fuso_horario)
    print(f"Fuso Horário {fuso}: {hora_local.strftime('%Y-%m-%d %H:%M:%S')}")