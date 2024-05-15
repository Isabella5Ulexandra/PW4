# Таблиця S-блоку
s_box = {
    0b0000: 0b01101100,
    0b0001: 0b11001010,
    0b0010: 0b01111011,
    0b0011: 0b11011101,
    0b0100: 0b01000010,
    0b0101: 0b11100000,
    0b0110: 0b00011110,
    0b0111: 0b10101101,
    0b1000: 0b11001100,
    0b1001: 0b01101101,
    0b1010: 0b11001011,
    0b1011: 0b01101001,
    0b1100: 0b11101100,
    0b1101: 0b01001111,
    0b1110: 0b11101000,
    0b1111: 0b01101010
}

def s_box_transform(input_data):
    # Розділення вхідних даних на дві тетради
    tetrad_1 = (input_data >> 4) & 0b1111
    tetrad_2 = input_data & 0b1111

    # Пряме перетворення S-блоку
    output_data = (s_box[tetrad_1] << 4) | s_box[tetrad_2]

    return output_data & 0b11111111  # Обмежуємо вихідні дані до 8 біт

def inverse_s_box_transform(output_data):
    # Пошук вихідних даних у таблиці S-блоку для отримання вхідних даних
    for input_val, output_val in s_box.items():
        if output_val == output_data:
            return input_val

    return None  # Якщо вихідний байт не знайдено у таблиці S-блоку

def test_forward_s_box_transform():
    input_data = 0b00000001
    expected_output_data = 0b11001010
    output_data = s_box_transform(input_data)
    assert output_data == expected_output_data, f"Помилка: Вихідні дані не співпадають з очікуваними. Отримано: {output_data:08b}, Очікувано: {expected_output_data:08b}"
    print("Пряме перетворення S-блоку пройшло успішно.")

def test_inverse_s_box_transform():
    output_data = 0b11001010
    expected_input_data = 0b00000001
    input_data = inverse_s_box_transform(output_data)
    assert input_data == expected_input_data, f"Помилка: Вхідні дані не співпадають з очікуваними. Отримано: {input_data:08b}, Очікувано: {expected_input_data:08b}"
    print("Зворотне перетворення S-блоку пройшло успішно.")

# Виконання тестів
test_forward_s_box_transform()
test_inverse_s_box_transform()
