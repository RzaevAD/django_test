from django.db import models


class VirtualMachineInterfaces(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=39, blank=True, default='')
    status = models.CharField(max_length=10)
    mac_adress = models.CharField(max_length=50)
    mtu = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'name: {self.name} ip: {self.ip}'
