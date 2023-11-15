from datetime import datetime, timezone, timedelta
import requests
import json

api_url = "http://188.120.255.185"


def format_datetime(day, month, year, hour, minute, second):
    try:
        # Создание объекта datetime с указанием временной зоны
        dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)

        # Преобразование в нужный формат
        formatted_datetime = dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

        return formatted_datetime
    except ValueError as e:
        # Обработка возможных ошибок, например, если переданы некорректные значения для создания datetime
        print(f"Ошибка: {e}")
        return None
    

def get_sample(from_dt: str, to_dt: str):
    params = {
        'from_dt': from_dt,
        'to_dt': to_dt
    }
    # Выполнение GET запроса
    response = requests.get(f"{api_url}/api/research/research.get_sample/", params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Получение JSON данных
        json_data = response.json()

        # Сохранение JSON данных в файл
        with open('output.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        print("JSON файл успешно сохранен.")
    else:
        print(f"Ошибка при выполнении запроса. Код ответа: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    from_dt = format_datetime(
        day=11, month=11, year=2023, hour=22, minute=8, second=29
    )
    to_dt = format_datetime(
        day=11, month=11, year=2024, hour=22, minute=8, second=29
    )
    get_sample(from_dt=from_dt, to_dt=to_dt)