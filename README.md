# Delivery MicroService Nameko

## ⚙️ Instalasi & Konfigurasi

### 1. Clone dan masuk folder
```bash
git clone https://github.com/C14220191/Delivery.git
cd Delivery
```
### 2. Install requirments
```bash
pip install -r requirements.txt
```

### 3. Jalankan service RabbitMQ dan MySQL(XAMPP/sejenisnya)
Import sql ke MySQL/dapat buat table delivery
```bash
CREATE DATABASE delivery;

CREATE TABLE delivery (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tujuan VARCHAR(255),
    jarak FLOAT,
    notes TEXT,
    harga_delivery DECIMAL(10,2),
    order_id INT,
    member_id INT,
    status VARCHAR(50) DEFAULT 'pending'
);
```
### 4. Ambil API dari OpenRouteService
https://openrouteservice.org/dev/#/signup
isi API key yang didapat
```bash
ORS_API_KEY = "your_api_key_here"
```
### 5. Jalankan delivery service dan gateway
```bash
nameko run delivery --broker amqp://guest:guest@localhost

##jalankan diterminal yang berbeda
nameko run gateway --broker amqp://guest:guest@localhost
```
---
# How to use?🤔
dapat menggunakkan Postman,YARC!, atau sejenisnya.

---
---
#### Get Method
    http://localhost:8000/delivery
    http://localhost:8000/delivery/<int:delivery_id>
        ex: http://localhost:8000/delivery/1

---
---

#### Post Method
Input menggunakkan Json Raw Body
```bash
http://localhost:8000/delivery  (create delivery)
        json example :
            {
                  "tujuan": "Jakarta",
                  "jarak": 320.5,
                  "notes": "kirim cepat",
                  "order_id": 1,
                  "member_id": 3
            }
http://localhost:8000/search    (search place)
        json example:
        {
          "q": "Maspion"
        }
        
http://localhost:8000/distance  (Get distance and estimation time)
        json example:
        {
          "lat": -6.2012,
          "lon": 106.7821
        }

http://localhost:8000/delivery/last (Get last data)

http://localhost:8000/delivery/<string:status> (get data by status, buat filter)
```

---
---
#### PUT Method
```bash
http://localhost:8000/delivery/<int:delivery_id>/status (edit status by id)
        json example:
        {"status": "completed" }
        
http://localhost:8000/delivery/<int:delivery_id>        (edit all data by id)
        json example:
        {
          "tujuan": "Bandung",
          "jarak": 180,
          "notes": "ubah tujuan",
          "harga_delivery": 40000,
          "order_id": 1,
          "member_id": 3,
          "status": "in_transit"
        }
```
---
---

#### DELETE
```bash
        http://localhost:8000/delivery/<int:delivery_id> (delete by id)
---

