from django.db import models
from django.contrib.auth.models import User


# Справочник модель техники
class TechnicModel(models.Model):
    name = models.CharField("Название",max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель техники"
        verbose_name_plural = "Модели техники"


# Справочник модель двигателя
class EngineModel(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель двигателя"
        verbose_name_plural = "Модели двигателя"


# Справочник модель трансмиссии
class TransmissionModel(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель трансмиссии"
        verbose_name_plural = "Модели трансмиссии"


# Справочник модель ведущего моста
class DrivingBridgeModel(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель ведущего моста"
        verbose_name_plural = "Модели ведущего моста"


# Справочник модель управляемого моста
class ControlledBridgeModel(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель управляемого моста"
        verbose_name_plural = "Модели управляемого моста"


# Справочник характер отказа
class FailureNode(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характеры отказов'


# Справочник способ восстановления
class RecoveryMethod(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ восстановления"
        verbose_name_plural = "Способы восстановления"


class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиент"


# Справочник Организация, проводившая ТО

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация, проводившая ТО"
        verbose_name_plural = "Организация, проводившая ТО"


# Сервисная компания
class ServiceCompany(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервисная компания"
        verbose_name_plural = "Сервисные компании"


# Вид ТО
class TypeOfMaintenance(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид ТО"
        verbose_name_plural = "Виды ТО"


# Машина
class Machine(models.Model):
    machine_factory_number = models.CharField("Заводской номер машины", max_length=4)
    technic_model = models.ForeignKey(TechnicModel, on_delete=models.CASCADE, verbose_name="Модель техники")
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE,  verbose_name="Модель двигателя")
    engine_factory_number = models.CharField("Заводской номер двигателя", max_length=16)
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, verbose_name="Модель трансмиссии")
    transmission_factory_number = models.CharField("Заводской номер трансмиссии", max_length=10)
    driving_bridge_model = models.ForeignKey(DrivingBridgeModel, on_delete=models.CASCADE, verbose_name="Модель ведущего моста")
    driving_bridge_factory_number = models.CharField("Заводской номер ведущего моста", max_length=10)  # Зав. № ведущего моста
    controlled_bridge_model = models.ForeignKey(ControlledBridgeModel, on_delete=models.CASCADE, verbose_name="Модель управляемого моста")
    controlled_bridge_factory_number = models.CharField("Заводской номер управляемого моста", max_length=10)
    delivery_contract = models.CharField("Договор поставки, №, дата", max_length=100)
    shipment_date = models.DateField("Дата отгрузки с завода")
    consignee = models.CharField("Грузополучатель", max_length=100)
    delivery_address = models.CharField("Адрес поставки (эксплуатации)", max_length=100)
    equipment = models.CharField("Комплектация, доп. опции", max_length=255)  # Комплект (доп. опции)
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")
    client1 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="admin",
                                related_name="client1_machines", null=True)
    client2 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="manager",
                                related_name="client2_machines", null=True)
    client3 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="server",
                                related_name="client3_machines", null=True)

    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name="Сервисная компания")

    def __str__(self):
        return self.machine_factory_number

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


# ТО
class Maintenance(models.Model):
    date_of_maintenance = models.DateField(verbose_name='Дата проведения ТО')  # дата ТО
    operating_time = models.IntegerField(verbose_name='Наработка мото/часов')  # наработка, м/час
    order_number = models.CharField(max_length=100, verbose_name='Номер заказа наряда')  # номер заказ-наряда
    data_of_order = models.DateField(verbose_name='Дата заказа-наряда')  # дата заказ-наряда
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО')  # Организация, проводившая ТО
    type_of_maintenance = models.ForeignKey(TypeOfMaintenance, on_delete=models.CASCADE, verbose_name='Вид ТО')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Техническое обслуживание (ТО)'
        verbose_name_plural = 'Техническое обслуживание (ТО)'
        ordering = ('date_of_maintenance',)


# Рекламации
class Complaints(models.Model):
    date_of_failure = models.DateField(verbose_name='Дата отказа')  # дата отказа
    operating_time = models.IntegerField(verbose_name='Наработка м/час')  # наработка, м/час
    spare_parts_used = models.TextField(null=True, blank=True, default=None, verbose_name='Используемые запасные части')  # используемые запасные части
    date_of_recovery = models.DateField(verbose_name='Дата восстановления')  # дата восстановления
    technic_downtime = models.IntegerField(default=None, verbose_name='Время простоя техники')  # время простоя техники (дата восстановления - дата отказа)
    description_of_failure = models.CharField(max_length=100, verbose_name='Описание отказа')  # Описание отказа
    failure_node = models.ForeignKey(FailureNode, on_delete=models.CASCADE, verbose_name='Узел отказа')  # узел отказа
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE,  verbose_name='Сервисная компания', null=True)

    def calculation_downtime(self):
        self.technic_downtime = (self.date_of_recovery - self.date_of_failure).days
        print(self.technic_downtime)
        self.save()

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
        ordering = ['date_of_failure']