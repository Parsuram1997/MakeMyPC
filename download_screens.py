import urllib.request
import json

screens_data = {
    "admin-dashboard-overview.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzAwMDY1NWE1ODY0N2NiMjkwOTI1ZDNlMGNjMTMwZTNiEgsSBxD8nYOajAcYAZIBJAoKcHJvamVjdF9pZBIWQhQxMzEwMDY3OTczMjU2MzM2MzY4OQ&filename=&opi=89354086",
    "product-management.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzAwMDY1NWE1ODcxMzBjYzgwMzM4NTkyMGEwMmM2MTFmEgsSBxD8nYOajAcYAZIBJAoKcHJvamVjdF9pZBIWQhQxMzEwMDY3OTczMjU2MzM2MzY4OQ&filename=&opi=89354086",
    "orders-management.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzAwMDY1NWE1ODYyMzJjN2MwNTc2MDJjODQzMjEyODliEgsSBxD8nYOajAcYAZIBJAoKcHJvamVjdF9pZBIWQhQxMzEwMDY3OTczMjU2MzM2MzY4OQ&filename=&opi=89354086",
    "compatibility-manager.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzAwMDY1NWE1ODY1OWRkNmIwNTAzYzIzMjY5MGE0M2Y4EgsSBxD8nYOajAcYAZIBJAoKcHJvamVjdF9pZBIWQhQxMzEwMDY3OTczMjU2MzM2MzY4OQ&filename=&opi=89354086"
}

for filename, url in screens_data.items():
    print(f"Downloading {filename}...")
    filepath = rf"c:\Projects\MakeMyPC\{filename}"
    urllib.request.urlretrieve(url, filepath)
    print(f"Saved {filepath}")

