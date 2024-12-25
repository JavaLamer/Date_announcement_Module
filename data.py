from important_information import MONTHS, time_hours_data, time_minutes_data, time_data, year_data, constant
import sys
import os
import pygame
import queue
import time

base_folder = "D:/Download/MCuc/лаб2"

sys.stdout.reconfigure(encoding='utf-8')

pygame.init()  # Инициализация pygame



def spliter(text):
    parts = text.split(" ")
    partstime = parts[0].split(".")
    am_pm = parts[1]
    data = parts[2].split("/")
    return data, am_pm, partstime 

def month_converter_to_russian(data):
    month_index, day_index, year_index = int(data[0]), int(data[1]), int(data[2]) 
    if month_index in MONTHS and day_index in time_data and year_index in year_data:
        month_name = MONTHS[month_index]["text"]
        day_name = time_data[day_index]["text"]
        year_name = year_data[year_index]["text"]
        return month_name, day_name, year_name
    else:    
        print("Error format")  

def hour_time_converter_to_russia(am_pm, partstime):
    time_hou, time_minut = int(partstime[0]), int(partstime[1])
    if am_pm == 'PM' or am_pm == 'AM':
        if am_pm == 'PM':
            time_hou += 12
    else:
        print('Error am/pm')

    if time_hou in time_hours_data and time_minut in time_minutes_data:
        hour_time = time_hours_data[time_hou]["text"]
        minute_time = time_minutes_data[time_minut]["text"]

        if 10 < time_hou % 100 < 20:
            hour_text = " часов "
        elif time_hou % 10 == 1:
            hour_text = " час "
        elif 2 <= time_hou % 10 <= 4:
            hour_text = " часа "
        else:
            hour_text = " часов "

        if 10 < time_minut % 100 < 20:
            minute_text = " минут "
        elif time_minut % 10 == 1:
            minute_text = " минута "
        elif 2 <= time_minut % 10 <= 4:
            minute_text = " минуты "
        else:
            minute_text = " минут "

    else:
        print('Error time format')
    
    return hour_time, hour_text, minute_time, minute_text

def true_flag(text):
    yeae_year = " года"
    data, am_pm, partstime = spliter(text)
    month_text, day_text, year_text = month_converter_to_russian(data)
    hour_time, hour_text, minute_time, minute_text = hour_time_converter_to_russia(am_pm, partstime)
    result = hour_time + hour_text + minute_time + minute_text + day_text + " " + month_text + " " + year_text + yeae_year
    print(result)
    return result

def false_flag(text):
    yeae_year = " года"
    data, am_pm, partstime = spliter(text)
    month_text, day_text, year_text = month_converter_to_russian(data)
    hour_time, hour_text, minute_time, minute_text = hour_time_converter_to_russia(am_pm, partstime)
    result = hour_time + hour_text + minute_time + minute_text + day_text + " " + month_text + " " + year_text + yeae_year
    print(result)
    make_noise(result)
    return result

def make_text(text, flag):
    if flag:
        result = true_flag(text)
        return result
    else: 
        result = false_flag(text)
        return result

def make_noise(text):
    print(f"Обрабатываем текст: {text}")
    words = text.lower().strip().split()  # Привести текст к нижнему регистру и разделить
    print(f"Слова для обработки: {words}")
    audio_queue = queue.Queue()

    for word in words:
        word_found = False

        for dictionary, data in [
            ("MONTHS", MONTHS),
            ("time_hours_data", time_hours_data),
            ("time_minutes_data", time_minutes_data),
            ("time_data", time_data),
            ("year_data", year_data),
            ("constant", constant)
        ]:
            print(f"Ищем слово '{word}' в словаре {dictionary}...")
            for entry in data.values():
                if word == entry["text"].lower():
                    audio_path = os.path.normpath(os.path.join(base_folder, entry["audio"]))
                    if os.path.exists(audio_path):
                        print(f"Найдено: {audio_path}, добавляем в очередь.")
                        audio_queue.put(audio_path)
                        word_found = True
                    else:
                        print(f"Аудиофайл {audio_path} не найден.")
                    break  # Перейти к следующему слову, если найдено

            if word_found:
                break

        if not word_found:
            print(f"Слово '{word}' не найдено в словарях.")
            return  # Завершить выполнение при отсутствии совпадения

    print("Фраза готова. Начинаем воспроизведение.")
    while not audio_queue.empty():
        audio_path = audio_queue.get()
        try:
            print(f"Воспроизводим файл: {audio_path}")
            sound = pygame.mixer.Sound(audio_path)
            sound.play()
            while pygame.mixer.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print(f"Ошибка при воспроизведении: {e}")

