from django.contrib.sitemaps import Sitemap
from django.urls import reverse



# =========================
# СТАТИЧЕСКИЕ СТРАНИЦЫ
# =========================
class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            ("glamping:home_page", {}),
            ("gallery:gallery", {}),
            ("bookings:booking", {}),
            ("reviews:reviews", {}),
        ]

    def location(self, item):
        return reverse(item[0], kwargs=item[1])