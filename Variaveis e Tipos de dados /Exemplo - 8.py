segundos_str = input("Por favor, entre com os segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600

minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print("Hrs=", horas, "mins=", minutos, "segs=", segs_restantes_final)
