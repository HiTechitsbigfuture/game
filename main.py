# импортируем необходимые модули
import datetime
import hashlib


# создаем класс клиента банка
class BankClient:

  def __init__(self, name, address, phone, email):
    self.name = name
    self.address = address
    self.phone = phone
    self.email = email
    self.registration_date = datetime.datetime.now()
    self.client_id = self.generate_client_id()

  # генерируем уникальный идентификатор клиента
  def generate_client_id(self):
    hash_str = self.name + self.address + self.phone + self.email + str(
      self.registration_date)
    return hashlib.md5(hash_str.encode('utf-8')).hexdigest()
