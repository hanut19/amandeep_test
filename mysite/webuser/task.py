from celery import shared_task
from PIL import Image

@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def resize_file(in_file, out_file, size):
    try:
        img = Image.open(in_file)
        img.thumbnail(size)
        img.save(out_file)                
    except Exception as e:
        print (e)