# mamal-service

Starter API sederhana yang **siap deploy** menggunakan Python stdlib + Docker (tanpa dependency runtime eksternal).

## Endpoint
- `GET /` -> status service
- `GET /health` -> healthcheck

## Jalankan lokal
```bash
python app.py
```

## Test
```bash
pytest -q
```

## Build & run dengan Docker
```bash
docker build -t mamal-service:latest .
docker run --rm -p 8000:8000 mamal-service:latest
```

Cek:
```bash
curl http://localhost:8000/
curl http://localhost:8000/health
```

## Deploy checklist
- [x] App punya endpoint healthcheck
- [x] Tidak ada runtime dependency eksternal
- [x] Dockerfile tersedia
- [x] Test otomatis tersedia
- [ ] CI/CD (opsional, bisa ditambah sesuai platform)
- [ ] Konfigurasi environment production (domain, TLS, secrets)
