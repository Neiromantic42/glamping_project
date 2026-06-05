from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings


# =========================
# СТАТИЧЕСКИЕ СТРАНИЦЫ
# =========================
class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"  # 🔥 ВАЖНО: фиксируем HTTPS

    def items(self):
        return [
            ("glamping:home_page", {}),
            ("gallery:gallery", {}),
            ("bookings:booking", {}),
            ("reviews:reviews", {}),
            ("info:about", {}),
        ]

    def location(self, item):
        return reverse(item[0], kwargs=item[1])

    def priority(self, item):
        if item[0] == "glamping:home_page":
            return 1.0
        if item[0] == "info:about":
            return 0.6
        return 0.8