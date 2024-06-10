def get_development_stages():
    stages = []
    print("Введите основные стадии эволюции человека по порядку:")
    while True:
        stage = input("Введите следующую стадию (или нажмите Enter для завершения): ")
        if stage == "":
            break
        stages.append(stage)
    
    print("Введенные стадии развития:")
    print(" => ".join(stages))
get_development_stages()
