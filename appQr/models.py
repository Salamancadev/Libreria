from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

class ZonaRiego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.qr_code:
            self.generar_qr()

    def generar_qr(self):
        data = f"http://127.0.0.1:8000/api/zonas/{self.id}"  # o localhost:8000 si se esta en local
        qr_img = qrcode.make(data)
        buffer = BytesIO()
        qr_img.save(buffer)
        file_name = f"zona_{self.id}.png"
        self.qr_code.save(file_name, File(buffer), save=True)