import time
from celery import shared_task

from .scrapers import scrape



#URL = 'https://www.portalinmobiliario.com/venta/departamento/metropolitana#applied_filter_id%3Dstate%26applied_filter_name%3DUbicaci%C3%B3n%26applied_filter_order%3D3%26applied_value_id%3DTUxDUE1FVEExM2JlYg%26applied_value_name%3DRM+%28Metropolitana%29%26applied_value_order%3D12%26applied_value_results%3D41056'


@shared_task
def scrape_dev_to():
    URL = 'https://dev.to/search?q=django'
    scrape(URL)
    return
