# Installation

## Setup Api

Setup virtual environment
```bash
python3 -m venv venv
```

Activate it
```bash
source venv/bin/activate 
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run app
```bash
python app.py
```

---
## UP Mongo

Run mongo container
```bash
sudo docker-compose up -d
```


#### In this project, normally, you do not need to do anything to prepare mongo environment, you can just post the below sample player document via /player [POST] endpoint
#### After you have posted, the mongo-engine will create the related indexes and fields according to your Player model.
```bash
{
    "rank": 9999,
    "name": "John Doe",
    "level": "Beginner",
    "country": "USA",
    "rating": 5
}
```

You can check the Player collection via mongo shell
```bash
sudo docker exec -it db sh -c mongo
```

Player collection's metadata will be as same as follows
```bash
{"indexes":[{"v":{"$numberInt":"2"},"key":{"_id":{"$numberInt":"1"}},"name":"_id_"},{"v":{"$numberInt":"2"},"unique":true,"key":{"rank":{"$numberInt":"1"}},"name":"rank_1","background":false,"sparse":false}],"uuid":"a3329bfbddc5495180c3889a7565e4f2","collectionName":"player"}
```

---

Here a dummy example to import easily
```bash
{"_id":{"$oid":"60151f666f117b7283a3bf35"},"rank":{"$numberInt":"1"},"name":"Garry Kasparov","level":"Grandmaster","country":"Russia","rating":{"$numberInt":"2849"}}
{"_id":{"$oid":"601521f90a1fc6373c7d4d7e"},"rank":{"$numberInt":"2"},"name":"Viswanathan Anand","level":"Grandmaster","country":"India","rating":{"$numberInt":"2774"}}
{"_id":{"$oid":"6015434eabef18dbcff81e31"},"rank":{"$numberInt":"3"},"name":"Vladimir Kramnik","level":"Grandmaster","country":"Russian","rating":{"$numberInt":"1975"}}
{"_id":{"$oid":"601548b78b0d2f342d6144df"},"rank":{"$numberInt":"4"},"name":"Michael Adams","level":"Grandmaster","country":"England","rating":{"$numberInt":"2754"}}
{"_id":{"$oid":"6015492a97ffd5c6c030c0e4"},"rank":{"$numberInt":"5"},"name":"Peter Leko","level":"Grandmaster","country":"Hungary","rating":{"$numberInt":"2748"}}
{"_id":{"$oid":"6015498697ffd5c6c030c0e5"},"rank":{"$numberInt":"6"},"name":"Alexei Shirov","level":"Grandmaster","country":"Spain","rating":{"$numberInt":"2734"}}
{"_id":{"$oid":"601549f0e96701acb59fbf26"},"rank":{"$numberInt":"15"},"name":"Nigel Short","level":"Grandmaster","country":"England","rating":{"$numberInt":"2684"}}
{"_id":{"$oid":"60154a91cc0424097837a6b4"},"rank":{"$numberInt":"8"},"name":"Vassily Ivanchuk","level":"Grandmaster","country":"Ukraine","rating":{"$numberInt":"2716"}}
{"_id":{"$oid":"60154b4bcc0424097837a6b5"},"rank":{"$numberInt":"9"},"name":"Veselin Topalov","level":"Grandmaster","country":"Bulgaria","rating":{"$numberInt":"2707"}}
{"_id":{"$oid":"60154b90cc0424097837a6b6"},"rank":{"$numberInt":"93"},"name":"Alexander Shabalov","level":"Grandmaster","country":"USA","rating":{"$numberInt":"2599"}}
{"_id":{"$oid":"60154bcccc0424097837a6b7"},"rank":{"$numberInt":"84"},"name":"Zbynek Hracek","level":"Grandmaster","country":"Czechia","rating":{"$numberInt":"2604"}}
```



