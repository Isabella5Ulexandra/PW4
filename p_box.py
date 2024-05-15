def p_box_transform(input_data):
  # Формула перестановки
  p_permutation = [1, 5, 2, 0, 3, 7, 4, 6]

  # Ініціалізація вихідних даних
  output_data = 0

  # Перестановка бітів за формулою перестановки
  for i, bit_position in enumerate(p_permutation):
      # Визначення значення біта на вході
      bit_value = (input_data >> (7 - bit_position)) & 1
      # Збирання вихідних даних
      output_data |= bit_value << (7 - i)

  return output_data

def inverse_p_box_transform(output_data):
  # Формула оберненої перестановки
  p_permutation = [3, 0, 2, 4, 6, 1, 7, 5]

  # Ініціалізація вихідних даних
  input_data = 0

  # Перестановка бітів за формулою оберненої перестановки
  for i, bit_position in enumerate(p_permutation):
      # Визначення значення біта на вході
      bit_value = (output_data >> (7 - bit_position)) & 1
      # Збирання вхідних даних
      input_data |= bit_value << (7 - i)

  return input_data

# Тест прямого перетворення P-блоку
def test_forward_p_box_transform():
  input_data = 0b00100101
  expected_output_data = 0b01100100
  output_data = p_box_transform(input_data)
  assert output_data == expected_output_data, f"Помилка: Вихідні дані не співпадають з очікуваними. Отримано: {output_data:08b}, Очікувано: {expected_output_data:08b}"
  print("Пряме перетворення P-блоку пройшло успішно.")

# Тест зворотного перетворення P-блоку
def test_inverse_p_box_transform():
  output_data = 0b01100100
  expected_input_data = 0b00100101
  input_data = inverse_p_box_transform(output_data)
  assert input_data == expected_input_data, f"Помилка: Вихідні дані не співпадають з очікуваними. Отримано: {input_data:08b}, Очікувано: {expected_input_data:08b}"
  print("Зворотне перетворення P-блоку пройшло успішно.")

# Виклик тестів
test_forward_p_box_transform()
test_inverse_p_box_transform()
