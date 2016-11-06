from django.contrib.sitemaps import Sitemap


class Sitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def lastmod(self, obj):
        return obj.pub_date
